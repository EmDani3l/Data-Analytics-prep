import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("datasets/IMDB_Dataset.csv")

# print(df.head())
# print()
# print(df.shape)
# print()
# print(df.columns)

# print(df.info())
# print(df["sentiment"].value_counts())

# # 25,000 positive, 25,000 negative

print(df["review"].iloc[0])
print()
print(df["review"].iloc[1])

print()
print()

vectorizer = TfidfVectorizer(
  stop_words = "english",
  max_features = 1000   # prevent using so may unique words
)

X = vectorizer.fit_transform(df["review"])
print(X.shape)

print()

tfidf_df = pd.DataFrame(
  X.toarray(),
  columns = vectorizer.get_feature_names_out()
)

avg_scores = tfidf_df.mean(axis = 0)

top_terms = (
  avg_scores.sort_values(ascending=False).head(20)
)

print(top_terms)

# br            0.158836
# movie         0.081215
# film          0.071504
# like          0.039808
# just          0.036872
# good          0.034723
# story         0.029514
# time          0.029505
# really        0.029123
# bad           0.026889
# great         0.026559
# people        0.024301
# don           0.024018
# movies        0.023748
# watch         0.022078
# make          0.021380
# think         0.020980
# way           0.020966
# seen          0.020959
# characters    0.020842

print()

positive_reviews = df[df["sentiment"] == "positive"]
negative_reviews = df[df["sentiment"] == "negative"]

print(len(positive_reviews))  # to check
print(len(negative_reviews))
print()

positive_vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
positive_X = positive_vectorizer.fit_transform(positive_reviews["review"])
positive_df = pd.DataFrame(positive_X.toarray(), columns=positive_vectorizer.get_feature_names_out())
positive_terms = positive_df.mean(axis=0).sort_values(ascending=False).head(20)
print(f"Positive terms:\n{positive_terms}")

negative_vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
negative_X = negative_vectorizer.fit_transform(negative_reviews["review"])
negative_df = pd.DataFrame(negative_X.toarray(), columns=negative_vectorizer.get_feature_names_out())
negative_terms = negative_df.mean(axis=0).sort_values(ascending=False).head(20)
print(f"Negative terms:\n{negative_terms}")

# Positive terms:
# br        0.183824
# movie     0.090010
# film      0.089352
# like      0.044322
# good      0.042449
# great     0.040419
# just      0.038225
# story     0.037973
# time      0.035573
# really    0.033349
# love      0.030536
# best      0.028989
# people    0.028610
# life      0.026956
# movies    0.026823
# watch     0.025840
# films     0.025837
# think     0.025407
# way       0.025077
# seen      0.025056

# Negative terms:
# br            0.192933
# movie         0.102294
# film          0.082495
# like          0.050664
# just          0.049121
# bad           0.043371
# good          0.040338
# really        0.035810
# time          0.035198
# story         0.032535
# don           0.032095
# movies        0.029570
# people        0.029469
# make          0.028757
# plot          0.028651
# acting        0.028183
# watch         0.026568
# way           0.025282
# characters    0.025241
# seen          0.024753


# 1. What are the top 10 terms overall?

# br, movie, film, like, just, time, story, movies, people, really

# 2. What words appear most strongly in positive reviews?

# Besides the words that appear in both types: good, great, love, best

# 3. What words appear most strongly in negative reviews?

# Besides the words that appear in both types: bad, don, plot, characters

# 4. Do the positive and negative vocabularies differ? If so, how?

# They have a pool of common words but the adjectives used can be obvious in determining what type it belongs to, as well as certain words relating to specific reviews. For instance, "plot" appears in negative reviews, indicating that reviewers could be more critical of movies if they think something was not right about the story of the film.
# Positive and negative reviews share many domain-specific words such as "movie", "film", and "story". However, sentiment-bearing words differ substantially. Positive reviews contain terms such as "great", "love", and "best", whereas negative reviews contain terms such as "bad" and "don't". This suggests that sentiment is often conveyed through evaluative language rather than topic-specific vocabulary.