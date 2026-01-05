import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Plot Example")
plt.show()
categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.show()
data = np.random.randn(100)
plt.hist(data, bins=10)
plt.title("Histogram Example")
plt.show()
x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 7, 6]

plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.show()
sizes = [40, 30, 20, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Seaborn Scatter Plot")
plt.show()
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Seaborn Bar Plot")
plt.show()
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Seaborn Box Plot")
plt.show()
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Heatmap")
plt.show()

