import os
import operator
import nltk
from nltk import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer


class Corpus:
    """
        a class used to encapsulate all the information of the corpus
    """

    def __init__(self, path):
        """
            an initializer of the corpus, responsible of creating a structure of objects encapsulating all the information
            of the corpus, its sentences, tokens and MWEs.

            This function iterate over the lines of corpus document to create the precedent ontology
        :param path: the physical path of the corpus document
        """
        self.sentNum, self.mweNum, self.intereavingNum, self.emeddedNum = 0, 0, 0, 0

        conlluFile = None
        if os.path.isfile(os.path.join(path, 'train.conllu')):
            conlluFile = os.path.join(path, 'train.conllu')
        mweFile = os.path.join(path, 'train.parsemetsv')
        self.sentences = []
        testConllu = None
        testBlind = os.path.join(path, 'test.blind.parsemetsv')
        if os.path.isfile(os.path.join(path, 'test.conllu')):
            testConllu = os.path.join(path, 'test.conllu')

        if conlluFile is not None and testConllu is not None:
            self.sentences = Corpus.readConlluFile(conlluFile)
            self.mweNum = Corpus.readMweFile(mweFile, self.sentences)
            self.sentNum = len(self.sentences)

            for sent in self.sentences:
                self.emeddedNum += sent.recognizeEmbededVMWEs()
                self.intereavingNum += sent.recognizeInterleavingVMWEs()

            self.testSents = Corpus.readConlluFile(testConllu)
        else:
            self.sentences, self.sentNum, self.mweNum = Corpus.readSentences(mweFile)
            self.testSents, x, y = Corpus.readSentences(testBlind, forTest=True)
            for sent in self.sentences:
                self.emeddedNum += sent.recognizeEmbededVMWEs()
                self.intereavingNum += sent.recognizeInterleavingVMWEs()

    @staticmethod
    def readConlluFile(conlluFile):
        sentences = []
        with open(conlluFile) as corpusFile:
            # Read the corpus file
            lines = corpusFile.readlines()
            sent = None
            senIdx = 0
            sentId = ''
            sentenceText = ''
            for line in lines:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('# sentid:'):
                    sentId = line.split('# sentid:')[1].strip()


                elif line.startswith('# sentence-text:'):
                    continue

                elif line.startswith('1\t'):
                    if sentId.strip() != '':
                        sent = Sentence(senIdx, sentid=sentId)
                    else:
                        sent = Sentence(senIdx)
                    senIdx += 1
                    sentences.append(sent)

                if not line.startswith('#'):
                    lineParts = line.split('\t')

                    if len(lineParts) != 10 or '-' in lineParts[0]:
                        continue
                    morpho = ''
                    if lineParts[5] != '_':
                        morpho = lineParts[5].split('|')
                    if lineParts[6] != '_':
                        token = Token(lineParts[0], lineParts[1], lemma=lineParts[2], posTag=lineParts[3],
                                      abstractPosTag=lineParts[3], morphologicalInfo=morpho,
                                      dependencyParent=int(lineParts[6]),
                                      dependencyLabel=lineParts[7])
                    else:
                        token = Token(lineParts[0], lineParts[1], lemma=lineParts[2], posTag=lineParts[3],
                                      abstractPosTag=lineParts[3], morphologicalInfo=morpho,
                                      dependencyLabel=lineParts[7])

                    # Associate the token with the sentence
                    sent.tokens.append(token)
                    sent.text += token.text + ' '
        return sentences

    @staticmethod
    def readMweFile(mweFile, sentences):
        mweNum = 0
        with open(mweFile) as corpusFile:

            # Read the corpus file
            lines = corpusFile.readlines()
            noSentToAssign = False
            sentIdx = 0
            for line in lines:
                if line == '\n' or line.startswith('# sentence-text:') or (
                             line.startswith('# sentid:') and noSentToAssign) :
                    continue
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('1\t'):
                    sent = sentences[sentIdx]
                    sentIdx += 1
                lineParts = line.split('\t')
                if '-' in lineParts[0]:
                    continue
                if lineParts is not None and len(lineParts) == 4 and lineParts[3] != '_':

                    token = sent.tokens[int(lineParts[0]) - 1] #[t for t in sent.tokens if t.position == int(lineParts[0])]
                    #if tokens is not None and len(tokens) > 0:
                    #    token = tokens[0]
                    vMWEids = lineParts[3].split(';')
                    for vMWEid in vMWEids:
                        id = int(vMWEid.split(':')[0])
                        # New MWE captured
                        if id not in sent.getWMWEIds():
                            if len(vMWEid.split(':')) > 1:
                                type = str(vMWEid.split(':')[1])
                                vMWE = VMWE(id, token, type)
                            else:
                                vMWE = VMWE(id, token)
                            mweNum += 1
                            sent.vMWEs.append(vMWE)
                        # Another token of an under-processing MWE
                        else:
                            vMWE = sent.getVMWE(id)
                            if vMWE is not None:
                                vMWE.addToken(token)
                        # associate the token with the MWE
                        token.setParent(vMWE)
        return mweNum

    @staticmethod
    def readSentences(mweFile, forTest=False):
        sentences = []
        sentNum, mweNum = 0, 0
        with open(mweFile) as corpusFile:
            # Read the corpus file
            lines = corpusFile.readlines()
            sent = None
            senIdx = 1
            for line in lines:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('1\t'):
                    # sentId = line.split('# sentid:')[1]
                    if sent is not None:
                        # Represent the sentence as a sequece of tokens and POS tags
                        sent.setTextandPOS()
                        if not forTest:
                            sent.recognizeEmbededVMWEs()
                            sent.recognizeInterleavingVMWEs()
                    sent = Sentence(senIdx)
                    senIdx += 1
                    sentences.append(sent)

                elif line.startswith('# sentence-text:'):
                    sentText = ''
                    if len(line.split(':')) > 1:
                        sent.text = line.split('# sentence-text:')[1]

                lineParts = line.split('\t')

                # Empty line or lines of the form: "8-9	can't	_	_"
                if len(lineParts) != 4 or '-' in lineParts[0]:
                    continue
                token = Token(lineParts[0], lineParts[1])
                # Trait the MWE
                if not forTest and lineParts[3] != '_':
                    vMWEids = lineParts[3].split(';')
                    for vMWEid in vMWEids:
                        id = int(vMWEid.split(':')[0])
                        # New MWE captured
                        if id not in sent.getWMWEIds():
                            type = str(vMWEid.split(':')[1])
                            vMWE = VMWE(id, token, type)
                            mweNum += 1
                            sent.vMWEs.append(vMWE)
                        # Another token of an under-processing MWE
                        else:
                            vMWE = sent.getVMWE(id)
                            if vMWE is not None:
                                vMWE.addToken(token)
                        # associate the token with the MWE
                        token.setParent(vMWE)
                # Associate the token with the sentence
                sent.tokens.append(token)
            sentNum = len(sentences)
            return sentences, sentNum, mweNum


