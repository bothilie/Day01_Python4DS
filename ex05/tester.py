from load_image import ft_load
import imageio as iio
from pimp_image import ft_invert
from pimp_image import ft_red


array = ft_load("landscape.jpg")
ft_invert(array)
M2 = ft_red(array)
iio.imwrite("new.jpeg", M2)
#ft_green(array)
#ft_blue(array)
#ft_grey(array)
print(ft_red.__doc__)