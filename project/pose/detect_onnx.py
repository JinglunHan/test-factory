'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-02-27 15:26:02
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-03-04 16:36:09
FilePath: \my_tools\AI_CLUB\project\pose\detect_onnx.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import onnx

# Preprocessing: load the ONNX model
model_path = 'x_yolov8m-pose.onnx'
onnx_model = onnx.load(model_path)

# print('The model is:\n{}'.format(onnx_model))

# Check the model
try:
    onnx.checker.check_model(onnx_model)
except onnx.checker.ValidationError as e:
    print('The model is invalid: %s' % e)
else:
    print('The model is valid!')