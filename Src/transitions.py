from config import Configuration
from corpus import VMWE, Sentence, Token
from enum import Enum


class TransitionType(Enum):
    SHIFT = 0
    REDUCE = 1
    WHITE_MERGE = 2
    MERGE_AS_LVC = 3
    MERGE_AS_VPC = 4
    MERGE_AS_IReflV = 5
    MERGE_AS_OTH = 6
    MERGE_AS_ID = 7
    MERGE_AS_MWT_VPC = 8
    MERGE_AS_MWT_IREFLV = 9
    MERGE_AS_MWT_ID = 10
    MERGE_AS_MWT_LVC = 11
    MERGE_AS_MWT_OTH = 12


def getTransitionType(idx):
    for tType in TransitionType:
        if tType.value == idx:
            return tType
    return None

class Transition(object):

    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.sent = sent
        if isInitial:
            self.configuration = Configuration([], sent.tokens, sent.tokens, sent, self, isInitial=True)
            self.type = TransitionType.SHIFT
            sent.initialTransition = self
        else:
            self.configuration = config
        if type != None:
            self.type = type
        self.previous = previous
        if previous is not None:
            previous.next = self
        self.next = next
        if self.previous is None:
            self.id = 0
        else:
            self.id = self.previous.id + 1

    def getRoot(self):
        transition = self
        while transition.previous is not None:
            transition = transition.previous
        return transition

    def isInitial(self):
        if self.configuration is not None:
            return self.configuration.isInitial
        return False

    def isTerminal(self):
        if self.configuration :
            return self.configuration.isTerminalConf()
        return False

    def apply(self, parent, sent, vMWEId=None, parse=False):
        pass

    def getLegalTransDic(self):

        config = self.configuration
        if config and config.legalTrans:
            return config.legalTrans
        transitions = {}
        if len(config.stack) > 0 and isinstance(config.stack[-1], Token):
            transitions[TransitionType.MERGE_AS_MWT_ID] = MergeAsMWT_ID(sent=self.sent)
            transitions[TransitionType.MERGE_AS_MWT_VPC] = MergeAsMWT_VPC(sent=self.sent)
            transitions[TransitionType.MERGE_AS_MWT_LVC] = MergeAsMWT_LVC(sent=self.sent)
            transitions[TransitionType.MERGE_AS_MWT_IREFLV] = MergeAsMWT_IREFLF(sent=self.sent)
            transitions[TransitionType.MERGE_AS_MWT_OTH] = MergeAsMWT_OTH(sent=self.sent)

            # transitions[TransitionType.MERGE_AS_MWT.value] = MergeAsMWT()

        if len(config.stack) > 1:
            mergeAsIReflV = MergeAsIReflV(sent=self.sent)
            transitions[TransitionType.MERGE_AS_IReflV] = mergeAsIReflV
            # transitions[TransitionType.MERGE_AS_IReflV.value] = mergeAsIReflV

            mergeAsID = MergeAsID(sent=self.sent)
            transitions[TransitionType.MERGE_AS_ID] = mergeAsID
            # transitions[TransitionType.MERGE_AS_ID.value] = mergeAsID

            mergeAsLVC = MergeAsLVC(sent=self.sent)
            transitions[TransitionType.MERGE_AS_LVC] = mergeAsLVC
            # transitions[TransitionType.MERGE_AS_LVC.value] =mergeAsLVC

            mergeAsVPC = MergeAsVPC(sent=self.sent)
            transitions[TransitionType.MERGE_AS_VPC] = mergeAsVPC
            # transitions[TransitionType.MERGE_AS_VPC.value] = mergeAsVPC

            mergeAsOTH = MergeAsOTH(sent=self.sent)
            transitions[TransitionType.MERGE_AS_OTH] = mergeAsOTH
            # transitions[TransitionType.MERGE_AS_OTH.value] = mergeAsOTH

            whiteMerge = WhiteMerge(sent=self.sent)
            transitions[TransitionType.WHITE_MERGE] = whiteMerge
            # transitions[TransitionType.WHITE_MERGE.value] = whiteMerge

        if config.buffer is not None and len(config.buffer) > 0:
            shift = Shift(sent=self.sent)
            transitions[TransitionType.SHIFT] = shift
            # transitions[TransitionType.SHIFT.value] = shift

        if config.stack is not None and len(config.stack) > 0:
            reduce = Reduce(sent=self.sent)
            transitions[TransitionType.REDUCE] = reduce
            # transitions[TransitionType.REDUCE.value] = reduce
        config.legalTrans = transitions

        return transitions

    @staticmethod
    def initialize(transType, sent):
        if isinstance(transType, int):
            transType = getTransitionType(transType)
        if transType == TransitionType.SHIFT:
            return Shift(sent=sent)
        if transType == TransitionType.REDUCE:
            return Reduce(sent=sent)
        if transType == TransitionType.WHITE_MERGE:
            return WhiteMerge(sent=sent)
        if transType == TransitionType.MERGE_AS_VPC:
            return MergeAsVPC(sent=sent)
        if transType == TransitionType.MERGE_AS_ID:
            return MergeAsID(sent=sent)
        if transType == TransitionType.MERGE_AS_IReflV:
            return MergeAsIReflV(sent=sent)
        if transType == TransitionType.MERGE_AS_LVC:
            return MergeAsLVC(sent=sent)
        if transType == TransitionType.MERGE_AS_OTH:
            return MergeAsOTH(sent=sent)
        if transType == TransitionType.MERGE_AS_MWT_IREFLV:
            return MergeAsMWT_IREFLF(sent=sent)
        if transType == TransitionType.MERGE_AS_MWT_ID:
            return MergeAsMWT_ID(sent=sent)
        if transType == TransitionType.MERGE_AS_MWT_LVC:
            return MergeAsMWT_LVC(sent=sent)
        if transType == TransitionType.MERGE_AS_MWT_VPC:
            return MergeAsMWT_VPC(sent=sent)
        return None

    def isLegal(self):
        pass

    def __str__(self):
        result, tab = '', '&nbsp;'
        transition = self

        while True:
            if transition.type is not None:
                type = transition.type.name
            else:
                type = tab * 8
            configuration = str(transition.configuration)
            result += str(
                transition.id) + '- **' + type + '**' + tab * 6 + '>' + tab * 3 + configuration + '\n\n'
            if transition.next is None:
                break
            transition = transition.next
        return result


