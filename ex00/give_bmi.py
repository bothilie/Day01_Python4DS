import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    give_bmi.__doc__ = "This function give the bmi of a person"
   # prendre en compte si height ou weight ne sont pas int ou float
    a = np.array(height)
    b = np.array(weight)
    if a.dtype != 'd' and a.dtype != 'f':
        AssertionError("not an int")
        return[]
    c = a**2
    if not c.all():
        return []
    else:
        try:
            d = b / c
        except:
            AssertionError("not the same dimension")
            return []
        return d.tolist()
    return []

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    apply_limit.__doc__ = "This function return a list of boolean that returns True is the bmi attein the limit"
    lst = list()
    if not bmi:
        return lst
    for x in bmi:
        if x > limit:
            lst.append(True)
        else:
            lst.append(False)
    return lst

if __name__ == "__main__":
    main()


