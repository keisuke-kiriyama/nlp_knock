import sys


def split_text(file_name, n):
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) % n != 0:
            raise Exception("Undividable by N=%d" % n)
        else:
            num_of_lines = int(len(lines) / n)
        for i in range(n):
            with open("text%s.txt" % str(i), "w") as writer:
                writer.writelines(lines[i*num_of_lines:i*num_of_lines + num_of_lines])


if __name__ == "__main__":
    n = int(sys.argv[1])
    try:
        split_text("hightemp.txt", n)
    except Exception as err:
        print(err)