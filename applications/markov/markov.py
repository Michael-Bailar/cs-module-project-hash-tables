import random

## understand ##
#

## Plan ##

# read in file and split
### already read in 
### split into words

#analyze text, building up dataset of what can follow each word.
### which words can follow a word? any word that actually does
#### any word at index + 1
### how to build dataset

### use a hashtable
#### good way to relate one pieve of info with another
#### frequent lookups 
### key: word, value is list of words that can follow the word

#choose a start word at random
## first or second character is capitalized

## make list of start words

# loop over, print, choose random following word, stop on stop words
## what's a stop word?
### ends with .?!, or second to last char is


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

split_words = words.split()


# TODO: analyze which words can follow other words
dataset = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in dataset:
        dataset[word] = [next_word]

    else:
        dataset[word].append(next_word)

start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)

# TODO: construct 5 random sentences
for _ in range(5):
    stopped = False

    stop_signs = ".?!"

    while not stopped:
        print(word, end=' ')

        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True

        following_words = dataset[word]
        word = random.choice(following_words)
    print(" ")

