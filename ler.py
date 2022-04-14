import numpy as np
import cv2 as cv
import pytesseract

# Lendo Video ---------------------------------
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Não foi possível abrir camera")
    exit()

while True:
    # Pega frame por frame
    ret, frame = cap.read()

    # Se frame lido ret = true
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Operações no Frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

    # Pega o frame resultante
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break



# Tudo pronto acaba captura
cap.release()
cv.destroyAllWindows()
