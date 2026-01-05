import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load sample dataset
tips = sns.load_dataset("tips")

# -------------------------------
# 1. SEABORN SCATTER PLOT
# -------------------------------
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Seaborn Scatter Plot")
plt.savefig("seaborn_scatter.png")
plt.show()

# -------------------------------
# 2. SEABORN LINE PLOT
# -------------------------------
sns.lineplot(x="size", y="tip", data=tips)
plt.title("Seaborn Line Plot")
plt.savefig("seaborn_line.png")
plt.show()

# -------------------------------
# 3. SEABORN BAR PLOT
# -------------------------------
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Seaborn Bar Plot")
plt.savefig("seaborn_bar.png")
plt.show()

# -------------------------------
# 4. SEABORN COUNT PLOT
# -------------------------------
sns.countplot(x="day", data=tips)
plt.title("Seaborn Count Plot")
plt.savefig("seaborn_count.png")
plt.show()

# -------------------------------
# 5. SEABORN BOX PLOT
# -------------------------------
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Seaborn Box Plot")
plt.savefig("seaborn_box.png")
plt.show()

# -------------------------------
# 6. SEABORN HISTOGRAM
# -------------------------------
sns.histplot(tips["total_bill"], bins=10)
plt.title("Seaborn Histogram")
plt.savefig("seaborn_histogram.png")
plt.show()

# -------------------------------
# 7. SEABORN KDE PLOT
# -------------------------------
sns.kdeplot(tips["total_bill"], fill=True)
plt.title("Seaborn KDE Plot")
plt.savefig("seaborn_kde.png")
plt.show()

# -------------------------------
# 8. SEABORN HEATMAP
# -------------------------------
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Seaborn Heatmap")
plt.savefig("seaborn_heatmap.png")
plt.show()

# -------------------------------
# 9. SEABORN REGRESSION PLOT
# -------------------------------
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("Seaborn Regression Plot")
plt.savefig("seaborn_regplot.png")
plt.show()

# -------------------------------
# 10. AREA CHART (MATPLOTLIB)
# -------------------------------
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

plt.fill_between(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Area Chart Example")
plt.savefig("area_chart.png")
plt.show()
