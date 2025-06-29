import sys

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}


def textToNorse(text: str) -> str:
    nors_char: list = []
    for char in text.upper():
        if char not in NESTED_MORSE:
            msg = f"Character '{char}' cannot be translated to Morse code."
            raise ValueError(msg)
        nors_char.append(NESTED_MORSE[char])
    return ''.join(nors_char)


def parse_args(args: list):
    if (len(args) != 2):
        raise AssertionError("the program take only one argument")


def main():
    args: list = sys.argv
    try:
        parse_args(args)
        norse_result = textToNorse(args[1])
        print(norse_result)
    except AssertionError or ValueError as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    main()
