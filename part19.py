# Use the local threshold when in doubt
# It divides the image into small regions and applies the thresh value to them
#Local threshold performs better

from skimage.filters import threshold_local
from skimage import data, io

image = data.page()

#block_size is 35 and offset is 10 (which is to the constant to balance the opposite contrast for obtaining a clearer image)
thresh = threshold_local(image, block_size=35, offset=10)
binary = image > thresh

io.imshow(binary)
io.show()
