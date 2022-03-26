import cv2


img = cv2.imread('../../images/5_of_diamonds.png')
cv2.imshow('my image', img)
cv2.waitkey()
cv2.destroyAllWindows()
