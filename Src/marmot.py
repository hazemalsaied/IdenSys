import os


def getTrainModelCorpus(filePath):
    with open(filePath) as corpusFile:
        lines = corpusFile.readlines()
        createMarmotTrainFile(lines, filePath + '.marmot.train')


def getTestModelCorpus(filePath):
    with open(filePath) as corpusFile:
        lines = corpusFile.readlines()
        createMarmotTestFile(lines, '/Users/halsaied/Downloads/MarMot/test.marmot.hu')


def evaluateMarMot(testOutEvalFile, sharedTaskTestConlluFile):
    with open(testOutEvalFile) as testOutEvalFile:
        testOutEvallines = testOutEvalFile.readlines()
        with open(sharedTaskTestConlluFile) as sharedTaskTestConlluFile:
            lines = sharedTaskTestConlluFile.readlines()
            lineIdx = 0

            finalResult = ''
            # iterating over test conllu file
            for line in lines:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('#'):
                    continue
                if line == '':
                    finalResult += '\n'
                    lineIdx += 1
                    continue
                lineParts = line.split('\t')
                if '-' in lineParts[0]:
                    continue

                newLine = testOutEvallines[lineIdx][:-1]
                newLineParts = newLine.split('\t')

                idx = 0
                result = ''
                for newlinePart in newLineParts:
                    if idx == 4:
                        result += str(lineParts[3])
                    else:
                        result += str(newLineParts[idx])
                    result += '\t'
                    idx += 1
                result = result[:-1] + '\n'
                finalResult += result
                lineIdx += 1

            marmotTestFile = open('/Users/halsaied/Downloads/MarMot/test.gold.eval.pl', 'w+')
            marmotTestFile.write(finalResult)


def integrateAutoPOS(conlluFilePath, marmotOutFilePath):
    with open(conlluFilePath) as testConlluFile:
        lines = testConlluFile.readlines()
        with open(marmotOutFilePath) as marmotOutFilePath:
            marmotTestOutLines = marmotOutFilePath.readlines()
            lineIdx = 0

            finalResult = ''
            # iterating over test conllu file
            for line in lines:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('#'):
                    finalResult += line + '\n'
                    continue
                if line == '':
                    finalResult += '\n'
                    lineIdx += 1
                    continue
                lineParts = line.split('\t')
                if '-' in lineParts[0]:
                    continue
                marmotTestOutLine = marmotTestOutLines[lineIdx][:-1]
                marmotTestOutLineParts = marmotTestOutLine.split('\t')

                idx = 0
                result = ''
                for linePart in lineParts:
                    if idx == 3:
                        result += str(marmotTestOutLineParts[5])
                    else:
                        result += str(lineParts[idx])
                    result += '\t'
                    idx += 1
                result = result[:-1] + '\n'
                finalResult += result
                lineIdx += 1

            marmotTestFile = open(conlluFilePath + '.autoPOS', 'w+')
            marmotTestFile.write(finalResult)


def jackknife(foldNum, langName):
    corpusPath = os.path.join('/Users/halsaied/Documents/IdenSys/sharedTask/', langName, 'train.conllu')
    with open(corpusPath) as corpusFile:
        lines = corpusFile.readlines()
        foldSize = len(lines) / foldNum

        ResultPath = os.path.join('/Users/halsaied/Documents/IdenSys/MarMot/Jackkniffing/', langName)
        for i in xrange(0, foldNum):

            trainPath = os.path.join(ResultPath, str(i) + '.train.jck.txt')
            testPath = os.path.join(ResultPath, str(i) + '.test.jck.txt')

            startCuttingIdx = i * foldSize
            startCuttingiIdx = approximateCuttingIdx(startCuttingIdx, lines)
            endCuttingIdx = (i + 1) * foldSize
            endCuttingIdx = approximateCuttingIdx(endCuttingIdx, lines)

            testLines = lines[startCuttingiIdx: endCuttingIdx]
            if startCuttingIdx == 0:
                trainLines = lines[endCuttingIdx:]
            elif endCuttingIdx == len(lines) - 1:
                trainLines = lines[: startCuttingIdx]
            else:
                trainLines = lines[:startCuttingiIdx] + lines[endCuttingIdx:]

            createMarmotTrainFile(trainLines, trainPath)
            createMarmotTestFile(testLines, testPath)


def createMarmotTrainFile(lines, trainPath):
    trainCorpus = ''
    for line in lines:
        if len(line) > 0 and line.endswith('\n'):
            line = line[:-1]
        if line.startswith('#'):
            continue
        if line == '':
            trainCorpus += line + '\n'
            continue
        lineParts = line.split('\t')
        if '-' in lineParts[0]:
            continue
        if len(lineParts) != 10 or '-' in lineParts[0]:
            print 'Error: not-well formatted line: file: ', trainPath, ', line:', line
            continue

        trainCorpus += lineParts[0] + '\t' + lineParts[1] + '\t' + lineParts[3] + '\n'

    marmotTrainFile = open(trainPath, 'w+')
    marmotTrainFile.write(trainCorpus)


