import cv2
import filters
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        self._window_manager = WindowManager('Cameo', self.onKeypress)
        self._capture_manager = CaptureManager(
            capture=cv2.VideoCapture(0),
            previewWindowManager=self._window_manager,
            shouldMirrorPreview=True)
        self._curveFilter = filters.BGRCurveFilter()

    def run(self):
        """Run the main loop"""
        self._window_manager.createWindow()
        while self._window_manager.isWindowCreated:
            self._capture_manager.enterFrame()
            frame = self._capture_manager.frame
            if frame is not None:
                filters.strokesEdge(frame, frame)
                self._curveFilter.apply(frame, frame)
            self._capture_manager.exitFrame()
            self._window_manager.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.
        space -> Take a screenshot.
        tab -> Start/stop recording a screencast.
        escape -> Quit.
        """
        if keycode == 32:  # space
            self._capture_manager.writeImage('../output/screenshot.png')
        elif keycode == 9:  # tab
            if not self._capture_manager.isWritingImage:
                self._capture_manager.startWritingVideo('../output/screencast.avi')
            else:
                self._capture_manager.stopWritingVideo()
        elif keycode == 27:  # escape
            self._window_manager.destroyWindow()


if __name__ == "__main__":
    Cameo().run()