class Merge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Merge, self).__init__(type, config, previous, next, isInitial, sent)
        self.type = TransitionType.MERGE

    def apply(self, parent, sent, vMWEId=None, parse=False):
        config = parent.configuration
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newConfig = Configuration(stack=newStack, buffer=list(config.buffer), tokens=list(config.tokens), sent=sent,
                                  transition=self)
        super(Merge, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def check(transition):
        config = transition.configuration
        sent = config.sent
        # Check up of a possible MERGE
        if len(config.stack) > 1:
            tokens = Sentence.getTokens(config.stack)
            selectedParents = VMWE.getParents(tokens)
            if selectedParents and len(selectedParents) == 1 and not selectedParents[0].isEmbedded \
                    and not selectedParents[0].isInterleaving:
                merge = Merge(sent=sent)
                merge.apply(transition, sent)
                return merge
        return None

    def isLegal(self):
        if self.configuration.stack and len(self.configuration.stack) > 1:
            return True
        return False


class Shift(Transition):

    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Shift, self).__init__(type, config, previous, next, isInitial, sent)
        self.type = TransitionType.SHIFT

    def apply(self, parent, sent, vMWEId=None, parse=False):
        config = parent.configuration
        lastToken = config.buffer[0]
        newStack = list(config.stack)
        newStack.append(lastToken)
        newConfig = Configuration(buffer=list(config.buffer)[1:], stack=newStack, tokens=list(config.tokens), sent=sent,
                                  transition=self)
        super(Shift, self).__init__(config=newConfig, previous=parent, sent=sent)

    def isLegal(self):
        if self.configuration.buffer:
            return True
        return False


