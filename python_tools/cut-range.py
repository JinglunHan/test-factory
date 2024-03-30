'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-02 17:42:37
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-24 15:30:07
FilePath: \my_tools\cut-range.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#截取视频一个范围内的所有帧
import cv2

def extract_frames(video_path, start_frame, end_frame, output_folder):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 确保开始和结束帧在有效范围内
    if start_frame < 0 or start_frame >= frame_count:
        start_frame = 0
    if end_frame >= frame_count or end_frame < start_frame:
        end_frame = frame_count - 1
    
    # 设置当前帧为开始帧
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    step = 5
    cut_step = start_frame+step
    # 遍历每一帧并保存为PNG图像
    current_frame = start_frame
    while current_frame <= end_frame:
        ret, frame = video.read()
        if not ret:
            break
        
        # 生成输出文件路径
        output_path = f'{output_folder}/pose_image_{str(current_frame+1).zfill(3)}.png'
        if current_frame == cut_step:
        # 保存当前帧为PNG图像
            cv2.imwrite(output_path, frame)
            cut_step = cut_step + step
        
        current_frame += 1
    
    # 释放视频对象
    video.release()

# 使用示例
video_path = '/home/roota/workstation/test-factory/data/fire/fire001.mp4'  # 视频文件路径
start_frame = 0  # 开始帧
end_frame = 2000  # 结束帧
output_folder = '/home/roota/workstation/caffe2om/pose/images'  # 输出文件夹路径

extract_frames(video_path, start_frame, end_frame, output_folder)