import sys


if (len(sys.argv) <= 1):
    sys.exit()
else:
    arg = sys.argv[1]


def isEven(number: int) -> bool:
    if (number % 2 == 0):
        return True
    return False


def parseArg() -> bool:
    return arg.isnumeric() or (arg.startswith('-') and arg[1:].isnumeric())


try:
    assert (len(sys.argv) == 2), "more than one argument is provided"
    assert parseArg(), "argument is not an integer"
    x = int(arg)
    if isEven(x):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(e)
