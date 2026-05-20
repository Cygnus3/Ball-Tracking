import numpy as np
import cv2 as cv

def rescaleFrame(frame , scale = 0.5):  # rescaling to ensure video fits on screen and reduce processing time
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation = cv.INTER_AREA)

capture = cv.VideoCapture(r"Video1.mp4") # Enter File Path here

while True:
    isTrue , frame = capture.read()
    
    if not isTrue:
        print("Video ended")
        break

    frame = rescaleFrame(frame , scale = 0.5)

    frame_hsv = cv.cvtColor(frame , cv.COLOR_BGR2HSV)


    # Setting HSV value ranges for colour masking. (this was found through HSV color picker tool)
    lower_red1 = np.array([0, 200, 80])
    upper_red1 = np.array([10, 255, 255]) 

    # red is at the end of the hue spectrum and hue spectrum is circular so we need to set two ranges for red color                                     
    lower_red2 = np.array([170, 200, 80])
    upper_red2 = np.array([179, 255, 255])

    # masking

    mask = cv.inRange(frame_hsv, lower_red1, upper_red1) | cv.inRange(frame_hsv, lower_red2, upper_red2)  
    result = cv.bitwise_and(frame , frame , mask = mask)  

    # contour detections (skipping noise cleaning, cus already less only, so not required)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv.contourArea)  # pick the largest contour (the ball)(in this file only 1 contour is there anyways)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        
        if radius > 10:  # filter noise 
            cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)  
            cv.circle(frame, (int(x), int(y)), 2, (0, 255, 0), -1)   

            print(f"x={int(x)}, y={int(y)}, radius={int(radius)}")

            cv.putText(frame, f"({int(x)}, {int(y)}) r={int(radius)}",(int(x)-40, int(y)-20),
            cv.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)

    cv.imshow("Tracking", frame)  # shows original frame with green circle overlay

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
