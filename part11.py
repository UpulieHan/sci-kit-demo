# Editing an image
# Applying filters (using filter modules)
# assits in various thresholding techniques
# assits in applying numerous filter algorithms onto an image

from skimage import filters
from skimage import data, io

image = data.astronaut()
image_median = filters.median(image)  # median turns a smoothened out image

io.imshow_collection([image_median, image])
io.show()
