# Saving an image
#done using imsave() (takes the image,location,desired name,format)
from skimage import data, io
image = data.logo()
#skimage should be a present location
io.imsave('skimage/logo.png',image)