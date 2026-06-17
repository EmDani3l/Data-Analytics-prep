import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datasets/titanic.csv")

# 1. Class 1 seems safest
class_survival = df.groupby("Pclass")["Survived"].mean()
print(f"Survival rate by class:\n{class_survival}")

# Pclass
# 1    0.63
# 2    0.47
# 3    0.24

# Now write down:
# How much more likely was a first-class passenger to survive compared to a third-class passenger?
# a first class passenger would have nearly a 2/3 chance of survival whereas a third class passenger has less than a quarter


# 2. Were survivors older or younger on average?
age_survival = df.groupby("Survived")["Age"].mean()
print(f"Survival rate by age:\n{age_survival}")

# Survived
# 0    30.626179
# 1    28.343690
# survivors were younger on average


# 3. Did survivors generally pay higher fares?
surivor_fares = df.groupby("Survived")["Fare"].mean()
print(f"Fares paid by survivors:\n{surivor_fares}")

# Survived
# 0    22.117887
# 1    48.395408
# yes, survivors paid more

# What might that suggest?
# Higher fares corresponds to a higher passenger class, and we know that generally passengers in a higher class had a much greater chance of survival. Therefore, we may conclude that fare acts as a proxy for passenger class, which determines how likely one was to be a survivor.