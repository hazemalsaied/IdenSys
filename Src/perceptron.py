import numpy as np

from param import XPParams

BIAS = 1


class MultiClassPerceptron():


    def __init__(self, classes, featureSet=set(), featureData=[]):
        self.classes = classes
        self.trainSet = featureData
        self.weights = {}
        for c in self.classes:
            self.weights[c] = {k: 0 for k in featureSet}
            # self.modelDic[c]['BIAS'] = 0
        self.avgWeights = {}
        for c in self.classes:
            self.avgWeights[c] = {k: 0 for k in featureSet}

    def train(self):
        trainIdx = 0
        for _ in xrange(XPParams.perceptronIterations):
            np.random.shuffle(self.trainSet)
            for category, featureDict in self.trainSet:
                trainIdx +=1
                # feature_dict['BIAS'] = 1
                argMax, predictedClass = 0, self.classes[0]
                for c in self.classes:
                    current_activation = self.getCurrentActivation(featureDict,c)
                    if current_activation >= argMax:
                        argMax, predictedClass = current_activation, c
                if not (category == predictedClass):
                    self.updateWeights(featureDict, category, trainIdx=trainIdx)
                    self.updateWeights(featureDict, predictedClass, add=False, trainIdx=trainIdx)
        self.getAveregedWeights(trainIdx)

    def getAveregedWeights(self, trainIdx):
        for c in self.classes:
            for k in self.weights[c].keys():
                self.weights[c][k] -= (self.avgWeights[c][k] / float(trainIdx))

    def predict(self, featureDict):
        newFeatureDic = {}
        for k in featureDict.keys():
            # if k in self.featureSet:
            newFeatureDic[k] = featureDict[k]

        argMax, predictedClass = 0, self.classes[0]
        for c in self.classes:
            currentActivation = self.getCurrentActivation(newFeatureDic, c) #np.dot(feature_vector, self.weight_vectors[c])
            if currentActivation >= argMax:
                argMax, predictedClass = currentActivation, c

        return [predictedClass]

    def getCurrentActivation(self, featureDict, cat):
        result = 0
        for k in featureDict.keys():
            result += self.weights[cat][k]
        return result


    def updateWeights(self, featureDict, cat, add=True, trainIdx=1):
        for k in featureDict.keys():
            if add:
                self.weights[cat][k] += featureDict[k]
                self.avgWeights[cat][k] += featureDict[k] * trainIdx
            else:
                self.weights[cat][k] -= featureDict[k]
                self.avgWeights[cat][k] -= featureDict[k] * trainIdx


class Vectorizer:

    def __init__(self, clf=None):
        self.featureSet = set()
        self.clf = clf

    def vectorize(self, dic, updateWeights=False):
        newDic = {}
        for k in dic:
            newK = str(k) + '=' + str(dic[k])
            newDic[newK] = 1
            if newK not in self.featureSet:
                self.featureSet.add(newK)
                if updateWeights:
                    # if newK not in self.clf.featureSet:
                        for c in self.clf.classes:
                            # if newK not in self.clf.modelDic[c].keys():
                            self.clf.weights[c][newK] = 0
                            self.clf.avgWeights[c][newK] = 0
        return newDic

    def transform(self, listOfOnDic):
        newDic = {}
        dic = listOfOnDic[0]
        for k in dic:
            newK = str(k) + '=' + str(dic[k])
            if newK in self.featureSet:
                newDic[newK] = 1
        return newDic

