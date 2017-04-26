from enum import Enum

from corpus import VMWE, Sentence, Token
import logging

class TransitionType(Enum):
    SHIFT = 0
    MERGE = 1
    COMPLETE = 2
    MWT_COMPLETE = 3
    REDUCE = 4
    MERGE_AS_LVC = 5
    MERGE_AS_VPC = 6
    MERGE_AS_IReflV = 7
    MERGE_AS_OTH = 8
    MERGE_AS_ID = 9
    WHITE_MERGE = 10


class Configuration:
    def __init__(self, buffer=[], stack=[], tokens=[], isInitial=False, isTerminal=False):

        self.buffer = buffer
        self.stack = stack
        self.tokens = tokens
        self.isInitial = isInitial
        self.isTerminal = self.isTerminalConf()

    def isTerminalConf(self):
        if len(self.buffer) == 0 and len(self.stack) == 0:
            return True
        return False

    def __str__(self):

        stackStr = Configuration.printStack(self.stack)
        if len(self.buffer) > 0:
            buffStr = '[' + self.buffer[0].text
            if len(self.buffer) > 1:
                buffStr += ', ' + self.buffer[1].text
                if len(self.buffer) > 2:
                    buffStr += ', ' + self.buffer[2].text + ' ,.. '
                else:
                    buffStr += ' ,.. '
            buffStr += ']'
        else:
            buffStr = '[ ]'
        return 'S= ' + stackStr + ' B= ' + buffStr  # + ' ; VMWEs = ' + tokensStr

    @staticmethod
    def printStack(elemlist):

        result = '['
        for elem in elemlist:
            if isinstance(elem, Token):
                result += elem.text + ', '
            elif isinstance(elem, list):
                result += Configuration.printStack(elem)
        if result == '[':
            return result + ']  '
        return result[:-2] + ']  '

    @staticmethod
    def getStackFeatures(elem, pos):
        transDic = {}
        elemTitle = 'S' + pos
        if isinstance(elem, Token):

            transDic[elemTitle + 'Token'] = elem.text
            transDic[elemTitle + 'POS'] = elem.posTag
            transDic[elemTitle + 'Lemma'] = elem.lemma
            return transDic
        elif isinstance(elem, list):
            tokens = Configuration.getToken(elem)
            transDic[elemTitle + 'Token'] = ''
            transDic[elemTitle + 'POS'] = ''
            transDic[elemTitle + 'Lemma'] = ''
            for token in tokens:
                transDic[elemTitle + 'Token'] += token.text + '-'
                transDic[elemTitle + 'POS'] += token.posTag + '-'
                transDic[elemTitle + 'Lemma'] += token.lemma + '-'

        return transDic

    @staticmethod
    def getToken(elemlist):

        if isinstance(elemlist, Token):
            return [elemlist]
        result = []
        for elem in elemlist:
            if isinstance(elem, Token):
                result.append(elem)
            elif isinstance(elem, list):
                result.extend(Configuration.getToken(elem))
        return result


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


class Shift(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.SHIFT

    def apply(self, parent, sent=None, vMWEId=None, parse=False):
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


class Reduce(Transition):
    def __init__(self, type=None, config=None, previous=None, next=None, isInitial=False, sent=None):
        self.type = TransitionType.REDUCE

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
