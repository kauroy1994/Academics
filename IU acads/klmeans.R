###############################################################################################################
#  																											  #
#		TITLE: KL-MEANS R PROGRAM																		      #
#		PACKAGES REQUIRED: hash package. Run "install.packages("hash")"										  #																  
#		REQUIRED WORKSPACE ELEMENTS: meddata.csv file provided in the attachment on oncourse				  #
#																											  #
###############################################################################################################
	
library(hash)
#generate test data set
#data_list<-list()
#for(i in 1:9){
	#data_list[[i]]<-c(1:100)
#}
#data_set<-data.frame(data_list)

#import actual data
original_data<-na.omit(read.csv("meddata.csv"))
#data_set<-na.omit(read.csv("meddata.csv"))[2:10]
data_set<-original_data[2:10]

#write distance function
distance = function(data_item1,data_item2){
	sum<-0
	for(i in 1:length(data_item1)){
		sum <- sum + (data_item1[i] - data_item2[i])*(data_item1[i] - data_item2[i])
	}
	return(sqrt(sum))
}

#initialize requirements
SCN_dict<-hash()
no_of_attributes<-length(colnames(data_set))
no_of_centroids<-3
no_of_iterations<-10
threshold<-0.01
l<-2

#sanity check
if(l==k){
	no_of_iterations<-1
}

#initialize_init_centroid
centroids_init<-list()
for(i in 1:no_of_centroids){
		centroids_init[[i]]<-rep(c(0),times=no_of_attributes)
	}

#get 2 random centroids from the data set
random_number<-NULL
centroids<-list()
random_number<-sample(1:length(rownames(data_set)),no_of_centroids)
for(i in 1:no_of_centroids){
centroids[[i]]<-data_set[random_number[i],]
}

#run klmeans number of iterations times
for(n in 1:no_of_iterations){
	#initialize centroid set to no_of_centroid sets with zero values, then convert to list
	centroid_set<-array(0,c((length(rownames(data_set))),no_of_attributes,no_of_centroids))
	centroid_set_list<-list()
	for(i in 1:no_of_centroids){
		centroid_set_list[[i]]<-centroid_set[,,i]
		}
	
	#initialize the centroid indices
	centroid_index<-rep(c(0),no_of_centroids)
	
	#assign data to l closest centroids
	for(i in 1:length(rownames(data_set))){
		
		distance_vector<-NULL
		#create distance vector
		for(j in 1:no_of_centroids){
			distance_vector[j]<-as.numeric(distance(data_set[i,],centroids[[j]]))
		}
		
		#create vector that stores l closest centroids
		l_vector<-NULL
		sorted_distance_vector<-NULL
		sorted_distance_vector<-sort(distance_vector)[1:l]
		for(j in 1:length(sorted_distance_vector)){
			for(k in 1:length(distance_vector)){
				if(sorted_distance_vector[j] == distance_vector[k]){
					l_vector[j] = k
				}
			}
		}
		
		#convert data point to vector
		data_point_vector<-NULL
		for(j in 1:length(data_set[i,])){
			data_point_vector[j]<-data_set[i,j]
		}
		
		#assign data point to the l closest centroids
		for(j in 1:length(l_vector)){
			if(centroid_index[l_vector[j]] < length(rownames(data_set))){
				centroid_index[l_vector[j]]<-centroid_index[l_vector[j]] + 1
				centroid_set_list[[l_vector[j]]][centroid_index[l_vector[j]],]<-data_point_vector
			}
		}
		SCN_dict[[toString(original_data[i,1])]]<-l_vector
	}
	#store old centroid
    old_centroids<-list()
    old_centroids<-centroids
    
	#calculate new centroids
	for(i in 1:no_of_centroids){
		for(j in 1:no_of_attributes){
			sum<-0
			for(k in 1:(centroid_index[i])){
				sum<-sum + centroid_set_list[[i]][k,j]
			}
			sum<-sum/(centroid_index[i])
			centroids[[i]][j]<-sum
		}
	}
	
	#initalize f0,f1
	f0<-0
	f1<-0
	
	#calculate f0
	for(i in 1:length(old_centroids)){
    		f0_individual<-0
    		for(j in 1:length(centroids_init)){
    			f0_individual<-f0_individual + distance(old_centroids[[i]],centroids_init[[j]])
    		}
    		f0<-f0 + f0_individual
    	}
    	
    #calculate f1
    for(i in 1:length(centroids)){
    		f1_individual<-0
    		for(j in 1:length(old_centroids)){
    			f1_individual<-f1_individual + distance(centroids[[i]],old_centroids[[j]])
    		}
    		f1<-f1 + f1_individual
    	}
    
    percentage_change<-abs(f1-f0)/f0
    if(percentage_change<=threshold){
    	break
    }
    centroids_init<-old_centroids
} 