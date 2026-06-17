import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datasets/titanic.csv")

df["Sex"].value_counts().plot(kind="bar")
plt.title("Passenger Gender Distribution")
plt.show()

# ================================================================

df["Pclass"].value_counts().sort_index().plot(kind="bar")
plt.title("Passengers by Class")
plt.show()

# ================================================================

df["Age"].hist(bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()

# ================================================================

df.groupby("Sex")["Survived"].mean().plot(kind="bar") # sex (x axis) against survival rate (y axis, given by mean, which gives sum of 1s divided by number)
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()

# ================================================================

df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()

# ================================================================

numeric_df = df.select_dtypes(include=["number"])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()