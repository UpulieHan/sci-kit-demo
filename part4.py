#The shape(size) of an image is important at manipulation
#To retrieve the size use 'shape' attribute
from skimage import data

image = data.coffee()
print(image.shape) #(400, 600, 3) 400 is height, 600 is width, 3 indicates that the image is multicolored


