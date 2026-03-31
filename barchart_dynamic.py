import matplotlib.pyplot as plt

# 1. Enable interactive mode
plt.ion()

categories = []
values = []

fig, ax = plt.subplots()

print("Enter Data (e.g., 'Apples 10'). Type 'stop' to finish.")

while True:
    user_input = input("Enter Category and Value: ")
    
    if user_input.lower() == 'stop':
        break
    
    try:
        # Split input into name and number
        parts = user_input.split()
        name = parts[0]
        val = float(parts[1])
        
        categories.append(name)
        values.append(val)
        
        # 2. Clear and redraw the bar chart
        ax.clear()
        ax.bar(categories, values, color='skyblue', edgecolor='navy')
        
        # Add labels back after clearing
        ax.set_title("User-Driven Bar Chart")
        ax.set_ylabel("Quantity")
        
        # 3. Refresh the window
        plt.draw()
        plt.pause(0.1)
        
    except (ValueError, IndexError):
        print("Format error! Use: Name Number (e.g., Mango 5)")

plt.ioff()
plt.show()