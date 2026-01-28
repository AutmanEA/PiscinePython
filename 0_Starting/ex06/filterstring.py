import sys
from ft_filter import ft_filter


def isStringValid(string: str) -> bool:
    """
    returns True if param string contains only
    alphanumeric or space characters
    """
    for char in string:
        if not (char.isalnum() or (char == " ")):
            return False
    return True


def main():
    """
    Filterstring takes a string and show all
    words bigger than len limit specified in 2nd argument
    """
    try:
        assert len(sys.argv) == 3, "AssertionError: bad arguments"
        assert isStringValid(sys.argv[1]), "AssertionError: bad arguments"
        assert sys.argv[2].isnumeric(), "AssertionError: bad arguments"
        wordlist = sys.argv[1].split()
        minlen = int(sys.argv[2])
        newlist = list(ft_filter(lambda x: len(x) > minlen, wordlist))
        print(newlist)
    except AssertionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nInterrupted")
    except Exception:
        print("Fatal error: something went wrong")


if __name__ == "__main__":
    main()