def createMarmotTestFile(lines, testFilepath):
    trainCorpus = ''
    for line in lines:
        if len(line) > 0 and line.endswith('\n'):
            line = line[:-1]
        if line.startswith('#'):
            continue
        if line == '':
            trainCorpus += line + '\n'
            continue
        lineParts = line.split('\t')
        if '-' in lineParts[0]:
            continue
        if len(lineParts) != 10 or '-' in lineParts[0]:
            print 'Error: not-well formatted line: file: ', testFilepath, ', line:', line
            continue

        trainCorpus += lineParts[1] + '\n'

    marmotTestFile = open(testFilepath, 'w+')
    marmotTestFile.write(trainCorpus)


def approximateCuttingIdx(cuttingIdx, lines):
    '''
        This method is used to make the fold end and start with complete sentences
    :param cuttingIdx:
    :param lines:
    :return:
    '''
    if cuttingIdx <= 0:
        return 0
    if cuttingIdx >= len(lines) - 1:
        return len(lines) - 1

    while True:
        if lines[cuttingIdx][:-1].strip() == '':
            return cuttingIdx
        if cuttingIdx < len(lines) - 1:
            cuttingIdx += 1
        else:
            return len(lines) - 1


def creatBatchForMarmotJCK(foldNum, langList):
    batch = '#!/bin/bash\n'
    jckPath = '/Users/halsaied/Documents/IdenSys/MarMot/Jackkniffing/'
    for lang in langList.split(','):
        for f in xrange(0, foldNum):
            trainFile = os.path.join(jckPath, lang, str(f) + '.train.jck.txt')
            modelFile = os.path.join(jckPath, lang, str(f) + '.model.jck.txt')
            batch += 'java -Xmx5G -cp marmot.jar marmot.morph.cmd.Trainer -train-file form-index=1,tag-index=2,' + trainFile + ' -tag-morph false -model-file ' + modelFile + '\n'
            testFile = os.path.join(jckPath, lang, str(f) + '.test.jck.txt')
            outputFile = os.path.join(jckPath, lang, str(f) + '.output.jck.txt')
            batch += 'java -cp marmot.jar marmot.morph.cmd.Annotator --model-file ' + modelFile + ' --test-file form-index=0,' + testFile + ' --pred-file ' + outputFile + '\n'

    batchFile = open(jckPath + 'postag.jck.batch.sh', 'w+')
    batchFile.write(batch)


def mergeJckOutFiles(outfilesPath, foldNum, langs):
    for lang in langs.split(','):
        lines = ''
        for subdir, dirs, files in os.walk(os.path.join(outfilesPath, lang)):
            for fileIdx in xrange(0, foldNum):
                fileFounded = False
                for file in files:
                    if file == str(fileIdx) + '.output.jck.txt':
                        fileFounded = True
                        with open(os.path.join(outfilesPath, lang, file)) as jckOutFile:
                            jckOutLines = jckOutFile.readlines()
                            jckOutLines = removeFinalEmptyLines(jckOutLines)
                            for line in jckOutLines:
                                lines += line
                if not fileFounded:
                    print 'Output File is not existing: '
                fileIdx += 1
        outFile = open(os.path.join(outfilesPath, lang, 'out.jck.txt'), 'w')
        outFile.write(lines)


def removeFinalEmptyLines(linelist):
    emptyLinesNum = 0
    for line in reversed(linelist):
        if line == '\n':
            emptyLinesNum += 1
        else:
            break
    for i in xrange(0, emptyLinesNum):
        linelist = linelist[:-1]

    linelist.append('\n')
    return linelist


def verifyAlignment(path1, path2):
    with open(path1) as file1:
        file1Lines = file1.readlines()
        file1Lines = removeFinalEmptyLines(file1Lines)
        with open(path2) as file2:
            file2Lines = file2.readlines()
            file2Lines = removeFinalEmptyLines(file2Lines)

            if len(file1Lines) != len(file2Lines):
                print 'not the same length'
                return False
            idx = 0
            for line in file1Lines:
                if line == '\n' and line != file2Lines[idx]:
                    print idx
                    return False

                line1Parts = line.split('\t')
                line2Parts = file2Lines[idx].split('\t')
                if line1Parts[0].strip() != line2Parts[0].strip():
                    print idx
                    return False
                idx += 1
    return True


# creatBatchForMarmotJCK(10, 'FR,HU,CS,PL')
# mergeJckOutFiles('/Users/halsaied/Documents/IdenSys/MarMot/Jackkniffing/', 10, 'FR')

# integrateAutoPOS('/Users/halsaied/Documents/IdenSys/sharedtask/FR/test.conllu', '/Users/halsaied/Documents/IdenSys/MarMot/Output/test.out.fr')

# print verifyAlignment('/Users/halsaied/Documents/IdenSys/sharedtask/HU/train.conllu', '/Users/halsaied/Documents/IdenSys/sharedtask/HU/train.conllu.autoPOS')

mergeJckOutFiles('/Users/halsaied/Documents/IdenSys/MateTools/HU/Jackkniffing/', 10, '')
