def my_filter(func, iterable):
    for itr in iterable:
        if func(itr):
            yield itr