from enum import Enum

from configuration import Configuration


class Transition:
    def __init__(self, type, config, previous=None, next=None):
        self.type = type
        self.configuration = config
        self.previous = previous
        self.next = next
        if self.previous is None:
            self.id = 0
        else:
            self.id = self.previous.id + 1

    @staticmethod
    def createInitialTransition(sent):

        initialConfig = Configuration(buffer=sent.tokens, isInitial=True)
        initialTransition = Transition(None, config=initialConfig)

        return initialTransition

    def isInitial(self):
        if self.configuration is not None:
            return self.configuration.isInitial
        return False

    def isTerminal(self):
        if self.configuration is not None:
            return self.configuration.isTerminalConf()
        return False

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
            if type == 'MERGE' :
                type = '**MERGE**&nbsp;&nbsp;&nbsp;'
            if len(type) == 'SHIFT':
                type = type + '&nbsp;&nbsp;&nbsp;'
            result += str(transition.id) + '- ' + type + '&nbsp;&nbsp;&nbsp;' + '>' +'&nbsp;&nbsp;&nbsp;' + configuration + '\n\n'
            if transition.next is None:
                break
            transition = transition.next
        return result


class TransitionType(Enum):
    SHIFT = 0
    MERGE = 1
    COMPLETE = 2
