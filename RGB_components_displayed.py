import cv2 as cv
import numpy as np

# Function to display the RGB values on mouse movement
def show_rgb(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        # Get the RGB values at the cursor position
        b, g, r = image[y, x]
        text = f'R: {r}%, G: {g}%, B: {b}%'
        
        # Create a copy of the image to display the text
        img_copy = image.copy()
        
        # Display the RGB values on the image
        cv.putText(img_copy, text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.imshow('Image', img_copy)

# Load the image
image = cv.imread(r"C:\Users\achil\OneDrive\Desktop\CLICK\Amrita\SEM 5\DIP\Codes\vish_formal.jpg")

# Resize the image if needed
# image = cv.resize(image, (800, 600))

# Display the image and set the mouse callback function
cv.imshow('Image', image)
cv.setMouseCallback('Image', show_rgb)

# Wait until a key is pressed
cv.waitKey(0)
cv.destroyAllWindows()
