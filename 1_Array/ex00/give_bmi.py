def check_bmi_lists(lst: list):
    """
    - check_bmi_list checks if height or weight list merged in
    'lst' param are only composed by integers or floats
    - raises exception on error
    """
    err_list = [elem for elem in lst if not isinstance(elem, (int, float))]
    if err_list != []:
        raise Exception("bad inputs in lists = ", err_list)


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    - give_bmi takes a height (h) list and a weight (w) list
    and returns BMI list of each elements of both lists,
    so lists must have same sizes and lists must be composed
    by integers and floats
    - raises exception on error
    """
    if not (isinstance(h, list) and isinstance(w, list)):
        raise Exception("height or weight must be lists")
    if len(h) != len(w):
        raise Exception("Both height and weight lists must have same sizes")
    check_bmi_lists(h + w)
    return [w / pow(h, 2) for h, w in zip(h, w)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    - apply_limit takes a bmi list and checks if every elements in this list
    is above the limit (True) or not (False) and return a bool list of
    all the results
    - raises exception on error
    """
    if not (isinstance(bmi, list) and isinstance(limit, int)):
        raise Exception("Error: height or weight must be lists")
    check_bmi_lists(bmi)
    return [(elem > limit) for elem in bmi]
