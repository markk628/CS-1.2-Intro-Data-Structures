import sys
import random

# empty array
word_list = []

# shuffles the word_list array
def shuffle_list(word_list):
    random.shuffle(word_list)
    return word_list

'''
user enters the words that will go into the word_list array. The shuffle_list function will then
shuffle the array and return a shuffled list
'''
if __name__ == "__main__":

    for arg in range(1, len(sys.argv)):
        word_list.append(sys.argv[arg])

    print(word_list)
    
    word_list = shuffle_list(word_list)

    print(word_list)