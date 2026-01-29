import os


def updateProgressBar(lst, progress):
    """
    """
    infoSize = 40
    rangeSize = len(str(len(lst)))
    minSize = (rangeSize * 2) + infoSize + 1
    termSize = os.get_terminal_size().columns
    if (minSize > termSize):
        pBarTotalSize = 1
    else:
        pBarTotalSize = termSize - infoSize
    percent = ((progress * 100) / len(lst)) / 100
    pBarActualSize = (percent * pBarTotalSize)
    bar = ''
    i = 0
    while i < int(pBarTotalSize):
        if (i <= int(pBarActualSize)):
            bar += '█'
        else:
            bar += ' '
        i += 1
    progressBar = str(f"{percent:.0%}").rjust(4) + '|' + bar + '| ' + str(progress + 1) + '/' + str(len(lst))
    print(progressBar, end='\r', flush=True)


def ft_tqdm(lst: range):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    for i in lst:
        yield updateProgressBar(lst, i)
