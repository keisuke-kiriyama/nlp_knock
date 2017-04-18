def sort_by_col3(file):
    with open(file) as f:
        lines = f.readlines()
    for line in sorted(lines, key=lambda x: x.split()[2], reverse=True):
        print(line)

if __name__ == '__main__':
    file = 'hightemp.txt'
    sort_by_col3(file)