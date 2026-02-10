# Assignment 2 Question 2
# Joseph Krosel

# Imports library
from collections import Counter

# Reads the file and saves it
with open("sample-file.txt", 'r') as file:
    data = file.read()

# Split the data by spaces
words_list = data.split()

token_list = []
# Sorts through the list to check for conditions and manipulates list
for index in range(0, len(words_list)):
    words_list[index] = words_list[index].lower()

    # Check for special characters
    if not words_list[index][len(words_list[index])-1].isalpha():
        words_list[index] = words_list[index][:-1]

    # Check is proper length
    if len(words_list[index]) > 1:
        token_list.append(words_list[index])

bigram_words_list = []
for i in range(0, len(token_list)-1):
    bigram_words_list.append(token_list[i] + " " + token_list[i+1])

# Count word frequencies
word_counts = Counter(bigram_words_list)

# Store the 10 most frequent words
top_10_frequent_words = word_counts.most_common(5)

print(top_10_frequent_words)