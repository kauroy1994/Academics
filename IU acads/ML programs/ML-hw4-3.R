#Question 3
#---------------------------------------------------- part (a) ------------------------------------------------
x1 <- read.table("pred1.dat") #data matrix
y1 <- read.table("resp1.dat") #response variables
x11st_half <- as.matrix(x1[1:500,]) #first half of both
y11st_half <- as.matrix(y1[1:500,])
what1 <- solve(t(x11st_half)%*%x11st_half)%*%(t(x11st_half)%*%y11st_half)
x2 <- read.table("pred2.dat") #data matrix
y2 <- read.table("resp2.dat") #response variables
x21st_half <- as.matrix(x2[1:500,]) #first half of both
y21st_half <- as.matrix(y2[1:500,])
what2 <- solve(t(x21st_half)%*%x21st_half)%*%(t(x21st_half)%*%y21st_half)
#---------------------------------------------------- part (b) ------------------------------------------------
var1Unbiased <- sum(((x11st_half%*%what1)-y11st_half)^2)/450 #SSE/n-k ,value: 0.01077716
var2Unbiased <- sum(((x21st_half%*%what2)-y21st_half)^2)/0 #n-k = 0 problem is n = k, value: Inf
#---------------------------------------------------- part (c) ------------------------------------------------
y12nd_half <- as.matrix(y1[501:1000,]) #get second half responses
y22nd_half <- as.matrix(y2[501:1000,])
x12nd_half <- as.matrix(x1[501:1000,]) #get second half of both data sets
x22nd_half <- as.matrix(x2[501:1000,])
y12nd_halfhat <- as.matrix(x12nd_half%*%what1) 
y22nd_halfhat <- as.matrix(x22nd_half%*%what2)
SSE12ndhalf <- sum((y12nd_half - y12nd_halfhat)^2) #SSE for 2nd half of first data set, value: 5.721507
SSE22ndhalf <- sum((y22nd_half - y22nd_halfhat)^2) #SSE for 2nd half of second data set, value: 32984664