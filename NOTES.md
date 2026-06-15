# Series
Series: a single column of data

# DataFrame
DataFrame: a table

students = pd.DataFrame({
  "Name": ["Alice", "Bob", "Charlie"],
  "Age": [20, 21, 22],
  "Score": [90, 75, 88]
})

## Common Operations

### View first rows
students.head()

### Information about data
students.info()

### Summary Statistics
students.describe()

### Get one column
students["Score"]

### Average Score
students["Score"].mean()

### Highest score
students["Score"].max()

### Lowest Score
students["Score"].min()

## Filtering
### Students scoring above 80
students[students["Score"] > 80]


# CSV exploration
## Some commands

### df.head(n) 
--> Outputs the first n rows of data. If no n specified, default of 5.
### df.tail(n) 
--> Outputs the last n rows of data. If no n specified, default of 5.

### print(df.shape)
--> Gives the number of rows and columns in the format (rows, columns)
### print(df.columns)
--> Shows all column names
### df.info()
--> Shows:
    1. datatype
    2. missing values
    3. memory usage
### print(df.describe())
--> Shows:
    1. mean
    2. min
    3. max
    4. quartiles
    For numerical columns
### print(df.isna().sum())
--> Shows missing values per column

### df["Sex"].value_counts()
--> shows count of each entry in specified column