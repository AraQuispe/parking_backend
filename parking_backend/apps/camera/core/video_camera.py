import threading

import cv2


class VideoCamera(object):
    def __init__(self, address):
        #self.video = cv2.VideoCapture('rtsp://admin:XLKAWA@192.168.0.6/video')
        self.video = cv2.VideoCapture(address)
        (self.grabbed, self.frame) = self.video.read()

        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
