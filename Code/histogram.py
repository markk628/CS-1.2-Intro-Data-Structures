import re

source_text = 'olivertwist.txt'

def scrubbed_words(source_text):
    with open(source_text, 'r') as file:
        words = file.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
        return scrubbed_words.split()

def unique_words(source_text):
    histogram = {}
    words = scrubbed_words(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    print(len(histogram))

def list_histogram(source_text):
   words = scrubbed_words(source_text)
   histogram = []
   for word in words:
       instance = [word, 0]
       for word2 in words:
           if word == word2:
               instance[1] += 1
       if instance not in histogram:
           histogram.append(instance)
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