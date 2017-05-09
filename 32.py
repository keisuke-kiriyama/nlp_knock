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


def get_verb_base(parsed_list):
    verb_list = []
    for element in parsed_list:
        if element['pos'] == '動詞':
            verb_list.append(element['base'])
    return verb_list


if __name__ == '__main__':
    parsed_list = read_mecab_data('neko.txt.mecab')
    verb_base_list = get_verb_base(parsed_list)
    print(verb_base_list)