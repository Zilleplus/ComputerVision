import cv2
import numpy as np
import os


img = np.zeros((3, 3), dtype=np.uint8)
img_brg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

image_read = cv2.imread('../../images/beans.jpg')

# make the array
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

# convert the array to grayscale
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('../output/randomGray.jpg', grayImage)

# conver the array to color
brgImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('../output/randomColor.jpg', brgImage)
