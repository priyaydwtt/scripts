# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

#numpy is a multidimensional array

# Prepare the data
x = np.linspace(0, 10, 10)
y = np.linspace(10,20,10)



# Plot the data
plt.plot(x, x, label='linear')
plt.plot(x,y,label='linear1')


# Add a legend
plt.legend("x axis")

# Show the plot
plt.show()