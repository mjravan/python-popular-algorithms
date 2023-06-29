# document for alphabet letters
from string import ascii_letters


def encrypt(string, key):
    # setting a variable and storage(result)
    alpha = ascii_letters
    result = ''

    for ch in string:
        # for other character like(/-\@)
        if ch not in alpha:
            result += ch
        else:
            # adding key to char index and save it into result
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result


# reversing key to decrypt string
def decrypt(string, key):
    key *= -1
    return encrypt(string, key)


print(encrypt('amir', 4))

