import re
## open the file and pull in the data

def read_file(file_name):
    with open(file_name) as f:
        return f.read()

file_contents = read_file("robin.txt")
words = re.sub('[^A-Za-z0-9 ]+', '', file_contents).lower().split()

def build_cache(words):
    cache = {}

    for i in range(len(words) - 1):
        word = words[i]

        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1
    
    return cache

cached_words = build_cache(words)

sorted_words = sorted(cached_words.items(), key=lambda word: (-word[1], word[0]))

def hash_count(string):
    hash_string = ''
    for _ in range (string):
        hash_string += "#"
    return hash_string
    

for i in range (0, len(sorted_words) - 1):
    print('%-19s %s' % (sorted_words[i][0], hash_count(sorted_words[i][1])))