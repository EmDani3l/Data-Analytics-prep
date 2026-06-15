import pandas as pd
import numpy as np

df = pd.read_csv("datasets/titanic.csv")

# Task 1
# What was the survival rate for men versus women?

print(df.groupby("Sex")["Survived"].mean())
# Sex
# female    0.742038
# male      0.188908
# Name: Survived, dtype: float64

# 74.2% of women and 18.9% of men survived

print()

# Task 2
# Find average age by gender

print(df.groupby("Sex")["Age"].mean())
# Sex
# female    27.915709
# male      30.726645    (males are older on average)
# Name: Age, dtype: float64

print()

# Task 3
# Find passenger counts by class

print(df["Pclass"].value_counts())

# Pclass
# 3    491 -- most
# 1    216
# 2    184
# Name: count, dtype: int64

print()

# Task 4
# Find survival rate by passenger class

print(df.groupby("Pclass")["Survived"].mean())

# Pclass
# 1    0.629630 -- highest survival rate
# 2    0.472826
# 3    0.242363
# Name: Survived, dtype: float64

print()

# Mini Challenge
# What was the average fare paid by passengers in each class?

print(df.groupby("Pclass")["Fare"].mean())

# Pclass
# 1    84.154687
# 2    20.662183
# 3    13.675550
# Name: Fare, dtype: float64
