#10000 samples of independent binomial(500,1/2) experiments stored in bvect
require

bvect<-NULL
#for(i in 1:20){
l = 500
	for(n in 1:l){
		bvect<-append(bvect,(choose(l,n)*(0.5^n)*(0.5^(l-n))))
	}
#}

#uniform(0,1) distribution

sample<-bvect

plot(bvect,type='l')

#2b standardize

sample<-(sample - (l*0.5))/sqrt(l*0.25)

#now mean, variance = 0 and 1
dev.new()
plot(sample,type='l')

