
def word_count(s):
    # Your code here
    s_stripped = s.replace('"', '').replace(':', '').replace(';', '').replace(',', '').replace('.', '').replace('-', '').replace('+', '').replace('=', '').replace('/', '').replace('\\', '').replace("|", '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('*', '').replace('^', '').replace('&', '')
    if s_stripped == "":
        return {}
    else:
        s_split = s_stripped.lower().split()
        s_word_count = {w:s_split.count(w) for w in s_split}
        print(s_word_count)
        return s_word_count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))