import pandas as pd

feedback = pd.DataFrame({
    "Comment": [
        "The service was excellent",
        "The app crashes frequently",
        "Customer support was helpful",
        "Very slow response time",
        "I love the new update",
        "The website is confusing",
        "Excellent customer service",
        "The app is terrible"
    ]
})

print(feedback)
print()

# Convert to lowercase
feedback["Comment_Lower"] = feedback["Comment"].str.lower()
print(feedback)
print()

# Find comments containing a word
app_comments = feedback[feedback["Comment_Lower"].str.contains("app")]
print("Comments containing the word \"app\"\n")
print(app_comments)
print()

excellent_comments = feedback[feedback["Comment_Lower"].str.contains("excellent")]
print("Comments containing the word \"excellent\"\n")
print(excellent_comments)
print()

# Simple category: How many comments mention performance issues?
feedback["Performance Issues"] = feedback["Comment_Lower"].str.contains("slow|crashes")
print("Comments mentioning performance issues\n")
print(feedback)
print(feedback["Performance Issues"].value_counts()) # 6 False, 2 true

# ========================== MINI TASK ================================

# 1. How many comments mention: 
# - app
# - support
# - service

# app_comments = feedback[feedback["Comment_Lower"].str.contains("app")]
# print("Comments containing the word \"app\"\n")
# print(app_comments)
# num_app = len(app_comments)
# print(f"\nThe number of comments mentioning app is {num_app}")

app_count = feedback["Comment_Lower"].str.contains("app").sum()
print(f"\nThe number of comments mentioning app is {app_count}\n")

# 2. How many performance issues were detected?

feedback["Performance Issues"] = feedback["Comment_Lower"].str.contains("slow|crashes")
print("Comments mentioning performance issues\n")
print(feedback)
print(feedback["Performance Issues"].value_counts())
num_issues = feedback["Performance Issues"].sum()
print(f"\nThere were {num_issues} performance issues detected")


# 3. Why is converting to lowercase useful?

# converting to lowercase helps because we are able to account for words being partially/fully capitalised when trying to do things like searching based on exact word spelling so nothing is missed out

# Converting text to lowercase standardizes the data and prevents words with different capitalization (e.g., "Excellent", "excellent", "EXCELLENT") from being treated as different terms during analysis.

# ==================== MINI CHALLENGE ========================

# Without filtering into a DataFrame first, try to compute:
# app: 2
# support: 1
# service: 2
# excellent: 2

print()

# numof_app = feedback["Comment"].str.lower().str.contains("app").sum()
# numof_support = feedback["Comment"].str.lower().str.contains("support").sum()
# numof_service = feedback["Comment"].str.lower().str.contains("service").sum()
# numof_excellent = feedback["Comment"].str.lower().str.contains("excellent").sum()
#                               |
#                               |
#                           Same thing
#                               |
#                               |
#                               v
numof_app = feedback["Comment_Lower"].str.contains("app").sum()
numof_support = feedback["Comment_Lower"].str.contains("support").sum()
numof_service = feedback["Comment_Lower"].str.contains("service").sum()
numof_excellent = feedback["Comment_Lower"].str.contains("excellent").sum()

print(f"app: {numof_app}")
print(f"support: {numof_support}")
print(f"service: {numof_service}")
print(f"excellent: {numof_excellent}")

print()
# What are the most common keywords appearing in feedback?

all_text = " ".join(feedback["Comment_Lower"])
print(all_text)
words = all_text.split()
print(words)