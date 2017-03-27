from configuration import Configuration
from corpus import Token
from corpus import Corpus, VMWE, Sentence
from param import Parameters
from transition import Transition, Complete, Shift, Merge, MWTComplete
from transition import TransitionType
from features import Extractor
from evaluate import Evaluation
from reports import Report


class Parser:
    @staticmethod
    def parse(corpus, clf, cls, crossIdx=''):

        if Parameters.useCrossValidation:
            Corpus.initializeSents(corpus.testingSents)
        # Parsing the test phrases
        for sent in corpus.testingSents:
            cls.parseSentence(clf[0], clf[1], sent, cls)

        # creating a parsing report
        Report.createParsingReport(corpus.testingSents, Corpus.mweDictionary, crossIdx)

    @staticmethod
    def parseSentence(classifier, dictVectorizer, sent, cls):

        initialTransition = Transition(None, isInitial=True, sent=sent)
        transition = initialTransition
        feats, labels = [], []
        while not transition.configuration.isTerminalConf():
            newTransition = cls.getNextTransition(transition, sent, classifier, dictVectorizer, feats)
            if newTransition is not None:
                newTransition.apply(transition, sent=sent, parse=True)
                labels.append(newTransition.type.value)
            transition = newTransition
        sent.initialTransition = initialTransition
        sent.featuresInfo = [labels, feats]
        return sent

    @staticmethod
    def getNextTransition(transition, sent, classifier, dictVectorizer, feats):

        config = transition.configuration
        complete, mwtComplete, shift, merge = Complete(), MWTComplete(), Shift(), Merge()
        if len(config.stack) == 0 and len(config.buffer) > 0:
            feats.append({})
            return Shift()

        if (len(config.buffer) == 0 and len(config.stack) == 1) \
                or (len(config.stack) == 1 and isinstance(config.stack[0], list)):
            if Parameters.enableSingleMWE:
                if isinstance(config.stack[0], Token) and config.stack[0].lemma in Corpus.mweDictionary.keys():
                    feats.append({})
                    return mwtComplete
            feats.append({})
            return Complete()

        acceptedTrans = [shift, complete, mwtComplete, merge]
        if not Parameters.enableSingleMWE:
            acceptedTrans.remove(mwtComplete)

        if len(config.stack) == 0:
            acceptedTrans.remove(complete)

        if len(config.stack) < 2:
            acceptedTrans.remove(merge)

        if len(config.buffer) == 0:
            acceptedTrans.remove(shift)

        if len(acceptedTrans) == 1:
            feats.append({})
            return acceptedTrans[0]

        featDic = Extractor.getFeatures(transition, sent)
        transTypes = (list)(classifier.decision_function(dictVectorizer.transform(featDic))[0])
        orderedTransTypes = list(sorted(transTypes, reverse=True))

        for transType in orderedTransTypes:
            for elem in acceptedTrans:
                if elem.type.value == transTypes.index(transType):
                    feats.append(featDic)
                    return elem
        return None
