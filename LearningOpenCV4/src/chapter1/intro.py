import cv2

grayImage = cv2.imread('../../images/car.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('../output/gray.jpg', grayImage)

# cameraCapture = cv2.VideoCapture(0)
# fps = 30  # an assumption
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)))
# videoWriter = cv2.VideoWriter(
#     '../output/myvid.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
#     fps, size)
