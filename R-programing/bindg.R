a =  c (1,2,3,4,5,6,7,42)
d = c (1:8)
a
d
a*2
d/10
a*d
sd = rbind(a, d)

col = cbind(a, d)
col

cbind(BOD,BOD)
rbind(BOD,BOD)
mat = matrix(data = c(a, d), nrow = 8, ncol = 2)
mat
mat1 = matrix(data = c(a, d), nrow = 8, ncol = 8)
mata = matrix(c(a, d), 8, 2, byrow = TRUE) 
mata = matrix(c(a, d), 8, 2, byrow = FALSE) 

a = rep(1:2,1:1 ,each =2)
a
fix(a)




