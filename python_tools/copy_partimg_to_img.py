'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-02-19 10:13:38
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-02-19 14:36:54
FilePath: \my_tools\python_tools\copy_partimg_to_img.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import os
import random

target_image_path = r'D:\hjl\thinking\my_tools\AI_CLUB\data\images\customer_nofire_0005_0466.png'
target_label_path = r'D:\hjl\thinking\my_tools\AI_CLUB\data\labels\customer_nofire_0005_0466.txt'

# 读取两张图片
image1 = cv2.imread(r'D:\hjl\thinking\my_tools\AI_CLUB\data\image\cut03.png')
image2 = cv2.imread(r'D:\hjl\thinking\my_tools\AI_CLUB\data\image\customer_nofire_0005_0466.png')

x,y,w,h = 361, 183, 50, 96

# 获取image1的截取内容（假设截取位置为(100, 100)到(300, 300)）
cropped_image = image1[y:y+h, x:x+w]
random_number = random.randint(100,350)
print(random_number)

# 将截取的内容放置到image2的指定位置（假设放置位置为(50, 50)）
image2[random_number:random_number+cropped_image.shape[0], random_number:random_number+cropped_image.shape[1]] = cropped_image
print(cropped_image.shape)
cv2.imwrite(target_image_path, image2)

image_height, image_width, _ = image2.shape
x_center = (random_number + w / 2) / image_width
y_center = (random_number + h / 2) / image_height
bbox_width = w / image_width
bbox_height = h / image_height

with open(target_label_path, 'w') as f:
    f.write(f'0 {x_center} {y_center} {bbox_width} {bbox_height}')

# 显示结果
# cv2.imshow('Result', image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()