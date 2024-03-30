'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-02 17:47:02
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-02 19:21:14
FilePath: \my_tools\path-file-label.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#将目标文件夹路径写入txt文件
import os

def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def write_file_paths_to_txt(file_paths, txt_file):
    with open(txt_file, 'w') as file:
        for file_path in file_paths:
            file.write(file_path + '\n')
    print("文件路径已写入到", txt_file)

target_directory = '/workdir/data/fire/customer-data/labels'  # 替换为你的目标路径
txt_file_path = '/workdir/data/fire/customer-data/labels/customer_labels.txt'  # 替换为你想要保存文件路径的txt文件路径

file_paths = get_file_paths(target_directory)
write_file_paths_to_txt(file_paths, txt_file_path)
