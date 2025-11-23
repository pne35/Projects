import numpy as np
import matplotlib.pyplot as plt

def simulate_poisson_process(lam, T):
    waiting_times = np.random.exponential(scale=1/lam, size=10000)

    arrival_times = np.cumsum(waiting_times)

    arrival_times = arrival_times[arrival_times <= T]

    N_t = np.arange(1, len(arrival_times) + 1)

    plt.step(arrival_times, N_t, where='post')
    plt.xlabel("Time")
    plt.ylabel("N(t)")
    plt.title(f"Poisson Process Sample Path (λ = {lam})")
    plt.show()

    return arrival_times

lam = 5
T = 5       
waiting_times = simulate_poisson_process(lam, T)

#Here I wrote a program to simulate the times at which poisson events occur during the process and graph them.
