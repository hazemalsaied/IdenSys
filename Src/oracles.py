from Src.features import Extractor
from Src.transitions import Reduce, WhiteMerge, MergeAsID, MergeAsLVC, MergeAsVPC, MergeAsIReflV, MergeAsOTH, \
    Transition, \
    Complete, TransitionType, MWTComplete, Merge
from corpus import VMWE, Sentence, Token
from transitions import Shift


class StaticOracle:
    @staticmethod
    def parseCorpus(sents, cls):
        features = []
        labels = []
        for sent in sents:
            # Parse the sentence
            trainingInfo = cls.parseSentence(sent, cls)
            if trainingInfo is not None:
                labels.extend(trainingInfo[0])
                features.extend(trainingInfo[1])
        print len(labels)
        return [labels, features]

    @staticmethod
    def parseSentence(sent, cls):
        # Create the initial transition
        transition = Transition(isInitial=True, sent=sent)
        while not transition.isTerminal():
            transition = cls.getNextTransition(transition, sent, cls)
        sent.initialTransition = transition.getRoot()
        labels, features = Extractor.extract(sent)
        if sent.isPrintable():
            print sent
        return labels, features

    @staticmethod
    def getNextTransition(parent, sent, cls):

        config = parent.configuration
        if config.isInitial:
            shift = Shift()
            shift.apply(parent)
            return shift

        newTransition = cls.checkForMWTComplete(config, parent, sent)
        if newTransition is not None:
            return newTransition

        # Check for VMWE complete
        newTransition = cls.checkForVMWEComplete(config, parent, sent)
        if newTransition is not None:
            return newTransition

        newTransition = cls.checkForMerge(config, parent)
        if newTransition is not None:
            return newTransition

        # Check for VMWE complete
        newTransition = cls.checkForTokenComplete(config, parent, sent)
        if newTransition is not None:
            return newTransition

        if len(config.buffer) == 0 and len(config.stack) > 0:
            complete = Complete()
            complete.apply(parent, sent)
            return complete
        # Apply the default transition: SHIFT
        shift = Shift()
        shift.apply(parent)
        return shift

    @staticmethod
    def checkForVMWEComplete(config, transition, sent):
        # Check up for a possible COMPLETE of MWE after a MERGE transition
        if transition.type == TransitionType.MERGE:
            if len(config.stack) == 1 and isinstance(config.stack[0], list):
                vMWE = None
                parents = []
                tokens = Sentence.getTokens(config.stack[0])
                for token in tokens:
                    if len(token.parentMWEs) == 1:
                        vMWE = token.parentMWEs[0]
                        break
                    for parent in token.parentMWEs:
                        if parent not in parents:
                            parents.append(parent)
                if vMWE is None:
                    for parent in parents:
                        for token in tokens:
                            if parent not in token.parentMWEs:
                                parents.remove(parent)
                    if len(parents) > 1:
                        for parent in parents:
                            if parent.isInterleaving or parent.isEmbedded:
                                parents.remove(parent)
                    vMWE = parents[0]
                if vMWE is not None and len(vMWE.tokens) == len(tokens):
                    complete = Complete()
                    complete.apply(transition, sent, vMWE.id, vMWE.type)
                    return complete
        return None

    @staticmethod
    def checkForTokenComplete(config, parent, sent):
        # Check again for one word COMPLETE
        if len(config.stack) > 0 and config.stack[-1] is not None and not isinstance(config.stack[-1], list):
            if (len(config.stack[-1].parentMWEs) == 0):
                complete = Complete()
                complete.apply(parent, sent)
                return complete

            complete = True
            for parentVme in config.stack[-1].parentMWEs:
                if not parentVme.isEmbedded and not parentVme.isInterleaving:
                    complete = False
            if complete:
                complete = Complete()
                complete.apply(parent, sent)
                return complete

    @staticmethod
    def checkForMWTComplete(config, transition, sent):

        if len(config.stack) >= 1 and isinstance(config.stack[0], Token) \
                and config.stack[0].parentMWEs is not None and len(config.stack[0].parentMWEs) == 1 \
                and len(config.stack[0].parentMWEs[0].tokens) == 1:
            mWTComplete = MWTComplete()
            mWTComplete.apply(transition, sent, config.stack[0].parentMWEs[0].id,
                              config.stack[0].parentMWEs[0].type)
            return mWTComplete
        return None

    @staticmethod
    def checkForMerge(config, transition):
        # Check up of a possible MERGE
        if len(config.stack) > 1:
            tokens = Sentence.getTokens(config.stack)
            selectedParents = VMWE.getSharedVMWEs(tokens)
            if selectedParents is not None and len(selectedParents) == 1 and not selectedParents[0].isEmbedded \
                    and not selectedParents[0].isInterleaving:
                merge = Merge()
                merge.apply(transition)
                return merge
        return None


