import sys
import random

# empty arrays
word_list = []
word_list2 = []

'''
code first picks a word from word_list randomly
That word is then added to word_list2
'''
def shuffle_list(word_list):
    while len(word_list) > 0:
        choice = random.choice(word_list)
        word_list2.append(choice)
        word_list.remove(choice)

'''
user enters the words that will go into the word_list array. The shuffle_list function will then
return an array with shuffled words
'''
if __name__ == "__main__":

    for arg in range(1, len(sys.argv)):
        word_list.append(sys.argv[arg])

    shuffle_list(word_list)
    print(word_list2)