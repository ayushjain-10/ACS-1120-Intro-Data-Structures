import re

def tokenize(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # remove all non-alphanumeric characters and split by whitespace
        tokens = re.findall(r'\w+', text.lower())
        return tokens

if __name__ == '__main__':
    tokens = tokenize('snippet.txt')
    print(tokens)