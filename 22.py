from extract_from_json import extract_from_json
import re

def get_category():
    text = extract_from_json('イギリス')
    lines = text.split('\n')
    pattern = re.compile('\[\[Category:(.+)\]\]')
    for line in lines:
        l = pattern.match(line)
        if l:
            print(l.group(1))


if __name__ == '__main__':
    category_rows = get_category()
    print(category_rows)