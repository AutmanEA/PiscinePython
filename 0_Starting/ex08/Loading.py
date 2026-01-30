import os


def updateProgressBar(lst, idx):
    """
    creates a progress bar based on terminal column size
    and progession in lst range (his index named idx)
    """
    infoSize = 40
    lstLen = str(len(lst))
    lstNbSize = len(lstLen)
    minSize = (lstNbSize * 2) + 1 + infoSize
    termSize = os.get_terminal_size().columns
    if (minSize > termSize):
        pBarTotalSize = 1
    else:
        pBarTotalSize = termSize - infoSize
    pct = ((idx * 100) / len(lst)) / 100
    pBarActualSize = (pct * pBarTotalSize)
    pBar = '|'
    i = 0
    while i < int(pBarTotalSize):
        if (i <= int(pBarActualSize)):
            pBar += '█'
        else:
            pBar += ' '
        i += 1
    pBar += '|'
    lstRatio = str(idx + 1) + '/' + lstLen
    output = str(f"{pct:.0%}").rjust(4) + pBar + ' ' + lstRatio
    print(output, end='\r', flush=True)


def ft_tqdm(lst: range):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    for i in lst:
        yield updateProgressBar(lst, i)
