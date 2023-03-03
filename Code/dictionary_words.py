import random
import sys

def read_words_file(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        return words

if __name__ == '__main__':
    file_path = '/usr/share/dict/words'  # replace with path to your file of words
    num_words = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    words = read_words_file(file_path)
    sentence_words = random.sample(words, num_words)
    sentence = ' '.join(sentence_words)
    print(sentence)