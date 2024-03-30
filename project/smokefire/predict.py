'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-03-11 10:37:05
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-03-11 11:24:43
FilePath: \my_tools\AI_CLUB\project\smokefire\predict.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from ultralytics import YOLO
import cv2

# Load a model
# model = YOLO('yolov8n-cls.pt')  # load an official model
model = YOLO(r'D:\hjl\thinking\my_tools\AI_CLUB\project\pose\x_yolov8m-pose.onnx')  # load a custom model

# Predict with the model
results = model(r'D:\hjl\thinking\my_tools\AI_CLUB\data\images\fire001_01.png')  # predict on an image

outpath = r"D:\hjl\thinking\my_tools\AI_CLUB\data\images\x_fire001_01.png"


for result in results:
    image=result.plot()
    cv2.imwrite(outpath, image)