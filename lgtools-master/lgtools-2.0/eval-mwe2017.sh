section="test"
projective=""
#dir="treebanks-mwe17/correctedpos"
dir="treebanks-mwe17/v0"
#dir="strict_ve_vd"
#mdir="models-mwe17"
mdir="tmp"
#outdir="outputs-mwe17"
outdir="tmp"
#for mwedef in va vb vc


#for version in va.correctedpos vb.correctedpos vc.correctedpos vd.correctedpos.strict vd.correctedpos
for version in v0
do
for lang in es_ancora nl_lassysmall sv ca fa
do
for i in `ls ../$dir/${lang}_${section}_${version}.conll`
do
#for baseline in "-F" "" "-B"
for baseline in "-B"
do
  echo $i
  model=$(basename $i)
  modeltmp=${model%_*_*}
  suffix=${version}.conll.${version}$baseline

  model=../$mdir/${modeltmp}_train_${suffix}  
  output=../$outdir/${modeltmp}_${section}_${suffix}.conll
  echo $model
  echo $output
  echo java -Xmx16g -cp classes:lib/JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m $model -o $output -i $i $baseline
  java -Xmx16g -cp classes:lib/JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m $model -o $output -i $i $baseline


done
done
done
done
