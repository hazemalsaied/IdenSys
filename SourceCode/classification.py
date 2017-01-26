import datetime

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OutputCodeClassifier, OneVsRestClassifier
from sklearn.svm import LinearSVC

from param import Parameters
from parser import Parser
from reports import Report


class Classification:
    @staticmethod
    def classify(sents, crossValidationIdx):

        staticParsingData = Classification.getStaticParseData(sents)
        if Parameters.printReport:
            Report.createStaticParsingReports(sents, crossValidationIdx)

        vec = DictVectorizer()
        X = vec.fit_transform(staticParsingData[1])
        Y = np.asarray(staticParsingData[0])
        F = vec.get_feature_names()
        report = '## Number of features used: ' + str(len(F)) + '\n\n'
        #time = datetime.datetime.now()
        # clfs = []
        # clfs.append(Classification.trainClassifier(X, Y, Perceptron()))
        # clfs.append(Classification.trainClassifier(X, Y, OneVsRestClassifier(LinearSVC(random_state=0))))
        # clfs.append(Classification.trainClassifier(X, Y, OutputCodeClassifier(LinearSVC(random_state=0), code_size=2,
        # clfs.append(Classification.trainClassifier(X, Y, OneVsOneClassifier(LinearSVC(random_state=0))))
        score = []
        clfs = []
        oneVsRest = Classification.evaluateOneVsRest(X, Y)
        report += '### 1- SVM One Vs Rest: \n' + 'Score: ' + str(oneVsRest[0]) + ', Number of merge operation: ' + str(
            oneVsRest[1]) + '\n'
        score.append(oneVsRest[1])
        clfs.append(oneVsRest[2])
        outputCode = Classification.evaluateOutputCode(X, Y)
        report += '### 2- SVM Output Code: \n' + 'Score: ' + str(outputCode[0]) + ', Number of merge operation: ' + str(
            outputCode[1]) + '\n'
        score.append(outputCode[1])
        clfs.append(outputCode[2])
        oneVsOne = Classification.evaluateOneVsOne(X, Y)
        report += '### 3- SVM One Vs One : \n' + 'Score: ' + str(oneVsOne[0]) + ', Number of merge operation: ' + str(
            oneVsOne[1]) + '\n'
        score.append(oneVsOne[1])
        clfs.append(oneVsOne[2])
        perceptron = Classification.evaluatePerceptron(X, Y)
        report += '### 4- Perceptron : \n' + 'Score: ' + str(
            perceptron[0]) + ', Number of merge operation: ' + str(
            perceptron[1]) + '\n'
        score.append(perceptron[1])
        clfs.append(perceptron[2])
        idx = score.index(max(score))
        report += '### The Selected Classifier is: ' + str(idx + 1) + '\n'
        clf = clfs[idx]


        if Parameters.printReport:
            Report.editReadme('a', report)

        return [clf, vec]

    @staticmethod
    def getStaticParseData(sents):
        trainingData = []
        trainDataLabel = []
        for sent in sents:
            # Parse the sentence
            trainingInfo = Parser.staticParse(sent)
            if trainingInfo is not None:
                trainDataLabel.extend(trainingInfo[0])
                trainingData.extend(trainingInfo[1])
        return [trainDataLabel, trainingData]

    @staticmethod
    def trainClassifier(X, Y, clf):
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf.fit(X_train, Y_train)
        return clf

    @staticmethod
    def evaluatePerceptron(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = Perceptron()
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OneVsRest: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def evaluateOneVsRest(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = OneVsRestClassifier(LinearSVC(random_state=0))
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OneVsRest: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def evaluateOutputCode(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OneVsOne: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def evaluateOneVsOne(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = OneVsOneClassifier(LinearSVC(random_state=0))
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OutputCode: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]