from corpus import Token


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
                buffStr += ', ' +self.buffer[1].text
                if len(self.buffer) > 2:
                    buffStr += ', ' + self.buffer[2].text + ' ,.. '
                else:
                    buffStr +=  ' ,.. '
            buffStr += ']'
        else:
            buffStr = '[ ]'
        return  'S= ' + stackStr + ' B= ' + buffStr  # + ' ; VMWEs = ' + tokensStr

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
