str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.split()
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

for i, element in enumerate(str):
    if i + 1 in single:
        dict[i + 1] = element[0]
    else:
        dict[i + 1] = element[0:2]
print(dict)
