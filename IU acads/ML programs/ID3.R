#ID3 to be continued ..
#write function to split on attribute and return entropy of resulting class set
splitOn <- function(feature,DummyData){
	attach(DummyData) #attach for faster computation
	distinct<-unique(get(feature)) #get distinct values of the feature
	subSet <- DummyData[get(feature) == distinct,] #subset based on those values
	classFrequencies <- as.vector(table(subSet$cl)) #get resulting classes frequencies
	return(entropy.empirical(classFrequencies)) #calculate entropy of the class split and return
}

#create dummy data set
#choose 10 random numbers for first feature f1 between 1 and 5 and so on ..
f1<- sample.int(5,10,replace=TRUE) 
f2<- sample.int(8,10,replace=TRUE)
f3<-sample.int(7,10,replace=TRUE)
f4<-sample.int(6,10,replace=TRUE)
#create dummy classes
cl<-c("apples","monkeys","monkeys","bannanas","apples","bannanas","apples","apples","monkeys","bannanas")
#compile into data frame
DummyData<-data.frame(f1,f2,f3,f4,cl)

library(entropy) #include entropy library. First install using install.packages

features<-colnames(DummyData) #get feature names
n<-length(features)-1

entropies<-NULL

#for every feature calculate entropy of resulting class split
for (i in 1:n) entropies[i]<-splitOn(features[i],DummyData) 

print(entropies) #print the entropies per feature