class EmbeddingOracle(StaticOracle):
    @staticmethod
    def getNextTransition(parent, sent, cls):
        # if len(sent.vMWEs) > 0:
        #     pass
        config = parent.configuration
        if config.isInitial:
            shift = Shift()
            shift.apply(parent)
            return shift

        newTransition = cls.checkForMWTComplete(config, parent, sent)
        if newTransition is not None:
            return newTransition

        newTransition = cls.checkForMerge(config, parent)
        if newTransition is not None:
            return newTransition

        # Check for VMWE complete
        newTransition = cls.checkForReduce(config, parent, sent)
        if newTransition is not None:
            return newTransition

        # Apply the default transition: SHIFT
        shift = Shift()
        shift.apply(parent)
        return shift

    @staticmethod
    def checkForMerge(config, transition):
        # Check up of a possible MERGE
        if len(config.stack) > 1:

            s0 = config.stack[-1]
            s1 = config.stack[-2]
            #
            s0Tokens = Sentence.getTokens(s0)
            s1Tokens = Sentence.getTokens(s1)
            # #TODO getParent MWE for WHite merge
            tokens = s1Tokens + s0Tokens
            shouldMerge = True
            for token in tokens:
                if token.directParent is not tokens[0].directParent:
                    shouldMerge = False
            # tokens = Sentence.getTokens(config.stack)
            selectedParents = VMWE.getSharedVMWEs(tokens)
            if selectedParents is not None and len(selectedParents) > 1:
                print 'Error'
            if selectedParents is not None and len(selectedParents) == 1:

                selectedParent = selectedParents[0]
                if selectedParent.type is not None and selectedParent.type != '':
                    if selectedParent.type.lower() == 'id':
                        merge = MergeAsID()
                    elif selectedParent.type.lower() == 'ireflv':
                        merge = MergeAsIReflV()
                    elif selectedParent.type.lower() == 'lvc':
                        merge = MergeAsLVC()
                    elif selectedParent.type.lower() == 'vpc':
                        merge = MergeAsVPC()
                    else:
                        merge = MergeAsOTH()
                    merge.apply(transition)
                    return merge
            selectedParents = VMWE.getSharedVMWEs(Sentence.getTokens(config.stack))
            if selectedParents is not None and len(selectedParents) > 1:
                print 'Error: two identic MWEs are defined'
            if selectedParents is not None and len(selectedParents) == 1:
                if len(config.stack) > 2:
                    merge = WhiteMerge()
                    merge.apply(transition)
                    return merge

        return None

    @staticmethod
    def checkForReduce(config, parent, sent):

        empyBufferWithFullStack = len(config.buffer) == 0 and len(config.stack) > 0

        stackWithTopTokenWitoutParents = len(config.stack) > 0 and isinstance(config.stack[-1], Token) and (
            config.stack[-1].parentMWEs is None or len(config.stack[-1].parentMWEs) == 0)

        stackWithTopTokenOfInterleavingMWE = len(config.stack) > 0 and isinstance(config.stack[-1], Token) and (
            config.stack[-1].parentMWEs is not None and len(config.stack[-1].parentMWEs) == 1 and
            config.stack[-1].parentMWEs[0].isInterleaving)

        stackWithSingleListWitOneSharedParentOnly = False
        if len(config.stack) > 0 and isinstance(config.stack[-1], list):
            tokens = Sentence.getTokens(config.stack[-1])
            if len(VMWE.getSharedVMWEs(tokens)) == 1 and not VMWE.getSharedVMWEs(tokens)[0].isEmbedded:
                stackWithSingleListWitOneSharedParentOnly = True

        if empyBufferWithFullStack or stackWithTopTokenWitoutParents or stackWithSingleListWitOneSharedParentOnly or stackWithTopTokenOfInterleavingMWE:
            complete = Reduce()
            complete.apply(parent, sent)
            return complete

        return None
