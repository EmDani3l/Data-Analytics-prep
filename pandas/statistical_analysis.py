import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datasets/titanic.csv")

# Mean vs Median
print(df["Fare"].mean())    # 32.20
print(df["Fare"].median())  # 14.45

# Visualising outliers
sns.boxplot(x=df["Fare"])
plt.show()

# If most passengers paid between 10-50 but a few paid >500, then Mean gets pulled upward while Median stays more stable

# MINI INVESTIGATION
# Try answering:

# Hypothesis 1
# Women were more likely to survive.
# Evidence?

df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()
# Survival rate of females was >0.7 while that of males was <0.2. This means if you were a woman, you were more likely to survive.

# More formal: Female passengers had a survival rate exceeding 70%, while male passengers had a survival rate below 20%. This suggests that gender was strongly associated with survival outcomes.

# Hypothesis 2
# Higher-class passengers were more likely to survive.
# Evidence?

df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()
# The survival rate decreased when progressing from the highest to lowest class. Class 1 passengers had a rate of 0.63, Class 2 had 0.47, Class 3 had 0.24
# Hence, higher class passengers were more likely to survive.

# Stronger version: Survival rates decreased consistently from first class to third class, indicating a strong relationship between passenger class and survival probability.

# Hypothesis 3
# People paying higher fares were more likely to survive.
# Evidence?

surivor_fares = df.groupby("Survived")["Fare"].mean()
print(f"Fares paid by survivors:\n{surivor_fares}")
# Higher fares corresponds to a higher passenger class, and we know that generally passengers in a higher class had a much greater chance of survival. Therefore, we may conclude that fare acts as a proxy for passenger class, which determines how likely one was to be a survivor. Since we know from above that higher class passengers were more likely to survive, we can then also conclude that those who paid higher fares were also more likely to survive.