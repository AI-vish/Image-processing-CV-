import cv2 as cv
import numpy as np

# Create a blank image with height and width of 500 pixels and 3 color channels
blank = np.zeros((500, 500, 3), dtype='uint8')

# Making the entire image green
blank[:] = 0, 255, 0
cv.imshow('Green blank window', blank)

# Draw a rectangle in red color
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=2)  #thickness= FILLEED/-1 will fill up the space enclosed
cv.imshow('Rectangular image', blank)

#Circel
cv.circle(blank, (250,250), 3, (250,0,0), thickness=200)
cv.imshow('Circle image', blank)

#Line
cv.line(blank, (0,0),(250,250),(255,255,255), thickness = 3)
cv.imshow('line image', blank)

cv.putText(blank,'VISHGAKL', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (250,250,250), thickness=3)
cv.imshow('Text window', blank)
# Wait for a key press and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()


