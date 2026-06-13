import pandas as pd

students = pd.DataFrame({
  "Name": ["Alice", "Bob", "Charlie"],
  "Age": [20, 21, 22],
  "Score": [90, 75, 88]
})

# print(students)
# print()
# print(students["Name"])

print("=== FIRST ROWS ===")
print(students.head())

print("\n=== INFO ===")
students.info()

print("\n=== SUMMARY ===")
print(students.describe())

print("\n=== STUDENTS SCORING ABOVE 80 ===")
print(students[students["Score"] > 80])