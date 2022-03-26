import cv2
import numpy as np


img = cv2.imread("../../images/hammer.jpeg")

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                            127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                  cv2.CHAIN_APPROX_SIMPLE)

black = np.zeros_like(img)
for cnt in contours:  # cnt is closed -> pull closed=True in calls
    # epsilon: maximum difference between approximation
    # and real contour.
    # arcLength: length across the curve, if curve is straighted out
    # it should stay constant
    epsilon = 0.01*cv2.arcLength(curve=cnt, closed=True)
    # approximation using Douglas-Peucker algo
    approx = cv2.approxPolyDP(curve=cnt, epsilon=epsilon, closed=True)
    convex_hull = cv2.convexHull(cnt)
    cv2.drawContours(black, [cnt], -1, (0, 255, 0), 2)
    cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
    cv2.drawContours(black, [convex_hull], -1, (0, 0, 255), 2)

cv2.imshow("convex_hull", black)
cv2.waitKey()
cv2.destroyAllWindows()
