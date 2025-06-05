import sys
import string


def handle_user_input() -> str:
    """Gets input from args or prompt."""
    args = sys.argv
    if len(args) > 2:
        print(
            "AssertionError: more than one argument is provided",
            file=sys.stderr
        )
        sys.exit(1)
    if len(args) == 2:
        return args[1]
    else:
        try:
            return input("What is the text to analyze?\n")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


def analyze_text(text: str) -> dict:
    """Counts char types in text."""
    return {
        "total": len(text),
        "uppers": len(list(filter(str.isupper, text))),
        "lowers": len(list(filter(str.islower, text))),
        "punctuation": len(
            list(filter(lambda c: c in string.punctuation, text))
        ),
        "spaces": len(list(filter(str.isspace, text))),
        "digits": len(list(filter(str.isdigit, text))),
    }


def display_result(stats: dict) -> None:
    """Prints stats."""
    print(f"The text contains {stats['total']} characters:")
    print(f"{stats['uppers']} upper letters")
    print(f"{stats['lowers']} lower letters")
    print(f"{stats['punctuation']} punctuation marks")
    print(f"{stats['spaces']} spaces")
    print(f"{stats['digits']} digits")


def main():
    """Runs the program."""
    try:
        user_input = handle_user_input()
        result = analyze_text(user_input)
        display_result(result)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
