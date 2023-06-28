def is_isomorphic(s, t):
    # check the length of two string
    if len(s) != len(t):
        return False
    # making a dictionary and setter
    dict = {}
    set_values = set()

    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_values:
                # checking new letter hasn't been set for another one
                return False
            # adding new letter
            dict[s[i]] = t[i]
            # setting letter for second word and using for checking isomorphic
            set_values.add(t[i])
        # checking two letter doesn't be different
        elif dict[s[i]] != t[i]:
            return False

    return True


print(is_isomorphic('paper', 'title'))
