from __future__ import division

import logging

def evaluate(corpus):
    tp, p, t, tpCat, pCat, tCat = getStatistics(corpus)
    scores = calculateScores(tp, p, t, 'Identification')
    scores += calculateScores(tpCat, pCat, tCat, 'Categorization')
    catList = ['lvc', 'ireflv', 'vpc', 'id', 'oth']
    for cat in catList:
        tp, p, t = getCategoryStatistics(corpus, cat)
        scores += calculateScores(tp, p, t, cat)
    return scores


def getStatistics(corpus):
    tp, p, t, tpCat, pCat, tCat = 0, 0, 0, 0, 0, 0

    for sent in corpus.testingSents:
        p += len(sent.vMWEs)
        t += len(sent.identifiedVMWEs)
        for vmw in sent.vMWEs:
            if len(vmw.tokens) > 1:
                pCat += 1
        for vmw in sent.identifiedVMWEs:
            if len(vmw.tokens) > 1:
                tCat += 1
        if sent.identifiedVMWEs:
            processedVmwe = []
            for m in sent.identifiedVMWEs:
                for vMWE in sent.vMWEs:
                    if m == vMWE and vMWE not in processedVmwe:
                        processedVmwe.append(vMWE)
                        tp += 1
                        if m.type == vMWE.type and len(vMWE.tokens) > 1:
                            tpCat += 1
    return tp, p, t, tpCat, pCat, tCat


def getCategoryStatistics(corpus, cat):
    tp, p, t = 0, 0, 0
    cat = cat.lower()
    for sent in corpus.testingSents:
        for vmw in sent.vMWEs:
            if vmw.type.lower() == cat:
                p += 1
        for vmw in sent.identifiedVMWEs:
            if vmw.type.lower() == cat:
                t += 1
        if not sent.identifiedVMWEs:
            continue
        processedVmwe = []
        for m in sent.identifiedVMWEs:
            for vMWE in sent.vMWEs:
                if m == vMWE and vMWE not in processedVmwe and m.type.lower() == vMWE.type.lower() \
                        and m.type.lower() == cat:
                    processedVmwe.append(vMWE)
                    tp += 1
    return tp, p, t


def getMWTStatistics(corpus):
    tp, p, t, tpCat, pCat, tCat = 0, 0, 0, 0, 0, 0

    for sent in corpus.testingSents:
        for vmw in sent.vMWEs:
            if len(vmw.tokens) == 1:
                p += 1
        for vmw in sent.identifiedVMWEs:
            if len(vmw.tokens) == 1:
                t += 1
        processedVmwe = []
        for m in sent.identifiedVMWEs:
            for vMWE in sent.vMWEs:
                if len(m.tokens) == 1 and m == vMWE and vMWE not in processedVmwe:
                    processedVmwe.append(vMWE)
                    tp += 1
                    if m.type.lower() == vMWE.type.lower():
                        tpCat += 1
    return tp, p, t, tpCat, p, t


def calculateScores(tp, p, t, title):
    """

    :param tp: True positive
    :param p: positive
    :param t: true
    :param title: logging indicator
    :return: Fscore, recall, precision
    """
    if p == 0 or t == 0 or tp == 0:
        if title == 'Identification':
            logging.warn('{0} : F-Score: {1}, Recall: {2}, Precision: {3}'.format(title, 0, 0, 0))
        return ['', 0, 0, 0]

    p = float(tp / p)
    r = float(tp / t)

    f = round(2 * (r * p) / (r + p), 3)
    r = round(r, 3)
    p = round(p, 3)
    logging.warn('{0} : F-Score: {1}, Recall: {2}, Precision: {3}'.format(title, f, r, p))

    return [title, f, r, p]
