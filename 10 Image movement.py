import cv2
import numpy as np
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\sample image.jpg")                          
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 50], [0, 1, 100]])                   
moved = cv2.warpAffine(img, M, (cols, rows))             
cv2.imshow('Moved Image', moved)
cv2.waitKey(0)
cv2.destroyAllWindows()
