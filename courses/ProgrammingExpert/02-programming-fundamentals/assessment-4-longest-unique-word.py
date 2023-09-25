
from collections import Counter

def longest_unique_words(words, n):
    # Count the frequency of each word
    word_counter = Counter(words)

    # Get the unique words
    unique_words = [word for word, freq in word_counter.items() if freq == 1]

    # Sort the unique words by length
    unique_words.sort(key=len)

    # Return the n longest words
    return unique_words[-n:]

words = ['Longer', 'Whatever', 'Longer', 'Ball', 'Rock', 'Rocky', 'Rocky']
n = 3
print(longest_unique_words(words, n))  # Output: ['Ball', 'Rock', 'Whatever']
