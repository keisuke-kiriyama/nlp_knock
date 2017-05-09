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


def get_noun_concatenation(parsed_list):
    noun_phrase_list = []
    temp =[]
    for i in range(len(parsed_list) - 2):
        if parsed_list[i]['pos'] =='名詞':
            temp.append(parsed_list[i]['surface'])
        else:
            if len(temp) > 1:
                noun_phrase_list.append(temp)
                temp =[]
            else:
                temp =[]
    return noun_phrase_list


if __name__ == '__main__':
    parsed_list = read_mecab_data('neko.txt.mecab')
    noun_phrase_list = get_noun_concatenation(parsed_list)
    print(noun_phrase_list)