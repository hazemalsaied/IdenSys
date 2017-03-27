from parser import Parser
from corpus import Token
from corpus import Corpus
from param import Parameters
from transition import Shift, MWTComplete
from features import Extractor
from embeddingTransitions import MergeAsID, MergeAsOTH, MergeAsIReflV,MergeAsVPC,MergeAsLVC,Reduce

class EmbeddedinParser(Parser):

    @staticmethod
    def getNextTransition(transition, sent, classifier, dictVectorizer, feats):

        config = transition.configuration
        reduce, mwtComplete, shift, mergeAsID, mergeAsOTH, mergeAsIReflV,mergeAsVPC,mergeAsLVC = Reduce(), MWTComplete(), Shift(), MergeAsID(), MergeAsOTH(), MergeAsIReflV(),MergeAsVPC(),MergeAsLVC()
        if len(config.stack) == 0 and len(config.buffer) > 0:
            feats.append({})
            return Shift()

        if len(config.stack)> 0 and Parameters.enableSingleMWE:
            if isinstance(config.stack[0], Token) and config.stack[0].lemma in Corpus.mweDictionary.keys():
                feats.append({})
                return mwtComplete

        if (len(config.buffer) == 0 and len(config.stack) == 1) :
                #or (len(config.stack) == 1 and isinstance(config.stack[0], list)):
            feats.append({})
            return Reduce()

        acceptedTrans = [shift, reduce, mwtComplete, mergeAsID, mergeAsOTH, mergeAsIReflV,mergeAsVPC,mergeAsLVC]
        if not Parameters.enableSingleMWE:
            acceptedTrans.remove(mwtComplete)

        if len(config.stack) == 0:
            acceptedTrans.remove(reduce)

        if len(config.stack) < 2:
            acceptedTrans.remove(mergeAsID)
            acceptedTrans.remove(mergeAsOTH)
            acceptedTrans.remove(mergeAsIReflV)
            acceptedTrans.remove(mergeAsVPC)
            acceptedTrans.remove(mergeAsLVC)

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
