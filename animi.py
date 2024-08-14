import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and an axis
fig, ax = plt.subplots()

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Define the petal shape
theta = np.linspace(0, 2 * np.pi, 100)
r = 1 + 0.3 * np.sin(6 * theta)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Initialize the plot
flower, = ax.plot(x, y)

# Animation function
def animate(i):
    # Rotate the flower by changing the angle
    angle = np.radians(i)
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)
    
    flower.set_data(x_rot, y_rot)
    return flower,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)

# Set plot limits
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Hide the axes
ax.axis('off')

# Show the animation
plt.show()