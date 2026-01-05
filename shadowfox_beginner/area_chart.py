import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y1 = [3, 4, 6, 8, 9]
y2 = [1, 2, 3, 4, 5]

plt.stackplot(x, y1, y2, labels=["Group 1", "Group 2"])
plt.legend(loc="upper left")
plt.title("Stacked Area Chart Example")
plt.show()
