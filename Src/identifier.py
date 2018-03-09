import logging
import os
import sys

from oracles import train
from corpus import Corpus
from evaluation import evaluate
from param import FeatParams, XPParams, Paths
from parsers import parse

def identify():
    # iterate over Sharedtask languages:
    for configFile in os.listdir(Paths.configsFolder):
        if not configFile.endswith('.json'):
            continue
        # encapsulate the corpus in a hierarchy of objects: Corpus => Sentence => MWE or Token
        logging.warn('Corpus encapsulation has started!')
        corpus = Corpus(configFile[:2])
        # Reading the parameters of the experiment
        logging.warn('Experiment paramaters are read!')
        FeatParams(os.path.join(Paths.configsFolder, configFile))
        # Crosss validation evaluation:
        if XPParams.useCrossValidation:
            logging.warn('Cross validation Evaluation:')
            scores = [0] * 12

            testRange, trainRange = corpus.getRangs()
            for x in range(len(testRange)):
                logging.warn('Iteration no.' + str(x + 1))
                XPParams.currentIteration = x
                evalScores = identifyCorpus(corpus)
                for i in range(len(evalScores)):
                    scores[i] += evalScores[i]
            for i in range(len(scores)):
                scores[i] = scores[i] / float(len(testRange))
            logging.warn(' F-Score: ' + str(scores[0]))
        else:
            # evaluation over Train-dev or Train-Test:
            identifyCorpus(corpus)

def identifyCorpus(corpus):
    corpus.update()
    clf = train(corpus)
    parse(corpus, clf)
    scores = evaluate(corpus)
    return scores


reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(level=logging.WARNING)


# Run the identifier
if __name__ == '__main__':
    XPParams.realExper = True
    identify()





