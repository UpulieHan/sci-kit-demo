# Example of histogram using exposure module and matplotlib library

from skimage import data
import matplotlib.pyplot as plt
from skimage.exposure import histogram

image = data.coins()
#histogram is useful in image processing(thresholding(simplest method in image segmentation),adjusting brightness and contrast,analyzing an image)
hist = histogram(image)
plt.plot(hist[0])
plt.show()
