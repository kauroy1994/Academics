data(iris)
X <- as.matrix(iris[1:4])
C <- as.matrix(as.integer(iris[,5]=="setosa"))
sig <- function(x) return(1/(1+exp(-x)))
W <- as.matrix(rep(0,4))
N <- nrow(X)
#s <- 0.001
l <- NULL
for (i in 1:N){
	p <- as.numeric(sig(X%*%W))
	Hd <- diag(p*(1-p))
	H <- t(X)%*%Hd%*%X
	print(H)
	grad <- t(X)%*%(C - p)
	s <- -1 * (solve(H)%*%grad)
	l[i] <- sum(C*log(p) + (1-C)*log(1-p))
	W <- W + grad*s
}
p <- sig(X%*%W)
pc <- as.integer(p > 0.5)
plot(sort(l),type='l')