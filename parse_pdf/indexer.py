#       ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#      	█▀█ █░▀░█ █▄█ █▀▄ ██▄

#         © Copyright 2022

#       https://t.me/amorescam

#     🔒 Licensed under the GNU GPLv3
#     🧟‍♂️ Not for open source

import re
import json
import numpy as np
from parse_pdf.PorterStemmer import PorterStemmer

with open('keywords.json', 'r') as f:
    dictionary = json.load(f)
    f.close()


def tokenize(text):
    clean_string = re.sub('[^a-z0-9-+# ]', ' ', text.lower().decode())
    tokens = clean_string.split()
    return tokens


def stemming(self, tokens):
    stemmed_tokens = []
    stemmer = PorterStemmer.PorterStemmer()
    stemmed_tokens = [stemmer.stem(t, 0, len(t) - 1) for t in tokens]
    return stemmed_tokens


def index(tokens):
    lst = np.zeros(len(dictionary))

    for t in tokens:
        if t in dictionary:
            lst[dictionary.index(t)] = 1
    return lst


def normalize(d):
    sum_vals = sum(d.values())
    for k, v in d.items():
        d[k] = v * 1.0 / sum_vals
    return d


def return_index(file_path='parse_pdf/outputtext.txt'):
    with open(file_path, 'rb') as f:
        text = f.read()
        f.close()

    tokenized = tokenize(text)
    # indexed = index(tokenized)

    return tokenized


if __name__ == "__main__":
    file_path = 'parse_pdf/outputtext.txt'
    return_index(file_path)
