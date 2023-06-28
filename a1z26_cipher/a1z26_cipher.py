# convert every string index to integer numbers
def encode(plain):
    return [ord(elm) for elm in plain]


# convert integer numbers to their unicode character
def decode(plain):
    return "".join(chr(elm) for elm in plain)


# test of algorithm with random input
print(encode('majed'))
