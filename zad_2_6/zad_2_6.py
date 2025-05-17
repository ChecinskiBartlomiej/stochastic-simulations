#By theoretical calculations X_inf = N(0,v^2/(1-alpha^2)) and X_n|x = N(alpha^n*x,v^2(1-alpha^(2n))/(1-alpha^2))

import random
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.9
v = 1
n = 1000000
burn = 900000
sigma2 = v**2 / (1 - alpha**2)

def step(x, alpha, v):
    w = random.gauss(0, v)
    return alpha*x+w

def trajectory(x):
    trajectory = []
    for j in range(n):
        x = step(x, alpha, v)
        trajectory.append(x)
    return trajectory

def plot_trajectory(trajectory):
    n_list = np.arange(1, n+1)
    plt.plot(n_list, trajectory)
    plt.show()

def plot_histogram(samples):
    plt.figure()
    plt.hist(samples, bins=50, density=True)
    counts, bins = np.histogram(samples, bins=100, density=True) #we do not need counts
    bin_centers = (bins[:-1] + bins[1:]) / 2
    plt.plot(bin_centers, 1/np.sqrt(2*np.pi*sigma2) * np.exp(-bin_centers**2/(2*sigma2))) #plot theoretical density
    plt.show()

#trajectory, starting from x=0
x = 0
traj1 = trajectory(x)
plot_trajectory(traj1) #for trajectory to be visible try smaller n

#trajectory, starting from sampled from stationary distribution point
x = random.gauss(0, np.sqrt(sigma2))
traj2 = trajectory(x)
plot_trajectory(traj2)

#plot histogram using only one trajectory
samples = traj1[burn:]
plot_histogram(samples) #for histogram to be good approximation of density try bigger n
    




