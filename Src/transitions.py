import reports
from config import Configuration
from transTypes import TransitionType, MWTTransitionType
from corpus import VMWE, Sentence, Token
from param import XPParams, Counters



class Transition(object):

    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.sent = sent
        if isInitial:
            self.configuration = Configuration(buffer=sent.tokens, isInitial=True, sent=sent, transition=self)
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
        if self.configuration is not None:
            return self.configuration.isTerminalConf()
        return False

    def apply(self, parent, sent, vMWEId=None, parse=False):
        pass

    def getLegalTransDic(self):
        config = self.configuration
        if config and config.legalTrans:
            return config.legalTrans
        transitions = {}

        if not XPParams.includeEmbedding:
            if config.buffer:
                shift = Shift(sent=self.sent)
                transitions[TransitionType.SHIFT] = shift
            if config.stack:
                transitions[TransitionType.COMPLETE] = Complete(sent=self.sent)
                if isinstance(config.stack[-1], Token):
                    transitions[TransitionType.MWT_COMPLETE] = MWTComplete(sent=self.sent)
                if len(config.stack) > 1:
                    transitions[TransitionType.MERGE] = Merge(sent=self.sent)

            return transitions
        return {}

    def getZeroCostTransType(self):
        config = self.configuration
        costDic = []
        legalTrans = self.getLegalTransDic()
        for transitionType in legalTrans.keys():
            if Transition.getCost(config, transitionType) == 0:
                costDic.append(transitionType)
        if not costDic:
            costDic = self.getOptimalTransTypes()
            reports.onlineTrainingProblems += str(self.sent) + str(config)
            reports.onlineTrainingProblems += '## Error: no zero Cost TransTypes '
            reports.onlineTrainingProblems += '### Transition ID: ' + str(self.id)
            reports.onlineTrainingProblems += str(self.sent)
        return costDic

    @staticmethod
    def getCost(config, transitionType):
        if transitionType == TransitionType.SHIFT:
            return Shift.getCost(config)
        elif transitionType == TransitionType.COMPLETE:
            return Complete.getCost(config)

        elif transitionType == TransitionType.MWT_COMPLETE:
            return MWTComplete.getCost(config)
        elif transitionType == TransitionType.MERGE:
            return Merge.getCost(config)
        else:
            return BlackMerge.getCost(config, transitionType)

    def getOptimalTransTypes(self):
        config = self.configuration
        result, costDic = [], {}
        for transitionType in self.getLegalTransDic().keys():
            costDic[transitionType] = Transition.getCost(config, transitionType)
        minVal = min(costDic.values())
        maxVal = max(costDic.values())
        if minVal == maxVal:
            return TransitionType.sort(costDic.keys())
        for val in xrange(minVal, maxVal):
            valList = []
            for k in costDic.keys():
                if costDic[k] == val:
                    valList.append(k)
            valList = TransitionType.sort(valList)
            result = result + valList
        return result

    @staticmethod
    def initialize(transType, sent):
        if isinstance(transType, int):
            transType = TransitionType.getType(transType)
        if transType == TransitionType.SHIFT:
            return Shift(sent=sent)
        if transType == TransitionType.COMPLETE:
            return Complete(sent=sent)
        if transType == TransitionType.REDUCE:
            return Reduce(sent=sent)
        if transType == TransitionType.MWT_COMPLETE:
            return MWTComplete(sent=sent)
        if transType == TransitionType.MERGE:
            return Merge(sent=sent)
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
        # if transType == TransitionType.MERGE_AS_MWT:
        #     return MergeAsMWT(sent=sent)
        if transType == TransitionType.MERGE_AS_OTH:
            return MergeAsOTH(sent=sent)
        if transType == MWTTransitionType.MERGE_AS_MWT_IREFLV:
            return MergeAsMWT_IREFLF(sent=sent)
        if transType == MWTTransitionType.MERGE_AS_MWT_ID:
            return MergeAsMWT_ID(sent=sent)
        if transType == MWTTransitionType.MERGE_AS_MWT_LVC:
            return MergeAsMWT_LVC(sent=sent)
        if transType == MWTTransitionType.MERGE_AS_MWT_VPC:
            return MergeAsMWT_VPC(sent=sent)
        return None

    def isLegal(self):
        pass

    def __str__(self):
        result , tab = '', '&nbsp;'
        transition = self

        while True:
            if transition.type is not None:
                type = transition.type.name
            else:
                type = tab*8
            configuration = str(transition.configuration)
            result += str(
                transition.id) + '- **' + type + '**' + tab*6 +  '>' + tab*3 + configuration + '\n\n'
            if transition.next is None:
                break
            transition = transition.next
        return result

