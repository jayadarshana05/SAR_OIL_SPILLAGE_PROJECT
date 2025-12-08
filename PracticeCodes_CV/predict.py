from ultralytics import YOLO
import cv2
# Load a pretrained YOLO11n model
model = YOLO(r"C:\Users\psadi\Downloads\best (1).pt")

# Single stream with batch-size 1 inference
source =( r"C:\Users\psadi\OneDrive\Documents\part_1[1]\part_1\img_0068_1.jpg" ) # RTSP, RTMP, TCP, or IP streaming address

# Run inference on the source
results = model(source, save=True , show=True) 
cv2.waitKey(0)
cv2.destroyAllWindows() # generator of Results objects