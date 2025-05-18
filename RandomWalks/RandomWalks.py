import random
import matplotlib.pyplot as plt
import numpy as np

#step function for absorbing case
def step_absorbing(x, p, k):
    if x == 0 or x == k:
        return x
    else:
        if random.uniform(0,1) < p:
            return x + 1
        else:
            return x - 1

#step function for elastic case
def step_elastic(x, p, k):
    if random.uniform(0,1) < p:
        return min(x+1, k)
    else:
        return max(x-1, 0)

#function for simulation of absorbing case
def trajectory_absorbing(x, n):
    traj_absorbing = []
    traj_absorbing.append(x)
    for j in range(n):
        x = step_absorbing(x, p, k)
        traj_absorbing.append(x)
    return traj_absorbing

#function for simulation of elastic state
def trajectory_elastic(x, n):
    traj_elastic = []
    traj_elastic.append(x)
    for j in range(n):
        x = step_elastic(x, p, k)
        traj_elastic.append(x)
    return traj_elastic

#function for plotting trajectory
def plot_trajectory(trajectory):
    n_list = np.arange(n+1)
    plt.plot(n_list, trajectory)
    plt.show()

#parameters
k = 20
p = 0.4
q = 1 - p
x = 10
n = 1000

traj_absorbing = trajectory_absorbing(x, n)
plot_trajectory(traj_absorbing)
traj_elastic = trajectory_elastic(x, n)
plot_trajectory(traj_elastic)

#now I will compute empirically p_k = P(exist n: X_n=k|X_0=x_0) and P(exist n: X_n=0|X_0=x_0) = 1 - P(exist n: X_n=k|X_0=x_0). Theoretical computation show that for p != 1/2 
#p_k = (1-(q/p)^x_0)/(1-(q/p)^k) and for p = 1/2 p_k = x_0/k
#perform m simulations untill barier is reached, count how many times 0 or k is absorbing state
m = 1000000
k_is_absorbing = 0
zero_is_absorbing = 0
for i in range(m):
    x = 10
    for j in range(n):
        x = step_absorbing(x, p, k)
        if x == k:
            k_is_absorbing += 1
            break
        elif x == 0:
            zero_is_absorbing += 1
            break

p_k = k_is_absorbing/m
p_0 = zero_is_absorbing/m
print(p_k)
print(p_0)
#agrees with theory

#now I will compute empirically pi(x), I will generate one long trajectory, consider only tail of trajectory by burning the begining and use ergodic theorem for markov chains
N = 10000000
burn = int(0.9 * N)
x = 10
traj_elastic = trajectory_elastic(x, N)
tail = traj_elastic[burn:]
total = len(tail)
counts = [0] * (k+1)          
for state in tail:
    counts[state] += 1
pi_emp = {state : counts[state]/total for state in range(k+1)}
for state in range(k+1):
    print(f"π_emp({state}) = {pi_emp[state]:.4f}")   
#agrees with theory