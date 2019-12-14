n = 20000 #number of experiments
prob <- NULL
for (i in 1:n){
	k = 500 #number of trials
	u <- runif(k)
	prob[i]<- sum(u > 0.5)	#generate vector of true, false
	probStd <- (prob - mean(prob))/sd(prob) #standardize
}
hist(probStd)