'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-29 11:27:40
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-01-31 15:05:06
FilePath: \my_tools\python_tools\compare.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2

def compare_images(image1, image2):
    # 将两张图片转换为灰度图像
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 获取矩形区域的图像信息
    roi1 = gray_image1[y:y+h, x:x+w]
    roi2 = gray_image2[y:y+h, x:x+w]

    # # 计算黑白像素的数量
    # total_pixels = roi1.shape[0] * roi1.shape[1]
    # white_pixels1 = cv2.countNonZero(roi1)
    # white_pixels2 = cv2.countNonZero(roi2)
    # black_pixels1 = total_pixels - white_pixels1
    # black_pixels2 = total_pixels - white_pixels2

    # # 计算黑白像素变化的百分比
    # percentage_change = abs(black_pixels1 - black_pixels2) / total_pixels * 100
    
    diff = cv2.absdiff(roi1, roi2)
    # 创建具有指定大小的窗口
    cv2.namedWindow('Difference', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Difference', 800, 600)
    # 显示差异图像
    cv2.imshow('Difference', diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    diff_percent = (cv2.countNonZero(diff) * 100) / diff.size
    print("Difference percentage:", diff_percent)

    # 比较百分比变化并返回结果
    if diff_percent > 50:
        return "检测成功"
    else:
        return "检测失败"

# 从文件读取两张图片
image1 = cv2.imread(r"D:\hjl\thinking\my_tools\AI_CLUB\data\image\nofire02_frame20.png")
image2 = cv2.imread(r"D:\hjl\thinking\my_tools\AI_CLUB\data\image\nofire02_frame50.png")

# 设置矩形区域的坐标和尺寸
# points = cv2.selectROI(image1, False)
# x,y,w,h = points
#x, y, w, h = 100, 100, 200, 200
height, width, _ = image1.shape
# 缩小图片的尺寸适应显示器
max_width = height //2  # 可根据需要调整边距
max_height = width //2
resized_image = cv2.resize(image1, (max_width, max_height))

# 在修改后的图片中选择ROI
points = cv2.selectROI(resized_image, False)

# 将ROI的坐标转换回原始图片的坐标
x, y, w, h = points
x = int(x * (image1.shape[1] / max_width))
y = int(y * (image1.shape[0] / max_height))
w = int(w * (image1.shape[1] / max_width))
h = int(h * (image1.shape[0] / max_height))

# 调用函数进行比较
result = compare_images(image1, image2)
print(result)