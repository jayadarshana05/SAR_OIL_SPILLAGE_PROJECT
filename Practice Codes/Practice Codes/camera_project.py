import cv2
import os

cap = cv2.VideoCapture(0)

# Create output folder for frames
os.makedirs("frames", exist_ok=True)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show live stream
    cv2.imshow("Camera Stream", frame)

    # Save frame to folder
    filename = f"frames/frame_{frame_count:06d}.jpg"
    cv2.imwrite(filename, frame)
    frame_count += 1

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()