import random

def random_word(histogram):
    words = list(histogram.keys())
    frequencies = list(histogram.values())
    return random.choices(words, weights=frequencies)[0]

histogram = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
random_word = random_word(histogram)
print(random_word)
