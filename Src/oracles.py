import datetime
import logging
import random
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Perceptron
from sklearn.multiclass import OutputCodeClassifier
from sklearn.svm import LinearSVC

import reports
from transTypes import TransitionType
from features import Extractor
from param import XPParams
from perceptron import MultiClassPerceptron, Vectorizer
from transitions import Reduce, BlackMerge, Transition, \
    Complete, MWTComplete, Merge, EmbeddingTransition, MergeAsMWT
from transitions import Shift


class Oracle:
    @staticmethod
    def train(corpus):
        time = datetime.datetime.now()
        if XPParams.useDynamicOracle:
            clf = DynamicOracle.train(corpus)
        elif XPParams.useHybridOracle:
            logging.info('Hybrid Oracle training')
            clf = HybridOracle.train(corpus)
        else:
            clf = StaticOracle.train(corpus)
        reports.createStaticParsingReports(corpus.trainingSents)
        # reports.createOracleErrorsReport(corpus)
        logging.info('Traingin Time: ' + str(int((datetime.datetime.now() - time).seconds / 60.)))
        return clf

class StaticOracle:

    @staticmethod
    def train(corpus):
        if XPParams.includeEmbedding:
            logging.info('Static Embedding Oracle')
            Y, X_dic = StaticOracle.parseCorpus(corpus.trainingSents, EmbeddingOracle)
        else:
            logging.info('Static Oracle')
            Y, X_dic = StaticOracle.parseCorpus(corpus.trainingSents, StaticOracle)

        vec = DictVectorizer()
        X = vec.fit_transform(X_dic)
        if XPParams.usePerceptron:
            transTypes = TransitionType.getAllClasses()
            featureData = []
            vec = Vectorizer()
            for i in range(len(Y)):
                featureData.append([Y[i], vec.vectorize(X_dic[i])])
            clf = MultiClassPerceptron(transTypes, featureSet=vec.featureSet, featureData=featureData)
            clf.train()
        else:
            clf = OutputCodeClassifier(Perceptron())
            # LinearSVC(random_state=0), code_size=2, random_state=0)
            clf.fit(X, Y)
        return clf, vec

    @staticmethod
    def parseCorpus(sents, cls):
        labels, features = [],[]
        for sent in sents:
            # Parse the sentence
            trainingInfo = cls.parseSentence(sent, cls)
            if trainingInfo is not None:
                labels.extend(trainingInfo[0])
                features.extend(trainingInfo[1])

        return labels, features

    @staticmethod
    def parseSentence(sent, cls):

        # Create the initial transition
        transition = Transition(isInitial=True, sent=sent)
        while not transition.isTerminal():
            transition = cls.getNextTransition(transition, sent)
        sent.initialTransition = transition.getRoot()
        labels, features = Extractor.extract(sent)
        return labels, features

    @staticmethod
    def getNextTransition(parent, sent):

        config = parent.configuration
        if config.isInitial:
            shift = Shift(sent=sent)
            shift.apply(parent, sent)
            return shift

        newTransition = MWTComplete.check( parent)
        if newTransition is not None:
            return newTransition

        # Check for VMWE complete
        newTransition = Complete.checkForVMWE( parent)
        if newTransition is not None:
            return newTransition

        newTransition = Merge.check(parent)
        if newTransition is not None:
            return newTransition

        # Check for VMWE complete
        newTransition = Complete.checkForToken(parent)
        if newTransition is not None:
            return newTransition

        if not config.buffer and config.stack:
            complete = Complete(sent=sent)
            complete.apply(parent, sent)
            return complete
        # Apply the default transition: SHIFT
        shift = Shift(sent=sent)
        shift.apply(parent,sent)
        return shift

