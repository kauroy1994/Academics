x <- scan(file="time_series.dat") #read the file
data <- data.frame(x[1:998],x[2:999],x[3:1000]) #construct data
x <- as.matrix(data[,1:2]) #data matrix
y <- as.matrix(data[,3]) #responses
w <- solve(t(x)%*%x)%*%(t(x)%*%y) #calculate weight vector, value: -0.9497247, 1.0037957
SSE <- sum((x%*%w - y)^2) #SSE, value: 2.347588
var <- SSE/(nrow(x)-ncol(x)) #SSE/(n-k) #unbiased variance estimate 0.002357016
empvar <- var(x%*%w-y) #empiral error variance 0.002354248, pretty close!