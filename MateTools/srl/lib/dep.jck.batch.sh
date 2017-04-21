#!/bin/bash
java -cp anna-3.3.jar is2.parser.Parser -train /Users/halsaied/Documents/IdenSys/MateTools/HU/Jackkniffing/9.train.jck.txt -model /Users/halsaied/Documents/IdenSys/MateTools/HU/Jackkniffing/9.model.jck.txt
java -cp anna-3.3.jar is2.parser.Parser -model /Users/halsaied/Documents/IdenSys/MateTools/HU/9.model.jck.txt -test /Users/halsaied/Documents/IdenSys/MateTools/HU/Jackkniffing/9.test.jck.txt -out /Users/halsaied/Documents/IdenSys/MateTools/HU/Jackkniffing/9.output.jck.txt



java -cp anna-3.3.jar is2.parser.Parser -model /Users/halsaied/Documents/IdenSys/sharedtask/HU/mate.trainbased.mode -test /Users/halsaied/Documents/IdenSys/sharedtask/HU/test.conllu.autoPOS.conllu2009 -out /Users/halsaied/Documents/IdenSys/sharedtask/HU/test.conllu.autoPOS.autoDep
