import datetime

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OutputCodeClassifier, OneVsRestClassifier
from sklearn.svm import LinearSVC
from corpus import Corpus
from param import Parameters
from reports import Report
from transition import StaticOracle
from embeddingTransitions import EmbeddingOracle


class Classification:
    @staticmethod
    def train(sents, crossValidationIdx=''):
        if Parameters.useCrossValidation:
            Corpus.initializeSents(sents)
        if Parameters.includeEmbedding:
            staticParsingData = EmbeddingOracle.parseCorpus(sents, EmbeddingOracle)
        else:
            staticParsingData = StaticOracle.parseCorpus(sents, StaticOracle)
        Report.createStaticParsingReports(sents, crossValidationIdx)

        vec = DictVectorizer()
        X = vec.fit_transform(staticParsingData[1])
        Y = np.asarray(staticParsingData[0])
        F = vec.get_feature_names()
        report = '## Number of features used: ' + str(len(F)) + '\n\n'

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

        idx = score.index(max(score))
        report += '### The Selected Classifier is: ' + str(idx + 1) + '\n'
        clf = clfs[idx]

        if Parameters.printReport:
            Report.editReadme('a', report)

        return [clf, vec]

    @staticmethod
    def trainClassifier(X, Y, clf):
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf.fit(X_train, Y_train)
        return clf

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
