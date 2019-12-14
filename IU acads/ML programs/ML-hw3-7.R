#Question 7
#step can be anywhere between 0.004 to 0.007 for 100% accuracy
#run using q7(0.004) and keep hitting return to see output
q7 <- function(step){
	data(iris)
	#part (a)
	classVector <- as.numeric(iris$Species == "setosa") #1 for setosa 0 otherwise

	#part(b)
	#sigmoid function p = 1/(1+e^-x) definition 
	sigma <- function(X){ 
		return(1/(1+exp(-X)))
	}
	
	#log likelihood function using the formula sum(c*log(p)+(1-c)log(1-p))
	loglikelihood <- function(W,data){
		result <- NULL
		f <- as.numeric(sigma(t(W)%*%data))
		result <- classVector*log(f) + (1-classVector)*log(1-f)
		return (sum(result)/N)
	}

	#gradient function using the formula (sum(c-p)Xi)/N
	gradient <- function(W,data,N){
		result <- NULL
		f <- as.numeric(sigma(t(W)%*%data))
		d <- classVector - f
		for(i in 1:4)
		result[i] <- sum(d*as.numeric(iris[,i]))/N
		return (result)
	}
	
	W <- rep(c(0),4) #initial weight vector of 4 zeros
	E <- step #step size given as input to function
	N <- nrow(iris) #number of rows
	likelihood <- NULL
	for(i in 1:N){
		X <- as.numeric(iris[i,][1:4])
		likelihood[i] <- loglikelihood(W,X)
		W <- W + E*gradient(W,X,N)
		print(paste("Log likelihood: ",likelihood[i],sep="")) #print log likelihood
		print("estimated weights are: ") #print estimated weights after each iteration
		print(W)
		readline() #wait for return key to advance program
	}
	prob <- NULL #probability vector of classes between 0 and 1
	for(i in 1:N)
	prob[i] <- as.numeric(sigma(t(W)%*%(as.numeric(iris[i,][1:4]))))
	predicted <- as.numeric(prob > 0.5) #1 if prob close to 1 else 0

	acc <- as.numeric(sum(classVector == predicted)) * 100/N #print accuracy as number correctly classified/total
	return (paste("Accuracy of classification: ",acc,"%")) #return accuracy
}