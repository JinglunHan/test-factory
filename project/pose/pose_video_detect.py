'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-24 11:48:01
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-03-11 11:12:31
FilePath: \my_tools\AI_CLUB\project\pose\pose_video_detect.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('/home/roota/workstation/test-factory/project/pose/x_yolov8m-pose.onnx')
#model = YOLO('yolov8s-pose.pt')

# Open the video file
video_path = "/home/roota/workstation/test-factory/data/fire/fire001.mp4"
print("Processing video:", video_path)
out_path = "/home/roota/workstation/test-factory/data/fire/xx_fire001.mp4"
print("Output video:", out_path)
cap = cv2.VideoCapture(video_path)

# Get the video frame properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to write the output video
out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video
        out.write(annotated_frame)
        # # Display the annotated frame
        # cv2.imshow("YOLOv8 Inference", annotated_frame)

        # # Break the loop if 'q' is pressed
        # if cv2.waitKey(1) & 0xFF == ord("q"):
        #     break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()