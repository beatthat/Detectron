import cv2
import time

def video2frames(video_path, logging=False):
    cap = cv2.VideoCapture(video_path)
    i = 0
    while(cap.isOpened()):
        t = time.time()
        
        ret, frame = cap.read()
        
        if not ret:
            break
            
        if logging:
            print('read frame ' + str(i) + ' in ' + str(time.time() - t) + "s")
        
        yield frame
        i += 1
        
    cap.release()

