

def no_dups(s):
    # Your code here
    cache = []
    s_split = s.split()
    s_concat = ""
    for word in s_split:
        if len(cache) < 1:
            cache.append(word)
            s_concat += word
        elif word in cache:
            pass
        else:
            cache.append(word)
            s_concat = s_concat + " " + word
    return s_concat



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))