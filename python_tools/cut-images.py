'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-12 18:09:15
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-19 09:28:11
FilePath: \my_tools\cut-images.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
from PIL import Image

def crop_images(input_dir, output_dir, width, height):
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 构建输入图片的完整路径
            input_path = os.path.join(input_dir, filename)

            # 打开图片
            img = Image.open(input_path)

            # 计算截取位置
            img_width, img_height = img.size
            if img_width < img_height:
                img = img.rotate(90, expand=True)
                img_width, img_height = img.size
            right = 640
            top = img_height - 640
            left = img_width - 640
            bottom = 640
            middle = img_height // 2

            # 截取图片01
            cropped_img = img.crop((0, 0, right, bottom))
            # 构建输出图片的完整路径
            output_path = os.path.join(output_dir, '01'+filename)
            # 保存截取后的图片
            cropped_img.save(output_path)
            # 截取图片03
            cropped_img = img.crop((left, 0, img_width, bottom))
            # 构建输出图片的完整路径
            output_path = os.path.join(output_dir, '03'+filename)
            # 保存截取后的图片
            cropped_img.save(output_path)
            # 截取图片04
            cropped_img = img.crop((0, top, right, img_height))
            # 构建输出图片的完整路径
            output_path = os.path.join(output_dir, '04'+filename)
            # 保存截取后的图片
            cropped_img.save(output_path)
            # 截取图片06
            cropped_img = img.crop((left, top, img_width, img_height))
            # 构建输出图片的完整路径
            output_path = os.path.join(output_dir, '06'+filename)
            # 保存截取后的图片
            cropped_img.save(output_path)
            # 截取图片02
            cropped_img = img.crop((middle-640, 0, middle+640, bottom))
            # 构建输出图片的完整路径
            output_path = os.path.join(output_dir, '02'+filename)
            # 保存截取后的图片
            cropped_img.save(output_path)
             # 截取图片05
            cropped_img = img.crop((middle-640, top, middle+640, img_height))
            # 构建输出图片的完整路径
            output_path = os.path.join(output_dir, '05'+filename)
            # 保存截取后的图片
            cropped_img.save(output_path)
            
            
            print(f"图片 {filename} 截取成功！")

# 调用函数进行截取
input_directory = "input_images"  # 输入图片所在的目录
output_directory = "output_images"  # 输出截取后的图片保存的目录
width = 640  # 截取后的宽度
height = 640  # 截取后的高度
crop_images(input_directory, output_directory, width, height)
