def get_word_n_gram(str, n):
    str = str.split(" ")
    n_gram = []
    for i in range(len(str) - n + 1):
        n_gram.append(str[i:i+n])
    print(n_gram)


def get_char_n_gram(str, n):
    n_gram = []
    for i in range(len(str) - n + 1):
        n_gram.append(str[i:i + n])
    print(n_gram)

if __name__ == "__main__":
    get_word_n_gram("I am an NLPer", 2)
    get_char_n_gram("I am an NLPer", 2)
