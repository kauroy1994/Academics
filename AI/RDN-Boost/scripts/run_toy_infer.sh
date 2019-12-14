dir="../data/toy_cancer/";
java -cp ../WILL.jar edu.wisc.cs.Boosting.RDN.RunBoostedRDN \
-aucJarPath ".." \
-target cancer \
-trees 20 \
-model $dir/train/models \
-i -test $dir/test/ \
