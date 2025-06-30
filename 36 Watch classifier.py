import cv2

# Load image
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\watch_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Preprocess
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours to find watch-like shapes
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 1000 < area < 10000:  # Watch-like area
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) >= 4:  # Looks like a rectangle
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Watch?", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

# Show result
cv2.imshow("Possible Watch Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

