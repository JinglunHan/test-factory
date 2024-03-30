'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-10 16:58:38
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-10 16:58:51
FilePath: \my_tools\xmltotxt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import glob
import xml.etree.ElementTree as ET


def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_xml_to_yolo(xml_file, output_dir, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    image_file = root.find('filename').text
    image_width = int(root.find('size/width').text)
    image_height = int(root.find('size/height').text)
    
    output_file = os.path.splitext(image_file)[0] + '.txt'
    output_path = os.path.join(output_dir, output_file)
    
    with open(output_path, 'w') as f:
        for obj in root.iter('object'):
            class_name = obj.find('name').text
            if class_name not in classes:
                continue
            
            class_id = classes.index(class_name)
            
            xml_box = obj.find('bndbox')
            bbox = (
                float(xml_box.find('xmin').text),
                float(xml_box.find('xmax').text),
                float(xml_box.find('ymin').text),
                float(xml_box.find('ymax').text)
            )
            
            yolo_bbox = convert_coordinates((image_width, image_height), bbox)
            f.write('{} {} {} {} {}\n'.format(class_id, *yolo_bbox))

    print('Converted {} to YOLO format'.format(xml_file))


def convert_directory(source_dir, output_dir, classes):
    os.makedirs(output_dir, exist_ok=True)
    
    xml_files = glob.glob(os.path.join(source_dir, '*.xml'))
    
    for xml_file in xml_files:
        convert_xml_to_yolo(xml_file, output_dir, classes)


# 示例用法
source_dir = '/path/to/source/directory'
output_dir = '/path/to/output/directory'
classes = ['class1', 'class2', 'class3']  # 替换为实际的类别列表

convert_directory(source_dir, output_dir, classes)
