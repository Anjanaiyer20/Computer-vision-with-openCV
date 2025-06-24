import cv2
import numpy as np

# Replace this with your actual image file name or full path
image_path = 'C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\sample image.jpg'

# Read the image in grayscale mode
img = cv2.imread(image_path, 0)

# Check if the image was loaded successfully
if img is None:
    print("❌ Error: Image not found. Check the file name and path.")
else:
    # Convert to binary image using thresholding
    _, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    # Define a kernel and apply dilation
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Show the result
    cv2.imshow('Dilated Image', dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
