# Import packages
import string
import re
import numpy as np
import Counter from "./Counter"
# from collections import Counter

# Reading all words and for this we need vocabulary dictionary
# wordLowerCase=['a','b','c'...,'z']
wordLowerCase = string.ascii_lowercase
def read_corpus(filename):
    with open(filename,"r",encoding="utf8") as file:
        lines =file.readlines()

        words=[]
        for word in lines:
            words+=re.findAll(r'\w+',word.lower())

    return words

corpus=read_corpus(r'big.txt') # All oords are stored in it

# Create our vocabulary for unique words

vocab=set(corpus) # It remove repetation of word
# len(vocab) #It return length of vocab
words_count=Counter(corpus) # It store how many times word repeats in form of dictionary
# words_count["for"] # It return how many times for repeat in corpus


### Interesting Part

## Calculate Word probability
#  P(word)=words_count[word]/len(corpus)

total_word_count=float(sum(words_count.values()))
words_probas={word:word_count[word]/total_word_count for word in words_count.keys()}
# It store all wordprobility and strore in form of dict where key is word

### Autocorrect Operation

## Split operation
# [("","hello"),("h","ello"),("he","llo"),("hel","lo"),("hell","o"),("hello","")]
def split(word):
    return {(word[:i],word[i:]) for i in range(len(word)+1)}
## Delete Operation
# why->['hy','wy','wh']
def delete(word):
    return [left+right[:1] for left,right in split(word) if len(right)>1]

## Swap Operation
def swap(word):
    return [left+right[1]+right[0]+right[2:]  for left,right in split(word) if len(right)>1]

## Replace Operation
def replace(word):
    return [ left+center+right[:1]   for left,right in split(word) if len(right)>1 for center in wordLowerCase]

## Insert Operation
def insert(word):
    return [ left+center+right[:1]   for left,right in split(word) for center in wordLowerCase]



### Find Minimum Distance
## To find best alternate(edit) words
def level_one_edits(word):
    return (delete(word)+swap(word)+replace(word)+insert(word))

def level_two_edits(word):
    return set(e2 for e1 in level_one_edits(word) for e2 in level_one_edits(e1))



def correct_spelling(word,vocab,word_prob):
    if word in vocab:
        print(f"{word} - is already in vocablary")
        return
    suggests=level_one_edits(word) or level_two_edits(word) or [word]
    best_guesses=[w for w in suggests if w in vocab]
    return [w,wordprobility[w] for w in best best_guesses]

guess=correct_spelling("laed",vocab,words_probas)
print(guess)