class Sentence:
    """
       a class used to encapsulate all the information of a sentence
    """

    def __init__(self, id, sentid=''):

        self.sentid = sentid
        self.id = id
        self.tokens = []
        self.vMWEs = []
        self.identifiedVMWEs = []
        self.text = ''
        self.initialTransition = None
        self.featuresInfo = []

    @staticmethod
    def fromTextToSent(text):

        tokenizer = WordPunctTokenizer()
        wordNetLemmatiser = WordNetLemmatizer()
        sent = Sentence(0)
        sent.text = text
        tokenList = tokenizer.tokenize(text)
        posTags = nltk.pos_tag(tokenList)
        for token in tokenList:
            tokenLemma = wordNetLemmatiser.lemmatize(token)
            tokenPos = posTags[tokenList.index(token)][1]
            tokenObj = Token(tokenList.index(token), token, lemma=tokenLemma, posTag=tokenPos)
            sent.tokens.append(tokenObj)
        return sent

    def getWMWEs(self):
        return self.vMWEs

    def getWMWEIds(self):
        result = []
        for vMWE in self.vMWEs:
            result.append(vMWE.getId())
        return result

    def getVMWE(self, id):

        for vMWE in self.vMWEs:
            if vMWE.getId() == int(id):
                return vMWE
        return None

    def setTextandPOS(self):

        tokensTextList = []
        for token in self.tokens:
            self.text += token.text + ' '
            tokensTextList.append(token.text)
        self.text = self.text.strip()

    def recognizeEmbededVMWEs(self):
        if len(self.vMWEs) <= 1:
            return 0
        result = 0
        traitedPairs = []
        for vMwe1 in self.vMWEs:
            for vMwe2 in self.vMWEs:
                if vMwe1 is not vMwe2:
                    isTraited = False
                    for pair in traitedPairs:
                        if vMwe1 in pair and vMwe2 in pair:
                            isTraited = True
                    if not isTraited:
                        traitedPairs.append([vMwe1, vMwe2])
                        # Get The longer VMWE
                        masterVmwe = vMwe1
                        slaveVmwe = vMwe2
                        if len(vMwe2.tokens) > len(vMwe2.tokens):
                            masterVmwe = vMwe2
                            slaveVmwe = vMwe1
                        slaveVmwe.isEmbeded = True
                        for token in slaveVmwe.tokens:
                            if masterVmwe not in token.parentMWEs:
                                slaveVmwe.isEmbeded = False
                        if slaveVmwe.isEmbeded:
                            result += 1
        return result

    def recognizeInterleavingVMWEs(self):
        if len(self.vMWEs) <= 1:
            return 0
        result = 0
        for vmwe in self.vMWEs:
            if vmwe.isEmbeded or vmwe.isInterleaving:
                continue
            for token in vmwe.tokens:
                if len(token.parentMWEs) > 1:
                    for parent in token.parentMWEs:
                        if parent is not vmwe:
                            if parent.isEmbeded:
                                continue
                            parents = sorted(token.parentMWEs, key=lambda VMWE: VMWE.id)
                            if parent != parents[0]:
                                parent.isInterleaving = True
                                result += 1
        return result

    def getCorpusText(self, gold=True):
        if gold:
            mwes = self.vMWEs
        else:
            mwes = self.identifiedVMWEs
        lines = ''
        idx = 1
        for token in self.tokens:
            line = str(idx) + '\t' + token.text + '\t_\t'
            idx += 1
            for mwe in mwes:
                if token in mwe.tokens:
                    if line.endswith('\t'):
                        line += str(mwe.id)
                    else:
                        line += ';' + str(mwe.id)
            if line.endswith('\t'):
                line += '_'
            lines += line + '\n'
        return lines

    def getCorpusTextWithPlus(self):
        goldMwes = self.vMWEs
        predMwes = self.identifiedVMWEs
        lines = ''
        idx = 1
        for token in self.tokens:
            line = str(idx) + '\t' + token.text + '\t_\t'
            idx += 1
            for mwe in goldMwes:
                if token in mwe.tokens:
                    if line.endswith('\t'):
                        line += '+'
                        break

            if line.endswith('\t'):
                line += '_\t'
            else:
                line += '\t'
            for mwe in predMwes:
                if token in mwe.tokens:
                    if line.endswith('\t'):
                        line += '+'
                        break
            if line.endswith('\t'):
                line += '_'
            lines += line + '\n'
        return lines

    def printSummary(self):
        vMWEText = ''
        for vMWE in self.vMWEs:
            vMWEText += str(vMWE) + '\n'
        if len(self.identifiedVMWEs) > 0:
            identifiedMWE = '### Identified MWEs: \n'
            for mwe in self.identifiedVMWEs:
                identifiedMWE += str(mwe) + '\n'
        else:
            identifiedMWE = ''

        return '## Sentence No. ' + str(self.id) + ' - ' + self.sentid + '\n' + self.text + \
               '\n### Existing MWEs: \n' + vMWEText + identifiedMWE

    def __str__(self):

        vMWEText = ''
        for vMWE in self.vMWEs:
            vMWEText += str(vMWE) + '\n'
        if len(self.identifiedVMWEs) > 0:
            identifiedMWE = '### Identified MWEs: \n'
            for mwe in self.identifiedVMWEs:
                identifiedMWE += str(mwe) + '\n\n'
        else:
            identifiedMWE = ''
        featuresInfo = ''

        result = ''
        transition = self.initialTransition
        idx = 0
        while True:
            type = ''
            configuration = ''
            if transition is not None:
                if transition.type is not None:
                    type = transition.type.name
                else:
                    type = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                configuration = str(transition.configuration)
                if type == 'MERGE':
                    type = '**MERGE**&nbsp;&nbsp;&nbsp;'
                if len(type) == 'SHIFT':
                    type = type + '&nbsp;&nbsp;&nbsp;'
                result += '\n\n' + str(
                    transition.id) + '- ' + type + '&nbsp;&nbsp;&nbsp;' + '>' + '&nbsp;&nbsp;&nbsp;' + configuration + '\n\n'
                if transition.next is None:
                    break
                transition = transition.next
                if len(self.featuresInfo) == 2 and len(self.featuresInfo[1] )> 0:
                    sortedDic = sorted(self.featuresInfo[1][idx].items(), key=operator.itemgetter(0))
                    for item in sortedDic:
                        result += str(item[0]) + ': ' + str(item[1]) + ', '
                idx += 1
            else:        #result += str(self.featuresInfo[1][idx]) + '\n\n'
                break

        # if len(self.featuresInfo) == 2:
        #     labels = self.featuresInfo[0]
        #     features = self.featuresInfo[1]
        #     for x in xrange(0, len(labels)):
        #         featuresInfo += str(x) + '- ' + str(labels[x]) + ' : ' + str(features[x]) + '\n\n'
        return '## Sentence No. ' + str(self.id) + ' - ' + self.sentid + '\n' + self.text + \
               '\n### Existing MWEs: \n' + vMWEText + identifiedMWE \
               + '\n' + result #str(self.initialTransition) + '\n### Features: \n' + featuresInfo


