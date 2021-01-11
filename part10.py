#A grayscale image can be tinted to the color of choice(by zeroing-out other colors)
from skimage import data, io, color

grayscale_image = data.camera()
image = color.gray2rgb(grayscale_image)

red_multiplier = [1, 0, 0]
yellow_multiplier = [1, 1, 0]

# io.imshow(yellow_multiplier * image)
# io.show()
io.imshow(red_multiplier * image)
io.show()