# Import matplotlib library
import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a new figure
plt.figure()

# Plot the data
plt.plot(x, y, label='Example plot')

# Set the labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Basic Matplotlib Plot')

# Show legend
plt.legend()

# Display the plot
plt.show()
