# Print exactly:

# Average rating: 8.62

# Highest rated movie: The Dark Knight

# Movies released after 2015:
# - Dune
# - Oppenheimer

# Movies with rating above 8.7:
# - Inception
# - The Dark Knight

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

avg_rate = movies["Rating"].mean()

highest_rated = movies.loc[movies["Rating"].idxmax(), "Title"]

late_movies = movies[movies["Year"] > 2015]["Title"].tolist()

highly_rated = movies[movies["Rating"] > 8.7]["Title"].tolist()

print(f"\n Average rating: {avg_rate:.2f}")
print(f"\n Highest rated movie: {highest_rated}")
print("\n Movies released after 2015:")
for movie in late_movies:
  print(f"- {movie}")
print("\n Movies with rating above 8.7:")
for movie in highly_rated:
  print(f"- {movie}")