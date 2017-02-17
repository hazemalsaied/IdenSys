import json
import os


class Parameters:
    xpName = ''
    configPath = ''
    languageName = ''
    readMe = "/Users/hazemalsaied/Parseme/IdenSys/Results/readMe.md"
    results = "/Users/hazemalsaied/Parseme/IdenSys/Results/results.csv"
    corpusPath = "/Users/hazemalsaied/Parseme/IdenSys/sharedtask/"
    xpPath = "/Users/hazemalsaied/Parseme/IdenSys/Results/"
    langFolder = "/Users/hazemalsaied/Parseme/IdenSys/Results/"
    resultPath = "/Users/hazemalsaied/Parseme/IdenSys/Results/"

    useCrossValidation = False

    usePreciseDictionary = False

    printReport = False
    serialize = True

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
    useDictionary = True

    transitionHistoryLength1 = True
    transitionHistoryLength2 = True
    transitionHistoryLength3 = True
    useS0B0Distance = True
    useS0S1Distance = True
    useStackLength = True

    enhanceMerge = False
    enableSingleMWE = False
    useLexic = False

    generateS1B1 = False

    def __init__(self, filePath):

        with open(filePath, 'r') as configFile:
            config = json.load(configFile)

            if len(filePath.split('/')) > 0:
                Parameters.xpName = filePath.split('/')[-1].split('.')[0]
            Parameters.configPath = filePath

            if "generateS1B1" in config.keys():
                Parameters.generateS1B1 = config["generateS1B1"]

            if "enhanceMerge" in config.keys():
                Parameters.enhanceMerge = config["enhanceMerge"]

            if "usePreciseDictionary" in config.keys():
                Parameters.usePreciseDictionary = config["usePreciseDictionary"]

            if "useLexic" in config.keys():
                Parameters.useLexic = config["useLexic"]

            if "enableSingleMWE" in config.keys():
                Parameters.enableSingleMWE = config["enableSingleMWE"]

            Parameters.useFirstBufferElement = config["useFirstBufferElement"]
            Parameters.useSecondBufferElement = config["useSecondBufferElement"]

            Parameters.usePOS = config["UseLinguistInfo"]["usePOS"]
            Parameters.useLemma = config["UseLinguistInfo"]["useLemma"]
            Parameters.useBiGram = config["UseLinguistInfo"]["useBiGram"]
            Parameters.useTriGram = config["UseLinguistInfo"]["useTriGram"]

            Parameters.useS0B0Distance = config["S0B0Distance"]
            Parameters.useS0S1Distance = config["S0S1Distance"]
            Parameters.useStackLength = config["useStackLength"]
            Parameters.useSyntax = config["UseLinguistInfo"]["useSytax"]
            Parameters.generateS0B2Bigram = config["generateS0B2Bigram"]

            Parameters.useDictionary = config["useDictionary"]

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
    def toABC():

        if Parameters.configPath == '':
            return ''
        idxs = 'ABCDEFGHIJKLMNOPQRST'
        result = ''
        with open(Parameters.configPath, 'r') as configFile:
            config = json.load(configFile)
            idx = 0
            idxxx = 0
            # print 'Nmber of Keys: ', len(config.keys())
            for key in config.keys():
                if isinstance(config[key], bool):
                    # print  idxs[idxxx: idxxx  +1], key#, config[key]
                    if config[key]:
                        result += str(idxs[idx:idx + 1]) + ' ' + key + ' '
                    idx += 1
                    idxxx += 1
                elif isinstance(config[key], dict):
                    for subkey in config[key].keys():
                        if isinstance(config[key][subkey], bool):
                            # print idxs[idxxx: idxxx  +1], subkey #, config[key][subkey]
                            if config[key][subkey]:
                                result += str(idxs[idx:idx + 1]) + ' ' + subkey + ' '
                        idx += 1
                        idxxx += 1

        # print result
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
                        result += ' = True\n\n'
                    else:
                        result += ' = False\n\n'

                elif isinstance(config[key], dict):
                    for subkey in config[key].keys():
                        if isinstance(config[key][subkey], bool):
                            result += str(subkey)
                            if config[key][subkey]:
                                result += ' = True\n\n'
                            else:
                                result += ' = False\n\n'
        return result


for subdir, dirs, files in os.walk('Done'):
    for dir in dirs:
        for subdir1, dirs1, configFiles in os.walk(os.path.join('Done', dir)):
            for configFile in configFiles:
                if not configFile.endswith('.json'):
                    continue
                Parameters.configPath = os.path.join(os.path.join('Done', dir), configFile)
                print Parameters.toABC()
