import sys
import random
import re
from histogram import dic_histogram

source_text = 'test.txt'

def read(source_text):
    with open(source_text, 'r') as file:
        words = file.read()
        #makes sure word is alphabetic
        s_words = re.sub(r'[^a-zA-Z\s]', '', words)
        ss_words = s_words.split()
        return ss_words
    

def random_word(ss_words):
    r_word = random.choice(ss_words)
    return r_word

def weights(histogram):
    words = []
    for key, value in histogram.items():
        for i in range(value):
            words.append(key)
    print(words)
    return words

def frequency(histogram, count):
    new_dict = {}
    for i in range(count):
        random_words = random_word(weights(histogram))
        new_dict[random_words] = new_dict.get(random_words, 0) + 1

    print(new_dict)

word_list = read(source_text)
print(random_word(word_list))
# hist = dic_histogram(source_text)
# weights(hist)
# frequency(hist, 100)
