import re

source_text = 'olivertwist.txt'

def scrubbed_words(source_text):
    with open(source_text, 'r') as file:
        words = file.read()
        #makes sure word is alphabetic
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
        return scrubbed_words.split()

def unique_words(source_text):
    histogram = {}
    #opens file stores data in words
    words = scrubbed_words(source_text)


    for word in words:
        #word is in histogram already
        if word in histogram:
            histogram[word] = histogram[word] + 1
        #word is not in histogram
        else:
            histogram[word] = 1
    print(len(histogram))

def list_histogram(source_text):
    words = scrubbed_words(source_text)
    histogram = []
    for word in words:
        item_in_histogram = False
        #look through histogram
        for item in histogram:
            #already in list increment count
            if item[0] == word:
                item[1] += 1
                item_in_histogram = True

        if item_in_histogram == False:
            histogram.append([word, 1])
            



    print(histogram) 

def dic_histogram(source_text):
    histogram = {}
    words = scrubbed_words(source_text)
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    for key in list(histogram.keys()):
        print(key, histogram[key])

dic_histogram(source_text)