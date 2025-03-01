import cv2
import torch

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Perform inference on a video
results = model('traffic_video.mp4')

# Print results
results.print()

# Save results
results.save('path/to/output')

cv2.destroyAllWindows()