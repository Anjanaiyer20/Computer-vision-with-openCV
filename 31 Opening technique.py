import cv2
import numpy as np

img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image5.jpg", 0)
kernel = np.ones((5,5), np.uint8)
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('Opening', opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
