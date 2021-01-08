#Python image processning libraries available
# Numpy, Scipy, Scikit, OpenCV, Python Image Library(PIL)

#An image
#Can be represented by a 2D arrays
# (each grid/pixel of an array represents a pixel in the image)
#A digital image can be classified into 2 types of channels: grayscale, multichannel
#Grayscale - only grey shades(different tones of black and white)
#Multichannel RGB - has 3 layers (Red, Green, Blue)

#About Scikit
#Opensource
#A Python package
#Works with NumPy arrays

#To install a package,
#pip install scikit-image
#or
#file -> settings -> project -> + search for the package -> install

# Displaying an image from the library itself
from skimage import data, io

#scikit includes a file with some preloaded images in them(inside the 'data' module)
image = data.coffee()
#imshow() displays an image
io.imshow(image)
#show() displays the pending images queued by imshow(used when displaying images from non-interactive shells)
io.show()


