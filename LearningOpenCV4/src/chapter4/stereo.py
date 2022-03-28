import numpy as np
import cv2


# Minimum possible disparity value. Normally, it is zero, but sometimes
# rectification algorithms can shift images so this parameter needs to be
# adjusted accordingly.
minDisparity = 16
# Maximum disparity minus minimum disparity. The value is always
# greater than zero. In the current implementation, this parameter must
# be divisible by 16.
numDisparities = 192 - minDisparity
# Matched block size. It must be an odd number >=1 . Normally, it should
# be somewhere in the 3-11 range.
blockSize = 5
# Margin in percentage by which the best (minimum) computed cost
# function value should win the second best value to consider the found
# match correct. Normally, a value within the 5-15 range is good enough.
uniquenessRatio = 1
# Maximum size of smooth disparity regions to consider their noise
# speckles and invalidate. Set it to 0 to disable speckle filtering.
# Otherwise, set it somewhere in the 50-200 range.
speckleWindowSize = 3
# Maximum disparity variation within each connected component. If you
# do speckle filtering, set the parameter to a positive value; it will be
# implicitly multiplied by 16. Normally, 1 or 2 is good enough.
speckleRange = 3
# Maximum allowed difference (in integer pixel units) in the left-right
# disparity check. Set it to a non-positive value to disable the check.
disp12MaxDiff = 200
# P1 is the penalty on the
# disparity change by plus or minus 1 between neighbor pixels.
P1 = 600
# P2 is the penalty on the
# disparity change by more than 1 between neighbor pixels.
P2 = 2400
# The algorithm requires P2 > P1 .
stereo = cv2.StereoSGBM_create(
    minDisparity=minDisparity,
    numDisparities=numDisparities,
    blockSize=blockSize,
    uniquenessRatio=uniquenessRatio,
    speckleRange=speckleRange,
    speckleWindowSize=speckleWindowSize,
    disp12MaxDiff=disp12MaxDiff,
    P1=P1,
    P2=P2)
imgL = cv2.imread('../../images/color1_small.jpg')
imgR = cv2.imread('../../images/color2_small.jpg')
disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0
cv2.imshow('Disparity', (disparity - minDisparity) / numDisparities)
cv2.waitKey()
cv2.destroyAllWindows()
