import datetime
import os
import sys

from classification import Classification
from corpus import Corpus
from evaluate import Evaluation
from param import Parameters
from parser import Parser
from reports import Report
from parserOfEmbedding import EmbeddedinParser

class Identifier:
    @staticmethod
    def identify():
        for subdir, dirs, files in os.walk(Parameters.configPath):
            for dir in dirs:
                Parameters.languageName = dir
                for subdir1, dirs1, configFiles in os.walk(os.path.join(Parameters.configPath, dir)):

                    corpus = Corpus(os.path.join(Parameters.corpusPath, Parameters.languageName))
                    corpus.printSentsWithEmbeddedMWEs()
                    for configFile in configFiles:
                        if not configFile.endswith('.json'):
                            continue
                        Parameters.configPath = os.path.join(Parameters.configPath, Parameters.languageName, configFile)
                        if Parameters.useCrossValidation:
                            fScore, recall, precision, newIdenMWEs, semiNewIdenMWEs = .0, .0, .0, .0, .0
                            testRange, trainRange = Corpus.getRangs(corpus.trainDataSet)
                            for x in xrange(0, len(testRange)):
                                Parameters.xpPath = os.path.join(Parameters.langFolder, str(x))
                                Parameters(Parameters.configPath, corpus=corpus)
                                corpus.divideSents(testRange,trainRange, x)
                                Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                                clf = Classification.train(corpus.trainingSents)
                                if Parameters.includeEmbedding:
                                    Parser.parse(corpus, clf, EmbeddedinParser)
                                else:
                                    Parser.parse(corpus, clf, Parser)
                                tempfScore, temprecall, tempprecision = Evaluation.evaluate(corpus)

                                fScore += tempfScore
                                recall += temprecall
                                precision += tempprecision

                                x, y = Corpus.getNewIdentifiedMWE(corpus.testingSents)
                                newIdenMWEs += x
                                semiNewIdenMWEs += y

                            print 'F: ', fScore / 5, 'R: ', recall / 5, 'P: ', precision / 5
                            if newIdenMWEs != 0:
                                newIdenMWEs = newIdenMWEs / 5
                            if semiNewIdenMWEs != 0:
                                semiNewIdenMWEs = semiNewIdenMWEs / 5
                            Report.editTotalReadMe(fScore / 5, recall / 5, precision / 5, corpus, [],
                                                   newIdenMWEs, semiNewIdenMWEs)
                        else:
                            Parameters.xpPath = Parameters.langFolder
                            Parameters(Parameters.configPath, corpus=corpus)
                            Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                            clf = Classification.train(corpus.trainingSents)
                            if Parameters.includeEmbedding:
                                Parser.parse(corpus, clf, EmbeddedinParser)
                            else:
                                Parser.parse(corpus, clf, Parser)
                            Evaluation.evaluate(corpus)


reload(sys)
sys.setdefaultencoding('utf8')

Identifier.identify()
