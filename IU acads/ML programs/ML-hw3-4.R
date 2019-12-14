n = 100 #number of months
prob <- NULL
obv <- NULL
for (i in 1:n){
	x <- rnorm(1,mean=10,sd=1) #sample i N(10,1) observations
	obv[i] <- x
	sampleMean <- mean(obv) #calculate sample mean
	pMean <- (sampleMean*i)/(10^-6+i) #calculate estimated mean
	pVariance <- 1/(10^-6+i) #calculate estimated variance
	range = c(1:20) #simulate density over this range
	prob <- dnorm(range,mean=pMean,sd=sqrt(pVariance)) #density
	print(paste("Number of earthquakes observed: ",x,"expected number of earthquakes in month ",i,": ",pMean))
	plot(range,prob,type='l',xlab="Number of earthquakes",ylab="Probability density") #plot distribution so far
	readline() #advance program for next month
}
#pMean is the final expected value of the posterior distribution and is equal to the sampleMean = 10.12726