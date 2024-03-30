'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-26 14:37:06
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-26 17:48:26
FilePath: \my_tools\color.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import tkinter as tk
import cv2
import numpy as np

def show_color():
    # 从输入框获取HSV值
    h = int(h_entry.get())
    s = int(s_entry.get())
    v = int(v_entry.get())

    # 创建一个空白图像
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    # 将输入的HSV值转换为BGR颜色
    color_hsv = np.array([[[h, s, v]]], dtype=np.uint8)
    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)
    color_bgr = color_bgr[0][0]

    # 在图像上绘制颜色矩形
    img = cv2.rectangle(img, (0, 0), (100, 100), color_bgr.tolist(), -1)

    # 显示图像
    cv2.imshow("Color", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 创建窗口
window = tk.Tk()
window.title("HSV颜色显示")
window.geometry("300x200")

# 创建输入框和标签
h_label = tk.Label(window, text="H值（0-179）：")
h_label.pack()
h_entry = tk.Entry(window)
h_entry.pack()

s_label = tk.Label(window, text="S值（0-255）：")
s_label.pack()
s_entry = tk.Entry(window)
s_entry.pack()

v_label = tk.Label(window, text="V值（0-255）：")
v_label.pack()
v_entry = tk.Entry(window)
v_entry.pack()

# 创建按钮
button = tk.Button(window, text="显示颜色", command=show_color)
button.pack()

# 运行窗口
window.mainloop()