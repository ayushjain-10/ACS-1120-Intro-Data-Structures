import random
from tokens import tokenize

class MarkovChain:
    def __init__(self, source_text):
        self.text = self.parse_text(source_text)
        self.order = 2

    def parse_text(self, source_text):
        with open(source_text) as f:
            text = f.read()
        return text

    def get_random_start(self):
        sentences = self.text.split('. ') + self.text.split('? ') + self.text.split('! ')
        sentences = [s.strip() for s in sentences if len(s) > 0]
        starting_sentences = [s for s in sentences if s[0].isupper()]
        starting_sentence = random.choice(starting_sentences)
        starting_point = starting_sentence.split()[:self.order]
        return starting_point

    def get_random_end(self):
        sentences = self.text.split('. ') + self.text.split('? ') + self.text.split('! ')
        sentences = [s.strip() for s in sentences if len(s) > 0]
        ending_sentences = [s for s in sentences if s[-1] in ('.', '?', '!')]
        ending_sentence = random.choice(ending_sentences)
        ending_point = ending_sentence.split()[-self.order:]
        return ending_point

    def create_ngram_map(self):
        words = self.text.split()
        ngrams = [tuple(words[i:i+self.order]) for i in range(len(words) - self.order)]
        map = {}
        for i, ngram in enumerate(ngrams):
            if i == len(ngrams) - 1:
                break
            if ngram not in map:
                map[ngram] = []
            map[ngram].append(ngrams[i+1][-1])
        return map

    def compose_sentence(self, max_words):
        starting_point = self.get_random_start()
        ending_point = self.get_random_end()
        map = self.create_ngram_map()

        sentence = starting_point
        current_ngram = tuple(sentence)
        while len(sentence) < max_words and current_ngram != tuple(ending_point):
            if current_ngram not in map:
                break
            next_word = random.choice(map[current_ngram])
            sentence.append(next_word)
            current_ngram = tuple(sentence[-self.order:])
        sentence += ending_point[self.order-1:]
        return ' '.join(sentence)

if __name__ == '__main__':
    markov = MarkovChain('output.txt')
    print(markov.compose_sentence(10))
    markov = tokenize('output.txt')
