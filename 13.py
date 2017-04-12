# def merge_cols(first_file, second_file):
#     with open(first_file) as ff:
#         first_col = ff.readlines()
#         for i, col in enumerate(first_col):
#             col = col.replace('\n', '\t')
#             first_col[i] = col
#     with open(second_file) as sf:
#         second_col = sf.readlines()
#     new_col = []
#     for i in range(len(first_col)):
#         new_col.append(first_col[i] + second_col[i])
#     new_col = "".join(new_col)
#     with open('new_col.txt', 'w') as writer:
#         writer.writelines(new_col)
#
#
# merge_cols('col1.txt', 'col2.txt')

def merge_cols(file_1, file_2):
    with open(file_1) as f1, open(file_2) as f2:
        lines1, lines2 = f1.readlines(), f2.readlines()

    with open("new_col.txt", "w") as writer:
        for col1, col2 in zip(lines1, lines2):
            writer.write("\t".join([col1.rstrip(), col2]))

merge_cols('col1.txt', 'col2.txt')