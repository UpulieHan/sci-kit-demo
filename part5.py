# To resize an image
from skimage import data, io, transform

image = data.coffee()
img = transform.resize(image, (100, 100), anti_aliasing=True)
io.imshow(img)
io.show()
print(img.shape)
