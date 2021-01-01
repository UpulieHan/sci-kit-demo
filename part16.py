# Image thresholding
# Useful in isolating objects in an image for apps like facial recognition, object detection
# Chiefly separates the background from the foreground(simplest method of image segmentation)
# Works best in high contrasted images

# Two types of thresholding in scikit
# Global - histogram based, performs well with a uniform background, applied when image is highly contrasted
# Local - adaptive, used for images with unevenly illuminated backgrounds

# Basic steps
# 1.Convert the RGB image to Grayscale
# 2.Set a threshold value (Eg: 127)
# 3.Use '>' operator for thresholding and '<=' for inverted thresholding
# 4.Show the image

from skimage import data, io

image = data.camera()

thresh = 127

binary1 = image > thresh
binary2 = image <= thresh  # for inverted thresholding

io.imshow(binary1)
io.show()

# inverted
io.imshow(binary2)
io.show()
