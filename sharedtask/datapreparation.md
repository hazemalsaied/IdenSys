### FR - Dependencies
1- merge the SPMRL files (train, dev, test) using MateTools.mergeConlluFiles()

2- transform the resulted file format from Conllu into Conllu2009 using MateTools.ConlluToConll2009()

3- converting the shredtask french corpus (train + test) to conllu 2009

4- excute the mate batsh for training and producing the result /MateToolssrl/lib/fr.dep.batsh.sh

**5- converting the two output files (train + test) into conllu format.**


### HU - Dependencies

1- Convert the current conllu train file into conllu 2009

2- extract the mate model based of the train file

3- predict the dep of test file. 

4- integrate the predictions.

5- divide the train file into 10 folds of train and tests. 

6- creat a batsh to train a model, predict the test

7- merge all resulting folds

8- integrate them with train file. 
 
