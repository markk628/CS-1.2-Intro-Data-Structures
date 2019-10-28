#got help from my boy Ricky
from random import choice
import sys

'''
opens words file and labels it as file. Code then chooses a random word from file and appends it 
to a list called random.
'''
def random_sentence(amount):
    with open("/usr/share/dict/words") as file:
        word_list = file.readlines()
        counter = 0
        random = []
        while counter < int(amount):
            random.append(choice(word_list).strip())
            counter +=1

    return ' '.join(random)

if __name__ == "__main__":

    amount = sys.argv[1]
    output = random_sentence(amount)
    print(output + ".")
