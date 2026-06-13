### Series
Series: a single column of data

### DataFrame
DataFrame: a table

students = pd.DataFrame({
  "Name": ["Alice", "Bob", "Charlie"],
  "Age": [20, 21, 22],
  "Score": [90, 75, 88]
})

## Common Operations

# View first rows
students.head()

# Information about data
students.info()

# Summary Statistics
students.describe()

# Get one column
students["Score"]

# Average Score
students["Score"].mean()

# Highest score
students["Score"].max()

# Lowest Score
students["Score"].min()

## Filtering
# Students scoring above 80
students[students["Score"] > 80]