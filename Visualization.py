import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# Define data for planets
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
semi_major_axis = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05]  # in AU (astronomical units)
orbit_period = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]  # in years


plt.style.use('dark_background')
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the Sun at the center
ax.scatter(0, 0, color='yellow', s=100, label='Sun')

# Plot orbits of planets
for i, planet in enumerate(planet_names):
    orbit_radius = semi_major_axis[i]
    orbit_theta = np.linspace(0, 2*np.pi, 100)
    x = orbit_radius * np.cos(orbit_theta)
    y = orbit_radius * np.sin(orbit_theta)
    ax.plot(x, y, label=planet)

# Set aspect ratio to equal, and add labels
ax.set_aspect('equal', 'box')
ax.set_xlabel('Distance (AU)')
ax.set_ylabel('Distance (AU)')
ax.set_title('Solar System')
ax.legend()

plt.grid(True)
plt.show()


# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the Sun
ax.scatter(0, 0, 0, color='yellow', s=100, label='Sun')

# Plot orbits
for i, planet in enumerate(planet_names):
    orbital_radius = semi_major_axis[i]
    orbit_theta = np.linspace(0, 2*np.pi, 100)

    x = orbital_radius * np.cos(orbit_theta)
    y = orbital_radius * np.sin(orbit_theta)
    z = np.zeros_like(x)

    ax.plot(x, y, z, label=planet)

# Labels and title
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('3D Solar System')

# Legend
ax.legend()

# Show plot
plt.show()