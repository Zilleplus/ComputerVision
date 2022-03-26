import cv2

output_file = "../output/canny.jpg"
img = cv2.imread("../../images/statue_small.jpg", 0)
cv2.imwrite(output_file, cv2.Canny(image=img, threshold1=200, threshold2=300))
cv2.imshow("canny", cv2.imread(output_file))
cv2.waitKey()
cv2.destroyAllWindows()
