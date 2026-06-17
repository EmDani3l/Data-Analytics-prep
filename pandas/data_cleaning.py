import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datasets/titanic.csv")

print(df.shape)             # (891, 12)
print(df["Age"].mean())     # 29.70
print()
print(df["Age"].median())   # 28.00

print("\nDropped na ages\n")

age_dropped = df.dropna(subset=["Age"])
print(age_dropped.shape)    # (714, 12) ---> 177 rows dropped

clean_df = df.copy()
clean_df["Age"] = clean_df["Age"].fillna(clean_df["Age"].median())
print(clean_df["Age"].isna().sum()) # 0 (no more empty/missing values)