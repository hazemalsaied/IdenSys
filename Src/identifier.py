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
        # reports.getEmbeddedSents(corpus)
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
    # report = ''
    # for sent in corpus.testingSents:
    #     if sent.identifiedVMWEs:
    #         for vmwe1 in sent.identifiedVMWEs:
    #            if len(vmwe1.tokens) == 1:
    #                exist = False
    #                for vmwe2 in sent.vMWEs:
    #                    if vmwe1 == vmwe2:
    #                        exist = True
    #                if not exist:
    #                    report += '#' + vmwe1.getLemmaString() + '\n\n' + '##Training dataset:'+ '\n\n'
    #                    if vmwe1.getLemmaString() in Corpus.mwtDictionaryWithSent and Corpus.mwtDictionaryWithSent[vmwe1.getLemmaString()] is not None :
    #                        for sent1 in Corpus.mwtDictionaryWithSent[vmwe1.getLemmaString()]:
    #                            report += str(sent1) + '\n\n'
    #                        report += '##Testing dataset:'+ '\n\n' + str(sent)
    # path = os.path.join(Paths.rootResultFolder, 'DE-MWT-annotation issues.md')
    # with open(path, 'a') as f:
    #     f.write(report)


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
        report, report2 = '', ''
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

XPParams.realExper = True

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




# corpus.update()
# print len(corpus.trainingSents)
# print len(corpus.testingSents)
# newvmweNum, vmweNum = 0, 0
# print corpus.mweNum
# newDic, newDicTotal = {}, {}
# for sent in corpus.testingSents:
#     for vmwe in sent.vMWEs:
#         vmweNum += 1
#         newDicTotal[vmwe.getLemmaString()] = 1
#         if vmwe.getLemmaString() not in Corpus.mweDictionary:
#             newvmweNum += 1
#             if vmwe.getLemmaString() in newDic:
#                 newDic[vmwe.getLemmaString()] += 1
#             else:
#                 newDic[vmwe.getLemmaString()] = 0
# print float(newvmweNum) / vmweNum
# print len(newDic)
# print len(newDicTotal)


