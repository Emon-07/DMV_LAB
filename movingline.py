import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 1. Setup the figure and data
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# 2. Function that updates the line for every frame
def update(frame):
    # Shift the sine wave by 'frame' amount
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

# 3. Create the animation
# interval=20 means 20 milliseconds between frames (very smooth)
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.title("Moving Sine Wave")
plt.show()