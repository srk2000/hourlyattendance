import numpy as np
import cv2
import time

x=1

while(True):

    cap = cv2.VideoCapture(0)
    framerate = cap.get(5)
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.release()
    # Our operations on the frame come here



    filename = 'E:/Co-curricular/Smartintern AI project/jumpooooooooooooo.png'
    x=x+1
    cv2.imwrite(filename, frame)
    time.sleep(60*60)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
