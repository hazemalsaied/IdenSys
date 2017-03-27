from transition import Transition, TransitionType, StaticOracle, Shift
from configuration import Configuration
from corpus import VMWE, Sentence, Token


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
            #tokens = Sentence.getTokens(config.stack)
            selectedParents = VMWE.getSharedVMWEs(tokens)
            if selectedParents is not None and len(selectedParents) > 1:
                print 'Error'
            if selectedParents is not None and len(selectedParents) == 1:

                selectedParent =selectedParents[0]
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
            selectedParents = VMWE.getSharedVMWEs(Sentence.getTokens(config.stack) )
            if selectedParents is not None and len(selectedParents) > 1:
                print 'Error'
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

class Reduce(Transition):

    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.Reduce

    def apply(self, parent, sent=None, vMWEId=None, parse=False):
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)
        newStack = newStack[:-1]
        newTokens = list(config.tokens)
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)
        super(Reduce, self).__init__(config=newConfig, previous=parent)


class WhiteMerge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(WhiteMerge, self).__init__(TransitionType.WHITE_MERGE, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newTokens = list(config.tokens)
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

        super(WhiteMerge, self).__init__(config=newConfig, previous=parent)


class BlackMerge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(BlackMerge, self).__init__(type, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):

        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newTokens = list(config.tokens)
        vMWETokens = Sentence.getTokens(newStack[-1])
        if len(vMWETokens) > 1:
            if vMWEId is None:
                vMWEId = VMWE.getVMWENumber(newTokens) + 1
            vMWE = VMWE(vMWEId, vMWETokens[0])
            if parse:
                sent.identifiedVMWEs.append(vMWE)
            vMWE.tokens = vMWETokens
            if vMWEType is not None:
                vMWE.type = vMWEType
            newTokens.append(vMWE)
        elif len(vMWETokens) == 1:
            newTokens.append(vMWETokens[0])

        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

        super(BlackMerge, self).__init__(config=newConfig, previous=parent)


class MergeAsID(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsID, self).__init__(TransitionType.MERGE_AS_ID, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):
        super(MergeAsID, self).apply(parent, sent, vMWEId, parse, vMWEType='ID')


class MergeAsLVC(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsLVC, self).__init__(TransitionType.MERGE_AS_LVC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):
        super(MergeAsLVC, self).apply(parent, sent, vMWEId, parse, vMWEType='LVC')


class MergeAsVPC(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsVPC, self).__init__(TransitionType.MERGE_AS_VPC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):
        super(MergeAsVPC, self).apply(parent, sent, vMWEId, parse, vMWEType='VPC')


class MergeAsIReflV(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsIReflV, self).__init__(TransitionType.MERGE_AS_IReflV, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):
        super(MergeAsIReflV, self).apply(parent, sent, vMWEId, parse, vMWEType='IReflV')


class MergeAsOTH(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsOTH, self).__init__(TransitionType.MERGE_AS_OTH, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None):
        super(MergeAsOTH, self).apply(parent, sent, vMWEId, parse, vMWEType='OTH')
