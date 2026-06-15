import pandas as pd
import numpy as np

df = pd.read_csv("datasets/titanic.csv")

# Task 1: Find the oldest passengers

oldest_passengers = df.sort_values("Age", ascending = False).head(10) # --descending order of age
print(oldest_passengers)

print()

youngest_passengers = df.sort_values("Age", ascending = True).head(10) # -- ascending order of age
print(youngest_passengers)

print()

# Task 2: Find the 10 passengers who paid the highest fare

highest_payers = df.sort_values("Fare", ascending=False).head(10)
print(highest_payers)

print()

# Task 3: Find the youngest passenger

youngest = df.sort_values("Age", ascending = True).head(1)
print(youngest)