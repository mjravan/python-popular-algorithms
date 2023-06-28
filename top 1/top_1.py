"""
    top one
    [1, 2, 1, 3, 2] => [1, 2]
"""


def top_1(arr):
    # making a dict, empty list(storage) and counter of Top Ones
    values = {}
    result = []
    f_val = 0

    for i in arr:
        if i in values:
            # the number existed counting 1  for it
            values[i] += 1
        else:
            # the number is new
            values[i] = 1
    # storing top one numbers
    f_val = max(values.values())

    # checking most top numbers
    for i in values.keys():
        if values[i] == f_val:
            # showing most top ones
            result.append(i)
        else:
            continue

    return result


print(top_1([1, 2, 1, 3, 2]))
