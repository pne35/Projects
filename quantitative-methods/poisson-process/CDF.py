import numpy as np
import matplotlib.pyplot as plt

lam = int(input("Enter your rate: "))
t = int(input("Enter the timeframe in which you want to determine the probability an event has happened: "))
theo = 1 - np.exp(-lam * t)
print(f"The probability an event has happened is {theo}")
# Made this code throughouly by myself. Simple code, implementing the equation 1-e^lam*t. The later lines I implement a way to calculate it against the actual probability from a simulation.

import numpy as np
import matplotlib.pyplot as plt
from PoissonProcessSim import plot

lam = int(input("Enter your rate: "))
t = float(input("Enter the timeframe in which you want to determine the probability an event has happened (hours): "))
theo = 1 - np.exp(-lam * t)
print(f"The probability an event has happened is {theo}")

emp = plot(lam,10000,t)
print(f"The probability an event happened in a simulation ran with rate {lam} is {emp}")
# I made a few user inferface upgrades and implementated the probabilty ran through a simulation (other script). 
