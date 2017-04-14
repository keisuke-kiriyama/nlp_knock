import sys


def get_start_lines(n):
    with open("hightemp.txt") as f:
        lines = f.readlines()
        for line in lines[:int(n)]:
            print(line)


if __name__ == '__main__':
    n = sys.argv[1]
    get_start_lines(n)