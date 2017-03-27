import operator
import os

from param import Parameters


class Report:
    @staticmethod
    def createLanguageFolder(langName):
        Parameters.langFolder = os.path.join(Parameters.resultPath, langName)
        if not os.path.exists(Parameters.langFolder):
            os.makedirs(Parameters.langFolder)

    @staticmethod
    def createMWELexic(dic):
        if Parameters.printReport:
            sortedDic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
            pathItems = Parameters.resultPath.split('/')
            if pathItems[-1].split() != '':
                pathItems = pathItems[:-1]
            else:
                pathItems = pathItems[:-2]
            path = ''
            for item in pathItems:
                path += item + '/'
            path = os.path.join(path, Parameters.languageName + '/Dictionary.md')
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
        if not Parameters.printReport:
            return
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
    def createParsingReport(testingSents, mweDictionary, crossValidationIdx=''):

        if not Parameters.printReport:
            return

            # Adding the source of MWE
        for sent in testingSents:
            for mwe in sent.vMWEs:
                if mwe.getLemmaString() in mweDictionary.keys():
                    mwe.isInTrainingCorpus = mweDictionary[mwe.getLemmaString()]

        sentsForPrinting = [s for s in testingSents if len(s.vMWEs) >= 1]

        result = ''
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        printingPath = os.path.join(Parameters.xpPath, 'Parsing' + str(crossValidationIdx) + '.md')
        parsingFile = open(printingPath, 'w')

        for sent in sentsForPrinting[0:5]:
            result += str(sent)
        parsingFile.write(result)

        # Producing a long report
        printingPath = os.path.join(Parameters.xpPath, 'Parsing' + str(crossValidationIdx) + '-long.md')
        parsingFile = open(printingPath, 'w')
        result = ''
        for sent in sentsForPrinting:
            result += sent.printSummary()
        parsingFile.write(result)

    @staticmethod
    def editTotalReadMe(fScore, recall, precision, corpus, testSents, identifiedIntellegentillyPrecent=.0,
                        identifiedSemiIntellegentillyPercent=.0):
        # if not Parameters.printReport:
        #    return
        report = ''
        mwes, singleMWE, continousMWEs, interleavingMwes, embeddedMwes, identifiedMwes, identifiedSingleMWE, identifiedContinousMWEs = 0, 0, 0, 0, 0, 0, 0, 0,
        if Parameters.useCrossValidation:
            report = Parameters.languageName + ',' + str("%.3f" % fScore) + ',' + str("%.3f" % recall) + ',' + str(
                "%.3f" % precision) + ',' + str("%.3f" % identifiedIntellegentillyPrecent) + ',' + str(
                "%.3f" % identifiedSemiIntellegentillyPercent) + ',-,-,' + ',' + Parameters.toABC() + '\n'
        else:
            mwes, singleMWE, continousMWEs, interleavingMwes, embeddedMwes, identifiedMwes, identifiedSingleMWE, identifiedContinousMWEs = 0, 0, 0, 0, 0, 0, 0, 0,
            if len(testSents) > 0:
                mwes, singleMWE, continousMWEs, interleavingMwes, embeddedMwes = Report.getTestStatistics(testSents)
                identifiedMwes, identifiedSingleMWE, identifiedContinousMWEs = Report.getIdentifiedTestStatistics(
                    testSents)

            report = Parameters.languageName + ',' + str("%.3f" % fScore) + ',' + str("%.3f" % recall) + ',' + str(
                "%.3f" % precision) + ','

            report += str(corpus.sentNum) + ',' + str(corpus.mweNum) + ',' + str(
                corpus.mweNum - corpus.continousExp) + ',' + str(corpus.intereavingNum) + ',' + str(
                corpus.singleWordExp) + ',' + str(corpus.emeddedNum) + ','
            report += str(mwes) + ',' + str(identifiedMwes) + ',' + str(singleMWE) + ',' + str(
                identifiedSingleMWE) + ','
            report += str(mwes - continousMWEs) + ',' + str(
                identifiedMwes - identifiedContinousMWEs) + ',' + Parameters.toBinary() + '\n'
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
                if mwe.isEmbedded:
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


    @staticmethod
    def createEvaluationFiles(sents):

        if not Parameters.useCrossValidation:
            if not Parameters.realExper:
                goldCorpus = ''
                for sent in sents:
                    goldCorpus += sent.getCorpusText() + '\n'
                path =   os.path.join(Parameters.langFolder,Parameters.languageName  + '.gold')
                wFile = open(path, 'w')
                wFile.write(goldCorpus)

            predCorpus = ''
            for sent in sents:
                predCorpus += sent.getCorpusText(gold=False) + '\n'
            if Parameters.realExper:
                path = os.path.join(Parameters.langFolder, 'test.system.parsemetsv')
            else:
                path = os.path.join( Parameters.langFolder, Parameters.languageName + '.pred')
            wFile = open(path, 'w')
            wFile.write(predCorpus)