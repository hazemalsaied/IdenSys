from __future__ import division

from param import PrintParams, XPParams, Paths
from reports import Report
import logging


class Evaluation:
    @staticmethod
    def evaluate(corpus, resultFilePath=Paths.evalResultsFile):
        if not XPParams.baseline:
            Report.createEvaluationFiles(corpus.testingSents)

        if XPParams.realExper:
            logging.warning('The evaluation is not possible in **real exeriements**!')
            return 0, 0, 0
        nubCorrectExpectedAnn, nubFoundAnn, nubCorrectFoundAnn, nubCorrectWithCatFoundAnn = 0, 0, 0, 0

        for sent in corpus.testingSents:

            nubCorrectExpectedAnn += len(sent.vMWEs)
            nubFoundAnn += len(sent.identifiedVMWEs)

            if len(sent.identifiedVMWEs) > 0:
                processedVmwe = []
                for m in sent.identifiedVMWEs:
                    for vMWE in sent.vMWEs:
                        if m.getString() == vMWE.getString() and vMWE not in processedVmwe:
                            processedVmwe.append(vMWE)
                            nubCorrectFoundAnn += 1
                            if m.type == vMWE.type:
                                nubCorrectWithCatFoundAnn += 1
        if nubCorrectExpectedAnn == 0 or nubFoundAnn == 0:
            logging.warning('Evaluation Failed: Zero values')
            return 0, 0, 0
        recall = nubCorrectFoundAnn / nubCorrectExpectedAnn
        precision = nubCorrectFoundAnn / nubFoundAnn
        if recall + precision != 0:
            fScore = 2 * (recall * precision) / (recall + precision)
        else:
            fScore = 0
        logging.info('R: ' + str("%.3f" % recall)+ ' Precision: ' + str("%.3f" % precision)+
                     ' F-Score: ' + str("%.3f" % fScore))

        if XPParams.includeEmbedding:
            # Evaluation of category identification :
            r = nubCorrectWithCatFoundAnn / nubCorrectExpectedAnn
            p = nubCorrectWithCatFoundAnn / nubFoundAnn
            f = 0
            if r + p != 0:
                f = (2 * (r * p) / (r + p))

            logging.info('Evaluation of Category identification:')
            logging.info('R: ' + str("%.3f" % r)+ ' Precision: ' + str("%.3f" % p)+ ' F-Score: ' + str("%.3f" % f))

        if not XPParams.useCrossValidation:
            Report.editTotalReadMe(fScore, recall, precision, corpus, corpus.testingSents, path=resultFilePath)
        return fScore, recall, precision

    @staticmethod
    def createReport(fScore, recall, precision):
        if PrintParams.printReport:
            report = '## Exact Identification Evaluation: ' + '\n'
            report += '#### Recall: ' + str("%.3f" % recall) + '\n'
            report += '#### Precision: ' + str("%.3f" % precision) + '\n'
            report += '#### F-Score: ' + str("%.3f" % fScore) + '\n'
            Report.editReadme('a', report)
