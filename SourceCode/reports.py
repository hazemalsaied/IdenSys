import operator
import os
from random import randint

from param import Parameters


class Report:
    NumOFSent = '### Number of Sentences: '
    NumOFMWEs = '\n### Number of MWEs: '
    NumOFEmbedded = '\n### Number of Embedded MWEs: '
    NumOFInterleaving = '\n### Number of Interleaving MWEs: '
    NumContinousMWEs = '\n### Number of Continous MWEs: '
    NumSingleWordMWEs = '\n### Number of Single Word MWEs: '

    @staticmethod
    def createLanguageFolder(langName):
        if Parameters.printReport:
            Parameters.langFolder = os.path.join(Parameters.resultPath, langName)
            if not os.path.exists(Parameters.langFolder):
                os.makedirs(Parameters.langFolder)

    @staticmethod
    def createXPFolder(configFile):
        xpFolder = Parameters.toBinary()
        if Parameters.printReport:
            Parameters.xpPath = os.path.join(Parameters.langFolder, configFile)
            if not os.path.exists(Parameters.xpPath):
                os.makedirs(Parameters.xpPath)

    @staticmethod
    def createConfigAndReadMe(corpus):
        if Parameters.printReport:
            staticParsingFile = open(os.path.join(Parameters.xpPath, 'config.md'), 'w')
            staticParsingFile.write(Parameters.toString())

            result = Report.NumOFSent + str(corpus.sentNum) + Report.NumOFMWEs + str(
                corpus.mweNum) + '\n' + Report.NumOFEmbedded + str(
                corpus.emeddedNum) + '\n' + Report.NumOFInterleaving + str(
                corpus.intereavingNum) + '\n' + Report.NumContinousMWEs + str(
                corpus.continousExp) + '\n' + Report.NumSingleWordMWEs + str(corpus.singleWordExp)
            Report.editReadme('w', result)

    @staticmethod
    def createMWELexic(dic, dir):
        sortedDic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        pathItems = Parameters.resultPath.split('/')
        if pathItems[-1].split() != '':
            pathItems = pathItems[:-1]
        else:
            pathItems = pathItems[:-2]
        path = ''
        for item in pathItems:
            path += item + '/'
        path = os.path.join(path, dir + '/Dictionary.md')
        # path += dir + '/Dictionary.md'
        result = ''
        for item in sortedDic:
            result += str(item[0]) + ': ' + str(item[1]) + '\n\n'
        dicFile = open(path, 'w')
        dicFile.write(result)

    @staticmethod
    def editReadme(mode, text):
        printingPath = os.path.join(Parameters.xpPath, 'Readme.md')
        staticParsingFile = open(printingPath, mode)
        staticParsingFile.write(text)

    @staticmethod
    def createStaticParsingReports(sents, crossValidationIdx=''):
        sentsForPrinting = [s for s in sents if len(s.vMWEs) >= 2]
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        sentsForPrinting = sentsForPrinting[0:5]
        printingPath = os.path.join(Parameters.xpPath, 'StaticParsing' + str(crossValidationIdx) + '.md')
        staticParsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting:
            result += str(sent)
        staticParsingFile.write(result)

    @staticmethod
    def createEmbeddingSentsReports(sents, crossValidationIdx=''):
        sentsForPrinting = [s for s in sents if Report.isEmbeddedSent(s)]

        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        printingPath = os.path.join(Parameters.xpPath, 'EmbeddedSents' + str(crossValidationIdx) + '.md')
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

        result = ''
        for sent in sentsForPrinting :
            if sent.id == 2795:
                result += str(sent)
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        printingPath = os.path.join(Parameters.xpPath, 'Parsing' + str(crossValidationIdx) + '.md')
        staticParsingFile = open(printingPath, 'w')

        for sent in sentsForPrinting[0:5]:
            result += str(sent)
        staticParsingFile.write(result)

        # Producing a long report
        printingPath = os.path.join(Parameters.xpPath, 'Parsing' + str(crossValidationIdx) + '-long.md')
        staticParsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting:
            result += sent.printSummary()
        staticParsingFile.write(result)

    @staticmethod
    def editTotalReadMe(fScore, recall, precision, corpus, testSents):

        mwes, singleMWE, continousMWEs, interleavingMwes, embeddedMwes = Report.getTestStatistics(testSents)

        identifiedMwes, identifiedSingleMWE, identifiedContinousMWEs = Report.getIdentifiedTestStatistics(testSents)

        report = Parameters.languageName + ',' + str("%.3f" % fScore) + ',' + str("%.3f" % recall) + ',' + str(
            "%.3f" % precision) + ','

        report += str(corpus.sentNum) + ',' + str(corpus.mweNum) + ',' + str(
            corpus.mweNum - corpus.continousExp) + ',' + str(corpus.intereavingNum) + ',' + str(
            corpus.singleWordExp) + ',' + str(corpus.emeddedNum) + ','

        report += str(mwes) + ',' + str(identifiedMwes) + ',' + str(singleMWE) + ',' + str(identifiedSingleMWE) + ','
        report += str(mwes - continousMWEs) + ',' + str(identifiedMwes - identifiedContinousMWEs) + ',' +  Parameters.toBinary() + '\n'

        with open(Parameters.results, "a") as staticParsingFile:
            staticParsingFile.write(report)

    @staticmethod
    def getTestStatistics(sents):
        singleMWE = 0
        continousMWEs = 0
        interleavingMwes = 0
        embeddedMwes = 0
        mwes = 0
        for sent in sents:
            mwes += len(sent.vMWEs)
            for mwe in sent.vMWEs:
                if mwe.isInterleaving:
                    interleavingMwes += 1
                if mwe.isSingleWordExp:
                    singleMWE += 1
                if mwe.isContinousExp:
                    continousMWEs += 1
                if mwe.isEmbeded:
                    embeddedMwes += 1
                if mwe.isInterleaving:
                    embeddedMwes += 1
        return mwes, singleMWE, continousMWEs, interleavingMwes, embeddedMwes

    @staticmethod
    def getIdentifiedTestStatistics(sents):
        singleMWE = 0
        continousMWEs = 0
        mwes = 0
        for sent in sents:
            mwes += len(sent.identifiedVMWEs)
            for mwe in sent.identifiedVMWEs:
                if len(mwe.tokens) == 1:
                    singleMWE += 1
                if sent.isContinousMwe(mwe):
                    continousMWEs += 1

        return mwes, singleMWE, continousMWEs
