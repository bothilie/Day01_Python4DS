import imageio.v2 as iio
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np 
from load_image import ft_load

def ft_transpose(arr: []) -> []: 
    M1=arr
    n=len(M1)
    p=len(M1[0])
    M2=[0]*p
    for i in range(len(M2)):
        M2[i]=n*[0]
    for i in range(n):
        for j in range(p):
            M2[j][i]=M1[i][j]
    M2 = np.array(M2)
    return M2



def main(path: str):
    main.__doc__ = "This function cut a square part from an image and transpose it"
    #verify path
    #verify dimensions to slice and transpose
    print(ft_load(path))
    img= iio.imread(path)
    L = img[80:480, 450:850]
    #print("New shape after slicing:"+ str(tuple(L.shape)))
    M2 = ft_transpose(img)
    print("New shape after Transpose: "+ str(tuple(M2.shape)))
    print(M2)
    iio.imwrite("new.jpeg", M2)
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
    main("new.jpeg")
    #help(main)