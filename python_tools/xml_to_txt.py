'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-02 17:50:55
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-02 17:57:01
FilePath: \my_tools\xml_to_txt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#转换xml格式标注为yolo的txt格式
import xml.etree.ElementTree as ET
import pickle
import os

sets=['dataset']

classes = ["smoke","fire"]


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_set, image_id):
    in_file = open('%s/Annotations/%s.xml'%(image_set, image_id))
    out_file = open('%s/labels/%s.txt'%(image_set, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:
            raise TypeError("class {%s} isn't expected"%cls)
#        if cls not in classes or int(difficult)==1:
#            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    out_file.close()
    in_file.close()

wd = os.getcwd()

for image_set in sets:
    path = "%s/Annotations/"%image_set
    annotations = os.listdir(path)
    bname = map(lambda x:os.path.splitext(os.path.basename(x))[0],annotations)
    with open('%s.txt'%image_set,'w') as list_file:
        for image_id in bname:
          list_file.write('%s/%s/JPEGImages/%s.png\n'%(wd,image_set, image_id))
          convert_annotation(image_set,image_id)    

#os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
#os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

