#Question 5
#---------------------------------------------------- part (a) ---------------------------------------------------------------
x <- as.matrix(read.table("pred2.dat")) #data matrix
y <- as.matrix(read.table("resp2.dat")) #responses
w <- solve(t(x[1:500,])%*%x[1:500,])%*%(t(x[1:500,])%*%y[1:500,])
lambda <- 20
wridge <- solve((t(x[1:500,])%*%x[1:500,])+lambda*diag(500))%*%(t(x[1:500,])%*%y[1:500,])
yridge <- x[501:1000,]%*%wridge
#---------------------------------------------------- part (b) ---------------------------------------------------------------
SSE <- sum((y[501:1000,]-x[501:1000,]%*%w)^2) #SSE normal regression 32984664
SSEridge <- sum((y[501:1000,]-x[501:1000,]%*%wridge)^2) #SSE ridge regression 35918.6
#ridge regression penalizes in proportion to how far displaced from the origin the weight is. So the weight vector isnt -
#- allowed to go too far from the origin. Since normal regression doesnt penalize this, its SSE is higher.
#---------------------------------------------------- part (c) ---------------------------------------------------------------
lambda <- c(1:25)
SSEs <- NULL
ridge <- function(lambda){
	what <- solve((t(x[1:500,])%*%x[1:500,])+lambda*diag(500))%*%(t(x[1:500,])%*%y[1:500,])
	yhat <- x[501:1000,]%*%what
	return(sum((y[501:1000,]-yhat)^2))
}
SSEs <- as.numeric(lapply(lambda,ridge))
bestLambda <- which.min(SSEs) #therefore the best value of lambda is 7 for which SSE is 30788.08 still large