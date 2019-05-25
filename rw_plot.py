# A program to create several scatter plots of the random walk class

import matplotlib.pyplot as plt
from random_walk import Random_Walk

# Generating a new random walk for use in plotting
rw = Random_Walk()
rw.fill_walk()

plt.scatter(rw.x_location, rw.y_location, s=10)
plt.show()

# Creating a colormap that darkens as the steps progress

step_list = list(range(rw.steps))
plt.scatter(rw.x_location, rw.y_location, c=step_list, cmap=plt.cm.Purples,
            edgecolor='none', s=10)
plt.show()

# Making the start(green) and end(red) points more visible
plt.scatter(rw.x_location, rw.y_location, c=step_list, cmap=plt.cm.Purples,
            edgecolor='none', s=10)
plt.scatter(0, 0, color='green', s=30)
plt.scatter(rw.x_location[-1], rw.y_location[-1], color='red', s=30)
plt.show()
