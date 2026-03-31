import matplotlib.pyplot as plt

# Data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Create scatter plot
plt.scatter(x, y, color='hotpink')

# Labels and Title
plt.title('Car Age vs Speed')
plt.xlabel('Age of Car')
plt.ylabel('Speed')

# Show plot
plt.show()