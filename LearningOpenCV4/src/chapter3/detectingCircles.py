import cv2
import numpy as np


img = cv2.imread('../../images/nasa_logo.png')
assert img is not None, "can't read the image"
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.medianBlur(gray_img, 5)
circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 120,
                           param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    _ = cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
# draw the center of the circle
_ = cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow("HoughCirlces", img)
cv2.waitKey()
cv2.destroyAllWindows()
