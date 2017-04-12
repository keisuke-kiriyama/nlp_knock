sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.split()
sentence_len = []

for word in sentence:
    sentence_len.append(len(word))
print(sentence_len)