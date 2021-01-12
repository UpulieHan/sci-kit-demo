#Trying the same with other color channels
# CEILAB
# XYZ

# HSV - (Hue, Saturation, Value)
# Hue is the degree on the color wheel (0,120 for blue,240 for green, 360 for red)
# Saturation is the percentage of color (0 white, 100 full color)
# Value is the amount of black and white in an image

from skimage import data, io, color

image = data.coffee()

img = color.rgb2hsv(image)
io.imshow(img)
io.show()
