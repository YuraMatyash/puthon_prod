# обединение аргументов в tuple
def sum_nums(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)

print(sum_nums(2, 3, 5))