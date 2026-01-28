import sys


def generateMorse():
    """
    generates a morse dictionnary
    """
    return {
        ' ': '/',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }


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
        assert len(sys.argv) == 2, "AssertionError: bad arguments"
        assert isStringValid(sys.argv[1]), "AssertionError: bad arguments"
        morse = generateMorse()
        stringToConvert = sys.argv[1]
        stringConverted = ""
        for char in stringToConvert:
            stringConverted += morse[char.upper()] + " "
        print(stringConverted[:-1])
    except AssertionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nInterrupted")
    except Exception:
        print("Fatal error: something went wrong")


if __name__ == "__main__":
    main()
