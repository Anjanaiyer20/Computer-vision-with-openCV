import cv2

# Load image
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image6.jpg")

# Extract face regions
rohit = img[100:240, 60:160]
virat = img[100:240, 180:280]

# Show only the extracted objects
cv2.imshow('Rohit Sharma', rohit)
cv2.imshow('Virat Kohli', virat)
cv2.waitKey(0)
cv2.destroyAllWindows()
