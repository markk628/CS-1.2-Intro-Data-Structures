source_text = 'olivertwist.txt'

def scrubbed_words(source_text):
    with open(source_text, 'r') as file:
        words = file.read().split()
        return words

def unique_words(source_text):
    histogram = {}
    words = scrubbed_words(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    print(len(histogram))


unique_words(source_text)