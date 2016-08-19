def super_sum(*args):
    if type(args) is list:
        result1 = sum(args)
    elif type(args) is int:
        for i in args:
            s = 0
            s = s + i

    return s + result1


print(super_sum(1, 3))
