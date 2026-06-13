import pandas as pd

movies = pd.DataFrame({
  "Title": ["Inception",
            "Interstellar",
            "The Dark Knight",
            "Dune",
            "Oppenheimer"
    ],
    "Rating": [8.8, 8.7, 9.0, 8.0, 8.6],
    "Year": [2010, 2014, 2008, 2021, 2023]
})

# 1.What is the average rating?

print("\n Average rating is \n", movies["Rating"].mean())

# 2.Which movie has the highest rating?

print("\nMovie with highest rating is \n", movies[movies["Rating"] == movies["Rating"].max()]["Title"])

# 3.Which movies were released after 2015?

print("\n Movies released after 2015 are \n", movies[movies["Year"] > 2015]["Title"].tolist())
# Alternate way:
movies.loc[movies["Rating"].idxmax()]
print("\n Movies released after 2015 are \n", movies.loc[movies["Rating"].idxmax(), "Title"])

# 4.Which movies have rating above 8.7?

print("\n Movies with rating above 8.7 are \n", movies[movies["Rating"] > 8.7])