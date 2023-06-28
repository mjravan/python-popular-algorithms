def move_zeros(seq):
    # making a empty list and initial value
    result = []
    zero = 0

    for i in seq:
        if i == 0 and type(i) != bool:
            # found zero. counting it in variable
            zero += 1
        else:
            # not zero. return back the number
            result.append(i)
    # final result
    result.extend([0] * zero)
    return result


print(move_zeros([False, 1, 0, 2, 0, 1]))
