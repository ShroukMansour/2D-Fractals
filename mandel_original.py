from PIL import Image
from numpy import complex, array
import colorsys

WIDTH = 200


def rgb_conv(i):
    if i in range(1, 5):
        color = array([0, 0 ,0])
    elif i in range(5, 10):
        color = array([46, 15, 86])
    elif i in range(10, 30):
        color = array([144, 53, 170])
    else:
        # color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
        color = array([220, 178, 245])
    return tuple(color.astype(int))


# function defining a mandelbrot
def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 100):
        if abs(c) > 2:  # circle of radius 2
            return rgb_conv(i)
        c = c * c + c0
    return (235, 230, 246)


img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4))


img.save('originalMandel2.png')
