import reports
from corpus import Corpus
from features import Extractor
from param import XPParams, Counters
from transTypes import TransitionType
from transitions import EmbeddingTransition, Transition

class Parser:

    @staticmethod
    def parse(corpus, clf):
        Counters.initCounters()
        if XPParams.useCrossValidation:
            corpus.initializeSents(training=False)
        for sent in corpus.testingSents:
            if XPParams.includeEmbedding:
                sent.initialTransition = EmbeddingTransition(None, isInitial=True, sent=sent)
            else:
                sent.initialTransition = Transition(None, isInitial=True, sent=sent)
            transition = sent.initialTransition
            feats, labels = [], []
            while not transition.configuration.isTerminalConf():
                newTransition = Parser.getNextTransition(transition, sent, clf[0], clf[1], feats)
                if newTransition is not None:
                    newTransition.apply(transition, sent, parse=True)
                    labels.append(newTransition.type.value)
                    transition = newTransition
            sent.featuresInfo = [labels, feats]
        reports.createParsingReport(corpus.testingSents, Corpus.mweDictionary)

    @staticmethod
    def getNextTransition(transition, sent, classifier, dictVectorizer, feats):

        legalTansDic = transition.getLegalTransDic()
        if len(legalTansDic) == 1:
            return Transition.initialize(legalTansDic.keys()[0], sent)
        featDic = Extractor.getFeatures(transition, sent)
        if not isinstance(featDic,list):
            featDic = [featDic]
        transTypeValue = classifier.predict(dictVectorizer.transform(featDic))[0]
        transType = TransitionType.getType(transTypeValue)
        if transType in legalTansDic:
            return legalTansDic[transType]
        if len(legalTansDic):
            return Transition.initialize(legalTansDic.keys()[0], sent)
        print sent
        raise
