library(entropy)

#data without SCN and class label, hence slicing[2:10]
data<-na.omit(read.csv("meddata.csv"))[2:10]

#calculate counts of values in each column
counts_of_values<-list()
for(i in 1:length(colnames(data))){
	count<-NULL
	#initialize counts and smooth to avoid infinite values
	for(x in 1:10){count[x]<-0.00000000000000000000000000000000000000000000000000000000000000000000000001}
	for(j in 1:10){
		for(k in 1:length(rownames(data))){
			if(data[k,i]==j){
				count[j]<-count[j]+1
			}
		}
	}
	counts_of_values[[i]]<-count
}

#initialize the entropies
column_entropies<-NULL

#calculating entropies for all columns
for(i in 1:length(colnames(data))){
	column_entropies[i]<-entropy.empirical(counts_of_values[[i]],unit=c("log2"))
}

#calculate KL-distances for Attribute pairs

#intialize the distances
KL_distances<-list()
n<-length(colnames(data))

#calculate distances

for(i in 1:n){
	for(j in 1:n){
		KL_distance<-KL.empirical(counts_of_values[[i]],counts_of_values[[j]],unit=c("log2"))
		KL_distances[[paste(c(i,j),collapse="")]]<-KL_distance
	}
}
