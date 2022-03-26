import cv2
import numpy as np
import utils


def strokesEdge(src, dst, blurKSize=7, edgeKsize=5):
    if blurKSize >= 3:
        # blur the image
        blurredSrc = cv2.medianBlur(src, blurKSize)
        # convert to gray
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
    else:
        # convert to gray
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)
    # normalize the image so the image has values between 0 and 1
    normalizeInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizeInverseAlpha
    cv2.merge(channels, dst)


class VConvolutionFilter(object):
    """A filter that applies a convolution to V (or all of BGR)."""
    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        """Apply the filter with a BGR or gray source/destination"""
        # ddetpth=-1 -> the same range is used to represent the image.
        cv2.filter2D(src=src, ddepth=-1, kenel=self._kernel, dst=dst)


class SharpenFilter(VConvolutionFilter):
    """A sharpen filter with 1-pixel radius"""
    def __init__(self):
        # The sum of the kernel is 1, as we need a
        # filter image. And we don't want to change
        # the brightness of the image.
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class FindEdgesFilter(VConvolutionFilter):
    """And edge-finding filter with a 1-pixel radius"""
    def __init__(self):
        # We need edges, so the sum of kernel is 0.
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """A blur with with a 2-pixel radius"""
    def __init__(self):
        kernel = np.ones((4, 4)) * 0.04
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """An emboss filter with a 1-pixel radius"""

    def __init__(self):
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)


class BGRFuncFilter(object):
    """A filter that applies different functions to each of BGR."""
    def __init__(self, vFunc=None, bFunc=None, gFunc=None,
                 rFunc=None, dtype=np.uint8):
        length = np.iinfo(dtype).max + 1
        self._bLookupArray = utils.createLookupArray(
            utils.createCompositeFunc(bFunc, vFunc), length)
        self._gLookupArray = utils.createLookupArray(
            utils.createCompositeFunc(gFunc, vFunc), length)
        self._rLookupArray = utils.createLookupArray(
            utils.createCompositeFunc(rFunc, vFunc), length)

    def apply(self, src, dst):
        """Apply the filter with a BGR source/destination."""
        b, g, r = cv2.split(src)
        utils.applyLookupArray(self._bLookupArray, b, b)
        utils.applyLookupArray(self._gLookupArray, g, g)
        utils.applyLookupArray(self._rLookupArray, r, r)
        cv2.merge([b, g, r], dst)


class BGRCurveFilter(BGRFuncFilter):
    """A filter that applies different curves to each of BGR."""
    def __init__(self, vPoints=None, bPoints=None,
                 gPoints=None, rPoints=None, dtype=np.uint8):
        BGRFuncFilter.__init__(self,
                               utils.createCurveFunc(vPoints),
                               utils.createCurveFunc(bPoints),
                               utils.createCurveFunc(gPoints),
                               utils.createCurveFunc(rPoints), dtype)