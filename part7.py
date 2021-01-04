#Color manipulation using scikit-image

#Grayscale image - they depict the intensity of light and do not give other color information.
#The tonal representation of grayscale images are between 0 (pure black) and 255 (pure white)

#Color image - broadly have 3 layers/channels (Red Green Blue)
#You can separate each layer as such
from skimage import data, io

image = data.chelsea()


#R, G, B
image[:, :, 0] = 0 #blue
# image[:, :, 1] = 0 #red
# image[:, :, 2] = 0 #green
io.imshow(image)
io.show()