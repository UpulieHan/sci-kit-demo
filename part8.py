#RGB images can be converted to grayscale and wiseversa
#Computational complexity is reduced when grayscale images are used

from skimage import data, color, io

#[height, width,channel] (a grayscale image would not have any channel(no color information))
image = data.astronaut()

gray = color.rgb2gray(image) #conversion to grayscale
color = color.gray2rgb(gray) #back to color

print(gray.shape)
print(color.shape)

io.imshow_collection([gray, color,image])
io.show()

