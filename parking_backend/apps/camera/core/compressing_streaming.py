import time


def compressing_streaming(camera, seconds=0):
    time_to_start = time.time()
    if seconds <= 0:
        while True:
            try:
                frame = camera.get_frame()
                yield (
                        b'--frame\r\n'
                        b'Content-Type: image/jpeg  \r\n\r\n' + frame +
                        b'\r\n\r\n'
                )
            except:
                camera.__del__()
    else:
        while ((time_to_start + seconds) - time.time()) >= 0:
            try:
                frame = camera.get_frame()
                yield (
                        b'--frame\r\n'
                        b'Content-Type: image/jpeg  \r\n\r\n' + frame +
                        b'\r\n\r\n'
                )
            except:
                camera.__del__()
