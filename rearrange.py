import sys
import random

if __name__ == '__main__':
    words = sys.argv[1:]
    word_list = []

    while words:
        word = random.sample(words, 1)[0]
        word_list.append(word)
        words.remove(word)

    print(' '.join(word_list))