#Global thresholding algorithms
# Applied when image is highly contrasted with a uniform background

from skimage.filters import try_all_threshold
from skimage import data, io

image = data.page()
thresh = try_all_threshold(image)
io.show()

