from dictogram import Dictogram
from histogram import dic_histogram, scrubbed_words
import random

class MarkovChain(dict):
    def __init__(self, word_list=None):
        super(MarkovChain, self).__init__()
        
        if word_list is not None:
            self.create_markov(word_list)

    
    def get_text(self, path = 'olivertwist.txt'):
        text = scrubbed_words(path)
    
        return text 
    
    def create_markov(self, word_list): 
        
        num_words = len(word_list)  
        
        for index, key1 in enumerate(word_list): 
            if num_words > index + 2:
                key2 = word_list[index + 1]
                word = word_list[index + 2]

                if (key1, key2) not in self:
                    self[(key1, key2)] = Dictogram([word])
                else:
                    self[(key1, key2)].add_count(word)


    def sentence(self, word_list, num_words):
        sentence = ""
        
        random_index = random.randint(0, len(word_list) - 1)
        key = (word_list[random_index], word_list[random_index + 1])

        while len(sentence) < num_words:  
            
            word = self[key].sample()

            sentence += " " + word

            key = (key[1], word)
        
        return sentence

def run_generator():
    text = 'olivertwist.txt'
    word_list = MarkovChain.get_text(text)
    markov_chain = MarkovChain(word_list)
    return(markov_chain.sentence(word_list, 60))


        
        
    




if __name__ == "__main__":
    print(run_generator())