import cv2 as cv
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale=0.75):
    width = frame.shape[1] *scale
    height = frame.shape[0] *scale
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

capture = cv.VideoCapture(r"C:\Users\achil\OneDrive\Desktop\CLICK\Amrita\SEM 5\DIP\Codes\trial_lut_tesls.mov")

while True:
    isTrue,frame = capture.read()
    cv.imshow('Tesla_video', frame)
    cv.imshow('tesla_video_resized', frame)
    
    frame_resized = rescaleFrame(frame, scale=.2) # scale here is like the size of the frame or videos
    
    
    if 0xFF==ord('a'):
        break

# Wait for a key press and close the image window
cv.waitKey(0)
cv.destroyAllWindows()

