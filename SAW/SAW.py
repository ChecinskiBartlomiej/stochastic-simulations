import random
import numpy as np
d = 2 #number of dimensions
k = 4 #number of steps
b = 2*k + 1 #size of board
N = 100000 #number of simulations

weights= [] # |SAW| = lim_n sum(weights)/n 

for i in range(N):
    M = np.array([[0 for _ in range(b)] for _ in range(b)]) #bxb board, 1 - visited, 0 - not visited
    s1 = k
    s2 = k #current state (k,k)
    M[s1][s2] = 1 #mark current state as visited
    weight = 1 #init weight
    for j in range(k):
        count = 0 #count how many steps are allowed
        allowed_steps = [] 

        if M[s1+1][s2] == 0:
            count += 1
            allowed_steps.append([1,0])
        if M[s1-1][s2] == 0:
            count += 1
            allowed_steps.append([-1,0])
        if M[s1][s2+1] == 0:
            count += 1
            allowed_steps.append([0,1])
        if M[s1][s2-1] == 0:
            count +=1
            allowed_steps.append([0,-1])
        if len(allowed_steps) == 0:
            weights.append(0)
            break

        weight = weight*count
        krok = random.choice(allowed_steps) #sample next step
        s1 += krok[0]
        s2 += krok[1] #update state
        M[s1][s2] = 1 #mark current state as visited
    weights.append(weight) 

#calculate estimator
E = np.mean(weights)
print("|SAW|=", E)

#calculate standard deviation of simulation
std = np.std(weights, ddof=1)
print("standard deviation:", std)


