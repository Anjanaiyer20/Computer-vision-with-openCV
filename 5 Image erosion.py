import cv2
import numpy as np
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image5.jpg")                     
kernel = np.ones((5, 5), np.uint8)                
eroded = cv2.erode(img, kernel, iterations=1)     
cv2.imshow('Eroded Image', eroded)                
cv2.waitKey(0)
cv2.destroyAllWindows()
