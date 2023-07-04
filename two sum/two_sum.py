def two_sum(numbers, target):
    # set initial index
    p1 = 0
    p2 = len(numbers)-1

    # i
    while p1 < p2:
        # sum two number
        s = numbers[p1] + numbers[p2]
        if s == target:
            # found two targets
            return [p1 + 1, p2 + 1]
        elif s > target:
            # sum is bigger than desired number
            p2 -= 1
        else:
            # sum is lower than desired number
            p1 += 1


print(two_sum([2, 7, 11, 15], 22))
