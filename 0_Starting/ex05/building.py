import sys


def countStr(s: str):
    """
    Analysis tool for counting text characters
      - upper-case characters
      - lower-case characters
      - punctuations
      - digits
      - spaces

    :param s: Text to count
    :type s: str
    """
    counters = {"upper": 0, "lower": 0, "punct": 0, "digit": 0, "spaces": 0}
    print(f"\nThe text contains {len(s)} characters:")
    for char in s:
        if (char.islower()):
            counters["lower"] += 1
        elif (char.isupper()):
            counters["upper"] += 1
        elif (char.isspace()):
            counters["spaces"] += 1
        elif (char.isdigit()):
            counters["digit"] += 1
        elif (char.isprintable()):
            counters["punct"] += 1
    print(f"""
    + {counters["upper"]} upper letters
    + {counters["lower"]} lower letters
    + {counters["punct"]} punctuation marks
    + {counters["spaces"]} spaces
    + {counters["digit"]} digits
    """)


def main():
    """
    This program counts a single string in argument
    and displays a complete analysis of its characters.

    Throws errors on input or arguments failure.
    """
    try:
        assert len(sys.argv) <= 2, "AssertionError: too many arguments"
        match len(sys.argv):
            case 1:
                str = sys.stdin.readline()
            case 2:
                str = sys.argv[1]
        countStr(str)
    except AssertionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nInterrupted")
    except Exception:
        print("Fatal error: something went wrong")


if __name__ == "__main__":
    main()
