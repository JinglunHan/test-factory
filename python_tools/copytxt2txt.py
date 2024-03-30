'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-02 19:12:17
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-10 17:01:45
FilePath: \my_tools\copytxt2txt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-

#一个脚本，将一个txt文件中的所有内容添加到目标目录下所有txt文件中
import os

def append_text_to_files(source_file, target_directory):
    # 读取源文件的内容
    with open(source_file, 'r') as f:
        source_content = f.read()

    # 遍历目标目录下的所有txt文件
    for file in os.listdir(target_directory):
        if file.startswith(''):
            if file.endswith('.txt'):
            # 打开目标文件，将源文件的内容追加到目标文件末尾
                target_file = os.path.join(target_directory, file)
                with open(target_file, 'a') as f:
                    f.write(source_content)

    print("内容已成功添加到目标目录下所有txt文件中！")

# 示例用法
source_file = '/workdir/data/fire/customer-data/labels/frame_149.txt'  # 源文件路径
target_directory = '/workdir/data/fire/customer-data/labels'  # 目标目录路径

append_text_to_files(source_file, target_directory)