import matplotlib.pyplot as plt

# Data
labels = ['Rent', 'Food', 'Transport', 'Savings']
sizes = [40, 30, 15, 15]

# Create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Ensure the pie is drawn as a circle
plt.axis('equal')  
plt.title('Monthly Expenses')

# Show the plot
plt.show()