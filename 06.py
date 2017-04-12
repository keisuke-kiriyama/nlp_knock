def get_char_n_gram(str, n):
    n_gram = []
    for i in range(len(str) - n + 1):
        n_gram.append(str[i:i + n])
    return n_gram


X = set(get_char_n_gram("paraparaparadise", 2))
Y = set(get_char_n_gram("paragraph", 2))

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

print('se' in X)
print('se' in Y)