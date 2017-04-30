import MeCab

def make_analyzed_file(input_file, output_file):
    mecab = MeCab.Tagger ('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    with open(input_file, encoding='utf-8') as input_file:
        with open(output_file, "w", encoding="utf-8") as output_file:
            output_file.write(mecab.parse(input_file.read()))

if __name__ == '__main__':
    make_analyzed_file('neko.txt', 'neko.txt.mecab')

