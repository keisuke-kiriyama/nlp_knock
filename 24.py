from extract_from_json import extract_from_json
import re


def get_file_pref():
    text = extract_from_json('イギリス')
    lines = text.split('\n')
    pattern = re.compile(u'(ファイル|File):(.+?)\|')
    for line in lines:
        l = pattern.match(line)
        if l:
            print(l.group(2))



if __name__ == '__main__':
    get_file_pref()