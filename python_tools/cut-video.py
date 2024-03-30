'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-12 14:25:08
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-02-22 19:16:49
FilePath: \my_tools\cut-video.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#加载目标目录下的所有视频，会弹出一个界面，在界面中画矩形框截取视频，截取完成回车
import cv2
import os

def crop_and_resize_frame(frame, x1, y1, x2, y2, width, height):
    cropped_frame = frame[y1:y2, x1:x2]
    resized_frame = cv2.resize(cropped_frame, (width, height))
    return resized_frame

def process_video(input_path, output_path, width, height):
    # 获取指定目录下的视频文件
    #video_files = [f for f in os.listdir(input_path) if f.endswith('.mp4') or f.endswith('.avi')]

    #for video_file in video_files:
        # video_path = os.path.join(input_path, video_file)
        # output_file = os.path.splitext(video_file)[0] + "_processed.mp4"
        # output_file_path = os.path.join(output_path, output_file)

        # 打开视频文件
        # video_capture = cv2.VideoCapture(video_path)
        video_capture = cv2.VideoCapture(input_path)

        # 获取视频的第一帧
        ret, frame = video_capture.read()

        # 显示第一帧并等待用户标记两个点
        # cv2.imshow('First Frame', frame)
        # print("请在图片中标记两个点，然后按下's'键继续...")
        # cv2.waitKey(0)

        # 获取用户标记的两个点
        points = cv2.selectROI(frame, False)
        x1, y1, w, h = points
        x2 = x1 + w
        y2 = y1 + h

        # 遍历视频的每一帧并进行裁剪和调整尺寸
        frame_count = 0
        output_frames = []
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # 裁剪并调整尺寸
            resized_frame = crop_and_resize_frame(frame, x1, y1, x2, y2, width, height)
            output_frames.append(resized_frame)

            frame_count += 1
            print("处理帧: ", frame_count)

        # 释放视频捕获对象
        video_capture.release()

        # 将裁剪后的图片帧重新合成为新的视频文件
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # output_video = cv2.VideoWriter(output_file_path, fourcc, 30.0, (width, height))
        output_video = cv2.VideoWriter(output_directory, fourcc, 30.0, (width, height))
        for frame in output_frames:
            output_video.write(frame)

        # 释放视频写入对象
        output_video.release()

        #print("视频处理完成: ", output_file_path)

        cv2.destroyAllWindows()

# 指定输入目录和输出目录
input_directory = r"D:\hjl\thinking\my_tools\AI_CLUB\data\video\e045085e3f55491e44602cb029522dc6.mp4"
output_directory =r"D:\hjl\thinking\my_tools\AI_CLUB\data\fire\xxx.mp4"

# 指定输出视频的宽度和高度
output_width = 1280
output_height = 960

# 执行视频处理
process_video(input_directory, output_directory, output_width, output_height)
