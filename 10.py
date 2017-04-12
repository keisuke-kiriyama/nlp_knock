import sys

def get_line_number(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        print(len(lines))

if __name__ == '__main__':
    file_name = sys.argv[1]
    get_line_number(file_name)
