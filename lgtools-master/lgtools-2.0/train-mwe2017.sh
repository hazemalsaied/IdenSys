baseline="-F"
projective=""
dir="treebanks-mwe17/correctedpos"
#dir="strict_ve_vd"
mdir="tmp"
#for mwedef in va vb vc

# for vd.correctedpos* need for training with -F as well

#for mwedef in va.correctedpos vb.correctedpos vc.correctedpos vd.correctedpos.strict vd.correctedpos
for mwedef in vd.correctedpos.strict vd.correctedpos
do
#for lang in es_ancora nl_lassysmall sv ca fa

for lang in fa
do
for i in `ls ../$dir/${lang}_train_${mwedef}.conll`
do
for baseline in "-B" ""
do 

  echo $i
  model=$(basename $i)
  model=../$mdir/$model.${mwedef}${baseline}${projective}
  echo $model
  t=/tmp/tmp.txt
  cat $i | sed -E "s/fixed_/mwe_/g;s/mwe_rmwe/fixed_rmwe/g" > $t
  echo java -Xmx16g -cp classes:lib/JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m $model -t $t --msize 2000000 $baseline $projective
  java -Xmx16g -cp classes:lib/JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m $model -t $t --msize 2000000 $baseline $projective

   model=$(basename $i)
  model=../$mdir/$model.${mwedef}${projective}
  #echo $model

  #echo java -Xmx16g -cp classes:lib/JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m $model -t $i --msize 2000000 $projective
  #java -Xmx16g -cp classes:lib/JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m $model -t $i --msize 2000000 $projective
done
done
done 
done

