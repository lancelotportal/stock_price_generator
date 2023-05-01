from random import gauss, seed
from math import sqrt, exp
import matplotlib.pyplot as plt
import numpy as np

## Values used

N = 5 * 365 #The number of iterations
mu_value = 0.1 #Excepted annual return
sigma_value = 0.05 #Value used to perfom the normal law
u0 = 60 #initial price

## Function

def GBM(ut, mu, sigma):

    ut *= exp((mu - 0.5 * sigma ** 2) * (1/365) + sigma* sqrt(1/365) * gauss(mu=0, sigma=1))

    return ut

## Program

ut = GBM(ut, mu, sigma)

tab = [[],[],[],[],[],[],[],[],[],[]] #To do multiple simulation

# Multiple simulation
for k in range(0,1):

    #For each simulation, we set the initial stock price to u0
    ut = u0
    mu = mu_value
    sigma = sigma_value

    for i in range(N):

        if (i % 200 == 0):

            #Because we randomly increase or decreae mu and sigma value, we must set them back
            #to their initial value in order to keep the simulation interesting
            mu = mu_value
            sigma = sigma_value

        #randomly increase or decrease mu and sigma value (so each simulation is different)
        mu *= np.random.uniform(low=0.9, high=1.1)
        sigma *= np.random.uniform(low=0.9, high=1.1)
        ut = GBM(ut, mu, sigma)
        tab[k].append(ut)


tab_x = np.linspace(0,N,N)

for k in range(0,1):
    plt.plot(tab_x, tab[k])

plt.show()