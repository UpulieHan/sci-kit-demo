from skimage import transform, io, data

image = data.coffee()
#Since resize parameter is on, the corners of the image are also included and no loss of data would occur
#By default resize if set False(corners would be cut of when rotated)
image_rotated = transform.rotate(image, angle=90, resize=True)
io.imshow(image_rotated)
io.show()