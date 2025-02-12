import numpy as np 


def slice_me(family: list, start: int, end: int) -> list:
    slice_me.__doc__ = "This slice an array" #ne fonctionne pas
    if not isinstance(family, list):
        print("there is no list as first argument")
        return[]
    if not isinstance(start, int) or not isinstance(end, int):
        print("there is no int as second or third argument")
        return[]  
    if start < 0:
        start = strat * -1
    if end < 0:
        end = end * -1
    if not family:
        print("empty list")
        return[]
    size = len(family[0])
    for x in family:
        if x != size:
            print("not the same size")
            return[]
    tab = np.array(family)
    length = len(family)
    print(f"My shape is : ({length},{tab.ndim})")
    tab.reshape(length, tab.ndim)
    L = tab[start:end,:]
    print(f"My shape is : ({end-start},{L.ndim})")    
    help(slice_me)
    print(L)

if __name__ == "__main__":
    slice_me()