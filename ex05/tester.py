from load_image import ft_load
import imageio as iio
from pimp_image import ft_invert
from pimp_image import ft_red, ft_green, ft_blue, ft_grey


array = ft_load("landscape.jpg")
M1 = ft_invert(array)
iio.imwrite("new_invert.jpeg", M1)
array = ft_load("landscape1.jpg")
M2 = ft_red(array)
if M2:
    iio.imwrite("new_red.jpeg", M2)
array = ft_load("landscape.jpg")
M3 = ft_green(array)
iio.imwrite("new_green.jpeg", M3)
array = ft_load("landscape.jpg")
M4 = ft_blue(array)
iio.imwrite("new_blue.jpeg", M4)
array = ft_load("landscape.jpg")
M5 = ft_grey(array)
iio.imwrite("new_grey.jpeg", M5)
print(ft_red.__doc__)