class Complete(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Complete, self).__init__(type, config, previous, next, isInitial, sent)
        self.type = TransitionType.COMPLETE

    def apply(self, parent, sent, vMWEId=None, parse=False):
        Counters.completeNum +=1
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)
        vMWETokens = Sentence.getTokens(newStack[0])
        newStack = newStack[:-1]
        newTokens = list(config.tokens)
        if len(vMWETokens) > 1:
            if sent is not None and not parse:
                sent.blackMergeNum += 1

            if vMWEId is None:
                vMWEId = VMWE.getVMWENumber(newTokens) + 1
            vMWE = VMWE(vMWEId, vMWETokens[0])
            if parse:
                sent.identifiedVMWEs.append(vMWE)
            vMWE.tokens = vMWETokens
            newTokens.append(vMWE)
        elif len(vMWETokens) == 1:
            newTokens.append(vMWETokens[0])
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)

        super(Complete, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def checkForVMWE( transition):
        config = transition.configuration
        sent = config.sent
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
                    complete = Complete(sent=sent)
                    complete.apply(transition, sent, vMWEId=vMWE.id)
                    return complete
        return None

    @staticmethod
    def checkForToken( parent):
        config = parent.configuration
        sent = config.sent
        # Check again for one word COMPLETE
        if len(config.stack) > 0 and config.stack[-1] is not None and not isinstance(config.stack[-1], list):
            if (len(config.stack[-1].parentMWEs) == 0):
                complete = Complete(sent=sent)
                complete.apply(parent, sent)
                return complete

            complete = True
            for parentVme in config.stack[-1].parentMWEs:
                if not parentVme.isEmbedded and not parentVme.isInterleaving:
                    complete = False
            if complete:
                complete = Complete(sent=sent)
                complete.apply(parent, sent)
                return complete

    @staticmethod
    def getCost(config, transType=None):
        sent = config.sent
        cost = 0
        if isinstance(config.stack[-1], list):
            for vmwe in sent.vMWEs:
                if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                    continue
                allInList, someInList= True, False
                stackTokens = Sentence.getTokens(config.stack[-1])
                for t in stackTokens :
                    if not t.In(vmwe):
                        allInList = False
                    else:
                        someInList = True
                if len(stackTokens) == len(vmwe.tokens) and allInList :
                    return 0
                else:
                    allInList = False
                if not allInList and someInList:
                    cost +=1

        elif isinstance(config.stack[-1], Token):
            if config.stack[-1].parentMWEs is None or len(config.stack[-1].parentMWEs) == 0:
                return 0
            else:
                for vmwe in config.stack[-1].parentMWEs:
                    if config.stack[-1].In(vmwe) and len(vmwe.tokens) > 1:
                        cost +=1
                return cost
        return cost

class Merge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Merge, self).__init__(type, config, previous, next, isInitial, sent)
        self.type = TransitionType.MERGE

    def apply(self, parent, sent,vMWEId=None,parse=False):
        Counters.mergeNum += 1
        config = parent.configuration
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newConfig = Configuration(stack=newStack, buffer=list(config.buffer), tokens=list(config.tokens), sent=sent, transition=self)
        super(Merge, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def check(transition ):
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

    @staticmethod
    def getCost(config, transType=None):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue
            s0BelongsToVmwe = True
            s1BelongsToVmwe = True

            for token in Sentence.getTokens(config.stack[-1]):
                if not token.In(vmwe):
                    s0BelongsToVmwe = False
                    break

            for token in Sentence.getTokens(config.stack[-2]):
                if not token.In(vmwe):
                    s1BelongsToVmwe = False
                    break

            if s0BelongsToVmwe and s1BelongsToVmwe:
                return 0
            else:
                cost += 1
        return cost

    def isLegal(self):
        if self.configuration.stack and len(self.configuration.stack) > 1:
            return True
        return False

class MWTComplete(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MWTComplete, self).__init__(type, config, previous, next, isInitial, sent)
        self.type = TransitionType.MWT_COMPLETE

    def apply(self, parent, sent, vMWEId=None, parse=False):
        Counters.mWTCompleteNum += 1
        config = parent.configuration
        newTokens = list(config.tokens)
        if vMWEId is None:
            vMWEId = VMWE.getVMWENumber(newTokens) + 1
        vMWE = VMWE(vMWEId, config.stack[-1])
        if parse:
            sent.identifiedVMWEs.append(vMWE)
        newTokens.append(vMWE)
        newConfig = Configuration(stack=list(config.stack)[:-1], buffer=list(config.buffer), tokens=newTokens, sent=sent, transition=self)
        super(MWTComplete, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def check(transition):
        config = transition.configuration
        sent = config.sent
        if config.stack and isinstance(config.stack[0], Token) \
                and config.stack[0].parentMWEs is not None and len(config.stack[0].parentMWEs) == 1 \
                and len(config.stack[0].parentMWEs[0].tokens) == 1:
            mWTComplete = MWTComplete(sent=sent)
            mWTComplete.apply(transition, sent, config.stack[0].parentMWEs[0].id,
                              config.stack[0].parentMWEs[0].type)
            return mWTComplete
        return None
    @staticmethod
    def getCost(config, transType=None):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue

            if isinstance(config.stack[-1],Token) and not config.stack[-1].isMWT():
                cost += 1
        # Precision score:
        if isinstance(config.stack[-1], list):
            cost += 1
        if isinstance(config.stack[-1], Token) and not config.stack[-1].isMWT():
            cost += 1
        return cost

    def isLegal(self):
        if self.configuration.stack:
            return True
        return False

class EmbeddingTransition(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(EmbeddingTransition, self).__init__(type, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False):
        pass

    @staticmethod
    def getCost(config, transitionType):

        if transitionType == TransitionType.SHIFT:
            return Shift.getCost(config)
        elif transitionType == TransitionType.REDUCE:
            return Reduce.getCost(config)

        elif transitionType == TransitionType.WHITE_MERGE:
            return WhiteMerge.getCost(config)
        # elif transitionType == TransitionType.MERGE_AS_MWT:
        #     return MergeAsMWT.getCost(config)
        elif transitionType == MWTTransitionType.MERGE_AS_MWT_ID:
            return MergeAsMWT_ID.getCost(config)
        elif transitionType == MWTTransitionType.MERGE_AS_MWT_IREFLV:
            return MergeAsMWT_IREFLF.getCost(config)
        elif transitionType == MWTTransitionType.MERGE_AS_MWT_VPC:
            return MergeAsMWT_VPC.getCost(config)
        elif transitionType == MWTTransitionType.MERGE_AS_MWT_LVC:
            return MergeAsMWT_LVC.getCost(config)
        else:
            return BlackMerge.getCost(config,  transitionType)

    def getLegalTransDic(self):
        if not XPParams.includeEmbedding:
            return Transition.getLegalTransDic(self)

        config = self.configuration
        if config and config.legalTrans:
            return config.legalTrans
        transitions = {}
        if len(config.stack) > 0 and isinstance(config.stack[-1], Token):
            transitions[MWTTransitionType.MERGE_AS_MWT_ID] = MergeAsMWT_ID(sent=self.sent)
            transitions[MWTTransitionType.MERGE_AS_MWT_VPC] = MergeAsMWT_VPC(sent=self.sent)
            transitions[MWTTransitionType.MERGE_AS_MWT_LVC] = MergeAsMWT_LVC(sent=self.sent)
            transitions[MWTTransitionType.MERGE_AS_MWT_IREFLV] = MergeAsMWT_IREFLF(sent=self.sent)

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

        if not transitions:
            # print 'Erro: No legal transitions for this configuration: ', config
            reports.onlineTrainingProblems += '## No legal transitions for this configuration'
            reports.onlineTrainingProblems += '### Transition ID: ' + str(self.id)
            reports.onlineTrainingProblems += str(self.sent)

        return transitions

    def getZeroCostTransType(self):
        if not XPParams.includeEmbedding:
            return Transition.getZeroCostTransType(self)
        config = self.configuration
        costDic = []
        legalTrans = self.getLegalTransDic()
        for transitionType in legalTrans.keys():
            if EmbeddingTransition.getCost(config, transitionType) == 0:
                costDic.append(transitionType)


        if not costDic:
            costDic = self.getOptimalTransTypes()
            reports.onlineTrainingProblems += str(self.sent) + str(config)
            reports.onlineTrainingProblems += '## Error: no zero Cost TransTypes '
            reports.onlineTrainingProblems += '### Transition ID: ' + str(self.id)
            reports.onlineTrainingProblems += str(self.sent)
        return costDic

    def getOptimalTransTypes(self):
        if not XPParams.includeEmbedding:
            return Transition.getOptimalTransTypes(self)
        config = self.configuration
        result, costDic = [], {}
        for transitionType in self.getLegalTransDic().keys():
            costDic[transitionType] = EmbeddingTransition.getCost(config, transitionType)
        minVal = min(costDic.values())
        maxVal = max(costDic.values())
        if minVal == maxVal:
            return TransitionType.sort(costDic.keys())
        for val in xrange(minVal, maxVal):
            valList = []
            for k in costDic.keys():
                if costDic[k] == val:
                    valList.append(k)
            valList = TransitionType.sort(valList)
            result = result + valList
        return result

class Shift(EmbeddingTransition):

    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Shift, self).__init__(type, config, previous, next, isInitial, sent)
        self.type = TransitionType.SHIFT

    def apply(self, parent, sent, vMWEId=None, parse=False):
        Counters.shiftNum += 1
        config = parent.configuration
        lastToken = config.buffer[0]
        newStack = list(config.stack)
        newStack.append(lastToken)
        newConfig = Configuration(buffer=list(config.buffer)[1:], stack=newStack, tokens=list(config.tokens), sent=sent, transition=self)
        super(Shift, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def getCost(config, transType=None ):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue
            b0BelongsToVmwe = config.buffer[0].In(vmwe)
            if not b0BelongsToVmwe:
                continue
            s0BelongsToVmwe = True
            if len(config.stack) > 0:
                for token in Sentence.getTokens(config.stack[-1]):
                    if not token.In(vmwe):
                        s0BelongsToVmwe = False
                if len(config.stack) > 1:
                    otherStackElementsBelongtoVmwe = False
                    for sElem in config.stack[:-1]:
                        for token in Sentence.getTokens(sElem):
                            if token.In(vmwe):
                                otherStackElementsBelongtoVmwe = True
                                break
                            if otherStackElementsBelongtoVmwe:
                                break
                else:
                    otherStackElementsBelongtoVmwe = False
            else:
                s0BelongsToVmwe = False
                otherStackElementsBelongtoVmwe = False
            if not s0BelongsToVmwe and otherStackElementsBelongtoVmwe:
                cost += 1
        return cost

    def isLegal(self):
        if self.configuration.buffer:
            return True
        return False

class Reduce(EmbeddingTransition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(Reduce, self).__init__(TransitionType.REDUCE, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False):
        Counters.reduceNum += 1
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)
        newStack = newStack[:-1]
        newTokens = list(config.tokens)
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)
        super(Reduce, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def getCost(config, transType=None ):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue
            s0BelongsToVmwe = True
            increaseCost = False
            for token in Sentence.getTokens(config.stack[-1]):
                if not token.In(vmwe):
                    s0BelongsToVmwe = False
            if len(vmwe.tokens) == 1 and s0BelongsToVmwe:
                if isinstance(config.stack[-1], Token):
                    cost +=1
                    continue
                elif isinstance(config.stack[-1], list) and len(config.stack[-1]) == 1:
                    if len(config.stack[-1][0].parentMWEs) == 1:
                        return 0
                    else:
                        cost += 1
            if not s0BelongsToVmwe:
                continue
            for s in config.stack[:-1]:
                for token in Sentence.getTokens(s):
                    if token.In(vmwe):
                        increaseCost = True
                        break
            if increaseCost:
                cost += 1
            else:
                for b in config.buffer:
                    if b.In(vmwe):
                        cost += 1
                        break
        return cost

    @staticmethod
    def check( parent):
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

        stackWithMWT = config.stack and isinstance(config.stack[-1], list) and len(config.stack[-1]) == 1 and config.stack[-1][0].parentMWEs == 1
        if stackWithMWT :
            reduce.apply(parent, sent)
            return reduce

        stackWithSingleListWitOneSharedParentOnly = False
        if config.stack and isinstance(config.stack[-1], list):
            tokens = Sentence.getTokens(config.stack[-1])
            if len(VMWE.getParents(tokens)) == 1 and not VMWE.getParents(tokens)[0].isEmbedded:
                stackWithSingleListWitOneSharedParentOnly = True

        if stackWithSingleListWitOneSharedParentOnly :
            reduce.apply(parent, sent)
            return reduce

        stackWithTopTokenOfInterleavingMWE = sent.containsInterleaving and  config.stack and isinstance(config.stack[-1], Token) and (
            config.stack[-1].parentMWEs and len(config.stack[-1].parentMWEs) == 1 and
            config.stack[-1].parentMWEs[0].isInterleaving)

        if stackWithTopTokenOfInterleavingMWE:
            reduce.apply(parent, sent)
            return reduce
        return None

    def isLegal(self):
        if self.configuration.stack:
            return True
        return False

class WhiteMerge(EmbeddingTransition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(WhiteMerge, self).__init__(TransitionType.WHITE_MERGE, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False, vMWEType=None):
        Counters.whiteMergeNum += 1
        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newTokens = list(config.tokens)
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)

        super(WhiteMerge, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def getCost(config, transType=None ):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue

            s0BelongsToVmwe = True
            s1BelongsToVmwe = True
            increaseCost = False

            for token in Sentence.getTokens(config.stack[-1]):
                if not token.In(vmwe):
                    s0BelongsToVmwe = False
            if len(vmwe.tokens) == 1 and s0BelongsToVmwe and isinstance(config.stack[-1], Token):
                cost += 1
                continue

            for token in Sentence.getTokens(config.stack[-2]):
                if not token.In(vmwe):
                    s1BelongsToVmwe = False

            if (s0BelongsToVmwe and s1BelongsToVmwe) and len(config.stack) > 1 and len(vmwe.tokens) == len(
                    Sentence.getTokens(config.stack[-2:])):
                cost += 1
                continue

            if (s0BelongsToVmwe and s1BelongsToVmwe) or (not s0BelongsToVmwe and not s1BelongsToVmwe):
                continue
            if len(config.stack) > 2:
                for stackElement in config.stack[:-2]:
                    for token in Sentence.getTokens(stackElement):
                        if token.In(vmwe):
                            increaseCost = True
                            break
                    if increaseCost:
                        break
            if increaseCost:
                cost += 1
                continue
            for b in config.buffer:
                if b.In(vmwe):
                    cost += 1
                    break
        return cost

    def isLegal(self):
        if self.configuration.stack and len(self.configuration.stack) > 1:
            return True
        return False

class BlackMerge(EmbeddingTransition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(BlackMerge, self).__init__(type, config, previous, next, isInitial, sent)

    def apply(self, parent, sent, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        Counters.blackMergeNum += 1
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
        elif len(vMWETokens) == 1 :
            newTokens.append(vMWETokens[0])

        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens, sent=sent, transition=self)

        super(BlackMerge, self).__init__(config=newConfig, previous=parent, sent=sent)

    @staticmethod
    def getCost(config, transType=None ):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue
            s0BelongsToVmwe = True
            s1BelongsToVmwe = True
            increaseCost = False
            for token in Sentence.getTokens(config.stack[-1]):
                if not token.In(vmwe):
                    s0BelongsToVmwe = False
            if len(vmwe.tokens) == 1 and s0BelongsToVmwe and isinstance(config.stack[-1], Token):
                cost += 1
                continue
            for token in Sentence.getTokens(config.stack[-2]):
                if not token.In(vmwe):
                    s1BelongsToVmwe = False
            if (s0BelongsToVmwe and not s1BelongsToVmwe) or (not s0BelongsToVmwe and s1BelongsToVmwe):
                cost += 1
                continue
            if s0BelongsToVmwe and s1BelongsToVmwe:
                if len(Sentence.getTokens(config.stack[-1])) + len(Sentence.getTokens(config.stack[-2])) == len(
                        vmwe.tokens) and transType.name[7:].lower() == vmwe.type.lower():
                    return 0
                if len(config.stack) > 2:
                    for stackElement in config.stack[:-2]:
                        for token in Sentence.getTokens(stackElement):
                            if token.In(vmwe):
                                increaseCost = True
                                break
                        if increaseCost:
                            break
                    if increaseCost:
                        cost += 1
                        continue
                for b in config.buffer:
                    if b.In(vmwe):
                        cost += 1
                        break
        # Precision score:
        correctlyIdentified = False
        vmwes = VMWE.getParents(Sentence.getTokens(config.stack[-2:]))
        if vmwes :
            for vmwe in vmwes:
                if vmwe.type.lower() in str(transType.name).lower():
                    correctlyIdentified = True
        if not correctlyIdentified:
            cost += 1
        return cost

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
            if selectedParents and len(selectedParents) > 1:
                reports.annotationReport += str(sent)
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
                    merge.apply(transition, sent=sent)
                    return merge
            # selectedParents = VMWE.getSharedVMWEs(Sentence.getTokens(config.stack))
            # if selectedParents and len(selectedParents) > 1:
            #     reports.annotationReport += str(sent)
            selectedParents = VMWE.haveSameParents(tokens)
            if selectedParents  and len(selectedParents) == 1:
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
        Counters.mergeAsIDNum +=1
        super(MergeAsID, self).apply(parent, sent, vMWEId, parse, vMWEType='ID', mwtMerge=mwtMerge)

class MergeAsLVC(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsLVC, self).__init__(TransitionType.MERGE_AS_LVC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        Counters.mergeAsLVCNum+= 1
        super(MergeAsLVC, self).apply(parent, sent, vMWEId, parse, vMWEType='LVC', mwtMerge=mwtMerge)

class MergeAsVPC(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsVPC, self).__init__(TransitionType.MERGE_AS_VPC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        Counters.mergeAsVPCNum += 1
        super(MergeAsVPC, self).apply(parent, sent, vMWEId, parse, vMWEType='VPC', mwtMerge=mwtMerge)

class MergeAsIReflV(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsIReflV, self).__init__(TransitionType.MERGE_AS_IReflV, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        Counters.mergeAsIReflVNum += 1
        super(MergeAsIReflV, self).apply(parent, sent, vMWEId, parse, vMWEType='IReflV', mwtMerge=mwtMerge)

class MergeAsOTH(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsOTH, self).__init__(TransitionType.MERGE_AS_OTH, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):
        Counters.mergeAsOTHNum += 1
        super(MergeAsOTH, self).apply(parent, sent, vMWEId, parse, vMWEType='OTH', mwtMerge=mwtMerge)

class MergeAsMWT(BlackMerge):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT, self).__init__(type, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=False):

        super(MergeAsMWT, self).apply(parent,sent=sent, vMWEId=vMWEId, parse=parse, vMWEType=vMWEType, mwtMerge=True)

    @staticmethod
    def getCost(config, transType=None, type=None ):
        sent = config.sent
        cost = 0
        for vmwe in sent.vMWEs:
            if vmwe.isInterleaving or vmwe.In(sent.identifiedVMWEs):
                continue
            if (config.stack[-1]).In(vmwe) and len(vmwe.tokens) == 1 and vmwe.type.lower()==type.lower():
                return 0
            if (config.stack[-1]).In(vmwe) and len(vmwe.tokens) > 1:
                cost += 1
                continue

        # Precision score:
        vmwes = VMWE.getParents(Sentence.getTokens(config.stack[-1]), type.lower())
        if not vmwes :
            cost += 1
        return cost

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
                print '### Error: MWT With non Valid type'
                print sent
                mWTComplete = BlackMerge()
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
        super(MergeAsMWT_VPC, self).__init__(MWTTransitionType.MERGE_AS_MWT_VPC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        Counters.mergeAsVPCNum+= 1
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='VPC', mwtMerge=mwtMerge)

    @staticmethod
    def getCost(config, transType=None, type='VPC'):
        return MergeAsMWT.getCost(config,transType, type)

class MergeAsMWT_LVC(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_LVC, self).__init__(MWTTransitionType.MERGE_AS_MWT_LVC, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        Counters.mergeAsLVCNum += 1
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='LVC', mwtMerge=mwtMerge)

    @staticmethod
    def getCost(config, transType=None, type='LVC'):
        return MergeAsMWT.getCost(config, transType, type)

class MergeAsMWT_ID(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_ID, self).__init__(MWTTransitionType.MERGE_AS_MWT_ID, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        Counters.mergeAsIDNum += 1
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='ID', mwtMerge=mwtMerge)

    @staticmethod
    def getCost(config, transType=None, type='ID'):
        return MergeAsMWT.getCost(config, transType, type)

class MergeAsMWT_IREFLF(MergeAsMWT):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        super(MergeAsMWT_IREFLF, self).__init__(MWTTransitionType.MERGE_AS_MWT_IREFLV, config, previous, next, isInitial, sent)

    def apply(self, parent, sent=None, vMWEId=None, parse=False, vMWEType=None, mwtMerge=True):
        Counters.mergeAsIReflVNum += 1
        super(MergeAsMWT, self).apply(parent, sent, vMWEId, parse, vMWEType='IReflV', mwtMerge=mwtMerge)

    @staticmethod
    def getCost(config, transType=None, type='IReflV'):
        return MergeAsMWT.getCost(config, transType, type)