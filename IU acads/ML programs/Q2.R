#question number 2
# n represents the number of experiments
#k is the number of trials
#p is the probability of success of the binomial trial
#prob is the probability vector

n = 10000
prob <- NULL
for (i in 1:n){
	k = 500 
	p = 0.5
	u <- runif(k)
	prob[i]<- sum(u > p)	
	probStd <- (prob - mean(prob))/sd(prob) #standardize
}
par(mfrow=c(1,3)) #to plot side by side
hist(prob) #answer to question 2a
print(mean(probStd)) #mean of the standardized binomial vector (2b)
print(sd(probStd)^2) #variance of the standardized binomial vector (2b)
hist(probStd) #answer to question 2c
prob <- rnorm(n) #normally distributed with mean 0 and sd 1  
hist(prob) #answer to question 2d
