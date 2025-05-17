#Calculate asymptotical variance. Theoretical result: sigma_as^2 = v^2/(1-alfa)^2

import random

def step(x, alfa, v):
    w = random.gauss(0, v)
    return alfa*x+w

def s(N, x, alfa, v):
    s = 0
    for j in range(N):
        x = step(x, alfa, v)
        s += x
    return s

N = 10000 #number of simulations
K = 1000 #for variance estimation
alfa = 0.99
v = 1 
x = 0

#calculate sum K times to estimate its variance
sums = []
for k in range(K):
    u = s(N, x, alfa, v)
    sums.append(u)

#calculate variance of sums
sums_mean = sum(sums)/len(sums)
diffs = [l - sums_mean for l in sums]
diffs_sq = [l**2 for l in diffs]
sums_var = sum(diffs_sq)/(len(sums)-1) 

#calculate asymptotical variance
sigma_sq_as = sums_var/N
print(sigma_sq_as)
