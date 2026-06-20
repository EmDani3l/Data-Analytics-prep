import pandas as pd

feedback = pd.DataFrame({
    "Comment": [
        "The service was excellent",
        "The app crashes frequently",
        "Customer support was helpful",
        "Very slow response time",
        "I love the new update",
        "The website is confusing",
        "Excellent customer service",
        "The app is terrible"
    ]
})

# filtered_words = [
#       "service",
#       "excellent", 
#       "app", 
#       "crashes", 
#       "frequently", 
#       "customer", 
#       "support", 
#       "helpful", 
#       "very", 
#       "slow", 
#       "response", 
#       "time", 
#       "love", 
#       "new", 
#       "update", 
#       "website", 
#       "confusing", 
#       "excellent", 
#       "customer", 
#       "service", 
#       "app", 
#       "terrible"
# ]

# bigrams = []

# for i in range(len(filtered_words) - 1):
#   bigrams.append(filtered_words[i] + " " + filtered_words[i + 1])

# print(bigrams)

# # ['service excellent', 'excellent app', 'app crashes', 'crashes frequently', 'frequently customer', 'customer support', 'support helpful', 'helpful very', 'very slow', 'slow response', 'response time', 'time love', 'love new', 'new update', 'update website', 'website confusing', 'confusing excellent', 'excellent customer', 'customer service', 'service app', 'app terrible']

# print()

# bigram_counts = {}

# for bigram in bigrams:
#   if bigram in bigram_counts:
#     bigram_counts[bigram] += 1
#   else:
#     bigram_counts[bigram] = 1

# common_bigram = max(bigram_counts, key=bigram_counts.get)
# print(common_bigram)

# service excellent

bigrams = []

feedback["Comment Lower"] = (feedback["Comment"].str.lower())
for comment in feedback["Comment Lower"]:
  words = comment.split()
  for i in range(len(words) - 1):
    bigram = words[i] + " " + words[i + 1]
    bigrams.append(bigram)

print(bigrams)

# ['the service', 'service was', 'was excellent', 'the app', 'app crashes', 'crashes frequently', 'customer support', 'support was', 'was helpful', 'very slow', 'slow response', 'response time', 'i love', 'love the', 'the new', 'new update', 'the website', 'website is', 'is confusing', 'excellent customer', 'customer service', 'the app', 'app is', 'is terrible']

print()

bigram_counts = {}

for bigram in bigrams:
  if bigram in bigram_counts:
    bigram_counts[bigram] += 1
  else:
    bigram_counts[bigram] = 1

common_bigram = max(bigram_counts, key=bigram_counts.get)
print(common_bigram)

# the app