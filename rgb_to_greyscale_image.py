import cv2 as cv
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image file using PIL
im = Image.open(r"C:\Users\achil\OneDrive\Desktop\CLICK\Amrita\SEM 5\DIP\Codes\vish_formal.jpg")

# Convert the image to grayscale
gray_image = im.convert('L')

# Convert the PIL image to a NumPy array
image_np = np.array(gray_image)

# Display the image using OpenCV
cv.imshow('Grayscale Image', image_np)
cv.waitKey(0)
cv.destroyAllWindows()
