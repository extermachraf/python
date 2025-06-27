def my_filter(func, iterable):
    for itr in iterable:
        if func(itr):
            yield itr
    
    # if func is not None:
    #     return [i for i in iterable if func(i)]
    # else
    #     return [i for i in iterable if i]
    
    
