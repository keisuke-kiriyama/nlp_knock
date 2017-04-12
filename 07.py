def template(x, y, z):
    return str(x) + u'時の' + str(y) + u'は' + str(z)

x = 12
y = u'気温'
z = 22.4

sentence = template(x, y, z)
print(sentence)