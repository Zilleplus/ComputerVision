import cv2
import numpy as np

img = cv2.imread('../../images/table.jpg')
assert img is not None, "can't read the image"
img = cv2.GaussianBlur(img, (5, 5), 0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(image=edges, theta=np.pi/180, rho=1.0,
                        threshold=10, minLineLength=minLineLength,
                        maxLineGap=maxLineGap)
print("we found " + str(len(lines)) + " lines")
for ls in lines:
    for x1, y1, x2, y2 in ls:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
