import cv2
import numpy as np


# I don't need this downsampling
# img = cv2.pyrDown(cv2.imread("../../images/hammer.jpeg"),
#                   cv2.IMREAD_UNCHANGED)
img = cv2.imread("../../images/hammer.jpeg")
kernel = np.ones((5, 5), np.uint8)
# this doesn't work, but quiet interesting
# img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_grey, 127, 255, cv2.THRESH_BINARY)

# cv2.RETR_EXTERNAL -> only return the outer contours
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                  cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # find the bouding box coordinates
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img=img, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0),
                  thickness=2)

    # find minimum area
    # (center(x, y), (width, height), angle_of_rotation)
    #      = cv2.minAreaRect(points)
    rect = cv2.minAreaRect(c)
    # calucate coordinates of the minimum area rectangle
    box = cv2.boxPoints(rect)
    # normalize coordinates to integers
    box = np.int0(box)
    # draw contours
    cv2.drawContours(
        image=img,
        contours=[box],
        contourIdx=0,
        color=(0, 0, 255),
        thickness=3)

    # calculate center and radius of minimum enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    # cast to integers
    center = (int(x), int(y))
    radius = int(radius)
    # draw the circle
    img = cv2.circle(img=img, center=center, radius=radius, color=(0, 255, 0),
                     thickness=2)

cv2.drawContours(
    image=img,
    contours=contours,
    contourIdx=-1,
    color=(255, 0, 0),
    thickness=1)
cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()
