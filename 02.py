str_1 = "パトカー"
str_2 = "タクシー"
str_3 = ""

for a, b in zip(str_1, str_2):
    str_3 = str_3 + a + b
print(str_3)