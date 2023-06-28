def rotate(s, k):
    # making double_s to move on character index
    double_s = s + s
    if k <= len(s):
        # key is smaller than length of string
        return double_s[k:len(s)+k]
    else:
        # key is bigger than length of string
        return double_s[k-len(s):k]


print(rotate('hello', 6))
