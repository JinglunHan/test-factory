'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-04 19:50:56
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-04 19:51:16
FilePath: \my_tools\new-txt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os

source_dir = "/path/to/source/directory"
target_dir = "/path/to/target/directory"

# 获取源目录下的所有文件名
file_names = os.listdir(source_dir)

# 遍历文件名列表
for file_name in file_names:
    # 拼接源文件路径和目标文件路径
    source_file = os.path.join(source_dir, file_name)
    target_file = os.path.join(target_dir, file_name + ".txt")
    
    # 创建并写入空的txt文件
    with open(target_file, "w") as f:
        pass
