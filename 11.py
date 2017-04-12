import sys

def convert_tab_to_space(file):
    with open(file) as f:
        str = f.read()
    print(str.replace("\t", " "))

if __name__ == '__main__':
    file = sys.argv[1]
    convert_tab_to_space(file)