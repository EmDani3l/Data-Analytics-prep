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

feedback["Comment Lower"] = (feedback["Comment"].str.lower())
all_text = " ".join(feedback["Comment Lower"])
print(all_text)
print(type(all_text)) # <class 'str'>

words = all_text.split()
print(words)
print(type(words)) # <class 'list'>

word_counts = {}
for word in words:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1

print(word_counts)
# {'the': 5, 'service': 2, 'was': 2, 'excellent': 2, 'app': 2, 'crashes': 1, 'frequently': 1, 'customer': 2, 'support': 1, 'helpful': 1, 'very': 1, 'slow': 1, 'response': 1, 'time': 1, 'i': 1, 'love': 1, 'new': 1, 'update': 1, 'website': 1, 'is': 2, 'confusing': 1, 'terrible': 1}

fraud = max(word_counts) # bro what does this bum even do
print(fraud)
# website

nonfraud = max(word_counts, key=word_counts.get)
print(nonfraud)
# the


# ==================== STOP WORDS ========================
stop_words = {
    "the",
    "is",
    "was",
    "a",
    "an",
    "i"
}

filtered_words = []

for word in words:
  if word not in stop_words:
    filtered_words.append(word)

print(filtered_words)
# ['service', 'excellent', 'app', 'crashes', 'frequently', 'customer', 'support', 'helpful', 'very', 'slow', 'response', 'time', 'love', 'new', 'update', 'website', 'confusing', 'excellent', 'customer', 'service', 'app', 'terrible']

filtered_words_counts = {}
for filtered_word in filtered_words:
  if filtered_word in filtered_words_counts:
    filtered_words_counts[filtered_word] += 1
  else:
    filtered_words_counts[filtered_word] = 1

print(filtered_words_counts)
# {'service': 2, 'excellent': 2, 'app': 2, 'crashes': 1, 'frequently': 1, 'customer': 2, 'support': 1, 'helpful': 1, 'very': 1, 'slow': 1, 'response': 1, 'time': 1, 'love': 1, 'new': 1, 'update': 1, 'website': 1, 'confusing': 1, 'terrible': 1}

freq_nonstop = max(filtered_words_counts, key=filtered_words_counts.get)
print(freq_nonstop)
# service

sorted_words = sorted(
    filtered_words_counts.items(),
    key=lambda x: x[1],
    reverse=True
)

print(sorted_words)

print()
#===============================================================
for item in filtered_words_counts.items():
    print(item)

print()

for item in filtered_words_counts.items():
    print(item[0], item[1])

print()

for word, count in filtered_words_counts.items():
    print(word, count)