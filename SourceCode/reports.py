import codecs
import os
from random import randint
import operator
from param import Parameters


class Report:
    NumOFSent = '## Number of Sentences: '
    NumOFMWEs = '\n## Number of MWEs: '
    NumOFEmbedded = '\n## Number of Embedded MWEs: '
    NumOFInterleaving = '\n## Number of Interleaving MWEs: '

    @staticmethod
    def createResultFolder(corpus):
        # creating an initial report
        if Parameters.printReport:
            Parameters.resultPath = os.path.join(Parameters.resultPath, Parameters.languageName)
            # languageName = Parameters.corpusPath.split('/')[-1]
            # if len(languageName) > 0:
            #     Parameters.resultPath = os.path.join(Parameters.resultPath, languageName)
            # else:
            #     Parameters.resultPath = os.path.join(Parameters.resultPath, Parameters.corpusPath.split('/')[-2])

            Parameters.resultPath = os.path.join(Parameters.resultPath, Parameters.xpName)
            if not os.path.exists(Parameters.resultPath):
                os.makedirs(Parameters.resultPath)
            # Create configuration file

            staticParsingFile = open(os.path.join(Parameters.resultPath, 'config.md'), 'w')
            staticParsingFile.write(Parameters.toString())

            result = Report.NumOFSent + str(corpus.sentNum) + Report.NumOFMWEs + str(
                corpus.mweNum) + '\n' + Report.NumOFEmbedded + str(
                corpus.emeddedNum) + '\n' + Report.NumOFInterleaving + str(
                corpus.intereavingNum) + '\n'
            Report.editReadme('w', result)
    @staticmethod
    def createMWELexic(dic, dir):
        sortedDic = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        pathItems = Parameters.resultPath.split('/')
        if pathItems[-1].split() != '':
            pathItems = pathItems[:-1]
        else:
            pathItems = pathItems[:-2]
        path = '/'
        for item in pathItems:
            path += item + '/'
        path = os.path.join(path, dir + '/Dictionary.md')
        #path += dir + '/Dictionary.md'
        result = ''
        for item in sortedDic:
            result += str(item[0]) + ': ' + str(item[1]) + '\n\n'
        dicFile = open(path, 'w')
        dicFile.write(result)

    @staticmethod
    def editReadme(mode, text):
        if Parameters.useCrossValidation:
            printingPath = os.path.join(Parameters.resultPath, 'Readme.md')
        else:
            printingPath = os.path.join(Parameters.resultPath, 'Readme.md')
        staticParsingFile = open(printingPath, mode)
        staticParsingFile.write(text)

    @staticmethod
    def createStaticParsingReports(sents, crossValidationIdx=''):
        sentsForPrinting = [s for s in sents if len(s.vMWEs) >= 2]
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        if len(sentsForPrinting) - 30 > 0:
            random = randint(1, len(sentsForPrinting) - 30)
        else:
            random = 0
        sentsForPrinting = sentsForPrinting[random:random + 5]
        printingPath = os.path.join(Parameters.resultPath, 'StaticParsing' + str(crossValidationIdx) + '.md')
        staticParsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting:
            result += str(sent)
        staticParsingFile.write(result)

    @staticmethod
    def createEmbeddingSentsReports(sents, crossValidationIdx=''):
        sentsForPrinting = [s for s in sents if Report.isEmbeddedSent(s)]

        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        printingPath = os.path.join(Parameters.resultPath, 'EmbeddedSents' + str(crossValidationIdx) + '.md')
        staticParsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting:
            result += str(sent)
        staticParsingFile.write(result)

    @staticmethod
    def isEmbeddedSent(sent):
        for mwe in sent.vMWEs:
            if mwe.isEmbeded or mwe.isInterleaving:
                return True
        return False

    @staticmethod
    def createParsingReport(testingSents, crossValidationIdx=''):
        sentsForPrinting = [s for s in testingSents if len(s.vMWEs) >= 1]
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        if len(sentsForPrinting) - 30 > 0:
            random = randint(1, len(sentsForPrinting) - 30)
        else:
            random = 0
        printingPath = os.path.join(Parameters.resultPath, 'Parsing' + str(crossValidationIdx) + '.md')
        staticParsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting[random:random + 5]:
            result += str(sent)
        staticParsingFile.write(result)

        # Producing a long report
        printingPath = os.path.join(Parameters.resultPath, 'Parsing' + str(crossValidationIdx) + '-long.md')
        staticParsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting:
            result += sent.printSummary()
        staticParsingFile.write(result)
