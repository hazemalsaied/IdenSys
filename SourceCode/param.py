import json


class Parameters:

    xpName = ''
    configPath = ''
    languageName = ''
    corpusPath = "/Users/hazemalsaied/Parseme/IdenSys/Corpora/sharedtask/"
    resultPath = "/Users/hazemalsaied/Parseme/IdenSys/Results/"
    testCorpusPath = "/Users/hazemalsaied/Parseme/IdenSys/Corpora/testing/"
    dumpingPath = "/Users/hazemalsaied/Parseme/IdenSys/Serialization/"

    printReport = True
    serialize = True
    useCrossValidation = False

    # Featue extraction parameters
    useFirstBufferElement = True
    useSecondBufferElement = True
    binaryMerge = True
    useToken = True
    useLemma = True
    usePOS = True
    useBiGram = True
    useTriGram = True
    useDistance = True
    useSyntax = True

    generateS0B2Bigram = True

    transitionHistoryLength1 = True
    transitionHistoryLength2 = True
    transitionHistoryLength3 = True
    useS0B0Distance = True
    useS0S1Distance = True
    useStackLength = True

    def __init__(self, filePath):

        with open(filePath, 'r') as configFile:
            config = json.load(configFile)

            if len(filePath.split('/')) > 0:
                Parameters.xpName = filePath.split('/')[-1].split('.')[0]
            Parameters.configPath = filePath

            Parameters.useFirstBufferElement = config["useFirstBufferElement"]
            Parameters.useSecondBufferElement = config["useSecondBufferElement"]

            Parameters.usePOS = config["UseLinguistInfo"]["usePOS"]
            Parameters.useLemma = config["UseLinguistInfo"]["useLemma"]
            Parameters.useBiGram = config["UseLinguistInfo"]["useBiGram"]
            Parameters.useTriGram = config["UseLinguistInfo"]["useTriGram"]

            Parameters.useS0B0Distance = config["S0B0Distance"]
            Parameters.useS0S1Distance = config["S0S1Distance"]
            Parameters.useStackLength =  config["useStackLength"]
            Parameters.useSyntax = config["UseLinguistInfo"]["useSytax"]
            Parameters.generateS0B2Bigram = config["generateS0B2Bigram"]

            Parameters.transitionHistoryLength1 = config["useTransitionHistory"]["transitionHistoryLength1"]
            Parameters.transitionHistoryLength2 = config["useTransitionHistory"]["transitionHistoryLength2"]
            Parameters.transitionHistoryLength3 = config["useTransitionHistory"]["transitionHistoryLength3"]


    @staticmethod
    def toBinary():

        if Parameters.configPath == '':
            return ''
        result = ''
        with open(Parameters.configPath, 'r') as configFile:
            config = json.load(configFile)
            for key in config.keys():
                if isinstance(config[key], bool):
                    if config[key]:
                        result += '1'
                    else:
                        result += '0'
                elif isinstance(config[key], dict):
                    for subkey in config[key].keys():
                        if isinstance(config[key][subkey], bool):
                            if config[key][subkey]:
                                result += '1'
                            else:
                                result += '0'

        return result

    @staticmethod
    def toString():
        if Parameters.configPath == '':
            return ''
        result = ''
        with open(Parameters.configPath, 'r') as configFile:
            config = json.load(configFile)
            for key in config.keys():
                if isinstance(config[key], bool):
                    result += str(key)
                    if config[key]:
                        result += ' = True\n'
                    else:
                        result += ' = False\n'

                elif isinstance(config[key], dict):
                    for subkey in config[key].keys():
                        if isinstance(config[key][subkey], bool):
                            result += str(subkey)
                            if config[key][subkey]:
                                result += ' = True\n'
                            else:
                                result += ' = False\n'
        return result
