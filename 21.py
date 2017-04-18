from extract_from_json import extract_from_json
import re

def get_category_row():
    text = extract_from_json('イギリス')
    lines = text.split('\n')
    pattern = re.compile('\[\[Category:(.+)\]\]')
    category_rows = []
    for line in lines:
        if pattern.match(line):
            category_rows.append(line)
    return category_rows

if __name__ == '__main__':
    category_rows = get_category_row()
    print(category_rows)