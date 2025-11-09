import cv2 as cv
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image using cv2
image = cv.imread(r"C:\Users\achil\OneDrive\Desktop\CLICK\Amrita\SEM 5\DIP\Codes\vish_formal.jpg")

# Display the image using OpenCV, window name, variable name
cv.imshow('I will make it-', image)

# Wait for a key press and close the image window
cv.waitKey(0)
cv.destroyAllWindows()