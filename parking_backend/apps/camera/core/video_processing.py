import cv2
import numpy as np


def video_processing(frame):
    amarillo_claro = np.array([22, 93, 0], np.uint8)
    amarillo_oscuro = np.array([45, 255, 255], np.uint8)
    # 1.Conversion a Escala de Grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(gray, amarillo_claro, amarillo_oscuro)

    # Eliminamos el posible ruido
    kernel_1 = np.ones((10, 10), np.uint8)
    mascara = cv2.erode(mask, kernel_1, iterations=2)
    mascara = cv2.dilate(mascara, kernel_1, iterations=2)

    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Numero de plazas
    total = 0
    for c in contornos:
        area = cv2.contourArea(c)
        # print("area", area)
        if area > 1700:
            # aproximacion de contorno
            peri = cv2.arcLength(c, True)  # Perimetro
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # Si la aproximacion tiene 4 vertices correspondera a un rectangulo
            if len(approx) == 4:
                # cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3, cv2.LINE_AA)
                total += 1

    # 5.Poner texto en imagen
    # letrero = 'Plazas: ' + str(total)
    # cv2.putText(frame, letrero, (350, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 4)
    return total
