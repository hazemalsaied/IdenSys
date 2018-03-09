import datetime
import logging

from sklearn.feature_extraction import DictVectorizer
from sklearn.multiclass import OutputCodeClassifier
from sklearn.svm import LinearSVC

from features import Extractor
from transitions import Shift
from transitions import Transition, Reduce, BlackMerge, MergeAsMWT


def train(corpus):
    time = datetime.datetime.now()
    logging.warn('Static Oracle analysis and feature extraction started!')
    Y, X_dic = parseCorpus(corpus.trainingSents)
    vec = DictVectorizer()
    logging.warn('SVM Multi-classes learning started!')
    X = vec.fit_transform(X_dic)
    clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)
    clf.fit(X, Y)
    logging.warn('Traingin has taken: {0} sec!'.format(int((datetime.datetime.now() - time).seconds / 60.)))
    return clf, vec


def parseCorpus(sents):
    labels, features = [], []
    for sent in sents:
        # Parse the sentence
        trainingInfo = parseSentence(sent)
        if trainingInfo:
            labels.extend(trainingInfo[0])
            features.extend(trainingInfo[1])

    return labels, features


def parseSentence(sent):
    if sent.id == 7208:
        pass
    sent.initialTransition = Transition(isInitial=True, sent=sent)
    transition = sent.initialTransition
    while not transition.isTerminal():
        transition = getNextTransition(transition, sent)
    labels, features = Extractor.extract(sent)
    return labels, features


def getNextTransition(parent, sent):
    newTransition = MergeAsMWT.check(parent)
    if newTransition:
        return newTransition

    newTransition = BlackMerge.check(parent)
    if newTransition:
        return newTransition

    # Check for VMWE complete
    newTransition = Reduce.check(parent)
    if newTransition:
        return newTransition

    # Apply the default transition: SHIFT
    shift = Shift(sent=sent)
    shift.apply(parent, sent)
    return shift
