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
#                 dict[temp[0]] = temp[1]
#             print(dict)
#         else:
#             print('error')
#     else:
#         print('error')


def get_template():
    dict = OrderedDict()
    text = extract_from_json('イギリス')
    base_info = re.search(u'(?<=\{\{基礎情報)(.+?)(?=\}\}\n)', text, re.DOTALL)
    pattern = re.compile(u'\|(.+?) = (.+?)(?<!<br/>)\n')
    info_list = pattern.findall(base_info.group(1))
    if info_list:
        for info in info_list:
            dict[info[0]] = info[1]
    print(dict)



if __name__ == '__main__':
    get_template()