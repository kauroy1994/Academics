#---------------------------------------------------- part (a) ---------------------------------------------------------------
x1 <- read.table("pred1.dat") #data matrix
y1 <- read.table("resp1.dat") #response variables
x11st_half <- as.matrix(x1[1:500,]) #first half of both
y11st_half <- as.matrix(y1[1:500,])
x12nd_half <- as.matrix(x1[501:1000,]) #second half of both
y12nd_half <- as.matrix(y1[501:1000,])
x <- c(1:50) #consider all 50 predictors first
SSEs <- NULL
vars <- x 
varslist <- NULL #initialize final variable list to NULL
w <- NULL #temporary place holder
what <- function(v){ #function to return all attribute SSE's
	wv <- solve(t(x11st_half[,v])%*%x11st_half[,v])%*%(t(x11st_half[,v])%*%y11st_half)
	yhat <- x11st_half[,v]%*%wv
	SSE <- sum((yhat - y11st_half)^2)
	return(SSE)
}
w <- as.numeric(lapply(vars,what))
varslist <- append(varslist,which.min(w)) #get minimum SSE predictor, number 21
SSEs <- append(SSEs,min(w)) #get the minimum SSE
vars <- x[-varslist] #cut the predictor list to all - 21
w <- NULL #recalculate min SSE using new predictor list and new data set with 21th predictor included
what <- function(v){
	wv <- solve(t(x11st_half[,c(varslist,v)])%*%x11st_half[,c(varslist,v)])%*%(t(x11st_half[,c(varslist,v)])%*%y11st_half)
	yhat <- x11st_half[,c(varslist,v)]%*%wv
	SSE <- sum((yhat - y11st_half)^2)
	return(SSE)
}
w <- as.numeric(lapply(vars,what))
varslist <- append(varslist,which.min(w)+1) #get minimum SSE predictor, number 47, plus one because 21 removed
SSEs <- append(SSEs,min(w)) #get the minimum SSE
vars <- x[-varslist] #cut the predictor list to all - 21 and 47
w <- NULL #recalculate min SSE using new predictor list and new data set with 21th and 46th predictor included
what <- function(v){
	wv <- solve(t(x11st_half[,c(varslist,v)])%*%x11st_half[,c(varslist,v)])%*%(t(x11st_half[,c(varslist,v)])%*%y11st_half)
	yhat <- x11st_half[,c(varslist,v)]%*%wv
	SSE <- sum((yhat - y11st_half)^2)
	return(SSE)
}
w <- as.numeric(lapply(vars,what))
varslist <- append(varslist,which.min(w)) #final varlist is 21, 47 and 16
SSEs <- append(SSEs,min(w)) #get the minimum SSE
#---------------------------------------------------- part (b) ---------------------------------------------------------------
wVarlist <- solve(t(x11st_half[,c(varslist)])%*%x11st_half[,c(varslist)])%*%(t(x11st_half[,c(varslist)])%*%y11st_half)
yVarlist <- x12nd_half[,c(varslist)]%*%wVarlist
SSEVarlist <- sum((yVarlist - y12nd_half)^2) #SSE with 3 predictors #5.099969
wAllPredictors <- solve(t(x11st_half)%*%x11st_half)%*%(t(x11st_half)%*%y11st_half)
yAllPredictors <- x12nd_half%*%wAllPredictors
SSEAllPredictors <- sum((yAllPredictors - y12nd_half)^2) #SSE with all predictors #5.721507
#SSE with 3 less than with all because just the 3 together form a more accurate dependence relationship with y than all
#This is because those 3 were chosen such that they minimize the SSE so are probably a better selection.