import cv2
import numpy as np
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\sample image.jpg", 0)  
laplacian_mask = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])
laplacian = cv2.filter2D(img, -1, laplacian_mask)
sharpened = cv2.subtract(img, laplacian)

cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
