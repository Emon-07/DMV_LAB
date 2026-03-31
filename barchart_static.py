import matplotlib.pyplot as plt

# Data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 40, 15, 30]

# Create bars
plt.bar(categories, values, color='skyblue', edgecolor='navy')

# Customization
plt.title('Fruit Inventory')
plt.xlabel('Fruit Type')
plt.show()