class Configuration:
    def __init__(self, stack, buffer, tokens, sent, transition, isInitial=False ):

        self.buffer = buffer
        self.stack = stack
        self.tokens = tokens
        self.isInitial = isInitial
        self.isTerminal = self.isTerminalConf()
        self.sent = sent
        self.transition = transition
        self.legalTrans = {}

    def isTerminalConf(self):
        if not self.buffer and not self.stack:
            return True
        return False

    def __str__(self):
        stackStr = printStack(self.stack)
        buffStr = '[ '
        if self.buffer:
            for elem in self.buffer[:2]:
                buffStr += elem.text + ','
            buffStr += ' ..' if len(self.buffer) > 2 else ''
        buffStr += ']'
        return 'S=' + stackStr + ' B=' + buffStr


def printStack(elemlist):
    stackStr = ''
    elemlistStrs = getStackElems(elemlist)
    for r in elemlistStrs:
        if r == '[' or r == ']':
            if stackStr.endswith(', '):
                stackStr = stackStr[:-2]
            stackStr += r
        else:
            stackStr += r + ', '
    return stackStr + ' ' * (25 - len(stackStr))


def getStackElems(elemlist):
    elemlistStrs = ['[']
    for elem in elemlist:
        if str(elem.__class__) == 'corpus.Token':
            elemlistStrs.append(elem.text)
        elif isinstance(elem, list) and len(elem) == 1 and isinstance(elem[0], list):
            elemlistStrs.extend(getStackElems(elem[0]))
        elif isinstance(elem, list) and len(elem):
            elemlistStrs.extend(getStackElems(elem))
    elemlistStrs.append(']')
    return elemlistStrs