class Token:
    """
        a class used to encapsulate all the information of a sentence tokens
    """

    def __init__(self, position, txt, lemma='', posTag='', abstractPosTag='', morphologicalInfo=[], dependencyParent=-1,
                 dependencyLabel=''):
        self.position = int(position)
        self.text = txt
        # if lemma == '':
        #    self.lemma = Token.wordNetLemmatiser.lemmatize(txt)
        # else:
        self.lemma = lemma
        self.abstractPosTag = abstractPosTag
        self.posTag = posTag
        self.morphologicalInfo = morphologicalInfo
        self.dependencyParent = dependencyParent
        self.dependencyLabel = dependencyLabel
        self.parentMWEs = []

    def setParent(self, vMWE):
        self.parentMWEs.append(vMWE)

    def __str__(self):
        parentTxt = ''
        if len(self.parentMWEs) != 0:
            for parent in self.parentMWEs:
                parentTxt += str(parent) + '\n'

        return str(self.position) + ' : ' + self.text + ' : ' + self.posTag + '\n' + 'parent VMWEs\n' + parentTxt


class VMWE:
    """
        A class used to encapsulate the information of a verbal multi-word expression
    """

    def __init__(self, id, token=None, type=None, isEmbeded=False, isInterleaving=False, isInTrainingCorpus=0):
        self.id = int(id)
        self.isInTrainingCorpus = isInTrainingCorpus
        self.tokens = []
        if token is not None:
            self.tokens.append(token)
        self.type = ''
        if type is not None:
            self.type = type
        self.isEmbeded = isEmbeded
        self.isInterleaving = isInterleaving
        self.isVerbal = True

    def getId(self):
        return self.id

    def addToken(self, token):
        self.tokens.append(token)

    @staticmethod
    def isVerbalMwe(mwe):
        isVerbal = False
        for token in mwe.tokens:
            if token.posTag.startswith('V'):
                isVerbal = True
        return isVerbal

    def __str__(self):
        tokensStr = ''
        for token in self.tokens:
            tokensStr += token.text + ' '
        tokensStr = tokensStr.strip()
        isInterleaving = ''
        if self.isInterleaving:
            isInterleaving = ', Interleaving '
        isEmbedded = ''
        if self.isEmbeded:
            isEmbedded = ', Embedded'
        inTrainingCorpus = ''
        if self.isInTrainingCorpus != 0:
            inTrainingCorpus = ', ' + str(self.isInTrainingCorpus)
        type = ''
        if self.type != '':
            type = '(' + self.type
            if self.isInTrainingCorpus != 0:
                type += ', ' + str(self.isInTrainingCorpus) + ')'
            else:
                type += ')'
        return str(self.id) + '- ' + '**' + tokensStr + '** ' + type + isEmbedded + isInterleaving

    def getString(self):
        result = ''
        for token in self.tokens:
            result += token.text + ' '
        return result[:-1]

    def getLemmaString(self):
        result = ''
        for token in self.tokens:
            if token.lemma.strip() != '':
                result += token.lemma + ' '
            else:
                result += token.text + ' '
        return result[:-1]
