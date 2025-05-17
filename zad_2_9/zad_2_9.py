#By theoretical calculations stationary distribution is Beta(1-a,a)

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


x = 0.5 #starting point
a = 0.3
n = 1000000 #length of trajectory
burn = 900000 #forget first burn points of trajectory

def step(x):
    if random.uniform(0,1) < a:
        return random.uniform(0,x)
    else:
        return random.uniform(x,1)
    
def trajectory(x):
    traj = []
    for j in range(n):
        x = step(x)
        traj.append(x)
    return traj

def plot_trajectory(trajectory):
    n_list = np.arange(1, n+1)
    plt.plot(n_list, trajectory)
    plt.show()

def plot_histogram_with_beta(trajectory):
    data = trajectory[burn:]  
    plt.hist(data, bins=30, density=True)
    bins = np.linspace(0, 1, 100)
    pdf_beta = beta.pdf(bins, 1-a, a)
    plt.plot(bins, pdf_beta)
    plt.xlabel("x")
    plt.ylabel("density")
    plt.title(f"Histogram and beta(1-a,a) density")
    plt.show()

traj = trajectory(x)
plot_trajectory(traj)
plot_histogram_with_beta(traj)
