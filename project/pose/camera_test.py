import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('/home/roota/workstation/onnx2caffe/yolov8_onnx2caffe/x_yolov8m-pose.onnx')

# 0 表示第一个摄像头，如果有多个摄像头，可以尝试不同的值
cap = cv2.VideoCapture(0)
# 创建窗口并设置大小
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)  # cv2.WINDOW_NORMAL 表示可调整大小的窗口
cv2.resizeWindow('Video', 800, 600)  # 设置窗口大小为 800x600
while True:
    ret, frame = cap.read()

    if not ret:
        print("无法读取视频流")
        break
    
    # Run YOLOv8 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    cv2.imshow('Video', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()