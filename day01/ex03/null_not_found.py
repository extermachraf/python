import math

def NULL_not_found(object: any) -> int:
    if object == None:
        print(f'Nothing: {object} {type(object)}')
        return 0
    elif isinstance(object, (int, float)) and math.isnan(object):
        print(f'Cheese: {object} {type(object)}')
        return 0
    elif not isinstance(object, bool) and object == 0:
        print(f'Zero: {object} {type(object)}')
        return 0
    elif isinstance(object, str) and  object == "":
        print(f'Empty: {type(object)}')
        return 0
    elif object == False:
        print(f'Fake: {object} {type(object)}')
        return 0
    elif object == True:
        print(f'Not fake: {object} {type(object)}')
        return 0
    else:
        print('Type not Found')
        return 1