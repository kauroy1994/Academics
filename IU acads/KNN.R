KNNClassifier<-function(train,test,k){
	distance<-function(data_item1,data_item2){
		#return(as.numeric(1-(cor(data_item1,data_item2))))
		return(as.numeric(sqrt(sum((data_item1-data_item2)^2))))
	}
	length<-length(train)
	fulltrain<-train
	train<-fulltrain[1:length-1]
	test<-test[1:length-1]
	train<-as.matrix(train)
	test<-as.matrix(test)
	knearest_list<-list()
	for(testpointer in 1:length(rownames(test))){
		print(paste("test point",c(testpointer)))
		knearest<-NULL
		distances<-apply(train,1,function(x) distance(x,test[testpointer,]))
		knearest_distances<-sort(distances)[1:k]
		for(kcount in 1:k)
		knearest[kcount]<-toString(fulltrain[match(knearest_distances[kcount],distances),length])
		knearest_list[[testpointer]]<-knearest
	}
	classLabels<-NULL
	for(testpointer in 1:length(rownames(test)))
	classLabels[testpointer]<-names(which.max(table(knearest_list[[testpointer]])))
	return(classLabels)
}