import matplotlib.pyplot as plt

# 1. Turn on interactive mode
plt.ion()
fig, ax = plt.subplots()

x_data = []
y_data = []
line, = ax.plot(x_data, y_data, 'b-o') # 'b-o' means blue line with dots

print("Enter numbers to plot (type 'exit' to stop):")

count = 0
while True:
    user_input = input(f"Value for point {count}: ")
    
    if user_input.lower() == 'exit':
        break
    
    try:
        val = float(user_input)
        
        # 2. Update data lists
        x_data.append(count)
        y_data.append(val)
        
        # 3. Update the line on the graph
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        
        # 4. Rescale the axes so the new data fits
        ax.relim()
        ax.autoscale_view()
        
        # 5. Draw the update
        plt.draw()
        plt.pause(0.1)
        
        count += 1
    except ValueError:
        print("Please enter a valid number.")

print("Graph finished.")
plt.ioff() # Turn off interactive mode
plt.show() # Keep the final graph open