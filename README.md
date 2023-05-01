# Generate Stock Price using Python and Brownian Motion
## Introduction

Brownian motion is a mathematical model that describes the random movement of particles in a fluid. In finance, it can be used to simulate the random fluctuations of stock prices. In a Brownian motion model, stock price changes are modeled as random movements, with the size and direction of each movement determined by a random variable. The movement of the stock price is assumed to be continuous and independent of past movements, and the variance of the random variable is proportional to the time interval between measurements. By simulating these random movements over time, you can generate a synthetic stock price that mimics the behavior of a real stock price.

## Generating Brownian Motion

We assume returns are normally distributed, meaning average returns tend to be $\mu$, and standard deviation tends to be $\sigma$.

To change the stock price at each iteration (i.e., each day), we multiply the price from the previous day by:

$$
\frac{1}{365}e^{(\mu-\frac{1}{2}\sigma^{2})} + \sigma\sqrt{\frac{1}{365}}N(0,1)
$$

We add a standard normal law to simulate a random return each day.

## Adjusting the $\mu$ and $\sigma$ Values

To ensure that the simulation is coherent, we must adjust the values of the average return and standard deviation. We can do this by running multiple simulations with different initial values of $\mu$ and $\sigma$ to find the best values. Alternatively, we can use real data to find appropriate values. Typically, a stock returns around 5-10% per year with a standard deviation of around 5%.

## Results

After adjusting all the values, we obtain interesting results. However, when annual return is too high (around 10%), the stock tend to increase constantly. The variations aren't real.

## Possible Upgrades

One way to upgrade the simulation is to incorporate the fact that the annual return changes each year. We can randomize $\mu$ in a different way than just multiplying it by a uniform law.

Secondly, we could integrate a notion of "news" or "annual result" of the company, where each news item could have an effect on the stock price.
