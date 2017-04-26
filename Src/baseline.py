import os
from corpus import Corpus, VMWE
from evaluation import Evaluation
from param import FeatParams, Paths, XPParams
import logging
from reports import Report


class BaseLine:
    @staticmethod
    def identify():
        if not XPParams.baseline:
            raise Exception('Hazem : Contradictory parameters!')

        analysisResults = ''
        Report.createRootResultFolder()

        constantConfigFolder = Paths.configsFolder
        for subdir, dirs, files in os.walk(constantConfigFolder):
            for dir in dirs:
                Paths.languageName = dir
                for subdir1, dirs1, configFiles in os.walk(os.path.join(constantConfigFolder, dir)):
                    corpus = Corpus(os.path.join(Paths.corporaPath, Paths.languageName))
                    for configFile in configFiles:
                        if not configFile.endswith('.json'):
                            continue
                        configFilePath = os.path.join(constantConfigFolder, Paths.languageName, configFile)

                        FeatParams(configFilePath, corpus=corpus)
                        Corpus.mweDictionary, Corpus.mweTokenDic = Corpus.getMWEDic(corpus.trainingSents)
                        report = ''
                        for sent in corpus.testingSents:
                            if len(sent.vMWEs) > 1:
                                pass
                            mweIdx = 1
                            lemmatizedText = ' '
                            for token in sent.tokens:
                                lemmatizedText += token.getLemma() + ' '
                            for entry in Corpus.mweDictionary.keys():
                                entryComps = entry.split(' ')
                                isInSent = True
                                expTokens = []
                                for entryComp in entryComps:
                                    if ' ' + entryComp + ' ' in lemmatizedText:
                                        for token in sent.tokens:
                                            if token.getLemma() == entryComp:
                                                expTokens.append(token)
                                                break
                                    else:
                                        isInSent = False
                                        break
                                if isInSent:
                                    expTokens = sorted(expTokens, key=lambda Token: Token.position)
                                    vmwe = VMWE(mweIdx)
                                    vmwe.tokens = expTokens
                                    sent.identifiedVMWEs.append(vmwe)
                                    mweIdx += 1

                            if len(sent.identifiedVMWEs) > 0:
                                report += str(sent)

                        with open(os.path.join(Paths.iterationPath, 'examples.md'),
                                  'w+') as reportFile:
                            reportFile.write(report)

                        Evaluation.evaluate(corpus, resultFilePath=os.path.join(Paths.rootResultFolder, '_RESULTS.csv'))
                        analysisResults += BaseLine.analyze(corpus) +  '\n'
        with open(os.path.join(Paths.rootResultFolder, '_statistics.md'),
                  'w+') as reportFile:
            reportFile.write(analysisResults)



    @staticmethod
    def analyze(corpus):
        result, processedVmwes, newStr, allStr, previouslySeenExp, previouslySeenStr, allExp = '', [], '', '', 0, '', 0
        for sent in corpus.testingSents:
            for vmwe in sent.vMWEs:
                if (vmwe.getLemmaString() in Corpus.mweDictionary or vmwe.getString() in Corpus.mweDictionary) \
                        and vmwe.getLemmaString() not in processedVmwes:
                    previouslySeenExp += 1
                    allExp += 1
                    previouslySeenStr += vmwe.getLemmaString() + '\n\n'
                    allStr += vmwe.getLemmaString() + '\n\n'
                    processedVmwes.append(vmwe.getLemmaString())
                elif vmwe.getLemmaString() not in Corpus.mweDictionary and vmwe.getLemmaString() not in processedVmwes:
                    allExp += 1
                    allStr += vmwe.getLemmaString() + '\n\n'
                    newStr += vmwe.getLemmaString() + '\n\n'
                    processedVmwes.append(vmwe.getLemmaString())
        perc = float(previouslySeenExp) / allExp
        result += Paths.languageName + ' : ' + str(previouslySeenExp) + ' ' + str(allExp) + ' pre: ' + str(
            "%.2f" % perc) + '\n\n'
        with open(os.path.join(Paths.iterationPath, 'seenMWEs.md'),
                  'w+') as reportFile:
            reportFile.write(previouslySeenStr)
        with open(os.path.join(Paths.iterationPath, 'allMWEs.md'),
                  'w+') as reportFile:
            reportFile.write(allStr)
        with open(os.path.join(Paths.iterationPath, 'newMWEs.md'),
                  'w+') as reportFile:
            reportFile.write(newStr)
        return  result

BaseLine.identify()
