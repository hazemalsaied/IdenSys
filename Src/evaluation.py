from __future__ import division

import logging

from param import XPParams, Counters, Paths
import reports, os


class Evaluation:
    @staticmethod
    def evaluate(corpus):
        reports.createEvaluationFiles(corpus.testDataSet)

        tp, p, t, tpCat, pCat, tCat = Evaluation.getStatistics(corpus)
        scores = Evaluation.calculateScores(tp, p, t,'Ordinary: ')
        scores += Evaluation.calculateScores(tpCat, pCat, tCat, 'Categorization: ')
        catList = ['lvc', 'ireflv', 'vpc', 'id', 'oth']
        for cat in catList:
            tp, p, t = Evaluation.getCategoryStatistics(corpus, cat)
            scores += Evaluation.calculateScores(tp, p, t, cat + ' categorization: ')
        tp, p, t, tpCat, pCat, tCat = Evaluation.getMWTStatistics(corpus)
        scores += Evaluation.calculateScores(tp, p, t, 'MWT: ')
        scores += Evaluation.calculateScores(tpCat, p, t, 'MWT Categorization: ')
        tp, p, t = Evaluation.getEmbeddedStatistics(corpus)
        if corpus.emeddedNum > 0:
            scores += Evaluation.calculateScores(tp, p, t, 'Embedded: ')
        else:
            scores += [0] * 3
        res = Evaluation.toString(scores)
        path = os.path.join(Paths.rootResultFolder, 'ArticleRes.csv')
        with open(path, 'a') as f:
            f.write(res)

        Counters.initCounters()
        return scores

    @staticmethod
    def toString(scores):
        comma = ','
        line = Paths.languageName + comma
        for i in range(len(scores)):
            if i % 3 == 0:
                line += str(scores[i]) + comma
        line = line[:-1] + '\n'
        return line

    @staticmethod
    def getStatistics(corpus):
        tp, p, t, tpCat, pCat, tCat = 0, 0, 0, 0, 0, 0

        for sent in corpus.testingSents:
            p += len(sent.vMWEs)
            t += len(sent.identifiedVMWEs)
            for vmw in sent.vMWEs:
                if len(vmw.tokens) > 1:
                    tCat += 1
            for vmw in sent.identifiedVMWEs:
                if len(vmw.tokens) > 1:
                    pCat += 1
            if len(sent.identifiedVMWEs) > 0:
                processedVmwe = []

                for m in sent.identifiedVMWEs:
                    for vMWE in sent.vMWEs:
                        if m == vMWE and vMWE not in processedVmwe:
                            processedVmwe.append(vMWE)
                            tp += 1
                            if m.type == vMWE.type and len(vMWE.tokens) > 1:
                                tpCat += 1
        return tp, p, t, tpCat, pCat, tCat

    @staticmethod
    def getCategoryStatistics(corpus, cat):
        tp, p, t = 0, 0, 0
        cat =cat.lower()
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
                    if m == vMWE and vMWE not in processedVmwe and m.type.lower() == vMWE.type.lower() and m.type.lower() == cat:
                        processedVmwe.append(vMWE)
                        tp += 1
        return tp, p, t

    @staticmethod
    def getMWTStatistics(corpus):
        tp, p, t, tpCat, pCat, tCat = 0, 0, 0, 0, 0, 0

        for sent in corpus.testingSents:
            for vmw in sent.vMWEs:
                if len(vmw.tokens) == 1:
                    p +=1
            for vmw in sent.identifiedVMWEs:
                if len(vmw.tokens) == 1:
                    t +=1
            processedVmwe = []
            for m in sent.identifiedVMWEs:
                for vMWE in sent.vMWEs:
                    if len(m.tokens) == 1 and m == vMWE and vMWE not in processedVmwe:
                        processedVmwe.append(vMWE)
                        tp += 1
                        if m.type.lower() == vMWE.type.lower():
                            tpCat += 1
        return tp, p, t, tpCat, p, t


    @staticmethod
    def getEmbeddedStatistics(corpus):
        # True positive, positive, true
        tp, p, t = 0, 0, 0
        for sent in corpus.testingSents:
            p += sent.embeddedNum
            for vmwe1 in sent.identifiedVMWEs:
                for vmwe2 in sent.identifiedVMWEs:
                    if vmwe1 in vmwe2:
                        vmwe1.isEmbedded = True
            for vmwe in sent.identifiedVMWEs:
                if vmwe.isEmbedded:
                    t+=1
            # t += sent.recognizeEmbedded(recognizeIdentified=True)
            for m1 in sent.identifiedVMWEs:
                if m1.isEmbedded:
                    for m2 in sent.vMWEs:
                        if m1 == m2 and m2.isEmbedded:
                            tp += 1
        if not XPParams.useCrossValidation:
            logging.warn('Embedding stats:' + str(tp) + ' ' + str(p) + ' ' + str(t))
        return [tp, p, t]

    @staticmethod
    def calculateScores(tp, p, t, title):
        """

        :param tp: True positive
        :param p: positive
        :param t: true
        :param title: logging indicator
        :return: Fscore, recall, precision
        """
        if p == 0 or t == 0 or tp == 0:
            # logging.warn(title + ' F-Score:0, Recall: 0, Precision: 0' )
            return  [0] * 3

        p = (float)(tp / p)
        r = (float)(tp / t)

        f = round(2 * (r * p) / (r + p),3)
        r = round(r, 3)
        p = round(p, 3)
        if not XPParams.useCrossValidation:
            logging.warn(
            title + ' F-Score: ' + str(f) + ' Recall: ' + str(r) + ' Precision: ' + str(p))

        return [f,r,p]

