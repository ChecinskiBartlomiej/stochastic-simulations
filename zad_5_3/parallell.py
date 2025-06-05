import numpy as np
import time

start = time.time()

alpha_0 = 4
alpha_1 = -2
beta = 0.5
d = 20
n = 200000
K = 2000

def init_batch():
    X = np.random.choice([0, 1], (K, d, d))
    X = np.pad(X, ((0,0), (1,1), (1,1)))
    return X

def batch_step(X_batch):
    d_vals = np.arange(1, d+1)
    C1 = np.random.choice(d_vals, K)
    C2 = np.random.choice(d_vals, K)

    idx = np.arange(K)
    left = X_batch[idx, C1, C2-1]
    right = X_batch[idx, C1, C2+1]
    up = X_batch[idx, C1+1, C2]
    down = X_batch[idx, C1-1, C2]
    sum_of_neighbours = left + right + up + down

    exponent = beta * (alpha_0 + alpha_1 * sum_of_neighbours)
    prob = 1/(1+np.exp(exponent))

    random_vals = np.random.rand(K)
    new_vals = (random_vals < prob).astype(int)
    X_batch[idx, C1, C2] = new_vals
    
    return X_batch

def simulate_and_estimate(X_batch):
    for j in range(n):
        X_batch = batch_step(X_batch)
    #esimtate S
    S = np.sum(X_batch, axis=(1,2)).mean()
    #estimate N
    center = X_batch[:, 1:d+1, 1:d+1]
    left = X_batch[:, 1:d+1, 0:d]
    right = X_batch[:, 1:d+1, 2:d+2]
    up = X_batch[:, 0:d, 1:d+1]
    down = X_batch[:, 2:d+2, 1:d+1]
    interactions = np.sum(center*(left + right + up + down), axis=(1,2)).mean()
    N = interactions/2
    return S, N

X_batch = init_batch()
(S, N) = simulate_and_estimate(X_batch)
print(S)
print(N)

end = time.time()

print(f"Czas wykonania: {end - start:.4f} sekund")