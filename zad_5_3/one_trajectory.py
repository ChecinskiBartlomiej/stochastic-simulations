#Since our process is markov chain and has stationary distribution I can use only one trajectory

import numpy as np
import math
import time

start = time.time()

alpha_0 = 4
alpha_1 = -2
beta = 0.5
d = 20
n = 2000000
burn = int(0.8 * n)

# generate dxd matrix with 1 zero padding so {d+2}x{d+2} matrix 
def matrix():
    Z = np.random.choice([0,1], (d, d))
    X = np.pad(Z, pad_width=1, constant_values=0)
    return X

def pi(X, c1, c2): #pi(x_t=1|x_{-t}), t=(c1,c2)
    e = math.exp(beta*(alpha_0+alpha_1*(X[c1][c2-1]+X[c1][c2+1]+X[c1-1][c2]+X[c1+1][c2]))) 
    return 1/(1+e)
def pi_prim(X, c1, c2): # 1-pi(x_t=1|x_{-t})=pi(x_t=0, x_{-t})
    return 1 - pi(X, c1, c2)

def step(X):
    d_values = np.arange(1, d+1) 
    c1 = np.random.choice(d_values)
    c2 = np.random.choice(d_values) 
    p1 = pi(X, c1, c2)
    p2 = pi_prim(X, c1, c2)
    k = np.random.choice([0,1], p=[p2, p1]) #sample 0 with probability p2 and 1 with probability p1
    X[c1][c2] = k
    return X

def estimate_S(X):
    S = 0
    for j in range(burn):
        X = step(X)
    for j in range(burn, n):
        X = step(X)
        S += np.sum(X)
    return S/(n-burn)


def estimate_N(X):
    N = 0
    for j in range(burn):
        X = step(X)
    for j in range(burn, n):
        X = step(X)
        center = X[1:d+1, 1:d+1]
        left = X[1:d+1, 0:d]
        right = X[1:d+1, 2:d+2]
        up = X[0:d, 1:d+1]
        down = X[2:d+2, 1:d+1]
        interactions = np.sum(center * (left + right + up + down))
        N += interactions
    return N/(2*(n-burn))

X = matrix()
print(f"Estimated S: {estimate_S(X)}")
X = matrix()
print(f"Estimated N: {estimate_N(X)}")

end = time.time()

print(f"Czas wykonania: {end - start:.4f} sekund")
