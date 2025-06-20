import sys

def check_if_odd(number : int) -> str:
    if number % 2 != 0:
        return "I'm Odd."
    return "I'm Even."

if not len(sys.argv) == 2:
    print('AssertionError: more than one argument is provided')
    sys.exit(-1)
    
arg = sys.argv[1]

try:
    number = int(arg) 
    print(check_if_odd(int(number)))
except:
    print("AssertionError: the argument is not an integer")
    exit(1)
        