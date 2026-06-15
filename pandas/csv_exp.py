import pandas as pd
import numpy as np

df = pd.read_csv("datasets/titanic.csv")
print(df.head())

# Question: What does head() show?
# first 5 rows of data in a dataset (default value)

print(df.shape)
# # (891, 12) --> (rows, columns)
print()

print(df.columns)
# List of column names
print()

df.info()
# Information (WOW WHO COULD HAVE GUESSED) about the columns and types of data
print()

print(df.describe())
# summary statistics of data for numerical data
print()

print(df.isna().sum())
# number of missing values for each column

# # Questions
# 1. How many passengers are there?

print(df.shape) # number of rows = number of passenger IDs = number of passengers

# 2. How many survived?

survival = df["Survived"].value_counts()
print(survival) # 0: 549, 1: 342

# 3. What is the average age?

average_age = df["Age"].mean()
print(f"{average_age:.2f}") # 29.70

# 4. What is the oldest passenger age?

oldest = df["Age"].max()
print(oldest) # 80.0

# 5. How many males and females?

gender_dist = df["Sex"].value_counts()
print(gender_dist) # male 577, female 314