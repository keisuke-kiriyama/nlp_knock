from collections import defaultdict


def get_high_freq(file):
    prefectures = defaultdict(int)
    with open(file) as f:
        line = f.readline()
        while line:
            prefectures[line.split()[0]] += 1
            line = f.readline()
        print(prefectures)
    for k, v in sorted(prefectures.items(), key=lambda x: x[1], reverse=True):
        print(k)



if __name__ == '__main__':
    file = 'hightemp.txt'
    get_high_freq(file)