from corpus import VMWE, Sentence, Token
from configuration import Configuration
from enum import Enum
from features import Extractor

class StaticOracle:
    @staticmethod
    def parseCorpus(sents, cls):
        features = []
        labels = []
        for sent in sents:
            # Parse the sentence
            trainingInfo = cls.parseSentence(sent,cls)
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
        labels, features =Extractor.extract(sent)
        if sent.isPrintable() :
            print sent
        return labels, features


    @staticmethod
    def getNextTransition(parent, sent,cls):

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
                            if parent.isInterleaving or parent.isEmbeded:
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
                if not parentVme.isEmbeded and not parentVme.isInterleaving:
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
            if selectedParents is not None and len(selectedParents) == 1 and not selectedParents[0].isEmbeded \
                    and not selectedParents[0].isInterleaving:
                merge = Merge()
                merge.apply(transition)
                return merge
        return None


class Transition(object):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):

        if isInitial:
            self.configuration = Configuration(buffer=sent.tokens, isInitial=True)
            self.type = TransitionType.SHIFT
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

    def apply(self, parent, sent=None, vMWEId=None, parse=False):
        pass

    def __str__(self):
        result = ''
        transition = self
        while True:
            type = ''
            configuration = ''
            if transition.type is not None:
                type = transition.type.name
            else:
                type = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            configuration = str(transition.configuration)
            result += str(
                transition.id) + '- **' + type + '**&nbsp;&nbsp;&nbsp; ' + '&nbsp;&nbsp;&nbsp;' + '>' + '&nbsp;&nbsp;&nbsp;' + configuration + '\n\n'
            if transition.next is None:
                break
            transition = transition.next
        return result


class TransitionType(Enum):
    SHIFT = 0
    MERGE = 1
    COMPLETE = 2
    MWT_COMPLETE = 3
    Reduce = 4
    MERGE_AS_LVC = 5
    MERGE_AS_VPC = 6
    MERGE_AS_IReflV = 7
    MERGE_AS_OTH = 8
    MERGE_AS_ID = 9
    WHITE_MERGE = 10

class Shift(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.SHIFT

    def apply(self, parent, sent=None, vMWEId=None, parse=False):
        # TODO: Verify of the length of the buffer
        config = parent.configuration
        lastToken = config.buffer[0]
        newStack = list(config.stack)
        newStack.append(lastToken)
        newConfig = Configuration(buffer=list(config.buffer)[1:], stack=newStack, tokens=list(config.tokens))
        super(Shift, self).__init__(config=newConfig, previous=parent)

class Complete(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.COMPLETE

    def apply(self, parent, sent=None, vMWEId=None, parse=False):

        config = parent.configuration
        newBuffer = list(config.buffer)
        newStack = list(config.stack)
        vMWETokens = Sentence.getTokens(newStack[0])
        newStack = newStack[:-1]
        newTokens = list(config.tokens)
        if len(vMWETokens) > 1:
            if vMWEId is None:
                vMWEId = VMWE.getVMWENumber(newTokens) + 1
            vMWE = VMWE(vMWEId, vMWETokens[0])
            if parse:
                sent.identifiedVMWEs.append(vMWE)
            vMWE.tokens = vMWETokens
            newTokens.append(vMWE)
        elif len(vMWETokens) == 1:
            newTokens.append(vMWETokens[0])
        newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

        super(Complete, self).__init__(config=newConfig, previous=parent)


class MWTComplete(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.MWT_COMPLETE

    def apply(self, parent, sent=None, vMWEId=None, parse=False):

        config = parent.configuration
        newTokens = list(config.tokens)
        if vMWEId is None:
            vMWEId = VMWE.getVMWENumber(newTokens) + 1
        vMWE = VMWE(vMWEId, config.stack[-1])
        if parse:
            sent.identifiedVMWEs.append(vMWE)
        newTokens.append(vMWE)
        newConfig = Configuration(stack=list(config.stack)[:-1], buffer=list(config.buffer), tokens=newTokens)
        super(MWTComplete, self).__init__(config=newConfig, previous=parent)


class Merge(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.MERGE

    def apply(self, parent, sent=None, vMWEId=None, parse=False):
        config = parent.configuration
        newStack = list(config.stack)[:-2]
        newStack.append([config.stack[-2], config.stack[-1]])
        newConfig = Configuration(stack=newStack, buffer=list(config.buffer), tokens=list(config.tokens))
        super(Merge, self).__init__(config=newConfig, previous=parent)
