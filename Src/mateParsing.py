import os

import marmot


def ConlluToConll2009(conllu2016Path):
    with open(conllu2016Path) as corpusFile:
        lines = corpusFile.readlines()
        Conll2009Text = ''

        for line in lines:
            if len(line) > 0 and line.endswith('\n'):
                line = line[:-1]
            if line.startswith('#'):
                continue
            if line == '':
                Conll2009Text += line + '\n'
                continue
            lineParts = line.split('\t')
            if '-' in lineParts[0]:
                continue
            if len(lineParts) != 10 or '-' in lineParts[0]:
                print 'Error: not-well formatted line: file: ', str(os.path.basename(conllu2016Path)), ', line:', line
                continue

            Conll2009Text += lineParts[0] + '\t' + lineParts[1] + '\t' + lineParts[2] + '\t' + lineParts[2] + '\t' + \
                             lineParts[3] + '\t' + lineParts[3] + '\t' + lineParts[5] \
                             + '\t' + lineParts[5] + '\t' + lineParts[6] + '\t' + lineParts[6] + '\t' + lineParts[
                                 7] + '\t' + lineParts[7] + '\t_\t' + lineParts[8] + '\t' + lineParts[8] + '\t_'

            idx = 0
            while idx < 14:
                Conll2009Text += '\t_'
                idx += 1
            Conll2009Text += '\n'
        mateFile = open(conllu2016Path + '.conllu2009', 'w+')
        mateFile.write(Conll2009Text)


def conllu2009Toconllu(conllu2009Path, Conll2016Path):
    with open(conllu2009Path) as Conll2009File:
        lines9 = Conll2009File.readlines()

        with open(Conll2016Path) as Conll2016File:
            lines16 = Conll2016File.readlines()

            Conll2016Text = ''
            idx = 0
            for line in lines16:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('#'):
                    Conll2016Text += line + '\n'
                    continue
                if line == '':
                    idx += 1
                    Conll2016Text += line + '\n'
                    continue

                lineParts16 = line.split('\t')
                lineParts09 = lines9[idx].split('\t')

                if '-' in lineParts16[0]:
                    continue

                idx += 1
                lineParts16[6] = lineParts09[9]
                lineParts16[7] = lineParts09[11]
                line = ''
                for linePart in lineParts16:
                    line += linePart + '\t'
                line = line[:-1] + '\n'
                Conll2016Text += line

            mateFile = open(Conll2016Path + '.autoDep', 'w+')
            mateFile.write(Conll2016Text)


def jackknife(foldNum, langName):
    corpusPath = '/Users/halsaied/Documents/IdenSys/sharedTask/'+ langName+ '/train.conllu.autoPOS.conllu2009'
    with open(corpusPath) as corpusFile:
        lines = corpusFile.readlines()
        foldSize = len(lines) / foldNum

        ResultPath = '/Users/halsaied/Documents/IdenSys/MateTools/'+langName + '/Jackkniffing/'
        for i in xrange(0, foldNum):

            trainPath = os.path.join(ResultPath, str(i) + '.train.jck.txt')
            testPath = os.path.join(ResultPath, str(i) + '.test.jck.txt')

            startCuttingIdx = i * foldSize
            startCuttingiIdx = marmot.approximateCuttingIdx(startCuttingIdx, lines)
            endCuttingIdx = (i + 1) * foldSize
            endCuttingIdx = marmot.approximateCuttingIdx(endCuttingIdx, lines)

            testLines = lines[startCuttingiIdx: endCuttingIdx]
            if startCuttingIdx == 0:
                trainLines = lines[endCuttingIdx:]
            elif endCuttingIdx == len(lines) - 1:
                trainLines = lines[: startCuttingIdx]
            else:
                trainLines = lines[:startCuttingiIdx] + lines[endCuttingIdx:]

            createMateFile(trainLines, trainPath)
            createMateFile(testLines, testPath)

def createMateFile(lines, path):
    trainCorpus = ''
    for line in lines:
        trainCorpus += line

    marmotTrainFile = open(path, 'w+')
    marmotTrainFile.write(trainCorpus)

def createMateBatchJCK(foldNum, langList):
    batch = '#!/bin/bash\n'
    outPutPath = '/Users/halsaied/Documents/IdenSys/MateTools/srl/lib/'
    jackPath = '/Users/halsaied/Documents/IdenSys/MateTools/HU/Jackkniffing/'
    for lang in langList.split(','):
        for f in xrange(0, foldNum):
            trainFile = os.path.join(jackPath, str(f) + '.train.jck.txt')
            modelFile = os.path.join(jackPath, str(f) + '.model.jck.txt')
            batch += 'java -cp anna-3.3.jar is2.parser.Parser -train ' + trainFile + ' -model ' + modelFile + '\n'
            testFile = os.path.join(jackPath, str(f) + '.test.jck.txt')
            outputFile = os.path.join(jackPath, str(f) + '.output.jck.txt')
            batch += 'java -cp anna-3.3.jar is2.parser.Parser -model ' + modelFile + ' -test '+ testFile +' -out '  + outputFile + '\n'

    batchFile = open(outPutPath + 'dep.jck.batch.sh', 'w+')
    batchFile.write(batch)


def mergeConlluFiles(outfilesPath,outputFileName):
        lines = ''
        for subdir, dirs, files in os.walk(outfilesPath):
            for file in files:
                with open(os.path.join(outfilesPath, file)) as conlluFile:
                    jckOutLines = conlluFile.readlines()
                    jckOutLines = marmot.removeFinalEmptyLines(jckOutLines)
                    for line in jckOutLines:
                        lines += line
        outFile = open(os.path.join(outfilesPath, outputFileName), 'w')
        outFile.write(lines)

#ConlluToConll2009('/Users/halsaied/Documents/IdenSys/sharedtask/HU/train.conllu.autoPOS')
#jackknife(10, 'HU')
#createMateBatchJCK(10, 'HU')
#conllu2009Toconllu('/Users/halsaied/Documents/IdenSys/sharedtask/HU/train.conllu.autoPOS.conllu2009', '/Users/halsaied/Documents/IdenSys/sharedtask/HU/train.conllu.autoPOS')
#ConlluToConll2009('/Users/halsaied/Documents/IdenSys/sharedtask/HU/test.conllu.autoPOS')

#mergeConlluFiles('/Users/halsaied/Documents/IdenSys/mateTools/SPMRL/','spmrl.conllu')
ConlluToConll2009('/Users/halsaied/Documents/IdenSys/sharedtask/FR/train.conllu')
ConlluToConll2009('/Users/halsaied/Documents/IdenSys/sharedtask/FR/test.conllu')