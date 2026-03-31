import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 45, 52]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Growth')

# Customization
plt.title("Static Growth Trend")
plt.xlabel("Time (Days)")
plt.ylabel("Value")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show the plot
plt.show()