#  Use collections.Counter to find the top 10 most frequent words.
from collections import Counter
import collections
import re

def get_word_generator(file_path):
    """Yields individual words from a file one by one."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Standardizing to lowercase and splitting by non-alphanumeric characters
            words = re.findall(r'\w+', line.lower())
            for word in words:
                yield word

# Initialize the counter
word_counts = Counter()

# Feed the generator into the counter
# .update() iterates through the generator without loading the file into a list
word_counts.update(get_word_generator('/home/mirafra/sys.txt'))

# Retrieve the top 10 results
top_10 = word_counts.most_common(10)

print("--- Top 10 Most Frequent Words ---")
for word, count in top_10:
    print(f"{word}: {count}")