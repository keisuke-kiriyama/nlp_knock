import sys

prefectures = set()

def get_str_set(file):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            prefectures.add(line.split()[0])
    print(prefectures)


if __name__ == '__main__':
    file = sys.argv[1]
    get_str_set(file)