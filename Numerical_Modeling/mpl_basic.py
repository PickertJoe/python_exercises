# Creating basic plots using matplotlib

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

# Adjusting the line width and adding features to the plot
plt.plot(squares, linewidth=3)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()

# Correcting offset of square values
x_values = [1, 2, 3, 4, 5]
plt.plot(x_values, squares, linewidth=3)
plt.title("Corrected Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
