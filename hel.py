import cv2
from datetime import datetime
def rec():

        vid = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        frame_width = int(vid.get(3))
        frame_height = int(vid.get(4))
        size = (frame_height,frame_width)
        storeVid = cv2.VideoWriter('recordings.avi', cv2.VideoWriter_fourcc(*'MJPG'),10,size)
        while True:
            ret,frame = vid.read()
            cv2.putText(frame,f'{datetime.now().strftime("%D-%H-%M-%S")}',(50,50),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,255),2)
            storeVid.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()
