from extract_from_json import extract_from_json
import re
from collections import OrderedDict


# def get_template():
#     dict = OrderedDict()
#     text = extract_from_json('イギリス')
#     base_info = re.search(u'(?<=\{\{基礎情報).+?(?=\}\}\n)', text, re.DOTALL)
#     if base_info:
#         pattern = re.compile(r'\|(.+?) = (.+?)(?<!<br/>)\n')
#         temp_list = pattern.findall(base_info.group(0))
#         if temp_list:
#             for temp in temp_list:
#                 tt = temp[1]
#                 tt = re.sub(r"'{2,5}", r"", tt)
#                 dict[temp[0]] = tt
#             print(dict)
#         else:
#             print('error')
#     else:
#         print('error')

# if __name__ == '__main__':
#     get_template()


def get_template():
    temp_dict = {}
    lines = re.split(r"\n[\|}]", extract_from_json(u"イギリス"))
    for line in lines:
        temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
        if temp_line is not None:
            temp_dict[temp_line.group(1)] = re.sub(r"'{2,5}", r"", temp_line.group(2))

    for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
        print(k, v)

if __name__ == '__main__':
    get_template()

