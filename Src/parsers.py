from Src.transitions import Reduce, WhiteMerge, MergeAsID, MergeAsLVC, MergeAsVPC, MergeAsIReflV, \
    MergeAsOTH
from corpus import Corpus
from corpus import Token
from features import Extractor
from param import FeatParams, XPParams
from reports import Report
from transitions import Transition, Complete, Shift, Merge, MWTComplete


class Parser:
    @staticmethod
    def parse(corpus, clf, cls, crossIdx=''):

        if XPParams.useCrossValidation:
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
            else:
                print 'Error: transition generation is broken for the sent = ', sent
                break
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
            if FeatParams.enableSingleMWE:
                if isinstance(config.stack[0], Token) and config.stack[0].lemma in Corpus.mweDictionary.keys():
                    feats.append({})
                    return mwtComplete
            feats.append({})
            return Complete()

        acceptedTrans = [shift, complete, mwtComplete, merge]
        if not FeatParams.enableSingleMWE:
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
        transType = classifier.predict(dictVectorizer.transform(featDic))[0]

        for elem in acceptedTrans:
            if elem.type.value == transType:
                feats.append(featDic)
                return elem

        if len(acceptedTrans) > 0:
            return acceptedTrans[0]
        return None


class EmbeddedinParser(Parser):
    @staticmethod
    def getNextTransition(transition, sent, classifier, dictVectorizer, feats):

        config = transition.configuration
        reduce, mwtComplete, shift, mergeAsID, mergeAsOTH, mergeAsIReflV, mergeAsVPC, mergeAsLVC, whiteMerge = Reduce(), MWTComplete(), Shift(), MergeAsID(), MergeAsOTH(), MergeAsIReflV(), MergeAsVPC(), MergeAsLVC(), WhiteMerge()
        if len(config.stack) == 0 and len(config.buffer) > 0:
            feats.append({})
            return Shift()

        if len(config.stack) > 0 and FeatParams.enableSingleMWE:
            if isinstance(config.stack[0], Token) and config.stack[0].lemma in Corpus.mweDictionary.keys():
                feats.append({})
                return mwtComplete

        if (len(config.buffer) == 0 and len(config.stack) == 1):
            # or (len(config.stack) == 1 and isinstance(config.stack[0], list)):
            feats.append({})
            return Reduce()

        acceptedTrans = [shift, reduce, whiteMerge, mergeAsID, mergeAsOTH, mergeAsIReflV, mergeAsVPC,
                         mergeAsLVC, mwtComplete]
        if not FeatParams.enableSingleMWE:
            acceptedTrans.remove(mwtComplete)

        if len(config.stack) == 0:
            acceptedTrans.remove(reduce)
            if mwtComplete in acceptedTrans:
                acceptedTrans.remove(mwtComplete)

        if len(config.stack) < 2:
            acceptedTrans.remove(mergeAsID)
            acceptedTrans.remove(mergeAsOTH)
            acceptedTrans.remove(mergeAsIReflV)
            acceptedTrans.remove(mergeAsVPC)
            acceptedTrans.remove(mergeAsLVC)
            acceptedTrans.remove(whiteMerge)

        if len(config.buffer) == 0:
            acceptedTrans.remove(shift)

        if len(acceptedTrans) == 1:
            feats.append({})
            return acceptedTrans[0]

        featDic = Extractor.getFeatures(transition, sent)  # classifier.predict(dictVectorizer.transform(featDic))
        transType = classifier.predict(dictVectorizer.transform(featDic))[0]

        for elem in acceptedTrans:
            if elem.type.value == transType:
                feats.append(featDic)
                return elem

        if len(acceptedTrans) > 0:
            return acceptedTrans[0]
        return None


