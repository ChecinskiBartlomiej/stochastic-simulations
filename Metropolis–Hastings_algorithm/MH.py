import math
import random
import numpy as np
import matplotlib.pyplot as plt
b = 1
m = 0
v = 1

def gestosc_normalna(x):
    c = math.sqrt(2*math.pi)*v #norming constant
    w = -(x-m)**2/(2*v**2)     #exponent
    return math.exp(w)/c

def a(x, y):
    return min(1, gestosc_normalna(y)/gestosc_normalna(x))

def MH_step(x):
    y = random.uniform(x-b, x+b)
    u = random.uniform(0, 1)
    if u <= a(x, y):
        z = y
    else:
        z = x
    return z

def MH_simulation(burn, steps): #burn parameter specifies how many initial samples we reject because MC is far from desired distribution
    x = 0
    MH = []
    for j in range(burn+steps):
        x = MH_step(x)
        if j >= burn:
            MH.append(x)
    return MH

def plot_histogram(MH):
    plt.hist(MH, bins=50)      
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

def estimate_sigma_sq_as(burn, steps):
    chain = MH_simulation(burn, steps)
    m = int(np.floor(np.sqrt(steps)))  
    k = steps // m                      
    block_means = [sum(chain[i*m:(i+1)*m])/m for i in range(k)]
    overall_mean = sum(chain[:k*m])/(k*m)
    sigma_sq_as = (m / k) * sum((bm - overall_mean)**2 for bm in block_means)
    return sigma_sq_as

burn = 100000
steps = 1000000
MH = MH_simulation(burn, steps)
plot_histogram(MH)
print(estimate_sigma_sq_as(burn, steps))




    