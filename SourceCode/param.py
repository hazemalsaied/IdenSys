import json


class Parameters:
    xpName = ''
    configPath = ''
    corpusPath = ''
    resultPath = ''
    testCorpusPath = ''
    dumpingPath = ''

    useFirstBufferElement = True
    useSecondBufferElement = True
    useCrossValidation = False
    binaryMerge = True
    useToken = True
    useLemma = True
    usePOS = True
    useBiGram = True
    useTriGram = True
    useDistance = True
    useSyntax = True

    usePreviousTransition = True
    useAntepenultimateTransition = True
    useTransitionHistory = True

    printReport = True
    serialize = False

    def __init__(self, filePath):
        with open(filePath, 'r') as configFile:
            config = json.load(configFile)

            if len(filePath.split('/')) > 0:
                Parameters.xpName = filePath.split('/')[-1].split('.')[0]
            Parameters.configPath = filePath
            Parameters.corpusPath = config["path"]["corpusPath"]
            Parameters.resultPath = config["path"]["resultPath"]
            Parameters.testCorpusPath = config["path"]["testCorpusPath"]
            Parameters.dumpingPath = config["path"]["dumpingPath"]

            Parameters.useFirstBufferElement = config["useFirstBufferElement"]
            Parameters.useSecondBufferElement = config["useSecondBufferElement"]

            Parameters.binaryMerge = config["UseLinguistInfo"]["binaryMerge"]
            Parameters.usePOS = config["UseLinguistInfo"]["usePOS"]
            Parameters.useLemma = config["UseLinguistInfo"]["useLemma"]
            Parameters.useBiGram = config["UseLinguistInfo"]["useBiGram"]
            Parameters.useTriGram = config["UseLinguistInfo"]["useTriGram"]
            Parameters.useDistance = config["UseLinguistInfo"]["useDistance"]
            Parameters.useSyntax = config["UseLinguistInfo"]["useSytax"]

            Parameters.usePreviousTransition = config["useTransitionHistory"]["usePreviousTransition"]
            Parameters.useAntepenultimateTransition = config["useTransitionHistory"]["useAntepenultimateTransition"]
            Parameters.useTransitionHistory = config["useTransitionHistory"]["useTransitionHistory"]

            Parameters.printReport = config["printReport"]
            Parameters.serialize = config["serialize"]
            Parameters.useCrossValidation = config["CrossValidationEvaluation"]

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
