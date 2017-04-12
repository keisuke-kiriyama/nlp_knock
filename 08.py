def cipher(input):
    ret = ''
    for element in input:
        ret += chr(219 - ord(element)) if element.islower() else element
    print(ret)

str = "Atbash is a simple substitution cipher for the Hebrew alphabet."
cipher(str)
