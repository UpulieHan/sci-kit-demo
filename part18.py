# Or use just one function

from skimage.filters import threshold_otsu
from skimage import data, io

image = data.page()

thresh = threshold_otsu(image)
binary = image > thresh

io.imshow(binary)
io.show()
