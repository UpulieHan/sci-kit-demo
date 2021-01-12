# Histogram - a graphical representation of the tonal distribution in a digital image
# The intensity of an image at each different pixel depending on its color is depicted using a histogram
# The Red Blue and Yellow as have corresponding histogram
# Intensity, 0 - pure black, 255 - pure white

from skimage import data
import matplotlib.pyplot as plt

image = data.coins()
# plotting of the histogram(intensities 0-255 are depicted using bins(there are 245 bins))
# Sometimes representing each intensity value is not needed. (Then quantize them into several groups(thus bins))
histogram = plt.hist(image.ravel(), bins=4)
plt.show()
