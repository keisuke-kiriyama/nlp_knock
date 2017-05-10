from collections import Counter
import matplotlib.pyplot as plt

def make_dict(line):
    surface = line.split()[0]
    elements = line.split()[1].split(',')
    parsed_dict = {}
    if 0 < len(elements) < 4:
        parsed_dict['surface'] = surface
        parsed_dict['base'] = ''
        parsed_dict['pos'] = ''
        parsed_dict['pos1'] = ''
    else:
        parsed_dict['surface'] = surface
        parsed_dict['base'] = elements[6]
        parsed_dict['pos'] = elements[0]
        parsed_dict['pos1'] = elements[1]
    return parsed_dict


def read_mecab_data(mecab_file):
    with open(mecab_file, 'r') as mecab_file:
        lines = mecab_file.readlines()
        parsed_list = []
        try:
            for line in lines:
                parsed_list.append(make_dict(line))
        except:
            return parsed_list


def count_words(parsed_list):
    word = []
    for element in parsed_list:
        word.append(element['surface'])
    return Counter(word)


def create_histgram(words_counter, outputfile):
    words = []
    counts = []
    for word, count in words_counter.most_common():
        words.append(word)
        counts.append(count)
    # histgram_counter = Counter(counts)
    # histgram_counter_sorted =sorted(histgram_counter.most_common(), key=lambda x: x[0])
    # x = list(map(lambda x:x[0], histgram_counter_sorted))
    # y = list(map(lambda x:x[1], histgram_counter_sorted))
    plt.hist(counts)
    plt.savefig(outputfile)


if __name__ == '__main__':
    outputfile = 'neko.mecab_hist.png'
    parsed_list = read_mecab_data('neko.txt.mecab')
    words_counter = count_words(parsed_list)
    create_histgram(words_counter, outputfile)