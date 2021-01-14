# Image segmentation
# The process of diving an image into segments(pixels) for highlighting and detecting areas of interest
# Helpful in making the image analysis more effective

# Used algorithms include (scikit provides built-in modules for some of these algorithms)
# Chan-Vese
# Random walker
# Felzenswalb

from skimage import data, io, feature, segmentation

image = data.camera()

#feature module contains many functionns to attain object,image detection
#canny() is a multi-stage edge detector
#it detects the edges of objects present in the image
# use canny edge detector from feature module
edges = feature.canny(image, sigma=3) #sigma as 3, effectively reduces the noice and gives a clear edge

#segmentation module incorporates many algorithms,object detection,image segmentation functions
#mark_boundaries() will  mark the boundaries detected by the canny edge detector
# use mark_boundaries from segmentation module to mark the edges and display the image
io.imshow(segmentation.mark_boundaries(image, edges))
io.show()