class Reduce(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Reduce, self).__init__(TransitionType.REDUCE, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False):
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)
        newStack = newStack[:-1]
        newTokens = list(config.tokens)
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)
        super(Reduce, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def check(parent):
        config = parent.configuration
        sent = config.sent

        reduce = Reduce(sent=sent)

        stackWithTopTokenWitoutParents = config.stack and isinstance(config.stack[-1], Token) and (
            not config.stack[-1].parentMWEs)
        if stackWithTopTokenWitoutParents:
            reduce.apply(parent, sent)
            return reduce

        empyBufferWithFullStack = not config.buffer and config.stack
        if empyBufferWithFullStack:
            reduce.apply(parent, sent)
            return reduce

        stackWithMWT = config.stack and isinstance(config.stack[-1], list) and len(config.stack[-1]) == 1 and \
                       config.stack[-1][0].parentMWEs == 1
        if stackWithMWT:
            reduce.apply(parent, sent)
            return reduce

        stackWithSingleListWitOneSharedParentOnly = False
        if config.stack and isinstance(config.stack[-1], list):
            tokens = Sentence.getTokens(config.stack[-1])
            if len(VMWE.getParents(tokens)) == 1 and not VMWE.getParents(tokens)[0].isEmbedded:
                stackWithSingleListWitOneSharedParentOnly = True

        if stackWithSingleListWitOneSharedParentOnly:
            reduce.apply(parent, sent)
            return reduce

        stackWithTopTokenOfInterleavingMWE = sent.containsInterleaving and config.stack and isinstance(config.stack[-1],
                                                                                                       Token) and (
                                                     config.stack[-1].parentMWEs and len(
                                                 config.stack[-1].parentMWEs) == 1 and
                                                     config.stack[-1].parentMWEs[0].isInterleaving)

        if stackWithTopTokenOfInterleavingMWE:
            reduce.apply(parent, sent)
            return reduce
        return None

    def isLegal(self):
        if self.configuration.stack:
            return True
        return False


class WhiteMerge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(WhiteMerge, self).__init__(TransitionType.WHITE_MERGE, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False, vMWEType=None):
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newTokens = list(config.tokens)
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)

        super(WhiteMerge, self).__init__(config=newConfig, previous=parent, sent=sent)

    def isLegal(self):
        if self.configuration.stack and len(self.configuration.stack) > 1:
            return True
        return False


