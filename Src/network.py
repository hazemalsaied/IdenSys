import keras
import copy
import pickle
import numpy as np

from os import path
from keras.models import Sequential
from keras.regularizers import l2
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers.merge import Concatenate
from keras.layers.embeddings import Embedding


class Network():
    batch_size = 10000
    nb_epoch = 1050

    def __init__(self):

        words = self.load_embedding("word.txt")
        tags = self.load_embedding("pos.txt")
        labels = self.load_embedding("label.txt")
        # make_softmax_arq(labels)

        words_indx = self.get_dict(words)
        tags_indx = self.get_dict(tags)
        labels_indx = self.get_dict(labels)

        w_weights = self.get_weights(words, words_indx, 100)
        p_weights = self.get_weights(tags, tags_indx, 100)
        l_weights = self.get_weights(labels, labels_indx, 100)


        self.make_softmax(labels)
        output_dim = (len(labels.keys()) - 1) * 2 + 1

        word_features = Sequential()
        word_features.add(Embedding(input_dim=len(words.keys()) + 1, input_length=18, output_dim=100, mask_zero=False,
                                    weights=[w_weights]))
        word_features.add(Flatten())

        pos_features = Sequential()
        pos_features.add(Embedding(input_dim=len(tags.keys()) + 1, input_length=18, output_dim=100, mask_zero=False,
                                   weights=[p_weights]))
        pos_features.add(Flatten())

        label_features = Sequential()
        label_features.add(Embedding(input_dim=len(labels.keys()) + 1, input_length=12, output_dim=100, mask_zero=False,
                                     weights=[l_weights]))
        label_features.add(Flatten())

        model = Sequential()

        model.add(Concatenate([word_features, pos_features, label_features], mode='concat', concat_axis=1))
        # model.add(Reshape(((18*100)+(16*18)+(12*16),)))
        model.add(Dropout((0.5)))
        model.add(Dense(output_dim=400, activation="relu", W_regularizer=l2(1e-6)))
        model.add(Dense(output_dim=400, input_dim=400, activation="relu", W_regularizer=l2(1e-6)))
        model.add(Dense(output_dim=400, input_dim=400, activation="relu", W_regularizer=l2(1e-6)))
        # To-do: Modelar a ativacao tripla X 3

        model.add(Dense(output_dim=output_dim, input_dim=400))
        model.add(Activation('softmax'))
        adagrad = keras.optimizers.Adagrad(lr=0.01, epsilon=1e-9)
        model.compile(loss='categorical_crossentropy', optimizer=adagrad)

        del l_weights,p_weights,w_weights,words_indx,tags_indx,labels_indx,words,tags,labels

        # Extract one-hot repersentations

        (dict_op, one_hot) = self.to_onehot(open("./corpus/temp/softmax_arq.txt"))
        self.save_dict(dict_op)
        dict_opaux = copy.deepcopy(dict_op)
        for element in range(0, len(one_hot[0])):
            for key in dict_op.keys():
                if dict_opaux[key] == element:
                    dict_op[key] = one_hot[0][element]

        return model

    def load_embedding(self, file_embedding_model):
        arquivo = open(path.join("./embeddings/", file_embedding_model))
        embeddings = dict()

        for s in arquivo:
            s = s.split(" ")
            if s[0] not in embeddings.keys():
                embeddings[s[0]] = [float(x) for x in s[1:]]
        arquivo.close()
        return embeddings


    def make_softmax(self, labels):

        #create a file that contains all the possible arc-standard operations
        operations_arq = open("./corpus/temp/softmax_arq.txt", "w")
        op = 0
        for i in range(0, 2):
            for l in labels.keys():
                if op == 0 and not ("NULL" in l):
                    operations_arq.write("LEFTARC" + ":" + l + "\n")

                elif op == 1 and not ("NULL" in l):
                    operations_arq.write("RIGHTARC" + ":" + l + "\n")
            op = 1
        operations_arq.write("SHIFT")


    def get_weights(self, dict_vec, dict_indx, dim):
        #get the weights and flatten them in to a matrix
        weights = np.zeros((len(dict_vec.keys()) + 1, dim))
        for key in dict_indx.keys():
            weights[dict_indx[key], :] = dict_vec[key]
        return weights

    def get_dict(self, dictionary):
        return_dict = dict()
        i = 0
        for key in dictionary.keys():
            return_dict[key] = i
            i += 1
        return return_dict

    def save_dict(self, dict):
        input_file = open("./corpus/temp/dict_onehot.pickl", "wb")
        pickle.dump(dict, input_file)
        input_file.close()

    def to_onehot(self, arq):
        text_ = dict()
        i = 0
        for line in arq:
            text_[line.rstrip()] = i
            i = i + 1
        keys2 = [key for key in text_.values()]
        keys2.sort()
        keys = np.array(keys2, ndmin=2)
        arq.close()
        return (text_, self.id_tensor_to_one_hot_tensor(keys, one_hot_dim=len(text_.keys())))

    def id_tensor_to_one_hot_tensor(self, tensor_2d, one_hot_dim=None):
        """
        :param tensor_2d: numpy array of sequences of ids
        :param one_hot_dim: if not specified, max value in tensor_2d + 1 is used
        :return:
        """

        # return np_utils.to_categorical(tensor_2d)
        if not one_hot_dim:
            one_hot_dim = tensor_2d.max() + 1

        tensor_3d = np.zeros((tensor_2d.shape[0], tensor_2d.shape[1], one_hot_dim), dtype=np.bool8)
        for (i, j), val in np.ndenumerate(tensor_2d):
            tensor_3d[i, j, val] = 1
        return tensor_3d