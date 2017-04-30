from extract_from_json import extract_from_json
import re


def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}(.+?)\]{2}", r"\1", str)
    return str

def get_template():
    temp_dict = {}
    lines = re.split(r"\n[\|}]", extract_from_json(u"イギリス"))
    for line in lines:
        temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
        if temp_line is not None:
            temp_dict[temp_line.group(1)] = remove_markup(temp_line.group(2))


    for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
        print(k, v)


if __name__ == '__main__':
    get_template()