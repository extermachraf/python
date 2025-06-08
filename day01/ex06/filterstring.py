from ft_filter import my_filter

def isLowerThan(number: int, ref: int):
    return number < ref

result = list(my_filter(lambda x: x >= 2, [1, 2, 3, 4]))