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

# Sorting

### ascending=False
--> descending order

### ascending=True
--> ascending order

# Filtering

For conditions, use '&' as AND, not '&&'

## Chaining operations together
### df.sort_values("Fare", ascending = False)["Name"].head(5)
--> Read from left to right
    1. Sort by fare
    2. Select Name column
    3. Show first 5

## Understanding idxmax()
Suppose:
counts = df["Pclass"].value_counts()
gives:
3    491
1    216
2    184

counts.max()
gives:
491

counts.idxmax()
gives:
3

# loc & iloc
loc → uses labels (row/column names)
iloc → uses integer positions (0-based indexes)

### loc (label-based)
import pandas as pd

df = pd.DataFrame(
    {"name": ["Alice", "Bob"], "age": [25, 30]},
    index=["a", "b"]
)

print(df.loc["a"])

Output:
name    Alice
age        25

Select a specific value:
df.loc["a", "age"]  ----> 25

### iloc (position-based)
df.iloc[row_position, column_position]
df.iloc[0]

Output:
name    Alice
age        25

Select a specific value:
df.iloc[0, 1] ------> 25

## Slicing difference

### df.iloc[0:2]
Returns rows 0 and 1, excluding 2.

### df.loc["a":"b"]
Returns rows "a" through "b".
The end label is included.

| Feature             | `loc`              | `iloc`            |
| ------------------- | ------------------ | ----------------- |
| Indexing type       | Labels             | Integer positions |
| Row selection       | `df.loc["a"]`      | `df.iloc[0]`      |
| Column selection    | `df.loc[:, "age"]` | `df.iloc[:, 1]`   |
| Slice end included? | Yes                | No                |
| Boolean filtering   | Commonly used      | Less common       |

A useful memory trick:

loc = locate by label
iloc = integer location

# Visualisation
## Correlation
Interpretation:

+1
Strong positive relationship

0
No relationship

-1
Strong negative relationship

# Data Cleaning
## Mean Imputation
### df["Age"] = df["Age"].fillna(df["Age"].mean()) --> Could use median instead if there are major outliers
Pros:
Keeps all rows
Easy

Cons:
Everyone missing becomes the same age
Reduces variance
Can distort relationships

## Dropping Rows
### df = df.dropna(subset=["Age"])
Pros:
No fake data

Cons:
Lose some data

## Tradeoffs in cleaning decisions
# Keep all rows
+ More data
- More assumptions
# Drop missing rows
+ No invented values
- Less data

# Text Analysis
## Finding number of instances containing a keyword
### feedback["Comment"].str.lower().str.contains("keyword").sum()
Take comments
↓
Convert to lowercase
↓
Check whether keyword exists
↓
Get True/False values
↓
Count the True values

## Which word appears the most?
### max(word_counts, key=word_counts.get)
For every key, what is its value?

## NLP style processing
Raw comments
↓
Lowercase
↓
Tokenize (split into words)
↓
Remove stop words
↓
Count frequencies
↓
Extract meaningful patterns

This exact pipeline is still used today before more advanced techniques like TF-IDF, embeddings, and transformers.

## Ways to return parts of a dict

filtered_words_counts = {
    "service": 2,
    "excellent": 2,
    "app": 2,
    "customer": 2,
    "crashes": 1
}
### filtered_words_counts.keys()
returns the keys

### filtered_words_counts.values()
returns the values

### filtered_words_counts.items()
returns BOTH together (tuple)

## lambda function
sorted_words = sorted(
    filtered_words_counts.items(),
    key=lambda x: x[1],
    reverse=True
)
### key=lambda x: x[1] 
So the lambda is effectively saying:
"Sort these tuples according to the second element."

### Is the SAME as:
def get_count(x):
    return x[1]

sorted(
    filtered_words_counts.items(),
    key=get_count
)

# N-grams

## Unigrams
One word at a time

## Bigrams
Two words together