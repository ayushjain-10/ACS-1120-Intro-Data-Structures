import random
from collections import defaultdict

def random_word(sentence):
    histogram = defaultdict(int)
    words = sentence.split()
    for word in words:
        histogram[word] += 1
    frequencies = list(histogram.values())
    return random.choices(list(histogram.keys()), weights=frequencies)[0]


