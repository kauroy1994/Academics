#----------------------------------------------------------- PROGRAM TO PREDICT PROBABILITY OF WINNING ------------------------------------------------------------------
#include necessary libraries
#install.packages("hash") --> uncomment if you don't have this package
library(hash)
#program to perform data exploration on tennis data
#clear workspace
rm(list=ls())
#simple linear regression function
linReg <- function(dm){
	dm <- as.matrix(dm)
	npred <- ncol(dm) - 1
	x <- as.matrix(dm[,1:npred])
	y <- as.matrix(dm[,npred+1])
	what <- solve(t(x)%*%x)%*%(t(x)%*%y)
	return(x%*%what)
}
#read data
data <- read.csv("tennis.csv")
#get Grandslam data only
GSwon <- na.omit(subset(data,tourney_level = "G",select = c(surface,round,winner_seed,loser_seed,w_ace:w_SvGms,w_bpSaved/w_bpFaced)))
GSlost <- na.omit(subset(data,tourney_level = "G",select = c(surface,round,winner_seed,loser_seed,l_ace:l_SvGms,w_bpSaved/w_bpFaced)))
colnames(GSwon)[length(GSwon)] <- "w_bpSaved"
#encode surfaces and round
surfaces <- hash(as.numeric(unique(GSwon$surface)),unique(GSwon$surface))
rounds <- hash(as.numeric(unique(GSwon$round)),unique(GSwon$round))
#replace encodings
GSwon[,1] <- as.numeric(GSwon[,1])
GSwon[,2] <- as.numeric(GSwon[,2])
GSlost[,1] <- as.numeric(GSlost[,1])
GSlost[,2] <- as.numeric(GSlost[,2])
#construct probability distribution of winning percentage per seed
wProb <- data.frame(table(GSwon[,3]))
wProb$Freq <- wProb$Freq*100/sum(wProb$Freq)
colnames(wProb) <- c("Seeding","Prob")
#create hash map of seeding and probabilities just in case
wProbHash <- hash(wProb$Seeding,wProb$Prob)
#define get hash function
get_hash <- function(x) return(wProbHash[[toString(x)]])
#regress probability of winning using different predictors
#first serve win percentage
fswp <- (GSwon$w_1stWon/GSwon$w_1stIn)*100
#second serve win percentage
sswp <- (GSwon$w_2ndWon/(GSwon$w_svpt - GSwon$w_1stIn - GSwon$w_df))*100
seeds <- as.numeric(GSwon$winner_seed)
#construct data matrix of seed, first serve win percentage and second serve win percentage
dm <- na.omit(data.frame(GSwon$winner_seed,fswp,sswp,GSwon$w_bpSaved))
#get unique seedings and number of them
dseeds <- as.numeric(unique(GSwon$winner_seed))
n <- length(dseeds)
#function to return average first serve win percentage per seed
averf <- function(x){
	X <- dm[dm[,1] == x,2]
	aver <- as.numeric(mean(X))
	return (aver)
}
#function to return average 2nd serve win percentage per seed
avers <- function(x){
	X <- dm[dm[,1] == x,3]
	aver <- as.numeric(mean(X))
	return (aver)
}
#function to return average number of break points saved per seed
averb <- function(x){
	X <- dm[dm[,1] == x,4]
	aver <- as.numeric(mean(X))
	return (aver)
}
#get average first,second serve and break points win percentage per seed
fp <- as.numeric(lapply(dseeds,averf))
sp <- as.numeric(lapply(dseeds,avers))
bp <- as.numeric(lapply(dseeds,averb))
#get probability of winning per seed
probs <- as.numeric(lapply(dseeds,get_hash))
#create data matrix
dm <- na.omit(data.frame(fp,sp,bp,sp/bp,probs))
colnames(dm) <- c("fwp","swp","bpwp","ratio","wprob")
#get regressed values for different combinations of predictors
yhat <- linReg(dm)
yhat2 <- linReg(dm[,c(1,2,5)])
yhat3 <- linReg(dm[,c(1,2,3,5)])
par(mfrow=c(1,4))
plot(dseeds,dm$wprob,type='p',col="green",pch=19)
plot(dseeds,yhat,type='p',col="red",pch=19)
plot(dseeds,yhat2,type='p',col="black",pch=19)
plot(dseeds,yhat3,type='p',col="black",pch=19)
#----------------------------------------------------------- RIGHT NOW THE PREDICTIONS SUCK ------------------------------------------------------------------