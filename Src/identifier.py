import os
import sys

from Src.parsers import EmbeddedinParser
from classification import Classification
from corpus import Corpus
from evaluation import Evaluation
from param import FeatParams, XPParams, Paths
from parsers import Parser
from reports import Report


class Identifier:
    @staticmethod
    def identify():
        Report.createRootResultFolder()
        for subdir, dirs, files in os.walk(Paths.configsFolder):
            for dir in dirs:
                Paths.languageName = dir
                for subdir1, dirs1, configFiles in os.walk(os.path.join(Paths.configsFolder, dir)):

                    corpus = Corpus(os.path.join(Paths.corpusPath, Paths.languageName))
                    for configFile in configFiles:
                        if not configFile.endswith('.json'):
                            continue
                        Paths.configsFolder = os.path.join(Paths.configsFolder, Paths.languageName,
                                                                configFile)
                        if XPParams.useCrossValidation:
                            fScore, recall, precision, newIdenMWEs, semiNewIdenMWEs = .0, .0, .0, .0, .0
                            testRange, trainRange = Corpus.getRangs(corpus.trainDataSet)
                            for x in xrange(0, len(testRange)):
                                Paths.xpPath = os.path.join(Paths.langResultFolder, str(x))
                                FeatParams(Paths.configsFolder, corpus=corpus)
                                corpus.divideSents(testRange, trainRange, x)
                                Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                                clf = Classification.train(corpus.trainingSents)
                                if XPParams.includeEmbedding:
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
                            Paths.xpPath = Paths.langResultFolder
                            FeatParams(Paths.configsFolder, corpus=corpus)
                            Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                            clf = Classification.train(corpus.trainingSents)
                            if XPParams.includeEmbedding:
                                Parser.parse(corpus, clf, EmbeddedinParser)
                            else:
                                Parser.parse(corpus, clf, Parser)
                            Evaluation.evaluate(corpus)


reload(sys)
sys.setdefaultencoding('utf8')

Identifier.identify()
