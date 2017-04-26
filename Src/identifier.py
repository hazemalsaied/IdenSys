import os
import sys

from classification import Classification
from corpus import Corpus
from evaluation import Evaluation
from param import FeatParams, XPParams, Paths
from parsers import Parser, EmbeddedingParser
from reports import Report
import logging


class Identifier:
    @staticmethod
    def identify():
        logging.basicConfig(level=logging.DEBUG)
        Report.createRootResultFolder()
        constantConfigFolder = Paths.configsFolder
        for subdir, dirs, files in os.walk(constantConfigFolder):
            for dir in dirs:
                Paths.languageName = dir
                for subdir1, dirs1, configFiles in os.walk(os.path.join(constantConfigFolder, dir)):
                    logging.info('Processing : ' + Paths.languageName)
                    corpus = Corpus(os.path.join(Paths.corporaPath, Paths.languageName))
                    logging.info('corpus reading is done!')
                    for configFile in configFiles:
                        if not configFile.endswith('.json'):
                            continue
                        Paths.configsFolder = os.path.join(constantConfigFolder, Paths.languageName,
                                                           configFile)
                        if XPParams.useCrossValidation:
                            logging.info('Cross validation iterations:')
                            fScore, recall, precision, newIdenMWEs, semiNewIdenMWEs = .0, .0, .0, .0, .0
                            testRange, trainRange = Corpus.getRangs(corpus.trainDataSet)
                            for x in xrange(0, len(testRange)):
                                logging.info('Iteration no.' + str(x + 1))
                                Paths.iterationPath = os.path.join(Paths.langResultFolder, str(x + 1))
                                if not os.path.exists(Paths.iterationPath):
                                    os.makedirs(Paths.iterationPath)
                                FeatParams(Paths.configsFolder, corpus=corpus)
                                corpus.divideSents(testRange, trainRange, x)
                                Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                                logging.info('Training : ')
                                clf = Classification.train(corpus.trainingSents)
                                if XPParams.includeEmbedding:
                                    logging.warn('Parser : Embeddeding Parser')
                                    Parser.parse(corpus, clf, EmbeddedingParser)
                                else:
                                    logging.warn('Parser : Normal Parser')
                                    Parser.parse(corpus, clf, Parser)
                                tempfScore, temprecall, tempprecision = Evaluation.evaluate(corpus)

                                fScore += tempfScore
                                recall += temprecall
                                precision += tempprecision

                                x, y = Corpus.getNewIdentifiedMWE(corpus.testingSents)
                                newIdenMWEs += x
                                semiNewIdenMWEs += y

                            logging.warn('F: ' + str(fScore / 5) + 'R: ' + str(recall / 5) + 'P: ' + str(precision / 5))
                            if newIdenMWEs != 0:
                                newIdenMWEs = newIdenMWEs / 5
                            if semiNewIdenMWEs != 0:
                                semiNewIdenMWEs = semiNewIdenMWEs / 5
                            Report.editTotalReadMe(fScore / 5, recall / 5, precision / 5, corpus, [],
                                                   newIdenMWEs, semiNewIdenMWEs, path= os.path.join(Paths.rootResultFolder, 'results.csv'))
                        else:

                            FeatParams(Paths.configsFolder, corpus=corpus)
                            Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                            logging.info('Trainging')
                            clf = Classification.train(corpus.trainingSents)
                            if XPParams.includeEmbedding:
                                Parser.parse(corpus, clf, EmbeddedingParser)
                            else:
                                Parser.parse(corpus, clf, Parser)
                            Evaluation.evaluate(corpus, resultFilePath= os.path.join(Paths.rootResultFolder, 'results.csv'))


reload(sys)
sys.setdefaultencoding('utf8')

Identifier.identify()
