import cv2
import numpy as np


def video_processing(frame):
    yellow_lower = np.array([22, 60, 200], np.uint8)
    yellow_upper = np.array([60, 255, 255], np.uint8)

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellow = cv2.inRange(frameHSV, yellow_lower, yellow_upper)
    # Eliminamos el posible ruido
    kernel_1 = np.ones((5, 5), np.uint8)
    yellow = cv2.dilate(yellow, kernel_1)
    res_yellow = cv2.bitwise_and(frame, frame, mask=yellow)

    # Tracking yellow
    total = 0
    contours, hierarchy = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 6000):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            total += 1

    # 5.Poner texto en imagen
    # letrero = 'Plazas: ' + str(total)
    # cv2.putText(frame, letrero, (350, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 4)
    return total
