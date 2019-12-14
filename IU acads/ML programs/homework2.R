q = 4 #question number
if(q==2){
	
	n = 1000 #Number of binomial trials
	#x = runif(10000,0,500) #uniformly distributed
	#X <- choose(n,x)*(0.5^x)*(0.5^(n-x))
	X<-NULL
	for(x in 1:n){
		X <- append(X,choose(n,x)*(0.5^x)*(0.5^(n-x)))
	}

	plot(X,type='l')

	#standardize by creating new random variable Z = (X-mean)/stddev

	Xstd <- (X-250)/sqrt(125) #standardized vector
	dev.new() #create new window for new plot
	plot(Xstd,type='l') #plotting standard variable

	stdNormal <- rnorm(n) #sampling 10000 points of normal distribution

	dev.new()
	plot(stdNormal,type='l')
}
if(q == 4){
	lambda = 3
	#vector = runif(10000) #get 10000 numbers
	vector = seq(0,1,length.out=10000)
	edist = 1 - exp(-vector/lambda)
	plot(edist,type='l')
	
	poisson = exp(-lambda)*vector/factorial(vector)
	dev.new() #create new window
	plot(poisson,type='l')
}