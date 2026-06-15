import pandas as pd
import numpy as np

df = pd.read_csv("datasets/titanic.csv")

# Task 4: Find all female passengers

females = df[df["Sex"] == "female"]
print(females)

print()

# Task 5: Find all female survivors

female_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(female_survivors)

print()

# Task 6: How many female survivors?

print(len(female_survivors))

print()

# Task 7: Find male passengers older than 50

old_males = df[(df["Sex"] == "male") & (df["Age"] > 50)]
print(old_males)

print()

# ====== VALUE COUNTS ======

# Task 8: Count males vs females

df["Sex"].value_counts()

# Task 9: Count passengers by class

class_counts = df["Pclass"].value_counts()
print(class_counts)

print()

# Pclass
# 3    491  <-- Highest number of passengers in this class
# 1    216
# 2    184
# Name: count, dtype: int64

# Task 10: Count embarkation locations

embark_locs = df["Embarked"].value_counts()
print(embark_locs)
print()
# Embarked
# S    644   <-- Appears the most often
# C    168
# Q     77
# Name: count, dtype: int64

for i in (1, 4):
  print()

print("===============================")
