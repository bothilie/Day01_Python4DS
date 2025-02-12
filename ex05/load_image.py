import imageio as iio
import numpy as np


def ft_load(path: str) -> []: 
    #handle error path, format, other
    try:
        img= iio.imread(path)
    except:
        AssertionError("path not found")
        return()
    i = 0
    phrase = "The shape of image is: " + str(tuple(img.shape)) + '\n'+ str(img)
    lst = np.array(phrase)
    return img