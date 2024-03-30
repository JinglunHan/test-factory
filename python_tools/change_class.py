'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-05 11:07:22
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-19 14:17:22
FilePath: \my_tools\change_class.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-
import os

def replace_lines(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # 将文件指针移回文件开头
        file.truncate()  # 清空文件内容
        for line in lines:
            if line.startswith('0'):
                line = '1' + line[1:]
            # elif line.startswith('1'):
            #     line = '0' + line[1:]
            file.write(line)

def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            replace_lines(file_path)
            print(f'处理文件：{filename} 完成')

# 替换目标目录下所有txt文件的每行开头数字
target_directory = '/workdir/data/fire/customer-data/smoke_wenzhouyitong/labels'
process_files(target_directory)
