#! /usr/bin/env python3

import argparse
import collections
import itertools
import os
import sys
import tsvlib


parser = argparse.ArgumentParser(description="""
        Evaluate input TSV `prediction` against `gold`.""")
parser.add_argument("--debug", action="store_true",
        help="""Print extra debugging information""")
parser.add_argument("--filter-categs", type=str, default=None,
        help="""Only evaluate MWE category labels from given comma-separated list""")
parser.add_argument("--combinatorial", action="store_true",
        help="""Run O(n!) algorithm for weighted bipartite matching""")
parser.add_argument("gold_file", type=argparse.FileType('r'),
        help="""The gold-standard file""")
parser.add_argument("prediction_file", type=argparse.FileType('r'),
        help="""The system prediction file""")


class Main(object):
    def __init__(self, args):
        self.args = args
        self.categs_to_filter = frozenset(self.args.filter_categs.split(",")) \
                if self.args.filter_categs else None
        # Gold = test.parsemetsv; Pred = test.system.parsemetsv
        if "test.parsemetsv" in self.args.prediction_file.name or "system" in self.args.gold_file.name:
            tsvlib.warn("Something looks wrong in the gold & system arguments.\n" \
                    "Is `{gold_file.name}` really the gold test.parsemetsv file?\n" \
                    "Is `{pred_file.name}` really a system prediction file?",
                    gold_file=self.args.gold_file, pred_file=self.args.prediction_file)

    def run(self):
        self.gold = collections.deque(tsvlib.iter_tsv_sentences(self.args.gold_file))
        self.pred = collections.deque(tsvlib.iter_tsv_sentences(self.args.prediction_file))
        mc_args = dict(debug=self.args.debug, tractable=not self.args.combinatorial)
        c_mwebased = MatchCounter("MWE-based", **mc_args)    # used below for exact match
        c_tokbased = MatchCounter("Token-based", **mc_args)  # used below for fuzzy match

        while self.gold or self.pred:
            self.check_eof()
            g = self.gold.popleft()
            p = self.pred.popleft()
            self.filter_categories(g)
            self.compare_sentences(g, p)
            g_mwes, p_mwes = self.to_mwes(g), self.to_mwes(p)
            if self.args.debug:
                self.print_debug_pairing(g, p)
                self.print_debug_mwes("gold", g_mwes)
                self.print_debug_mwes("pred", p_mwes)
            c_mwebased.increment_mwebased(g_mwes, p_mwes)
            c_tokbased.increment_tokbased(g_mwes, p_mwes)

            if self.args.debug:
                print("DEBUG:", file=sys.stderr)

        self.print_stats(c_mwebased)
        self.print_stats(c_tokbased)


    def print_stats(self, mcounter):
        precision = mcounter.correct / (mcounter.total_pred or 1)
        recall = mcounter.correct / (mcounter.total_gold or 1)
        f1 = 2*precision*recall/(precision+recall) if precision else 0
        print(">> {mcounter.name}:\n  * P = {precision:.4f} ({mcounter.correct} / {mcounter.total_pred})\n" \
                "  * R = {recall:.4f} ({mcounter.correct} / {mcounter.total_gold})\n  * F = {f1:.4f}\n" \
                .format(mcounter=mcounter, precision=precision, recall=recall, f1=f1))


    def print_debug_pairing(self, g, p):
        triples = [["ID", "GOLD", "PRED", "WORD"]]
        for i, tok_g in enumerate(g.words):
            try:
                tok_p_mwe_codes = p.words[i].mwe_codes
            except IndexError:
                tok_p_mwe_codes = ""

            triples.append(["t{}".format(i+1),
                    ";".join(sorted(tok_g.mwe_codes)),
                    ";".join(sorted(tok_p_mwe_codes)),
                    tok_g.surface])
        print("DEBUG:\t+====================================")
        for triple in triples:
            print("DEBUG:\t|", "\t".join(triple), sep="")
        print("DEBUG:\t+------------------------------------")

    def print_debug_mwes(self, name, mwes):
        print("DEBUG:\t{} = {}".format(name, mwes2t(mwes)))


    def filter_categories(self, sentence):
        r"""Filter MWEs in `sentence` so as to only have the requested categories."""
        if not self.categs_to_filter: return  # do not filter
        good_mwe_ids = set()
        for i, word in enumerate(sentence.words):
            good_mwe_ids.update(mwe_id for (mwe_id, mwe_categ)
                    in word.mwes_id_categ() if mwe_categ in self.categs_to_filter)
            sentence.words[i] = word._replace(mwe_codes={m for m in word.mwe_codes
                    if tsvlib.mwe_code_to_id_categ(m)[0] in good_mwe_ids})


    def to_mwes(self, tsv_sent):
        r"""Return a list of MWEs, each one represented as a set of integers.
        MWEs are ordered in an "arbitary" order (but in practice, we sort it, for human readability).
        NOTE: we group identical MWEs as a single unit, as per the Shared Task meeting's discussion
        regarding a set-based definition of MWEs.
        """
        tsv_sent.absorb_mwes_from_contraction_ranges()
        return list(sorted(set(frozenset(i+1 for i in x.token_indexes)
                for x in tsv_sent.mwe_infos().values()), key=lambda fset: list(fset)))


    def check_eof(self):
        r"""Generate an error if one of the files is in EOF and the other is not."""
        if not self.gold:
            error("Prediction file is larger than the gold file (extra data?)")
        if not self.pred:
            error("Prediction file is smaller than the gold file (missing data?)")

    def compare_sentences(self, g, p):
        if len(g.words) != len(p.words):
            tsvlib.global_last_lineno(None, 0)
            len_g, len_p = len(g.words), len(p.words)
            tsvlib.warn("Sentence sizes do not match\n" \
                    "In sentence starting at `{args.gold_file.name}` line {g.lineno_beg} ({len_g} tokens)\n" \
                    "In sentence starting at `{args.prediction_file.name}` line {p.lineno_beg} ({len_p} tokens)",
                    g=g, p=p, args=self.args, len_g=len_g, len_p=len_p)


