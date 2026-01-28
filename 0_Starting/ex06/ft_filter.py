def ft_filter(function, iterable, /):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if (function):
        return (elem for elem in iterable if function(elem))
    return (elem for elem in iterable if elem)
