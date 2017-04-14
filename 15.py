import sys


def get_end_lines(n):
    with open("hightemp.txt") as f:
        lines = f.readlines()
        for line in lines[len(lines) - int(n):]:
            print(line)


if __name__ == '__main__':
    n = sys.argv[1]
    get_end_lines(n)