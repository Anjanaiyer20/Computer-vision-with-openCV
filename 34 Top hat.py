import cv2
import numpy as np
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\sample image.jpg", 0)
kernel = np.ones((5,5), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('Top Hat', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
