import imageio as iio
import numpy as np


def ft_load(path: str) -> np.array: 
    ft_load.__doc__="This display the shape of an image"
    #handle error path, format, other
    img= iio.imread(path)
    i = 0
    phrase = "The shape of image is: " + str(tuple(img.shape)) + '\n'+ str(img)
    lst = np.array(phrase)
    return lst

if __name__ == "__main__":
    ft_load()
