import random


def shuffle_str(str):
    words = str.split(' ')
    shuffled_str = ''
    for word in words:
        if len(word) > 4:
            middle_word = list(word[1:-1])
            random.shuffle(middle_word)
            word = word[0] + "".join(middle_word) + word[-1]
        if word == ".":
            shuffled_str = shuffled_str[:-1]
            shuffled_str += word
        else:
            shuffled_str += word + " "

    print(shuffled_str)

if __name__ == '__main__':
    str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    shuffle_str(str)