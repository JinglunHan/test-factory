#处理标记数据并存储为yolo格式标签
import os
import cv2

# 指定保存txt文件的目录
output_dir = "/workdir/data/fire/fire-dataset-dunnings/superpixels/isolated-superpixels/test/labels"
#input_dir = "/workdir/data/fire/fire-dataset-dunnings/superpixels/isolated-superpixels/train/fire"
# 获取当前目录下的所有文件
file_list = os.listdir()


# 遍历文件列表
for file_name in file_list:
    # 判断文件是否为图片文件
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        # 获取文件名（不包含扩展名）
        name = os.path.splitext(file_name)[0]
        name = name.split("sp")[0]
        # get image file path
        image = cv2.imread(file_name)
        # 将图片转换为灰度图像
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 阈值处理，将非黑色区域变为白色
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        # 轮廓检测
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 生成txt文件的路径
        txt_path = os.path.join(output_dir, name + ".txt")
        for contour in contours:
            #  获取边界框的坐标
            x, y, w, h = cv2.boundingRect(contour)
    
            #  转换为YOLOv5格式
            image_width, image_height, _ = image.shape
            x_center = (x + w / 2) / image_width
            y_center = (y + h / 2) / image_height
            width = w / image_width
            height = h / image_height
        
            # 判断txt文件是否已存在，如果存在则跳过
            #if os.path.isfile(txt_path):
            #   continue
        
                # 创建并打开txt文件
            with open(txt_path, 'a') as f:
                # 写入内容到txt文件
                line = f"{0} {x_center} {y_center} {width} {height}\n"
                f.write(line)
        
        print(f"Created {txt_path}")
