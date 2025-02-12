import imageio as iio
import numpy as np


def ft_load(path: str) -> np.array: 
    #handle error path, format, other
    img= iio.imread(path)
    i = 0
    phrase = "The shape of image is: " + str(tuple(img.shape)) + str(img)
    lst = np.array(phrase)
    return lst