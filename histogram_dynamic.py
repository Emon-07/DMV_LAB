import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  # Turn on interactive mode

data = []

for i in range(20):
    # Add new random data
    new_values = np.random.randn(100)
    data.extend(new_values)

    plt.clf()  # Clear previous plot
    plt.hist(data, bins=20)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Dynamic Histogram")

    plt.pause(1)  # Pause for 1 second

plt.ioff()
plt.show()