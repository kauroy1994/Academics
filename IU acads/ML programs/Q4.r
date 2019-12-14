#Question 2b solution
#n is number of experiments
#prob is the probability vector
#lambda is the parameter
#numEvents is the number of events
#sum records the time elapsed

n = 10000
prob <- NULL
lambda <- 3 
for (i in 1:n){
	numEvents = 0
	sum = 0
	while (sum <= 1){
		u <- runif(1)
		sum <- sum + -log(u)/lambda
		numEvents <- numEvents + 1
	}
	prob[i] <- numEvents/n
}
par(mfrow=c(1,2))
hist(prob)
hist(rpois(n,lambda)) #Poisson(lambda)