'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-05 16:01:27
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-06 10:33:44
FilePath: \my_tools\delete_file.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os

target_dir = '目标目录路径'

file_list = os.listdir(target_dir)

for file_name in file_list:
    file_path = os.path.join(target_dir, file_name)
    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        os.remove(file_path)
