import cv2 as cv

capture = cv.VideoCapture(r"C:\Users\achil\OneDrive\Desktop\CLICK\Amrita\SEM 5\DIP\Codes\trial_lut_tesls.mov")

while True:
    isTrue,frame = capture.read()
    cv.imshow('Tesla_video', frame)
    
    if 0xFF==ord('a'):
        break

capture.release()
cv.destroyAllWindows()

