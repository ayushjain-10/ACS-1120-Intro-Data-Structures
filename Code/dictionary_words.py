import random
import sys

def read_words_file(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        return words

def generate_sentence(words, num_words):
    sentence_words = random.sample(words, num_words)
    sentence = ' '.join(sentence_words)
    return sentence

if __name__ == '__main__':
    file_path = '/usr/share/dict/words'  # replace with path to your file of words
    num_words = int(sys.argv[1])  # replace with number of words you want in the sentence
    words = read_words_file(file_path)
    sentence = generate_sentence(words, num_words)
    print(sentence)
