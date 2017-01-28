import datetime
import os
import sys

from classification import Classification
from corpus import Corpus
from evaluate import Evaluation
from param import Parameters
from parser import Parser
from reports import Report


class Identifier:


    @staticmethod
    def identify(configPath, realExper=False):
        for subdir, dirs, files in os.walk(configPath):
            for dir in dirs:
                for subdir1, dirs1, configFiles in os.walk(os.path.join(configPath, dir)):
                    Parameters.languageName = dir
                    corpus = Corpus(os.path.join(Parameters.corpusPath, dir))
                    Report.createLanguageFolder(dir)
                    # corpus, languageName = Identifier.readCorpus(dir)
                    trainingSents, testingSents = Identifier.getTrainAndTestSents(realExper, corpus)
                    Parser.mweDictionary, Parser.mweTokenDic = Identifier.getMWEDic(trainingSents)
                    Report.createMWELexic(Parser.mweDictionary, dir)
                    for configFile in configFiles:
                        if not configFile.endswith('.json'):
                            continue
                        Parameters.configPath = os.path.join(os.path.join(configPath, dir), configFile)
                        Report.createXPFolder(configFile)
                        config = Parameters(os.path.join(os.path.join(configPath, dir), configFile))
                        Report.createConfigAndReadMe(corpus)
                        Identifier.initializeSents(trainingSents)
                        Identifier.initializeSents(testingSents)
                        clf = Identifier.train('', corpus, trainingSents)
                        fScore, recall, precision = Identifier.parse(testingSents, clf, Parser.mweDictionary,
                                                                     Parameters.languageName)
                        Report.editTotalReadMe(fScore, recall, precision , corpus)


    @staticmethod
    def getTrainAndTestSents(realExper, corpus):
        if realExper:
            trainingSents = corpus.sentences
            testingSents = corpus.testSents
        else:
            idx = 0
            trainingSents = []
            testingSents = []
            for sent in corpus.sentences:
                if idx % 5 == 0:
                    testingSents.append(sent)
                else:
                    trainingSents.append(sent)
                idx += 1
        return trainingSents, testingSents

    @staticmethod
    def getMWEDic(trainingSents):
        mweTokenDictionary = {}
        mweDictionary = {}
        for sent in trainingSents:
            for mwe in sent.vMWEs:
                if mwe.getLemmaString() in mweDictionary.keys():
                    mweDictionary[mwe.getLemmaString()] += 1
                    for token in mwe.tokens:
                        if token.lemma.strip() != '':
                            mweTokenDictionary[token.lemma] = 1
                        else:
                            mweTokenDictionary[token.text] = 1
                else:
                    mweDictionary[mwe.getLemmaString()] = 1
                    for token in mwe.tokens:
                        if token.lemma.strip() != '':
                            mweTokenDictionary[token.lemma] = 1
                        else:
                            mweTokenDictionary[token.text] = 1

        for key1 in mweDictionary.keys():
            for key2 in mweDictionary.keys():
                if key1 != key2:
                    if key1 in key2:
                        #if ('\'' in  key1 and '\\' not in  key1) or ('\'' in  key2 and '\\' not in  key2) :
                        #    continue
                        mweDictionary.pop(key1, None)
                    elif key2 in key1:
                        mweDictionary.pop(key2, None)
        return mweDictionary, mweTokenDictionary

    @staticmethod
    def train(x, corpus, trainingSents):

        # if Parameters.useCrossValidation:
        Identifier.initializeSents(corpus.sentences)
        # Training classifier
        clf = Classification.classify(trainingSents, x)
        return clf

    @staticmethod
    def initializeSents(sents):
        # Erasing each effect of the previous iteration
        for sent in sents:
            sent.identifiedVMWEs = []
            sent.initialTransition = None
            sent.featuresInfo = []
            for mwe in sent.vMWEs:
                mwe.isInTrainingCorpus = 0

    @staticmethod
    def parse(testingSents, clf, mweDictionary, languageName, crossIdx=''):

        time = datetime.datetime.now()

        # Parsing the test phrases
        for sent in testingSents:
            Parser.parse(clf[0], clf[1], sent)

        # Adding the source of MWE
        for sent in testingSents:
            for mwe in sent.vMWEs:
                if mwe.getLemmaString() in mweDictionary.keys():
                    mwe.isInTrainingCorpus = mweDictionary[mwe.getLemmaString()]

        # creating a parsing report
        if Parameters.printReport:
            Report.createParsingReport(testingSents, crossIdx)
            # Evaluation

        fScore, recall, precision = Evaluation.evaluate(testingSents)
        # clf.append(fScore)
        print 'Parsing duration: ' + str(datetime.datetime.now() - time)

        goldCorpus = ''
        for sent in testingSents:
            goldCorpus += sent.getCorpusText() + '\n'
        goldtestingCorpusPath = os.path.join(Parameters.xpPath,
                                             languageName + str(crossIdx) + '.gold')
        goldtestingCorpusFile = open(goldtestingCorpusPath, 'w')
        goldtestingCorpusFile.write(goldCorpus)

        predCorpus = ''
        for sent in testingSents:
            predCorpus += sent.getCorpusText(gold=False) + '\n'
        goldtestingCorpusPath = os.path.join(
            Parameters.xpPath, languageName + str(crossIdx) + '.pred')
        goldtestingCorpusFile = open(goldtestingCorpusPath, 'w')
        goldtestingCorpusFile.write(predCorpus)

        return fScore, recall, precision

    @staticmethod
    def getRangs(sents):

        testNum = int(len(sents) * 0.2)
        testRanges = [[0, testNum], [testNum, 2 * testNum], [2 * testNum, 3 * testNum], [3 * testNum, 4 * testNum],
                      [4 * testNum, len(sents)]]

        trainRanges = [[testNum, len(sents)], [0, testNum, 2 * testNum, len(sents)],
                       [0, 2 * testNum, 3 * testNum, len(sents)], [0, 3 * testNum, 4 * testNum, len(sents)],
                       [0, 4 * testNum]]

        return [testRanges, trainRanges]

    @staticmethod
    def divideSents(sents, testing, training, x):

        testingSents = sents[testing[x][0]: testing[x][1]]
        if len(training[x]) == 2:
            trainingSents = sents[training[x][0]: training[x][1]]
        else:
            trainingSents = sents[training[x][0]: training[x][1]] + \
                            sents[training[x][2]: training[x][3]]
        return testingSents, trainingSents

    @staticmethod
    def getStaticParseData(sents):
        trainingData = []
        trainDataLabel = []
        time = datetime.datetime.now()
        for sent in sents:
            trainingInfo = Parser.staticParse(sent)
            if trainingInfo is not None:
                trainDataLabel.extend(trainingInfo[0])
                trainingData.extend(trainingInfo[1])
        return [trainDataLabel, trainingData]


reload(sys)
sys.setdefaultencoding('utf8')

# lst = list(itertools.product([0, 1], repeat=14))
Identifier.identify('Config')
