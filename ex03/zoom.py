import imageio.v2 as iio
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#import numpy as np 
from load_image import ft_load

def main(path: str):
    main.__doc__ = "This function zoom to an image"
    print(ft_load(path))
    img= iio.imread(path)
    L = img[80:480, 450:850, :]
    print("New shape after slicing:"+ str(tuple(L.shape)))
    print(L)
    iio.imwrite("new.jpeg", L)
    img = mpimg.imread('new.jpeg')
    imgplot = plt.imshow(img)
    plt.show()

#The size in pixel on both X and Y axis
#The number of channel
#The pixel content of the image.
#Display the scale on the x and y axis on the image
#colors ???
#verify numpy

if __name__ == "__main__":
    main("animal.jpeg")
    #help(main)