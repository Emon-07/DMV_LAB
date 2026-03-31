import matplotlib.pyplot as plt

# 1. Enable interactive mode
plt.ion()

labels = []
sizes = []

fig, ax = plt.subplots()

print("Enter Data (e.g., 'Rent 500'). Type 'stop' to finish.")

while True:
    user_input = input("Enter Category and Value: ")
    
    if user_input.lower() == 'stop':
        break
    
    try:
        # Split input into name and number
        parts = user_input.split()
        name = parts[0]
        val = float(parts[1])
        
        labels.append(name)
        sizes.append(val)
        
        # 2. Clear and redraw the pie chart
        ax.clear()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Keep it a circle
        
        plt.title("User-Driven Pie Chart")
        
        # 3. Refresh the window
        plt.draw()
        plt.pause(0.1)
        
    except (ValueError, IndexError):
        print("Format error! Use: Name Number (e.g., Food 100)")

# Turn off interactive mode and keep the final window open
plt.ioff()
plt.show()