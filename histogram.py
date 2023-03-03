import string

def histogram(source_text):
    # Read the text from the file or string
    if isinstance(source_text, str):
        text = source_text
    else:
        with open(source_text, 'r') as file:
            text = file.read()

    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Split the text into words and count them
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, 0)

def print_frequencies(histogram):
    for word, count in histogram.items():
        print(f'{word}: {count}')

# Generate a histogram from the source text
hist = histogram("one fish two fish three fish four fish")

# Count the total number of unique words in the histogram
num_unique_words = unique_words(hist)
print(f'Total number of unique words: {num_unique_words}')

# Print the frequency of all words
print('\nFrequencies of all words:')
print_frequencies(hist)