def mwe2t(mwe):
    r"""mwe2t(frozenset[int]) -> str
    Return a string representation such as "t1_t3_t4"."""
    return "_".join("t{}".format(i) for i in sorted(mwe))

def mwes2t(mwes):
    r"""mwes2t(frozenset[frozenset[int]]) -> str"""
    return "{" + ", ".join(sorted(mwe2t(mwe) for mwe in mwes)) + "}"

def pairing2t(pairing):
    r"""pairing2t(dict[frozenset[int], frozenset[int]]) -> str"""
    return "{" + ", ".join(sorted("{}=>{}".format(mwe2t(mwe1), mwe2t(mwe2))
            for (mwe1,mwe2) in pairing.items())) + "}"


def error(message, **kwargs):
    r"""Print error message and quit."""
    tsvlib.warn(message, warntype="ERROR", **kwargs)
    sys.exit(1)



class MatchCounter:
    def __init__(self, name, debug, tractable):
        self.name = name
        self.debug = debug
        self.tractable = tractable
        self.total_gold = 0
        self.total_pred = 0
        self.correct = 0

    def do_debug(self, plus_g, plus_p, inc, debug_pairing):
        if self.debug:
            print("DEBUG:\tMapping gold=>pred ({name}): {debug_pairing}  " \
                    "@@ P+={inc}/{plus_p} R+={inc}/{plus_g}".format(
                    name=self.name, debug_pairing=debug_pairing,
                    inc=inc, plus_g=plus_g, plus_p=plus_p))

    def increment(self, plus_g, plus_p, plus_correct, debug_pairing="???"):
        self.total_gold += plus_g
        self.total_pred += plus_p
        self.correct += plus_correct
        self.do_debug(plus_g, plus_p, plus_correct, debug_pairing)

    def increment_per_pairing(self, g_mwes, p_mwes, pairing):
        self.increment(len(g_mwes), len(p_mwes), len(pairing), pairing2t(pairing))

    def increment_per_token(self, g_mwes, p_mwes, pairing):
        self.increment(sum(len(m) for m in g_mwes), sum(len(m) for m in p_mwes),
                sum(len(a&b) for (a,b) in pairing.items()), pairing2t(pairing))


    def increment_mwebased(self, g_mwes, p_mwes):
        pairing = {x:x for x in set(g_mwes) & set(p_mwes)}
        self.increment_per_pairing(g_mwes, p_mwes, pairing)

    def increment_tokbased(self, g_mwes, p_mwes):
        pairing = tokbased_pairing(g_mwes, p_mwes, tractable=self.tractable)
        self.increment_per_token(g_mwes, p_mwes, pairing)


def tokbased_pairing(g_mwes, p_mwes, tractable):
    if tractable:  # Use O(n^3) algorithm
        if not g_mwes or not p_mwes: return {}
        return ParsemeBipartiteGraph(g_mwes, p_mwes).mapping

    else:  # Use O(n!) algorithm
        g_mwes += [frozenset()] * (len(p_mwes) - len(g_mwes))
        p_mwes += [frozenset()] * (len(g_mwes) - len(p_mwes))
        ret, ret_count = {}, 0
        for p_mwes_permut in itertools.permutations(p_mwes):
            pairing = {a:b for (a,b) in zip(g_mwes, p_mwes_permut) if a and b}
            pairing_count = sum(len(set(a)&set(b)) for (a,b) in pairing.items())
            if pairing_count > ret_count:
                ret, ret_count = pairing, pairing_count
        return ret


class ParsemeBipartiteGraph:
    def __init__(self, g_mwes, p_mwes):
        self.g_mwes, self.p_mwes = g_mwes, p_mwes
        self.cost_mtx = [
            [self.cost(g, p) for p in self.p_mwes]
            for g in self.g_mwes]

        from bmc_munkres import munkres
        m = munkres.Munkres()
        self.result_indexes = m.compute(self.cost_mtx)
        self.mapping = {self.g_mwes[a]: self.p_mwes[b]
                for (a, b) in self.result_indexes}

    def cost(self, g, p):
        r"""cost(set, set) -> int"""
        return - self.weight(g, p)
    
    def weight(self, g, p):
        r"""weight(set, set) -> int"""
        return len(g&p)



#####################################################

if __name__ == "__main__":
    Main(parser.parse_args()).run()
