import sys

# def split_col(file, write_file_first, write_file_second):
#     with open(file) as f:
#         lines = f.readlines()
#         for line in lines:
#             first_col = get_first_col(line)
#             second_col = get_second_col(line)
#             with open(write_file_first, "w") as writer:
#                 writer.writelines(first_col)
#             with open(write_file_second, "w") as writer:
#                 writer.writelines(second_col)
#
#
#
# def get_first_col(line):
#     cols = line.split("\t")
#     return cols[0]
#
#
# def get_second_col(line):
#     cols = line.split("\t")
#     return cols[1]

def split_col(file, col_number, write_file):
    col = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            col.append(line.split("\t")[col_number] + "\n")
        col = "".join(col)
    with open(write_file, "w") as writer:
        writer.writelines(col)


if __name__ == '__main__':
    split_col('hightemp.txt', 0, 'col1.txt')
    split_col('hightemp.txt', 1, 'col2.txt')
