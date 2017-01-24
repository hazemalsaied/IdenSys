from __future__ import division

from param import Parameters
from reports import Report


class Evaluation:
    @staticmethod
    def evaluate(sents):
        nubCorrectExpectedAnn = 0
        nubFoundAnn = 0
        nubCorrectFoundAnn = 0

        for sent in sents:

            nubCorrectExpectedAnn += len(sent.vMWEs)
            nubFoundAnn += len(sent.identifiedVMWEs)
            mwesStrings = []
            for m in sent.vMWEs:
                mwesStrings.append(m.getString())
            for m in sent.identifiedVMWEs:
                if m.getString() in mwesStrings:
                    nubCorrectFoundAnn += 1
        if nubCorrectExpectedAnn == 0 or nubFoundAnn == 0:
            print 'Evaluation Failed: Zero values'
            return
        recall = nubCorrectFoundAnn / nubCorrectExpectedAnn
        precision = nubCorrectFoundAnn / nubFoundAnn
        fScore = 2 * (recall * precision) / (recall + precision)

        print "%.3f" % 12.34432645373647

        if Parameters.printReport:
            report = '## Exact Identification Evaluation: ' + '\n'
            report += '#### Recall: ' + str("%.3f" % recall) + '\n'
            report += '#### Precision: ' + str("%.3f" % precision) + '\n'
            report += '#### F-Score: ' + str("%.3f" % fScore) + '\n'
            Report.editReadme('a', report)

        print 'Recall: ' + str("%.3f" % recall)
        print 'Precision: ' + str("%.3f" % precision)
        print 'F-Score: ' + str("%.3f" % fScore)
        return fScore, recall, precision
