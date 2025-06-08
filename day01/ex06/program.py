from part1.ft_filter import my_filter
import sys
import re 


def parseArgs(args: list) -> tuple[list[str], int]:
    try:
        if len(args) != 3:
            raise AssertionError("Program should receive exactly 2 arguments")
        counter: int = int(args[2])
        isNotSafe: bool = not bool(re.fullmatch(r"[A-Za-z0-9 ]*", args[1]))
        if isNotSafe:
            raise AssertionError("the first arg should not containe a special caracters att all")
        return [args[1].split(), counter]
    except ValueError as e:
        raise AssertionError("the second arg should be a number")
        

def main():
    args: list = sys.argv
    try:
        data: tuple =  parseArgs(args)
        words, counter = data
        result: list = list(my_filter(lambda x: len(x) > counter, words))
        print(result)
    except AssertionError as e:
        print(e, file=sys.stderr)
        
    
if __name__ == "__main__":
    main()