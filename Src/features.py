from Src.transitions import Configuration
from corpus import Corpus, Sentence, Token
from param import FeatParams


class Extractor:
    @staticmethod
    def extract(sent):
        transition = sent.initialTransition
        labels, features = [], []
        while True:
            if transition.next is None:
                break
            if transition.next.type.value != 3:
                labels.append(transition.next.type.value)
                features.append(Extractor.getFeatures(transition, sent))
            transition = transition.next

        sent.featuresInfo = [labels, features]
        return labels, features

    @staticmethod
    def getFeatures(transition, sent):

        transDic = {}
        configuration = transition.configuration

        if FeatParams.useStackLength and len(configuration.stack) > 1:
            transDic['StackLengthIs'] = len(configuration.stack)

        if len(configuration.stack) >= 2:
            stackElements = [configuration.stack[-2], configuration.stack[-1]]
        else:
            stackElements = configuration.stack

        # General linguistic Informations
        if len(stackElements) > 0:
            elemIdx = len(stackElements) - 1
            for elem in stackElements:
                Extractor.generateLinguisticFeatures(elem, 'S' + str(elemIdx), transDic)
                elemIdx -= 1

        if len(configuration.buffer) > 0:
            if FeatParams.useFirstBufferElement:
                Extractor.generateLinguisticFeatures(configuration.buffer[0], 'B0', transDic)

            if FeatParams.useSecondBufferElement and len(configuration.buffer) > 1:
                Extractor.generateLinguisticFeatures(configuration.buffer[1], 'B1', transDic)

        # Bi-Gram Generation
        if FeatParams.useBiGram:
            if len(stackElements) > 1:
                # Generate a Bi-gram S1S0 S0B0 S1B0 S0B1
                Extractor.generateBiGram(stackElements[-2], stackElements[-1], 'S1S0', transDic)
                if FeatParams.generateS1B1 and len(configuration.buffer) > 1:
                    Extractor.generateBiGram(stackElements[-2], configuration.buffer[1], 'S1B1', transDic)
            if len(stackElements) > 0 and len(configuration.buffer) > 0:
                Extractor.generateBiGram(stackElements[-1], configuration.buffer[0], 'S0B0', transDic)
                if len(stackElements) > 1:
                    Extractor.generateBiGram(stackElements[-2], configuration.buffer[0], 'S1B0', transDic)
                if len(configuration.buffer) > 1:
                    Extractor.generateBiGram(stackElements[-1], configuration.buffer[1], 'S0B1', transDic)
                    if FeatParams.generateS0B2Bigram and len(configuration.buffer) > 2:
                        Extractor.generateBiGram(stackElements[-1], configuration.buffer[2], 'S0B2', transDic)

        # Tri-Gram Generation
        if FeatParams.useTriGram and len(stackElements) > 1 and len(configuration.buffer) > 0:
            Extractor.generateTriGram(stackElements[-2], stackElements[-1], configuration.buffer[0], 'S1S0B0', transDic)

        # Syntaxic Informations
        if len(stackElements) > 0 and FeatParams.useSyntax:
            Extractor.generateSyntaxicFeatures(configuration.stack, configuration.buffer, transDic)

        # Distance information
        if FeatParams.useS0B0Distance and len(configuration.stack) > 0 and len(configuration.buffer) > 0:
            stackTokens = Configuration.getToken(configuration.stack[-1])
            transDic['S0B0Distance'] = str(
                sent.tokens.index(configuration.buffer[0]) - sent.tokens.index(stackTokens[-1]))
        if FeatParams.useS0S1Distance and len(configuration.stack) > 1 and isinstance(configuration.stack[-1], Token) \
                and isinstance(configuration.stack[-2], Token):
            transDic['S0S1Distance'] = str(
                sent.tokens.index(configuration.stack[-1]) - sent.tokens.index(configuration.stack[-2]))
        Extractor.addTransitionHistory(transition, transDic)

        if FeatParams.useLexic and len(configuration.buffer) > 0 and len(configuration.stack) >= 1:
            Extractor.generateDisconinousFeatures(configuration, sent, transDic)

        Extractor.enhanceMerge(transition, transDic)

        return transDic

    @staticmethod
    def enhanceMerge(transition, transDic):

        if not FeatParams.enhanceMerge:
            return
        config = transition.configuration
        if transition.type.value != 0 and len(config.buffer) > 0 and len(
                config.stack) > 0 and isinstance(config.stack[-1], Token):
            if isinstance(config.stack[-1], Token) and Extractor.areInLexic([config.stack[-1], config.buffer[0]]):
                transDic['S0B0InLexic'] = True

            if len(config.buffer) > 1 and Extractor.areInLexic([config.stack[-1], config.buffer[0], config.buffer[1]]):
                transDic['S0B0B1InLexic'] = True
            if len(config.buffer) > 2 and Extractor.areInLexic(
                    [config.stack[-1], config.buffer[0], config.buffer[1], config.buffer[2]]):
                transDic['S0B0B1B2InLexic'] = True
            if len(config.buffer) > 1 and len(config.stack) > 1 and Extractor.areInLexic(
                    [config.stack[-2], config.stack[-1], config.buffer[1]]):
                transDic['S1S0B1InLexic'] = True

        if len(config.buffer) > 0 and len(config.stack) > 1 and Extractor.areInLexic(
                [config.stack[-2], config.buffer[0]]) and not Extractor.areInLexic(
            [config.stack[-1], config.buffer[0]]):
            transDic['S1B0InLexic'] = True
            transDic['S0B0tInLexic'] = False
            if len(config.buffer) > 1 and Extractor.areInLexic(
                    [config.stack[-2], config.buffer[1]]) and not Extractor.areInLexic(
                [config.stack[-1], config.buffer[1]]):
                transDic['S1B1InLexic'] = True
                transDic['S0B1InLexic'] = False

    @staticmethod
    def generateDisconinousFeatures(configuration, sent, transDic):
        tokens = Sentence.getTokens([configuration.stack[-1]])
        tokenTxt = Sentence.getTokenLemmas(tokens)
        for key in Corpus.mweDictionary.keys():
            if tokenTxt in key and tokenTxt != key:
                bufidx = 0
                for bufElem in configuration.buffer[:5]:
                    if bufElem.lemma != '' and (
                                    (tokenTxt + ' ' + bufElem.lemma) in key or (bufElem.lemma + ' ' + tokenTxt) in key):
                        transDic['S0B' + str(bufidx) + 'ArePartsOfMWE'] = True
                        transDic['S0B' + str(bufidx) + 'ArePartsOfMWEDistance'] = sent.tokens.index(
                            bufElem) - sent.tokens.index(tokens[-1])
                    bufidx += 1
                break

    @staticmethod
    def generateLinguisticFeatures(token, label, transDic):

        if isinstance(token, list):
            token = Extractor.concatenateTokens([token])[0]
        transDic[label + 'Token'] = token.text
        if FeatParams.usePOS and token.posTag is not None and token.posTag.strip() != '':
            transDic[label + 'POS'] = token.posTag
        if FeatParams.useLemma and token.lemma is not None and token.lemma.strip() != '':
            transDic[label + 'Lemma'] = token.lemma
        if not FeatParams.useLemma and not FeatParams.usePOS:
            transDic[label + '_LastThreeLetters'] = token.text[-3:]
            transDic[label + '_LastTwoLetters'] = token.text[-2:]
        if FeatParams.useDictionary and ((
                                                         token.lemma != '' and token.lemma in Corpus.mweTokenDic.keys()) or token.text in Corpus.mweTokenDic.keys()):
            transDic[label + 'IsInLexic'] = 'true'

    @staticmethod
    def generateSyntaxicFeatures(stack, buffer, dic):

        if stack is not None and len(stack) > 0:
            stack0 = stack[-1]
            if not isinstance(stack0, Token):
                return
            if int(stack0.dependencyParent) == -1 or int(
                    stack0.dependencyParent) == 0 or stack0.dependencyLabel.strip() == '' or buffer is None and len(
                buffer) <= 0:
                return
            for bElem in buffer:
                if bElem.dependencyParent == stack0.position:
                    dic['hasRighDep_' + bElem.dependencyLabel] = 'true'
                    dic[stack0.getLemma() + '_hasRighDep_' + bElem.dependencyLabel] = 'true'
                    dic[stack0.getLemma() + '_' + bElem.getLemma() + '_hasRighDep_' + bElem.dependencyLabel] = 'true'

            if stack0.dependencyParent > stack0.position:
                for bElem in buffer:
                    if bElem.position == stack0.dependencyParent:
                        dic[stack0.lemma + '_isGouvernedBy_' + bElem.getLemma()] = 'true'
                        dic[stack0.lemma + '_isGouvernedBy_' + bElem.getLemma() + '_' + stack0.dependencyLabel] = 'true'
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

        tokens = Extractor.concatenateTokens([token0, token1, token2])
        Extractor.getFeatureInfo(transDic, label + 'Token', tokens, 'ttt')
        Extractor.getFeatureInfo(transDic, label + 'Lemma', tokens, 'lll')
        Extractor.getFeatureInfo(transDic, label + 'POS', tokens, 'ppp')
        Extractor.getFeatureInfo(transDic, label + 'LemmaPOSPOS', tokens, 'lpp')
        Extractor.getFeatureInfo(transDic, label + 'POSLemmaPOS', tokens, 'plp')
        Extractor.getFeatureInfo(transDic, label + 'POSPOSLemma', tokens, 'ppl')
        Extractor.getFeatureInfo(transDic, label + 'LemmaLemmaPOS', tokens, 'llp')
        Extractor.getFeatureInfo(transDic, label + 'LemmaPOSLemma', tokens, 'lpl')
        Extractor.getFeatureInfo(transDic, label + 'POSLemmaLemma', tokens, 'pll')

    @staticmethod
    def generateBiGram(token0, token1, label, transDic):

        tokens = Extractor.concatenateTokens([token0, token1])
        Extractor.getFeatureInfo(transDic, label + 'Token', tokens, 'tt')
        Extractor.getFeatureInfo(transDic, label + 'Lemma', tokens, 'll')
        Extractor.getFeatureInfo(transDic, label + 'POS', tokens, 'pp')
        Extractor.getFeatureInfo(transDic, label + 'LemmaPOS', tokens, 'lp')
        Extractor.getFeatureInfo(transDic, label + 'POSLemma', tokens, 'pl')

    @staticmethod
    def concatenateTokens(tokens):
        idx = 0
        tokenDic = {}
        result = []
        for token in tokens:
            if isinstance(token, Token):
                result.append(Token(-1, token.text, token.lemma, token.posTag))
            elif isinstance(token, list):
                tokenDic[idx] = Token(-1, '', '', '')
                for subToken in Sentence.getTokens(token):
                    tokenDic[idx].text += subToken.text + '_'
                    tokenDic[idx].lemma += subToken.lemma + '_'
                    tokenDic[idx].posTag += subToken.posTag + '_'
                tokenDic[idx].text = tokenDic[idx].text[:-1]
                tokenDic[idx].lemma = tokenDic[idx].lemma[:-1]
                tokenDic[idx].posTag = tokenDic[idx].posTag[:-1]
                result.append(tokenDic[idx])
            idx += 1
        return result

    @staticmethod
    def getFeatureInfo(dic, label, tokens, features):
        feature = ''
        idx = 0
        for token in tokens:
            if features[idx].lower() == 'l':
                if FeatParams.useLemma:
                    if token.lemma.strip() != '':
                        feature += token.lemma.strip() + '_'
                    else:
                        feature += '*' + '_'
            elif features[idx].lower() == 'p':
                if FeatParams.usePOS:
                    if token.posTag.strip() != '':
                        feature += token.posTag.strip() + '_'
                    else:
                        feature += '*' + '_'
            elif features[idx].lower() == 't':
                if token.text.strip() != '':
                    feature += token.text.strip() + '_'
            idx += 1
        if len(feature) > 0:
            feature = feature[:-1]
            dic[label] = feature

        return ''

    @staticmethod
    def areInLexic(tokensList):
        if Sentence.getTokenLemmas(tokensList) in Corpus.mweDictionary.keys():
            return True
        return False

    @staticmethod
    def addTransitionHistory(transition, transDic):

        if FeatParams.historyLength1:
            Extractor.getTransitionHistory(transition, 1, 'TransHistory1', transDic)
        if FeatParams.historyLength2:
            Extractor.getTransitionHistory(transition, 2, 'TransHistory2', transDic)
        if FeatParams.historyLength3:
            Extractor.getTransitionHistory(transition, 3, 'TransHistory3', transDic)

    @staticmethod
    def getTransitionHistory(transition, length, label, transDic):
        idx = 0
        history = ''
        transRef = transition
        transition = transition.previous
        while transition is not None and idx < length:
            if transition.type is not None:
                history += str(transition.type.value)
            transition = transition.previous
            idx += 1
        if len(history) == length:
            transDic[label] = history
        transition = transRef
