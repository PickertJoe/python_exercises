# Generates a simple scatterplot of cubic numbers using a colormap gradient

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples,
            edgecolor='none', s=20)

plt.xlabel("Cubic Root", fontsize=14)
plt.ylabel("Cube", fontsize=14)
plt.title("Cubic Values with Colormap", fontsize=24)
plt.tick_params(axis='both', labelsize=14)

plt.show()
