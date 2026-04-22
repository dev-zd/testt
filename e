# Define points
xpoints = np.array([10, 20, 70, 200])
ypoints = np.array([20, 30, 150, 200])

# Plot line with markers
plt.plot(xpoints, ypoints, marker='o')

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot")

# Show grid
plt.grid()

# Display graph
plt.show()