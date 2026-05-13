words = ['mountain', 'river', 'sky', 'ocean', 'forest', 'tree', 'sun', 'moon', 'star', 'cloud']
word_lengths = {word: len(word) for word in words if len(word)>5}
print(word_lengths)