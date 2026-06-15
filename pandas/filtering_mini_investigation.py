import pandas as pd
import numpy as np

df = pd.read_csv("datasets/titanic.csv")

# A
# How many passengers were:
# Female
# Survived

female_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(f"\n The number of passengers who were female and survived is: {len(female_survivors)}")

# B
# How many passengers were:
# Male
# Older than 60

older_males = df[(df["Sex"] == "male") & (df["Age"] > 60)]
print(f"\n The number of passengers who were male and older than 60 is: {len(older_males)}")


# C
# What were the 5 highest fares paid?

high_fares = df.sort_values("Fare", ascending=False)["Fare"].head(5).tolist()
print(f"\n The 5 highest fares paid were:{high_fares}")

# D
# Which passenger class had the most people?

popular_class = df["Pclass"].value_counts().idxmax()
print(f"\n The passenger class with the most people was: {popular_class}")