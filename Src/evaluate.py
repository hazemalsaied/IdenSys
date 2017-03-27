from __future__ import division

from param import Parameters
from reports import Report


class Evaluation:
    @staticmethod
    def evaluate( corpus):
        Report.createEvaluationFiles(corpus.testingSents)

        if Parameters.realExper:
            print 'The evaluation is not possible in real exeriements!'
            return  0, 0, 0
        nubCorrectExpectedAnn, nubFoundAnn, nubCorrectFoundAnn = 0, 0, 0

        for sent in corpus.testingSents:

            nubCorrectExpectedAnn += len(sent.vMWEs)
            nubFoundAnn += len(sent.identifiedVMWEs)
            mwesStrings = []
            if len(sent.identifiedVMWEs) > 0:
                for m in sent.vMWEs:
                    mwesStrings.append(m.getString())
                for m in sent.identifiedVMWEs:
                    if m.getString() in mwesStrings:
                        nubCorrectFoundAnn += 1
        if nubCorrectExpectedAnn == 0 or nubFoundAnn == 0:
            print 'Evaluation Failed: Zero values'
            return 0, 0, 0
        recall = nubCorrectFoundAnn / nubCorrectExpectedAnn
        precision = nubCorrectFoundAnn / nubFoundAnn
        fScore = 2 * (recall * precision) / (recall + precision)
        print 'R: ' + str("%.3f" % recall), ' Precision: ' + str("%.3f" % precision), ' F-Score: ' + str(
            "%.3f" % fScore)
        if not Parameters.useCrossValidation:
            Report.editTotalReadMe(fScore, recall, precision, corpus, corpus.testingSents)
        return fScore, recall, precision

    @staticmethod
    def createReport(fScore, recall, precision):
        if Parameters.printReport:
            report = '## Exact Identification Evaluation: ' + '\n'
            report += '#### Recall: ' + str("%.3f" % recall) + '\n'
            report += '#### Precision: ' + str("%.3f" % precision) + '\n'
            report += '#### F-Score: ' + str("%.3f" % fScore) + '\n'
            Report.editReadme('a', report)
