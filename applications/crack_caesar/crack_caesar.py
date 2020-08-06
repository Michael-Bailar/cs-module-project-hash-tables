# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

import re
#1. import the file 
def read_file(file_name):
    with open(file_name) as f:
        return f.read()

file_contents = read_file("ciphertext.txt")
cleaned_file = re.sub('[^A-Za-z]+', '', file_contents)

#2. count occurrance of each letter

def build_letter_percent_cache(string):
    cache = {}
    total_length = len(string) - 1

    for i in range(total_length):
        letter = string[i]
        if letter == " ":
            pass
        elif letter not in cache:
            cache[letter] = 1
        else:
            cache[letter] = cache[letter] + 1

    return cache

letter_percent_cache = build_letter_percent_cache(cleaned_file)

#3. determine the cypher key()
sorted_letter_count= sorted(letter_percent_cache.items(), key=lambda letter: -letter[1])
sort_keys = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def create_cypher_key():
    cache = {}

    for i in range(26):
        letter = sorted_letter_count[i][0]
        transposed_letter = sort_keys[i]
        cache[letter] = transposed_letter
    return cache

cypher_key = create_cypher_key()

#4. print out decoded version
print(file_contents.translate(str.maketrans(cypher_key)))