class EmbeddingOracle(StaticOracle):

    @staticmethod
    def parseSentence(sent, cls):

        sent.initialTransition = EmbeddingTransition(isInitial=True, sent=sent)
        transition = sent.initialTransition
        while not transition.isTerminal():
            transition = cls.getNextTransition(transition, sent)
        labels, features = Extractor.extract(sent)
        return labels, features

    @staticmethod
    def getNextTransition(parent, sent):
        # if len(sent.vMWEs) > 0:
        #     pass
        config = parent.configuration
        if config.isInitial:
            shift = Shift(sent=sent)
            shift.apply(parent, sent)
            return shift

        newTransition = MergeAsMWT.check(parent)
        if newTransition is not None:
            return newTransition

        newTransition = BlackMerge.check( parent)
        if newTransition is not None:
            return newTransition

        # Check for VMWE complete
        newTransition = Reduce.check(parent)
        if newTransition is not None:
            return newTransition

        # Apply the default transition: SHIFT
        shift = Shift(sent=sent)
        shift.apply(parent,sent)
        return shift

class DynamicOracle:

    @staticmethod
    def train(corpus):
        transTypes = TransitionType.getAllClasses()
        clf = MultiClassPerceptron(transTypes)
        vec = Vectorizer(clf)
        trainIdx= 0
        for iterIdx in range(XPParams.perceptronIterations):
            if iterIdx >= XPParams.explorationIteration:
                logging.warn('With Exploration')
            np.random.shuffle(corpus.trainingSents)
            printIdx = 0
            for sent in corpus:
                printSent = False
                if len(sent.vMWEs) > 1 and (len(sent.vMWEs[0].tokens) == 1 or len(sent.vMWEs[1].tokens) == 1) and printIdx  < 7:
                    printIdx += 1
                    printSent = False
                    # print sent
                if XPParams.includeEmbedding:
                    transition = EmbeddingTransition(isInitial=True, sent=sent)
                else:
                    transition = Transition(isInitial=True, sent=sent)
                while not transition.isTerminal():
                    trainIdx += 1
                    legalTransDic = transition.getLegalTransDic()
                    if printSent:
                        print 'legalTransDic', legalTransDic.keys()
                    zeroCostTransTypes = TransitionType.sort(transition.getZeroCostTransType())
                    if printSent:
                        print 'zeroCostTransTypes', zeroCostTransTypes
                    featureDict = vec.vectorize(Extractor.getFeatures(transition, sent),updateWeights=True)
                    argMax, predictedTransTypeValue = 0, transTypes[0]
                    for transType in transTypes:
                        current_activation = clf.getCurrentActivation(featureDict, transType)
                        if current_activation >= argMax:
                            argMax, predictedTransTypeValue = current_activation, transType
                    if printSent:
                        print 'predictedTransTypeValue', predictedTransTypeValue
                    argMax, zeroCostTransTypevalue = 0, zeroCostTransTypes[0].value
                    for transType in zeroCostTransTypes:
                        current_activation = clf.getCurrentActivation(featureDict, transType.value)
                        if current_activation >= argMax:
                            argMax, zeroCostTransTypevalue = current_activation, transType.value
                    if printSent:
                        print 'zeroCostTransTypevalue', zeroCostTransTypevalue
                    if not TransitionType.inZeroCostTrans(predictedTransTypeValue, zeroCostTransTypes):
                        clf.updateWeights(featureDict, zeroCostTransTypevalue, trainIdx=trainIdx)
                        clf.updateWeights(featureDict, predictedTransTypeValue, add=False, trainIdx=trainIdx)
                        if DynamicOracle.explore(iterIdx):
                            predictedTransType = TransitionType.getType(predictedTransTypeValue)
                            if predictedTransType not in legalTransDic.keys():
                                nextTransition = random.choice(legalTransDic.values())
                            else:
                                nextTransition = legalTransDic[predictedTransType]
                        else:
                            nextTransition = Transition.initialize(zeroCostTransTypevalue, sent)
                    else:
                        nextTransition = Transition.initialize(predictedTransTypeValue, sent)
                    if printSent:
                        print 'nextTransition', nextTransition.type
                    nextTransition.apply(transition, sent)
                    transition = nextTransition
        clf.getAveregedWeights(trainIdx)
        reports.creatOnlineTrainingReport()
        return [clf, vec]

    @staticmethod
    def trainFolds(corpus, clf=None, vec=None, foldSize=5):
        transTypes = TransitionType.getAllClasses()
        if clf is None or vec is None:
            clf = MultiClassPerceptron(transTypes)
            vec = Vectorizer(clf)
        trainIdx = 0
        for iterIdx in range(foldSize):
            np.random.shuffle(corpus.trainingSents)
            for sent in corpus:
                if XPParams.includeEmbedding:
                    transition = EmbeddingTransition(isInitial=True, sent=sent)
                else:
                    transition = Transition(isInitial=True, sent=sent)
                while not transition.isTerminal():
                    trainIdx += 1
                    legalTransDic = transition.getLegalTransDic()
                    zeroCostTransTypes = TransitionType.sort(transition.getZeroCostTransType())
                    featureDict = vec.vectorize(Extractor.getFeatures(transition, sent), updateWeights=True)
                    argMax, predictedTransTypeValue = 0, transTypes[0]
                    for transType in transTypes:
                        current_activation = clf.getCurrentActivation(featureDict, transType)
                        if current_activation >= argMax:
                            argMax, predictedTransTypeValue = current_activation, transType

                    argMax, zeroCostTransTypevalue = 0, zeroCostTransTypes[0].value
                    for transType in zeroCostTransTypes:
                        current_activation = clf.getCurrentActivation(featureDict, transType.value)
                        if current_activation >= argMax:
                            argMax, zeroCostTransTypevalue = current_activation, transType.value
                    if not TransitionType.inZeroCostTrans(predictedTransTypeValue, zeroCostTransTypes):
                        clf.updateWeights(featureDict, zeroCostTransTypevalue, trainIdx=trainIdx)
                        clf.updateWeights(featureDict, predictedTransTypeValue, add=False, trainIdx=trainIdx)
                        if DynamicOracle.explore(iterIdx):
                            predictedTransType = TransitionType.getType(predictedTransTypeValue)
                            if predictedTransType not in legalTransDic.keys():
                                nextTransition = Transition.initialize(random.choice(legalTransDic.keys()), sent)
                            else:
                                nextTransition = Transition.initialize(predictedTransType, sent)
                        else:
                            nextTransition = Transition.initialize(zeroCostTransTypevalue, sent)
                    else:
                        nextTransition = Transition.initialize(predictedTransTypeValue, sent)
                    nextTransition.apply(transition, sent)
                    transition = nextTransition
        return [clf, vec]

    @staticmethod
    def explore(iterationIdx):
        if iterationIdx >= XPParams.explorationIteration and random.getrandbits(1):
            return True
        return False

