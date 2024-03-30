'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-25 19:06:38
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-02-20 20:06:27
FilePath: \my_tools\AI_CLUB\project\pose\export.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from ultralytics import YOLO

model = YOLO("/home/roota/workstation/test-factory/project/pose/yolov8n-pose.pt")

# model.export(format="onnx",simplify=True,opset=9)
model.export(format="onnx",simplify=True)