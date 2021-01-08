# Displaying an image from a directory
import os
from skimage import io

# to import an image from a directory in our system
file = os.path.join('skimage_data', 'books.jpg')
book = io.imread(file)
io.imshow(book)
io.show()

