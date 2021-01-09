# Adjusting brightness
# exposure module is used for analyzing image light intensities using histograms
from skimage import exposure, io, data

image = data.rocket() #by default gamma value is 1
image_bright = exposure.adjust_gamma(image, gamma=0.5)
image_dark = exposure.adjust_gamma(image, gamma=2)

io.imshow_collection([image, image_bright, image_dark])
io.show()
