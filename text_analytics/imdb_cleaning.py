import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

df = pd.read_csv("datasets/IMDB_Dataset.csv")

def clean_text(text):                                 # HTML removed, punctuation removed, everything lowercase
  text = text.lower()
  text = re.sub(r"<.*?>", " ", text)
  text = re.sub(r"[^a-z\s]", " ", text)
  text = re.sub(r"\s+", " ", text)
  return text.strip()

sample = df["review"].iloc[0]
print(sample)
print("\n================================\n")
print(clean_text(sample))

print()

df["clean review"] = df["review"].apply(clean_text)
print(df["clean review"].head())

print()

vectorizer = TfidfVectorizer(
  stop_words = "english",
  max_features = 1000   # prevent using so may unique words
)

X = vectorizer.fit_transform(df["clean review"])
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

print(f"The top terms are:\n{top_terms}")