class BlackMerge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = type
        super(BlackMerge, self).__init__(type, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        if sent and not parse:
            sent.blackMergeNum += 1
        config = parent.configuration
        newBuffer = list(config.buffer)
        if mwtMerge:
            newStack = list(config.stack)[:-1]
            newStack.append([config.stack[-1]])
        else:
            newStack = list(config.stack)[:-2]
            newStack.append([config.stack[-2], config.stack[-1]])
        newTokens = list(config.tokens)
        vMWETokens = Sentence.getTokens(newStack[-1])
        if len(vMWETokens) > 1 or (len(vMWETokens) == 1 and mwtMerge):
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

        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)

        super(BlackMerge, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def check(transition):
        config = transition.configuration
        sent = config.sent
        # Check up of a possible MERGE
        if len(config.stack) > 1:

            s0Tokens = Sentence.getTokens(config.stack[-1])
            s1Tokens = Sentence.getTokens(config.stack[-2])
            # #TODO getParent MWE for WHite merge
            tokens = s1Tokens + s0Tokens
            # tokens = Sentence.getTokens(config.stack)
            selectedParents = VMWE.getParents(tokens)
            if selectedParents and len(selectedParents) == 1:

                selectedParent = selectedParents[0]
                if selectedParent.type is not None and selectedParent.type != '':
                    if selectedParent.type.lower() == 'id':
                        merge = MergeAsID(sent=sent)
                    elif selectedParent.type.lower() == 'ireflv':
                        merge = MergeAsIReflV(sent=sent)
                    elif selectedParent.type.lower() == 'lvc':
                        merge = MergeAsLVC(sent=sent)
                    elif selectedParent.type.lower() == 'vpc':
                        merge = MergeAsVPC(sent=sent)
                    else:
                        merge = MergeAsOTH(sent=sent)
                else:
                    merge = MergeAsOTH(sent=sent)
                merge.apply(transition, sent=sent)
                return merge
            # selectedParents = VMWE.getSharedVMWEs(Sentence.getTokens(config.stack))
            # if selectedParents and len(selectedParents) > 1:
            #     reports.annotationReport += str(sent)
            selectedParents = VMWE.haveSameParents(tokens)
            if selectedParents and len(selectedParents) == 1:
                if selectedParents[0].tokens[-1] == tokens[-1]:
                    # if len(config.stack) > 2:
                    merge = WhiteMerge(sent=sent)
                    merge.apply(transition, sent)
                    return merge

        return None

    def isLegal(self):
        if self.configuration.stack and len(self.configuration.stack) > 1:
            return True
        return False


class MergeAsID(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsID, self).__init__(TransitionType.MERGE_AS_ID, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        super(MergeAsID, self).apply(parent, sent, vMWEId, parse, vMWEType='ID', mwtMerge=mwtMerge)


class MergeAsLVC(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsLVC, self).__init__(TransitionType.MERGE_AS_LVC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        super(MergeAsLVC, self).apply(parent, sent, vMWEId, parse, vMWEType='LVC', mwtMerge=mwtMerge)


class MergeAsVPC(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsVPC, self).__init__(TransitionType.MERGE_AS_VPC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        super(MergeAsVPC, self).apply(parent, sent, vMWEId, parse, vMWEType='VPC', mwtMerge=mwtMerge)


class MergeAsIReflV(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsIReflV, self).__init__(TransitionType.MERGE_AS_IReflV, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        super(MergeAsIReflV, self).apply(parent, sent, vMWEId, parse, vMWEType='IReflV', mwtMerge=mwtMerge)


class MergeAsOTH(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsOTH, self).__init__(TransitionType.MERGE_AS_OTH, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        super(MergeAsOTH, self).apply(parent, sent, vMWEId, parse, vMWEType='OTH', mwtMerge=mwtMerge)


class MergeAsMWT(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT, self).__init__(type, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):

        super(MergeAsMWT, self).apply(parent, sent=sent, vMWEId=vMWEId, parse=parse, vMWEType=vMWEType, mwtMerge=True)

    @staticmethod
    def check(transition):
        config = transition.configuration
        sent = config.sent

        if config.stack and isinstance(config.stack[-1], Token):
            mwt = config.stack[-1].isMWT()
            if not mwt:
                return None
            type = mwt.type
            if type.lower() == 'vpc':
                mWTComplete = MergeAsMWT_VPC(sent=sent)
            elif type.lower() == 'ireflv':
                mWTComplete = MergeAsMWT_IREFLF(sent=sent)
            elif type.lower() == 'lvc':
                mWTComplete = MergeAsMWT_LVC(sent=sent)
            elif type.lower() == 'id':
                mWTComplete = MergeAsMWT_ID(sent=sent)
            else:
                mWTComplete = MergeAsMWT_OTH(sent=sent)
            mWTComplete.apply(transition, sent, vMWEId=config.stack[-1].parentMWEs[0].id,
                              vMWEType=type, mwtMerge=True)
            return mWTComplete
        return None

    def isLegal(self):
        if self.configuration.stack:
            return True
        return False


class MergeAsMWT_VPC(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_VPC, self).__init__(TransitionType.MERGE_AS_MWT_VPC, config, previous, next, isInitial,
                                             sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='VPC', mwtMerge=mwtMerge)


class MergeAsMWT_LVC(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_LVC, self).__init__(TransitionType.MERGE_AS_MWT_LVC, config, previous, next, isInitial,
                                             sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='LVC', mwtMerge=mwtMerge)


class MergeAsMWT_ID(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_ID, self).__init__(TransitionType.MERGE_AS_MWT_ID, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='ID', mwtMerge=mwtMerge)


class MergeAsMWT_IREFLF(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_IREFLF, self).__init__(TransitionType.MERGE_AS_MWT_IREFLV, config, previous, next,
                                                isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='IReflV', mwtMerge=mwtMerge)


class MergeAsMWT_OTH(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_OTH, self).__init__(TransitionType.MERGE_AS_MWT_OTH, config, previous, next, isInitial,
                                             sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='OTH', mwtMerge=mwtMerge)
