
import random
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.9 
beta = 0.4
n = 100 #number of steps

def step(x):
    if x == 1:
        if random.uniform(0,1) < 1 - alpha:
            return 1
        else:
            return 2
    if x == 2:
        if random.uniform(0,1) < beta:
            return 1
        else:
            return 2
        
def trajectory(x):
    trajectory = []
    for j in range(n):
        x = step(x)
        trajectory.append(x)
    return trajectory

def plot_trajectory(trajectory):
    n_list = np.arange(1, n+1)
    plt.plot(n_list, trajectory)
    plt.show()

#calculate stationary distribution
def calculate_pi(x):
    traj = trajectory(x)
    traj1 = [z for z in traj if z==1]
    traj2 = [z for z in traj if z==2]
    pi1 = len(traj1)/n
    pi2 = len(traj2)/n
    return (pi1, pi2)

#start from deterministic point
x = 1
traj1 = trajectory(x)
plot_trajectory(traj1)
print(calculate_pi(x))

#sample starting point from stationary distribution
pi1 = beta/(alpha+beta)
pi2 = alpha/(alpha+beta)
if random.uniform(0, 1) < pi1:
    x = 1
else:
    x = 2
traj2 = trajectory(x)
plot_trajectory(traj2)