from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

comments = [
    "The service was excellent",
    "The app crashes frequently",
    "Customer support was helpful",
    "Very slow response time",
    "I love the new update",
    "The website is confusing",
    "Excellent customer service",
    "The app is terrible"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(comments)
print(vectorizer.get_feature_names_out())

# ['app' 'confusing' 'crashes' 'customer' 'excellent' 'frequently' 'helpful'
#  'is' 'love' 'new' 'response' 'service' 'slow' 'support' 'terrible' 'the'
#  'time' 'update' 'very' 'was' 'website']

print()

print(X.shape)

# (8, 21) --> 8 comments, 21 unique words

print()

tfidf_df = pd.DataFrame(
  X.toarray(),
  columns=vectorizer.get_feature_names_out()
)

print(tfidf_df)

#         app  confusing   crashes  customer  excellent  frequently   helpful        is  ...   support  terrible       the  time    update  very       was   website
# 0  0.000000   0.000000  0.000000  0.000000   0.538498    0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.360638   0.0  0.000000   0.0  0.538498  0.000000
# 1  0.482467   0.000000  0.575683  0.000000   0.000000    0.575683  0.000000  0.000000  ...  0.000000  0.000000  0.323114   0.0  0.000000   0.0  0.000000  0.000000
# 2  0.000000   0.000000  0.000000  0.454195   0.000000    0.000000  0.541948  0.000000  ...  0.541948  0.000000  0.000000   0.0  0.000000   0.0  0.454195  0.000000
# 3  0.000000   0.000000  0.000000  0.000000   0.000000    0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000   0.5  0.000000   0.5  0.000000  0.000000
# 4  0.000000   0.000000  0.000000  0.000000   0.000000    0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.308268   0.0  0.549233   0.0  0.000000  0.000000
# 5  0.000000   0.575683  0.000000  0.000000   0.000000    0.000000  0.000000  0.482467  ...  0.000000  0.000000  0.323114   0.0  0.000000   0.0  0.000000  0.575683
# 6  0.000000   0.000000  0.000000  0.577350   0.577350    0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000   0.0  0.000000   0.0  0.000000  0.000000
# 7  0.508181   0.000000  0.000000  0.000000   0.000000    0.000000  0.000000  0.508181  ...  0.000000  0.606364  0.340334   0.0  0.000000   0.0  0.000000  0.000000

# [8 rows x 21 columns]