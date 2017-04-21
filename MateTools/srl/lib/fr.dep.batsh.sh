#!/bin/bash
#java -Xmx8g -cp anna-3.3.jar is2.parser.Parser -train /Users/halsaied/Documents/IdenSys/MateTools/SPMRL/spmrl.conllu.conllu2009 -model /Users/halsaied/Documents/IdenSys/MateTools/FR/spmrl.based.model
java -Xmx8g -cp anna-3.3.jar is2.parser.Parser -model /Users/halsaied/Documents/IdenSys/MateTools/FR/spmrl.based.model -test /Users/halsaied/Documents/IdenSys/sharedtask/FR/train.conllu.conllu2009 -out /Users/halsaied/Documents/IdenSys/sharedtask/FR/train.conllu.conllu2009.autoDep
java -Xmx8g -cp anna-3.3.jar is2.parser.Parser -model /Users/halsaied/Documents/IdenSys/MateTools/FR/spmrl.based.model -test /Users/halsaied/Documents/IdenSys/sharedtask/FR/test.conllu.conllu2009 -out /Users/halsaied/Documents/IdenSys/sharedtask/FR/test.conllu.conllu2009.autoDep

