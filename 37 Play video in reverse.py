import cv2

# Load video
cap = cv2.VideoCapture("C:\\Users\\user\\OneDrive\\Pictures\\Camera Roll\\WIN_20250630_09_59_29_Pro.mp4")

# Get total frames
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Read all frames into a list
frames = []
for _ in range(frame_count):
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play frames in reverse
for frame in reversed(frames):
    cv2.imshow('Reverse Video', frame)
    if cv2.waitKey(30) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
