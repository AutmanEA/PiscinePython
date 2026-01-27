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
    print(f"The text contains {len(s)} characters:")
    print(s)


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
                print("What is the text to count ?")
                str = input()
            case 2:
                str = sys.argv[1]
        countStr(str)
    except AssertionError as e:
        print(e)
    except EOFError:
        pass
    except:
        print("Fatal error: something went wrong")


if __name__ == "__main__":
    main()
