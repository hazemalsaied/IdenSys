from configuration import Configuration
from corpus import Token
from corpus import VMWE
from param import Parameters
from trannsition import Transition
from trannsition import TransitionType


class Parser:
    IMPOSSIBLE_SHIFT_TRANSITION = "ERROR: It's impossible to apply a SHIFT transition, the BUFFER is empty!"
    IMPOSSIBLE_MERGE_TRANSITION = "ERROR: It's impossible to apply a MERGE transition, the STACK doesn't contain two elements!"
    IMPOSSIBLE_COMPLETE_TRANSITION = "ERROR: It's impossible to apply a COMPLETE transition, the head of the STACK doesn't contain any element!"
    NO_TRANSITION_TYPE = "ERROR: No transition has been predicted by the classifier"

    @staticmethod
    def parse(classifier, dictVectorizer, sent):

        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        transDicList = []
        transLebelsList = []
        while not transition.configuration.isTerminalConf():

            config = transition.configuration
            if len(config.stack) == 0 and len(config.buffer) > 0:
                transition = Parser.applyShift(transition)
                transDicList.append({})
                transLebelsList.append(0)
            elif len(config.buffer) == 0 and len(config.stack) == 1:
                transition = Parser.applyComplete(transition, sent, parse=True)
                transDicList.append({})
                transLebelsList.append(2)
            else:
                featDic = Parser.getConfigurationFeatures(transition, sent)
                transDicList.append(featDic)
                # print sent# transPossibilities = []
                transType = classifier.predict(dictVectorizer.transform(featDic))
                # transType = Parser.getTransType(transPossibilities)
                if transType == 0:
                    if len(config.buffer) > 0:
                        transition = Parser.applyShift(transition)
                        transLebelsList.append(0)
                    else:
                        transition = Parser.applyComplete(transition, sent, parse=True)
                        transLebelsList.append(2)
                elif transType == 1:
                    if len(transition.configuration.stack) > 1:
                        transition = Parser.applyMerge(transition)
                        transLebelsList.append(1)
                    else:
                        transition = Parser.applyComplete(transition, sent, parse=True)
                        transLebelsList.append(2)
                elif transType == 2:
                    transition = Parser.applyComplete(transition, sent, parse=True)
                    transLebelsList.append(2)
                else:
                    print(Parser.NO_TRANSITION_TYPE)
        sent.initialTransition = initialTransition
        sent.featuresInfo = [transLebelsList, transDicList]
        return sent

    # @staticmethod
    # def getTransType(possibilities):
    #
    #     zeros = Parser.getFrequency(possibilities, 0)
    #     ones = Parser.getFrequency(possibilities, 1)
    #     twos = Parser.getFrequency(possibilities, 2)
    #     if zeros >= 2:
    #         return 0
    #     if twos >= 2:
    #         return 2
    #     if Parameters.useSurMerge:
    #         if ones > 2:
    #             return 1
    #     elif ones >= 2:
    #         return 1
    #     return 2

    @staticmethod
    def getFrequency(list, value):
        frequency = 0
        for item in list:
            if item == value:
                frequency += 1
        return frequency

    @staticmethod
    def staticParse(sent):
        sent = Parser.generateTransitions(sent)
        if sent is not None:
            return Parser.extractFeatures(sent)
        return None

    @staticmethod
    def extractFeatures(sent):

        transition = sent.initialTransition
        transDicList = []
        transLebelsList = []
        while True:
            if transition.next is None:
                break
            transLebelsList.append(transition.next.type.value)
            transDic = Parser.getConfigurationFeatures(transition, sent)
            transDicList.append(transDic)
            transition = transition.next
        sent.featuresInfo = [transLebelsList, transDicList]
        return [transLebelsList, transDicList]

    @staticmethod
    def getConfigurationFeatures(transition, sent):

        # print sent.text
        # if len(transition.configuration.stack) > 0:
        #     if isinstance(transition.configuration.stack[-1], Token):
        #         print 'S0 : ' + transition.configuration.stack[-1].text
        #     if len(transition.configuration.stack) > 1:
        #         if isinstance(transition.configuration.stack[-2], Token):
        #             print 'S1 : ' + transition.configuration.stack[-2].text
        #
        # if len(transition.configuration.buffer) > 0:
        #     print 'B0 : ' + transition.configuration.buffer[0].text
        #
        # print transition.configuration

        transDic = {}
        elemIdx = 0
        configuration = transition.configuration
        if Parameters.useStackLength and len(configuration.stack) > 0:
            transDic['StackLength'] = len(configuration.stack)
        if len(configuration.stack) >= 2:
            stackElements = [configuration.stack[-2], configuration.stack[-1]]
        else:
            stackElements = configuration.stack
        # General linguistic Informations
        if len(stackElements) > 0:
            elemIdx = len(stackElements) - 1
            for elem in stackElements:
                Parser.generateLinguisticFeatures(elem, 'S' + str(elemIdx), transDic)
                elemIdx -= 1
        if len(configuration.buffer) > 0:
            if Parameters.useFirstBufferElement:
                Parser.generateLinguisticFeatures(configuration.buffer[0], 'B0', transDic)
            if Parameters.useSecondBufferElement and len(configuration.buffer) > 1:
                Parser.generateLinguisticFeatures(configuration.buffer[1], 'B1', transDic)
        # Bi-Gram Generation
        if Parameters.useBiGram:
            if len(stackElements) > 1:
                # Generate a Bi-gram
                Parser.generateBiGram(stackElements[0], stackElements[1], 'S0S1', transDic)
            if len(stackElements) > 0 and len(configuration.buffer) > 0:
                Parser.generateBiGram(stackElements[-1], configuration.buffer[0], 'S0B0', transDic)
                if len(stackElements) > 1:
                    Parser.generateBiGram(stackElements[-2], configuration.buffer[0], 'S1B0', transDic)
                if len(configuration.buffer) > 1:
                    Parser.generateBiGram(stackElements[-1], configuration.buffer[1], 'S0B1', transDic)
                    if Parameters.generateS0B2Bigram and len(configuration.buffer) > 2:
                        Parser.generateBiGram(stackElements[-1], configuration.buffer[2], 'S0B2', transDic)
        # Tri-Gram Generation
        if Parameters.useTriGram and len(stackElements) > 1 and len(configuration.buffer) > 0:
            Parser.generateTriGram(stackElements[-2], stackElements[-1], configuration.buffer[0], 'S1S0B0', transDic)
        # Syntaxic Informations
        if len(stackElements) > 0 and Parameters.useSyntax:
            Parser.generateSyntaxicFeatures(configuration.stack, configuration.buffer, transDic)
        # Distance information
        if Parameters.useS0B0Distance and len(configuration.stack) > 0 and len(configuration.buffer) > 0:
            stackTokens = Configuration.getToken(configuration.stack[-1])
            transDic['S0B0Distance'] = str(
                sent.tokens.index(configuration.buffer[0]) - sent.tokens.index(stackTokens[-1]))
        if Parameters.useS0S1Distance and len(configuration.stack) > 1 and isinstance(configuration.stack[-1], Token) \
                and isinstance(configuration.stack[-2], Token):
            transDic['S0S1Distance'] = str(
                sent.tokens.index(configuration.stack[-1]) - sent.tokens.index(configuration.stack[-2]))
        Parser.addTransitionHistory(transition, transDic)
        return transDic

    @staticmethod
    def addTransitionHistory(transition, transDic):
        transitionHistoryLength1 = ''
        transitionHistoryLength2 = ''
        transitionHistoryLength3 = ''
        if transition.previous is not None and transition.previous.type is not None:
            transitionHistoryLength1 = str(transition.previous.type.value)
            if transition.previous.previous is not None and transition.previous.previous.type is not None:
                transitionHistoryLength2 = transitionHistoryLength1 + str(transition.previous.previous.type.value)
                if transition.previous.previous.previous is not None and transition.previous.previous.previous.type is not None:
                    transitionHistoryLength3 = transitionHistoryLength2 + str(
                        transition.previous.previous.previous.type.value)
        if Parameters.transitionHistoryLength1 and transitionHistoryLength1.strip() != '':
            transDic['transitionHistoryLength1'] = transitionHistoryLength1
        if Parameters.transitionHistoryLength2 and transitionHistoryLength2.strip() != '':
            transDic['transitionHistoryLength2'] = transitionHistoryLength2
        if Parameters.transitionHistoryLength3 and transitionHistoryLength3.strip() != '':
            transDic['transitionHistoryLength3'] = transitionHistoryLength3

    @staticmethod
    def generateLinguisticFeatures(token, label, transDic):

        if isinstance(token, Token):
            transDic[label + 'Token'] = token.text
            if Parameters.usePOS and token.posTag is not None and token.posTag.strip() != '':
                transDic[label + 'POS'] = token.posTag
            if Parameters.useLemma and token.lemma is not None and token.lemma.strip() != '':
                transDic[label + 'Lemma'] = token.lemma
            if not Parameters.useLemma and not Parameters.usePOS:
                transDic[label + '_LastThreeLetters'] = token.text[-3:]
        elif isinstance(token, list):
            tokens = Parser.getToken(token)
            transDic[label + 'Token'] = ''
            if Parameters.usePOS:
                transDic[label + 'POS'] = ''
            if Parameters.useLemma:
                transDic[label + 'Lemma'] = ''
            for token in tokens:
                transDic[label + 'Token'] += token.text + '_'
                if Parameters.usePOS and token.posTag.strip() != '':
                    transDic[label + 'POS'] += token.posTag + '_'
                if Parameters.useLemma and token.lemma.strip() != '':
                    transDic[label + 'Lemma'] += token.lemma + '_'
            transDic[label + 'Token'] = transDic[label + 'Token'][:-1]
            if Parameters.usePOS:
                if transDic[label + 'POS'].strip() == '':
                    transDic.pop(label + 'POS')
                else:
                    transDic[label + 'POS'] = transDic[label + 'POS'][:-1]
            if Parameters.useLemma:
                if transDic[label + 'Lemma'].strip() == '':
                    transDic.pop(label + 'Lemma')
                else:
                    transDic[label + 'Lemma'] = transDic[label + 'Lemma'][:-1]

    @staticmethod
    def generateSyntaxicFeatures(stack, buffer, dic):

        if stack is not None and len(stack) > 0:
            stack0 = stack[-1]
            if not isinstance(stack0, Token):
                return
            if int(stack0.dependencyParent) == -1 or int(
                    stack0.dependencyParent) == 0 or stack0.dependencyLabel.strip() == '':
                return

            if buffer is not None and len(buffer) > 0:
                for bElem in buffer:
                    if int(bElem.dependencyParent) != -1 and bElem.dependencyLabel.strip() != '':
                        if bElem.dependencyParent == stack0.position:
                            dic['hasRighDep_' + bElem.dependencyLabel] = 'true'
                            if stack0.lemma.strip() != '':
                                dic[stack0.lemma + '_hasRighDep_' + bElem.dependencyLabel] = 'true'
                                if bElem.lemma.strip() != '':
                                    dic[stack0.lemma + '_' + bElem.lemma + '_hasRighDep_' + bElem.dependencyLabel] \
                                        = 'true'
                                else:
                                    dic[stack0.lemma + '_' + bElem.text + '_hasRighDep_' + bElem.dependencyLabel] \
                                        = 'true'

                            else:
                                dic[stack0.text + 'hasRighDep_' + bElem.dependencyLabel] = 'true'
                                if bElem.lemma.strip() != '':
                                    dic[stack0.text + '_' + bElem.lemma + '_hasRighDep_' + bElem.dependencyLabel] \
                                        = 'true'
                                else:
                                    dic[stack0.text + '_' + bElem.text + '_hasRighDep_' + bElem.dependencyLabel] \
                                        = 'true'

            if stack0.dependencyParent > stack0.position:
                for bElem in buffer:
                    if bElem.position == stack0.dependencyParent:
                        if stack0.lemma.strip() != '':
                            if bElem.lemma.strip() != '':
                                dic[stack0.lemma + '_isGouvernedBy_' + bElem.lemma] = 'true'
                                if stack0.dependencyLabel != '':
                                    dic[
                                        stack0.lemma + '_isGouvernedBy_' + bElem.lemma + '_' + stack0.dependencyLabel] = 'true'
                            else:
                                dic[stack0.lemma + '_isGouvernedBy_' + bElem.text] = 'true'
                                if stack0.dependencyLabel != '':
                                    dic[stack0.lemma + '_isGouvernedBy_' + bElem.text + '_' + stack0.dependencyLabel] \
                                        = 'true'
                        else:
                            dic[stack0.text + '_isGouvernedBy_' + bElem.text] = 'true'
                            if stack0.dependencyLabel != '':
                                dic[stack0.text + '_isGouvernedBy_' + bElem.text + '_' + stack0.dependencyLabel] \
                                    = 'true'
                        break
            if len(stack) > 1:
                stack1 = stack[-2]
                if not isinstance(stack1, Token):
                    return
                if stack0.dependencyParent == stack1.position:
                    dic['SyntaxicRelation'] = '+' + stack0.dependencyLabel
                elif stack0.position == stack1.dependencyParent:
                    dic['SyntaxicRelation'] = '-' + stack1.dependencyLabel

    @staticmethod
    def generateTriGram(token0, token1, token2, label, transDic):
        idx = 0
        tokenDic = {}
        for token in [token0, token1, token2]:
            if isinstance(token, Token):
                tokenDic[idx] = Token(-1, token.text, token.lemma, token.posTag)
            elif isinstance(token, list):
                tokenDic[idx] = Token(-1, '', '', '')
                for subToken in Parser.getToken(token):
                    tokenDic[idx].text += subToken.text + '_'
                    if Parameters.useLemma:
                        if subToken.lemma.strip() != '':
                            tokenDic[idx].lemma += subToken.lemma + '_'
                    if Parameters.usePOS:
                        if subToken.posTag.strip() != '':
                            tokenDic[idx].posTag += subToken.posTag + '_'
                tokenDic[idx].text = tokenDic[idx].text[:-1]
                if Parameters.useLemma:
                    tokenDic[idx].lemma = tokenDic[idx].lemma[:-1]
                if Parameters.usePOS:
                    tokenDic[idx].posTag = tokenDic[idx].posTag[:-1]

            idx += 1
        token0 = tokenDic[0]
        token1 = tokenDic[1]
        token2 = tokenDic[2]
        transDic[label + 'Token'] = token0.text + '_' + token1.text + '_' + token2.text
        if Parameters.useLemma:
            if token0.lemma.strip() != '' and token1.lemma.strip() != '' and token2.lemma.strip() != '':
                transDic[label + 'Lemma'] = token0.lemma + '_' + token1.lemma + '_' + token2.lemma
        if Parameters.usePOS:
            if token0.posTag.strip() != '' and token1.posTag.strip() != '' and token2.posTag.strip() != '':
                transDic[label + 'POS'] = token0.posTag + '_' + token1.posTag + '_' + token2.posTag
        if Parameters.useLemma and Parameters.usePOS:
            if token0.lemma.strip() != '' and token1.posTag.strip() != '' and token2.posTag.strip() != '':
                transDic[label + 'LemmaPOS'] = token0.lemma + '_' + token1.posTag + '_' + token2.posTag
            if token0.posTag.strip() != '' and token1.lemma.strip() != '' and token2.posTag.strip() != '':
                transDic[label + 'POSLemma'] = token0.posTag + '_' + token1.lemma + '_' + token2.posTag
            if token0.posTag.strip() != '' and token1.posTag.strip() != '' and token2.lemma.strip() != '':
                transDic[label + 'POSLemma'] = token0.posTag + '_' + token1.posTag + '_' + token2.lemma

    @staticmethod
    def generateBiGram(token0, token1, label, transDic):
        idx = 0
        tokenDic = {}
        for token in [token0, token1]:
            if isinstance(token, Token):
                tokenDic[idx] = Token(-1, token.text, token.lemma, token.posTag)
            elif isinstance(token, list):
                tokenDic[idx] = Token(-1, '', '', '')
                for subToken in Parser.getToken(token):
                    tokenDic[idx].text += subToken.text + '_'
                    if Parameters.useLemma and subToken.lemma.strip() != '':
                        tokenDic[idx].lemma += subToken.lemma + '_'
                    if Parameters.usePOS and subToken.posTag.strip() != '':
                        tokenDic[idx].posTag += subToken.posTag + '_'
                tokenDic[idx].text = tokenDic[idx].text[:-1]
                if Parameters.useLemma:
                    tokenDic[idx].lemma = tokenDic[idx].lemma[:-1]
                if Parameters.usePOS:
                    tokenDic[idx].posTag = tokenDic[idx].posTag[:-1]

            idx += 1
        token0 = tokenDic[0]
        token1 = tokenDic[1]
        transDic[label + 'Token'] = token0.text + '_' + token1.text
        if Parameters.useLemma and token0.lemma.strip() != '' and token1.lemma.strip() != '':
            transDic[label + 'Lemma'] = token0.lemma + '_' + token1.lemma
        if Parameters.usePOS and token0.posTag.strip() != '' and token1.posTag.strip() != '':
            transDic[label + 'POS'] = token0.posTag + '_' + token1.posTag
        if Parameters.usePOS and Parameters.usePOS:
            if token0.lemma.strip() != '' and token1.posTag.strip() != '':
                transDic[label + 'LemmaPOS'] = token0.lemma + '_' + token1.posTag
            if token0.posTag.strip() != '' and token1.lemma.strip() != '':
                transDic[label + 'POSLemma'] = token0.posTag + '_' + token1.lemma

    @staticmethod
    def generateTransitions(sent):
        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        while transition is not None and not transition.isTerminal():
            transition = Parser.getNextTransition(transition, sent)
        if transition is not None:
            sent.initialTransition = initialTransition
            return sent
        return None

    @staticmethod
    def getNextTransition(transition, sent):

        config = transition.configuration
        if config.isInitial:
            return Parser.applyShift(transition)

        # Check for VMWE complete
        newTransition = Parser.checkForComplete(config, transition, sent)
        if newTransition is not None:
            return newTransition

        newTransition = Parser.checkForMerge(config, transition)
        if newTransition is not None:
            return newTransition

        # Check again for one word COMPLETE
        if len(config.stack) > 0 and config.stack[-1] is not None and not isinstance(config.stack[-1], list):
            if (len(config.stack[-1].parentMWEs) == 0):
                return Parser.applyComplete(transition, sent, parse=False)

            complete = True
            for parent in config.stack[-1].parentMWEs:
                if not parent.isEmbeded and not parent.isInterleaving:
                    complete = False
            if complete:
                return Parser.applyComplete(transition, sent, parse=False)

        if len(config.buffer) == 0 and len(config.stack) > 0:
            return Parser.applyComplete(transition, sent, parse=False)
        else:
            # Apply the default transition: SHIFT
            return Parser.applyShift(transition)

    @staticmethod
    def checkForComplete(config, transition, sent):
        # Check up for a possible COMPLETE of MWE after a MERGE transition
        if transition.type == TransitionType.MERGE:
            if len(config.stack) == 1 and isinstance(config.stack[0], list):
                vMWE = None
                parents = []
                tokens = Parser.getToken(config.stack[0])
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
                                # print sent
                                # print config
                                # print 'unexpected Scenario: two VMWE with the same lenght and the same components!'
                    vMWE = parents[0]
                if vMWE is not None and len(vMWE.tokens) == len(tokens):
                    return Parser.applyComplete(transition, sent, vMWE.id, vMWE.type)
        return None

    @staticmethod
    def checkForMerge(config, transition):
        # Check up of a possible MERGE
        if len(config.stack) > 1:
            hasParent = True

            tokens = []
            for elem in config.stack:
                tokens.extend(Parser.getToken(elem))

            for token in tokens:
                if len(token.parentMWEs) == 0:
                    hasParent = False
                    break
            if hasParent:
                parents = []
                for token in tokens:
                    for parent in token.parentMWEs:
                        if parent not in parents:
                            parents.append(parent)
                selectedParents = parents
                for parent in list(parents):
                    if len(parent.tokens) != len(tokens):
                        if parent in selectedParents:
                            selectedParents.remove(parent)
                        continue
                    for token in tokens:
                        if parent not in token.parentMWEs:
                            if parent in selectedParents:
                                selectedParents.remove(parent)
                if len(selectedParents) == 1 and not selectedParents[0].isEmbeded and not selectedParents[
                    0].isInterleaving and len(selectedParents[0].tokens) == len(tokens):
                    selectedParent = selectedParents[0]
                    return Parser.applyMerge(transition)
        return None

    @staticmethod
    def applyShift(transition):
        config = transition.configuration
        if len(config.buffer) > 0:

            lastToken = config.buffer[0]
            newBuffer = list(config.buffer)
            newBuffer = newBuffer[1:]
            newTokens = list(config.tokens)
            newStack = list(config.stack)
            newStack.append(lastToken)

            newConfig = Configuration(buffer=newBuffer, stack=newStack, tokens=newTokens)

            newTransition = Transition(TransitionType.SHIFT, newConfig, previous=transition)
            transition.next = newTransition
            return newTransition

        else:
            print config
            print(Parser.IMPOSSIBLE_SHIFT_TRANSITION)
            return None

    @staticmethod
    def applyMerge(transition):
        config = transition.configuration
        if len(config.stack) > 1:
            newBuffer = list(config.buffer)
            if Parameters.binaryMerge:
                newStack = list(config.stack)[:-2]
                newStack.append([config.stack[-2], config.stack[-1]])
            else:
                newStack = [list(config.stack)]
            newTokens = list(config.tokens)
            newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)
            newTransition = Transition(TransitionType.MERGE, newConfig, previous=transition)
            transition.next = newTransition
            return newTransition
        else:
            print config
            print(Parser.IMPOSSIBLE_MERGE_TRANSITION)
            return None

    @staticmethod
    def applyComplete(transition, sent, vMWEId=None, vMWEType=None, parse=False):
        config = transition.configuration
        if len(config.stack) > 0:

            newBuffer = list(config.buffer)
            newStack = list(config.stack)
            vMWETokens = Parser.getToken(newStack[0])
            newStack = newStack[:-1]
            newTokens = list(config.tokens)
            Parser.getVMWENumber(newTokens)
            if len(vMWETokens) > 1:
                if vMWEId is None:
                    vMWEId = Parser.getVMWENumber(newTokens) + 1
                vMWE = VMWE(vMWEId, vMWETokens[0], vMWEType)
                if parse:
                    sent.identifiedVMWEs.append(vMWE)
                vMWE.tokens = vMWETokens
                newTokens.append(vMWE)
            else:
                newTokens.append(vMWETokens[0])
            newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

            newTransition = Transition(TransitionType.COMPLETE, newConfig, previous=transition)
            transition.next = newTransition
            return newTransition

        else:
            print sent
            print config
            print(Parser.IMPOSSIBLE_COMPLETE_TRANSITION)
            return None

    @staticmethod
    def getVMWENumber(tokens):
        result = 0
        for token in tokens:
            if isinstance(token, VMWE):
                result += 1
        return result

    @staticmethod
    def getToken(elemlist):

        if isinstance(elemlist, Token):
            return [elemlist]
        result = []
        for elem in elemlist:
            if isinstance(elem, Token):
                result.append(elem)
            elif isinstance(elem, list):
                result.extend(Parser.getToken(elem))
        return result
