import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)

df = pd.read_csv("datasets/IMDB_Dataset.csv")

def clean_text(text):                                 # HTML removed, punctuation removed, everything lowercase
  text = text.lower()
  text = re.sub(r"<.*?>", " ", text)
  text = re.sub(r"[^a-z\s]", " ", text)
  text = re.sub(r"\s+", " ", text)
  return text.strip()

df["clean review"] = df["review"].apply(clean_text)

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(df["clean review"])
y = df["sentiment"].map({
  "negative": 0,
  "positive": 1
})

# print(y.head())
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # random state is just a random seed

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(accuracy)

# 0.8883

print(classification_report(y_test, predictions))

#               precision    recall  f1-score   support

#            0       0.90      0.87      0.89      4961
#            1       0.88      0.91      0.89      5039

#     accuracy                           0.89     10000
#    macro avg       0.89      0.89      0.89     10000
# weighted avg       0.89      0.89      0.89     10000

print()

print(confusion_matrix(y_test, predictions))

# [[4321  640]
#  [ 477 4562]]

# =========== QUESTIONS ==============
# 1. What accuracy dod you get?

# 0.8883

# 2. How many reviews were used for training and testing?

# 80% were used for training, while 20% was used for testing.

# 3. What does model.fit(...) mean in your own words?

# model.fit(X_train, y_train) trains the logistic regression model by learning patterns that connect TF-IDF features to sentiment labels.

# 4. What do you think model.predict(...) does?

# model.predict() uses the learned relationships from training to predict the sentiment labels of unseen reviews.

print()

print(f"\nX_train shape:\n{X_train.shape}")
print(f"\nX_test shape:\n{X_test.shape}")
print(f"\ny_train shape:\n{y_train.shape}")
print(f"\ny_test shape:\n{y_test.shape}")