import cv2
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image2.jpg")                
blur = cv2.GaussianBlur(img, (5, 5), 0)       
cv2.imshow('Blurred Image', blur)             
cv2.waitKey(0)
cv2.destroyAllWindows()
