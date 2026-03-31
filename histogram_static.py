import matplotlib.pyplot as plt
import numpy as np

# 1. Generate random data (1000 numbers following a normal distribution)
data = np.random.randn(1000)

# 2. Create the histogram
# bins=20 means the data is divided into 20 bars
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# 3. Add labels and title
plt.title("Simple Static Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency (Count)")

# 4. Show the plot
plt.show()