from extract_from_json import extract_from_json
import re

def get_section():
    text = extract_from_json('イギリス')
    pattern = re.compile(r'=(=+)(.+)=')
    section_list = pattern.findall(text)
    for section in section_list:
        equal = re.compile(r'([^=]+)=*')
        sec = equal.match(section[1])
        if sec:
            print('level:'+ str(len(section[0])) + ' ' + sec.group(1))
        else:
            print('level:'+ str(len(section[0])) + ' ' + section[1])

if __name__ == '__main__':
    category_rows = get_section()
