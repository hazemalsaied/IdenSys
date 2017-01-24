import datetime
import os
import pickle
import sys

from classification import Classification
from corpus import Corpus
from evaluate import Evaluation
from param import Parameters
from parser import Parser
from reports import Report


class Identifier:
    config = {}

    @staticmethod
    def identify(realExper=False):

        time = datetime.datetime.now()
        corpus, languageName = Identifier.readCorpus()
        print 'Reading Corpus duration: ' + str(datetime.datetime.now() - time)

        Report.createResultFolder(corpus)

        if not realExper and Parameters.useCrossValidation:
            fScore, recall, precision = .0, .0, .0
            testRange, trainRange = Identifier.getRangs(corpus.sentences)

            for x in xrange(0, len(testRange)):
                testingSents, trainingSents = Identifier.divideSents(corpus.sentences, testRange,
                                                                     trainRange, x)
                mweDictionary = {}
                clfs = Identifier.train(x, corpus, trainingSents, testingSents, languageName, mweDictionary)
                tempfScore, temprecall, tempprecision = Identifier.parse(testingSents, clfs, mweDictionary,
                                                                         languageName, x)
                fScore += tempfScore
                recall += temprecall
                precision += tempprecision
            fScore = fScore / 5
            recall = recall / 5
            precision = precision / 5

            if Parameters.printReport:
                result = '## The Total Score for cross validation : F-score' + str(
                    "%.3f" % fScore) + ' ,Recall: ' + str("%.3f" % recall) + ' ,Precision: ' + str("%.3f" % precision)
                Report.editReadme('a', result)
            return fScore , recall, precision

        else:
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

            mweDictionary = {}
            clf = Identifier.train(6, corpus, trainingSents, testingSents, languageName, mweDictionary)
            return Identifier.parse(testingSents, clf, mweDictionary, languageName, 6)

    @staticmethod
    def train(x, corpus, trainingSents, testingSents, languageName, mweDictionary):

        time = datetime.datetime.now()
        # if Parameters.useCrossValidation:
        # Erasing each effect of the previous iteration
        for sent in corpus.sentences:
            sent.identifiedVMWEs = []
            sent.initialTransition = None
            sent.featuresInfo = []
            for mwe in sent.vMWEs:
                mwe.isInTrainingCorpus = 0
        # Create MWE dictionary

        for sent in trainingSents:
            for mwe in sent.vMWEs:
                if mwe.getLemmaString() in mweDictionary.keys():
                    mweDictionary[mwe.getLemmaString()] += 1
                else:
                    mweDictionary[mwe.getLemmaString()] = 1

                    # Training classifier
        clf = Classification.classify(trainingSents, x)
        print 'Traingin duration: ' + str(datetime.datetime.now() - time)
        return clf

    @staticmethod
    def parse(testingSents, clf, mweDictionary, languageName, crossIdx):

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
        goldtestingCorpusPath = os.path.join(Parameters.resultPath,
                                             languageName + str(crossIdx) + '.gold')
        goldtestingCorpusFile = open(goldtestingCorpusPath, 'w')
        goldtestingCorpusFile.write(goldCorpus)

        predCorpus = ''
        for sent in testingSents:
            predCorpus += sent.getCorpusText(gold=False) + '\n'
        goldtestingCorpusPath = os.path.join(
            Parameters.resultPath, languageName + str(crossIdx) + '.pred')
        goldtestingCorpusFile = open(goldtestingCorpusPath, 'w')
        goldtestingCorpusFile.write(predCorpus)

        return fScore, recall, precision

    @staticmethod
    def readCorpus():

        languageName = Parameters.corpusPath.split('/')[-1]
        if languageName.strip() == '':
            languageName = Parameters.corpusPath.split('/')[-2]
        if not os.path.exists(Parameters.dumpingPath):
            os.makedirs(Parameters.dumpingPath)

        if Parameters.serialize:
            # Reading the corpus
            corpus = Corpus(Parameters.corpusPath)
            with open(os.path.join(Parameters.dumpingPath, languageName + '.pickle'), 'wb') as f:
                pickle.dump(corpus, f)
        else:
            with open(os.path.join(Parameters.dumpingPath, languageName + '.pickle'), 'rb') as f:
                corpus = pickle.load(f)
        return corpus, languageName

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
            # Parse the sentence
            trainingInfo = Parser.staticParse(sent)
            if trainingInfo is not None:
                trainDataLabel.extend(trainingInfo[0])
                trainingData.extend(trainingInfo[1])
        return [trainDataLabel, trainingData]


reload(sys)
sys.setdefaultencoding('utf8')
readMe = "/Users/hazemalsaied/Parseme/MWEIdSys/Results/readMe.md"
if not os.path.isfile(readMe):
    staticParsingFile = open(readMe, 'w')
else:
    staticParsingFile = open(readMe, 'a')
#staticParsingFile.write('')

for subdir, dirs, files in os.walk('Config'):
    for dir in dirs:
        for subdir1, dirs1, files1 in os.walk(os.path.join('Config', dir)):
            report = '# The experiementations on ' + dir + '\n'
            with open(readMe, "a") as staticParsingFile:
                staticParsingFile.write(report)
            for file in files1:
                path = os.path.join(os.path.join('Config', dir), file)
                print path
                config = Parameters(path)
                fScore, recall, precision = Identifier.identify()
                report = '### The Score of the experiementation ' + str(Parameters.xpName) + ' is' + '\n' + 'F-score: '  + str(
                    "%.3f" % fScore) + ' ,Recall: ' + str("%.3f" % recall) + ' ,Precision: ' + str("%.3f" % precision) + '\n\n'
                with open(readMe, "a") as staticParsingFile:
                    staticParsingFile.write(report)
# configPath = 'Config/FR/tuned.json'
# config = Parameters(configPath )
# print Parameters.toBinary()
# Identifier.identify()
