# List of strings (example)
string_list = [
    "apple banana apple",
    "banana orange apple",
    "grape banana"
]

# Step 1: Extract all words and store them in a set to find unique words
all_words = []
for sentence in string_list:
    words = sentence.split()
    for word in words:
        all_words.append(word)

# Create a set of unique words
unique_words = set(all_words)

# Step 2: Count frequency of each unique word
word_frequency = {}

for word in unique_words:
    count = 0
    for w in all_words:
        if w == word:
            count += 1
    word_frequency[word] = count

# Display results
print("Unique words:", unique_words)
print("Word frequencies:")
for word in word_frequency:
    print(f"{word}: {word_frequency[word]}")
