import matplotlib.pyplot as plt

# 1. Enable interactive mode
plt.ion()

x_values = []
y_values = []

fig, ax = plt.subplots()

print("Enter coordinates (e.g., '5 10'). Type 'stop' to finish.")

while True:
    user_input = input("Enter X and Y: ")
    
    if user_input.lower() == 'stop':
        break
    
    try:
        # Split input into X and Y coordinates
        parts = user_input.split()
        x_val = float(parts[0])
        y_val = float(parts[1])
        
        x_values.append(x_val)
        y_values.append(y_val)
        
        # 2. Clear and redraw the scatter plot
        ax.clear()
        ax.scatter(x_values, y_values, color='purple', s=100, edgecolor='black')
        
        # Re-add labels after clearing
        ax.set_title("User-Driven Scatter Plot")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.grid(True, linestyle='--', alpha=0.6)
        
        # 3. Refresh the window
        plt.draw()
        plt.pause(0.1)
        
    except (ValueError, IndexError):
        print("Format error! Use: X Y (e.g., 5 10.5)")

# Keep the final window open
plt.ioff()
plt.show()