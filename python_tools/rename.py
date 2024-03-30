'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-19 14:15:51
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-19 14:17:52
FilePath: \my_tools\rename.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-
import os

directory='/workdir_test/0_hjl/data/smoke'
# 获取当前文件夹中的所有文件
files = os.listdir(directory)

# 遍历文件并重命名
for i, file in enumerate(files):
    # 获取文件的扩展名
    ext = os.path.splitext(file)[1]
    # 新的文件名
    new_name =  os.path.join(directory,f"smoke_{str(i+1).zfill(4)}{ext}")
    # 重命名文件
    os.rename(os.path.join(directory, file), new_name)