import cv2

img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\sample image.jpg")                              # Read the image
small = cv2.resize(img, None, fx=0.5, fy=0.5)               
big = cv2.resize(img, None, fx=2.0, fy=2.0)                

cv2.imshow('Smaller Image', small)
cv2.imshow('Bigger Image', big)
cv2.waitKey(0)
cv2.destroyAllWindows()
