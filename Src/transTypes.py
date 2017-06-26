from enum import Enum
from param import XPParams

class TransitionType(Enum):
    SHIFT = 0
    MERGE = 1
    COMPLETE = 2
    MWT_COMPLETE = 3
    REDUCE = 4
    WHITE_MERGE = 5
    MERGE_AS_LVC = 10
    MERGE_AS_VPC = 6
    MERGE_AS_IReflV = 7
    MERGE_AS_OTH = 8
    MERGE_AS_ID = 9


    @staticmethod
    def getAllClasses():
        if not XPParams.includeEmbedding:
            return [0,1,2,3]
        allClasses = []
        for tType in EmbedTransType:
            allClasses.append(tType.value)
        for tType in MWTTransitionType:
            allClasses.append(tType.value)
        return allClasses

    @staticmethod
    def getType(idx):
        for tType in TransitionType:
            if tType.value == idx:
                return tType
        for tType in MWTTransitionType:
            if tType.value == idx:
                return tType
        return None

    @staticmethod
    def inZeroCostTrans(transTypeValue, zeroCostTrans):

        for elem in zeroCostTrans:
            if transTypeValue == elem.value:
                return True
        return False

    @staticmethod
    def sort(transTypes):
        result = []

        if not XPParams.includeEmbedding:
            for elem in transTypes:
                if elem == TransitionType.MWT_COMPLETE:
                    result.append(elem)
            for elem in transTypes:
                if elem == TransitionType.MERGE:
                    result.append(elem)
            for elem in transTypes:
                if elem == TransitionType.COMPLETE:
                    result.append(elem)
            for elem in transTypes:
                if elem == TransitionType.SHIFT:
                    result.append(elem)
        else:
            for elem in transTypes:
                if elem == MWTTransitionType.MERGE_AS_MWT_VPC or elem == MWTTransitionType.MERGE_AS_MWT_LVC or elem == MWTTransitionType.MERGE_AS_MWT_ID or elem == MWTTransitionType.MERGE_AS_MWT_IREFLV:
                    result.append(elem)
            for elem in transTypes:
                if  elem == TransitionType.MERGE_AS_ID or elem == TransitionType.MERGE_AS_IReflV or elem == TransitionType.MERGE_AS_VPC \
                        or elem == TransitionType.MERGE_AS_LVC or elem == TransitionType.MERGE_AS_OTH:
                    result.append(elem)
            for elem in transTypes:
                if elem == TransitionType.WHITE_MERGE:
                    result.append(elem)
            for elem in transTypes:
                if elem == TransitionType.REDUCE:
                    result.append(elem)
            for elem in transTypes:
                if elem == TransitionType.SHIFT:
                    result.append(elem)
        return result

class EmbedTransType(Enum):
    SHIFT = 0
    REDUCE = 4
    WHITE_MERGE = 5
    MERGE_AS_LVC = 10
    MERGE_AS_VPC = 6
    MERGE_AS_IReflV = 7
    MERGE_AS_OTH = 8
    MERGE_AS_ID = 9
    MERGE_AS_MWT = 11

class MWTTransitionType(Enum):
    MERGE_AS_MWT_VPC = 20
    MERGE_AS_MWT_IREFLV = 21
    MERGE_AS_MWT_ID = 22
    MERGE_AS_MWT_LVC = 23

