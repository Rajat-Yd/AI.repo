import cv2
from datetime import datetime


def Record():
    cap = cv2.VideoCapture(0)
   

    while True:
        ret, frame = cap.read()
      
        cv2.imshow('esc tp stop',frame)

        if cv2.waiteKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break