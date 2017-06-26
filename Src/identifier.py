import logging
import os
import sys

from oracles import Oracle, DynamicOracle
from corpus import Corpus
from evaluation import Evaluation
from param import FeatParams, XPParams, Paths
from parsers import Parser
import reports

def identify():
    reports.createRootResultFolder()
    constantConfigFolder = Paths.configsFolder
    for configFile in os.listdir(Paths.configsFolder):
        if not configFile.endswith('.json'):
            continue
        corpus = Corpus(configFile[:2])
        reports.getEmbeddedSents(corpus)
        FeatParams(os.path.join(constantConfigFolder, configFile), corpus=corpus)
        if XPParams.useCrossValidation:
            scores = [0] * 12
            testRange, trainRange = corpus.getRangs()
            for x in range(len(testRange)):
                logging.warn('Iteration no.' + str(x + 1))
                XPParams.currentIteration = x
                Paths.iterationPath = os.path.join(Paths.langResultFolder, str(x + 1))
                if not os.path.exists(Paths.iterationPath):
                    os.makedirs(Paths.iterationPath)
                evalScores = identifyCorpus(corpus)
                for i in range(len(evalScores)):
                    scores[i] += evalScores[i]
            for i in range(len(scores)):
                scores[i] = scores[i] / float(len(testRange))
            logging.warn(' F-Score: ' + str(scores[0]))
            reports.editTotalReadMe(scores, corpus)
        else:
            # identifyCorpusWithIterations(corpus)
            scores = identifyCorpus(corpus)
            reports.editTotalReadMe(scores, corpus)

def identifyCorpus(corpus):
    corpus.update()
    clf = Oracle.train(corpus)
    Parser.parse(corpus, clf)
    scores = Evaluation.evaluate(corpus)
    return scores

def identifyCorpusWithIterations(corpus):
    foldSize = 5
    corpus.update()
    for i in range(int(XPParams.perceptronIterations / foldSize)):
        if i == 0:
            clf = DynamicOracle.trainFolds(corpus)
        else:
            clf = DynamicOracle.trainFolds(corpus, clf[0] , clf[1], foldSize)
        corpus.initializeSents(training=False)
        Parser.parse(corpus, clf)
        scores = Evaluation.evaluate(corpus)
        reports.editTotalReadMe(scores, corpus)
        report = ''
        report2 = ''
        for sent in corpus.testingSents:
            if len(sent.vMWEs) > 0:
                report += str(sent)
            if len(sent.identifiedVMWEs)> 0:
                report2 += str(sent)
        p2 = os.path.join(Paths.langResultFolder, str(i) + ' - testSents.md')
        with open(p2, 'w') as f:
            f.write(report)
        p3 = os.path.join(Paths.langResultFolder, str(i) + ' - testSents - Identified.md')
        with open(p3, 'w') as f:
            f.write(report2)

    return scores

reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(level=logging.WARNING)

identify()

# FeatParams.smartMWTDetection = True
# XPParams.useCrossValidation = True
# XPParams.perceptronIterations = 7
# XPParams.explorationIteration = 6
#
# # #CV + static + simpl + preceptron
# # XPParams.includeEmbedding = False
# # XPParams.usePerceptron = True
# # identify()
# #
# #
# # XPParams.includeEmbedding = True
# # XPParams.usePerceptron = False
# # #CV + static + Embedd + Sci-kit
# # identify()
# #
# # XPParams.usePerceptron = True
# # identify()
# # XPParams.useHybridOracle= True
# # identify()
# XPParams.useDynamicOracle= True
# identify()
#
