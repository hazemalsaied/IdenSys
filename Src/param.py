import json
import os


# Experiment settings
class XPParams:
    debug = False
    realExper = False
    useCrossValidation = False
    currentIteration = 0
    baseline = False

    useAutoGeneratedPOS = True
    useAutoGeneratedDEP = True
    useUniversalPOSTag = True


# Corpus and configuration paths
class Paths:
    projectPath = os.path.dirname(__file__)[:-len(os.path.basename(os.path.dirname(__file__)))]
    configsFolder = os.path.join(projectPath, 'Experiments/xp')
    corporaPath = os.path.join(projectPath, "sharedtask/")


# Feature extraction configurations
class FeatParams:
    usePreciseDictionary = False

    # Featue extraction parameters
    useFirstBufferElement = True
    useSecondBufferElement = True
    useToken = True
    useLemma = True
    usePOS = True
    useBiGram = True
    useTriGram = True
    useDistance = True
    useSyntax = True

    generateS0B2Bigram = True
    useDictionary = True

    historyLength1 = True
    historyLength2 = True
    historyLength3 = True
    useS0B0Distance = True
    useS0S1Distance = True
    useStackLength = True

    enhanceMerge = False
    enableSingleMWE = False
    useLexic = False
    smartMWTDetection = True
    generateS1B1 = False


    def __init__(self, filePath):

        with open(filePath, 'r') as configFile:
            config = json.load(configFile)

            if len(filePath.split('/')) > 0:
                Paths.xpName = filePath.split('/')[-1].split('.')[0]
                # Paths.configsFolder = filePath

            if "generateS1B1" in config.keys():
                FeatParams.generateS1B1 = config["generateS1B1"]

            if "enhanceMerge" in config.keys():
                FeatParams.enhanceMerge = config["enhanceMerge"]

            if "usePreciseDictionary" in config.keys():
                FeatParams.usePreciseDictionary = config["usePreciseDictionary"]

            if "useLexic" in config.keys():
                FeatParams.useLexic = config["useLexic"]

            if "enableSingleMWE" in config.keys():
                FeatParams.enableSingleMWE = config["enableSingleMWE"]

            FeatParams.useFirstBufferElement = config["useFirstBufferElement"]
            FeatParams.useSecondBufferElement = config["useSecondBufferElement"]

            FeatParams.usePOS = config["UseLinguistInfo"]["usePOS"]
            FeatParams.useLemma = config["UseLinguistInfo"]["useLemma"]
            FeatParams.useBiGram = config["UseLinguistInfo"]["useBiGram"]
            FeatParams.useTriGram = config["UseLinguistInfo"]["useTriGram"]

            FeatParams.useS0B0Distance = config["S0B0Distance"]
            FeatParams.useS0S1Distance = config["S0S1Distance"]
            FeatParams.useStackLength = config["useStackLength"]
            FeatParams.useSyntax = config["UseLinguistInfo"]["useSytax"]
            FeatParams.generateS0B2Bigram = config["generateS0B2Bigram"]

            FeatParams.useDictionary = config["useDictionary"]

            FeatParams.historyLength1 = config["useTransitionHistory"]["transitionHistoryLength1"]
            FeatParams.historyLength2 = config["useTransitionHistory"]["transitionHistoryLength2"]
            FeatParams.historyLength3 = config["useTransitionHistory"]["transitionHistoryLength3"]
