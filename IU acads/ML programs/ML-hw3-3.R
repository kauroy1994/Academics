#Question 3
#install.packages("mvtnorm") -- > uncomment this line and delete this text if you dont have the package when running
library(mvtnorm) 

data(iris) #read iris data

train <- iris #training set is whole data set
testIndices <- c(c(26:49),c(76:99),c(126:150)) #second half of each class
test <- iris[testIndices,] #test set

Ntrain = nrow(train) #number of rows in both
Ntest = nrow(test)

par(mfrow = c(1,3)) #create a 1x3 platform to plot graph

#answer to part (a)
plot(iris[,1],iris[,2],pch=c(19,24),xlab="Sepal.Length(dot)",ylab="Sepal.Width(triangle)") #plot sepal length vs width

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#answer to part (b)
#optimal bayes classifier
M <- NULL #initialize list of mean vectors per class
V <- NULL #initialize list of covariance matrices per class
P <- NULL #initialize list of prior probabilities per class
	
classes<-as.character(unique(train[,5])) #get names of the 3 classes
#for each class make a vector of mean and variance vectors per column that is per feature
for (i in 1:3){
	subMatrix <- train[train[,5]==classes[i],1:4]
	M[[classes[i]]] <- as.vector(colMeans(subMatrix))
	V[[classes[i]]] <- as.matrix(cov(subMatrix))
	P[[classes[i]]] <- nrow(subMatrix)/Ntrain
	}
	
bayesClassifier <- function(dataVector,M,V,P){
	probVect <- NULL #probability vector containing probability of each class given the data P(c/D)
	setosaProb <- dmvnorm(dataVector,mean=M$setosa,sigma=V$setosa) #density of the three class conditional probabilities P(D/c)
	versicolorProb <- dmvnorm(dataVector,mean=M$versicolor,sigma=V$versicolor) 
	virginicaProb <- dmvnorm(dataVector,mean=M$virginica,sigma=V$virginica)
	probVect[c(1:3)]<-c(prod(setosaProb)*P["setosa"],prod(versicolorProb)*P["versicolor"],prod(virginicaProb)*P["virginica"]) #P(D/c)*P(c)
	classIndex <- which.max(probVect) #classify using argmax{P(D/c)*P(c)}
	if (classIndex == 1) return("setosa")
	if (classIndex == 2) return("versicolor")
	if (classIndex == 3) return("virginica")
}

#classify all the test data based on training set
predicted <- rep(FALSE,Ntest)
for (i in 1:Ntest) #for every test point
if (as.character(iris$Species[i]) == bayesClassifier(as.numeric(test[i,][1:4]),M,V,P)) predicted[i] <- TRUE #set predicted true if predicted correctly
color <- gsub(TRUE,"green",predicted) #color true as green
color <- gsub(FALSE,"red",color) #color false as red
plot(iris[,1],iris[,2],pch=c(19,24),xlab="Sepal.Length(dot)",ylab="Sepal.Width(triangle)",col=color) #plot
print(paste("Prediction accuracy in part(b): ",length(predicted[predicted==TRUE])*100/length(predicted)," %")) #print accuracy as numberOf(true)/(length(testset))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#answer to part(c)
trainIndices <- c(c(1:25),c(50:75),c(100:125)) #choose first half of each class as train set indices
train <- iris[trainIndices,] #training set
Ntrain <- nrow(train) #number of rows in both
Ntest <- nrow(test)

M <- NULL #initialize list of mean vectors per class
V <- NULL #initialize list of covariance matrices per class
P <- NULL #initialize list of prior probabilities per class

classes<-as.character(unique(train[,5])) #get names of the 3 classes
#for each class make a vector of mean and variance vectors per column that is per feature
for (i in 1:3){
	subMatrix <- train[train[,5]==classes[i],1:4]
	M[[classes[i]]] <- as.vector(colMeans(subMatrix))
	V[[classes[i]]] <- as.matrix(cov(subMatrix))
	P[[classes[i]]] <- nrow(subMatrix)/Ntrain
	}

#classify all the test data based on training set
predicted <- rep(FALSE,Ntest)
for (i in 1:Ntest) #for every test point
if (as.character(iris$Species[i]) == bayesClassifier(as.numeric(test[i,][1:4]),M,V,P)) predicted[i] <- TRUE #set predicted true if predicted correctly
color <- gsub(TRUE,"green",predicted) #color true as green
color <- gsub(FALSE,"red",color) #color false as red
plot(iris[,1],iris[,2],pch=c(19,24),xlab="Sepal.Length(dot)",ylab="Sepal.Width(triangle)",col=color) #plot
print(paste("Prediction accuracy in part(c): ",length(predicted[predicted==TRUE])*100/length(predicted)," %")) #print accuracy as numberOf(true)/(length(testset))

#The reason both the accuracy is same = 34% approximately, is because to classify the second half in each part we are #using the same training set, only difference being the training set has been bifurcated in the second part