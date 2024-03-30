'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-02 17:42:37
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-03-11 10:04:26
FilePath: \my_tools\cut-one.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#截取视频某一帧的数据
import cv2

def extract_frame(video_path, frame_num, output_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("无法打开视频文件")
        return
    
    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames)
    
    # 检查帧数是否在有效范围内
    if frame_num < 0 or frame_num >= total_frames:
        print("无效的帧数")
        return
    
    # 设置视频帧的位置
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    
    # 读取指定帧的数据
    ret, frame = cap.read()
    
    # 检查帧是否成功读取
    if not ret:
        print("无法读取帧数据")
        return
    
    # 将帧保存为PNG图像
    cv2.imwrite(output_path, frame)
    
    # 释放视频文件
    cap.release()
    
    print("成功保存帧数据为PNG图像")

# 示例用法
video_path = r"D:\hjl\thinking\my_tools\AI_CLUB\data\fire\fire001.mp4"
frame_num = 21  # 要提取的帧数
output_path = r"D:\hjl\thinking\my_tools\AI_CLUB\data\images\fire001_01.png"

extract_frame(video_path, frame_num, output_path)