class HybridOracle:

    @staticmethod
    def train(corpus):
        if XPParams.useCrossValidation:
            corpus.initializeSents()
        logging.warn('HybridOracle')
        clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)
        feats, labels, transitinIdx, transitionThreshold, randommlySelectedIdx = [], [], 0, int(
            corpus.tokenNum * 2 * XPParams.randomSelectionPercentage), 0
        for sent in corpus.trainingSents:
            transition = EmbeddingTransition(isInitial=True, sent=sent)
            transitinIdx += 1
            while not transition.isTerminal():
                legalTransDic = transition.getLegalTransDic()
                randomSelection = XPParams.useHybridOracle and transitinIdx >= transitionThreshold and random.getrandbits(
                    1)
                optimalTransTypes = transition.getOptimalTransTypes()
                if randomSelection:
                    sent.withRandomSelection = True
                    randommlySelectedIdx += 1
                    nextTransition = random.choice(legalTransDic.values())
                else:
                    nextTransition = legalTransDic[optimalTransTypes[0]]
                feats.append(Extractor.getFeatures(transition, sent))
                labels.append(optimalTransTypes[0].value)
                nextTransition.apply(transition, sent)

                transition = nextTransition
                transitinIdx += 1
        logging.warn('Randomlly selected : ' + str(randommlySelectedIdx) + ' ' + str((corpus.tokenNum * 2)))

        vec = DictVectorizer()
        X = vec.fit_transform(feats)
        Y = np.asarray(labels)
        clf.fit(X, Y)
        return clf, vec

