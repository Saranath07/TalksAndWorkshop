import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axis
fig, ax = plt.subplots()

# Generate an imperfect circle
theta = np.linspace(0, 2 * np.pi, 500)
r = 1 + 0 * np.random.randn(500)  # Adding some randomness to the radius
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the imperfect circle
ax.plot(x, y, color="black")
ax.set_aspect('equal')  # Ensure the aspect ratio is equal to make the plot circular

# Hide the axes
ax.axis('off')

plt.savefig("circle.png")

plt.show()
