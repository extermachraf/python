def all_thing_is_obj(Object: any) -> int:
    if isinstance(Object, list):
        print(f"List : {type(Object)}")
    elif isinstance(Object, tuple):
        print(f"Tuple : {type(Object)}")
    elif isinstance(Object, set):
        print(f"Set : {type(Object)}")
    elif isinstance(Object, dict):
        print(f"Dict : {type(Object)}")
    elif isinstance(Object, str):
        print(f"{Object} is in the kitchen : {type(Object)}")
    else:
        print("Type not found")
    return 42