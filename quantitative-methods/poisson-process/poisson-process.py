import numpy as np
import matplotlib.pyplot as plt

def plot(lam, n):
    lam = lam              # rate λ = 3 per hour
    n = n           # number of samples

    # Step 1: simulate exponential waiting times
    samples = np.random.exponential(scale=1/lam, size=n)

    # Step 2: histogram of simulated data
    plt.hist(samples, bins=100, density=True)

    # Theoretical density curve
    x = np.linspace(0, np.max(samples), 300)
    pdf = lam * np.exp(-lam * x)
    plt.plot(x, pdf)

    plt.xlabel("Waiting time (hours)")
    plt.ylabel("Density")
    plt.title(f"Exponential Distribution Simulation (λ = {lam})")
    plt.show()


print("This program will you show how the probability of an event occuring over a period of time is exponential. It also shows that as you increase the amount of samples the curve is smoother.")
lam = int(input("What is your rate: "))
for count in range(10):
    n = int(input("How much samples do you want to run: "))
    plot(lam, n)

# First project so yes I did use help. However I fully understand the code and implemented myself the final touch of the loop and the function. In my next snippet I will implement a probability for wether an event has happened after a certain time.
