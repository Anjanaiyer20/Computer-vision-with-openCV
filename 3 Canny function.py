import cv2
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image3.jpg")                  
edges = cv2.Canny(img, 100, 200)               
cv2.imshow('Image Outline', edges)             
cv2.waitKey(0)
cv2.destroyAllWindows()
