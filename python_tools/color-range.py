'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-01-26 14:47:35
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-02-19 10:09:48
FilePath: \my_tools\color-range.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2

def check_color_percentage(image, color_range, percentage_threshold):
    # 读取图片
    img = cv2.imread(image)
    points = cv2.selectROI(img, False)
    print(points)
    x,y,width,height = points
    # 裁剪画框区域
    roi = img[y:y+height, x:x+width]
    # 将画框区域转换为HSV颜色空间
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # 设定颜色范围
    lower_color = (color_range[0][0], color_range[1][0], color_range[2][0])
    upper_color = (color_range[0][1], color_range[1][1], color_range[2][1])
    # 创建颜色掩码
    mask = cv2.inRange(hsv_roi, lower_color, upper_color)
    # 计算颜色像素数量
    total_pixels = mask.size
    colored_pixels = cv2.countNonZero(mask)
    # 计算百分比
    color_percentage = (colored_pixels / total_pixels) * 100
    print(color_percentage)
    # 判断是否识别成功
    if color_percentage >= percentage_threshold:
        return "识别成功"
    else:
        return "识别失败"

# 示例用法
image_path = r"D:\hjl\thinking\my_tools\AI_CLUB\data\image\cut04.png"
# x = 100  # 画框左上角x坐标
# y = 100  # 画框左上角y坐标
# width = 200  # 画框宽度
# height = 200  # 画框高度
color_range = [(0, 50), (80, 255), (80, 255)]  # RGB颜色范围，例如：红色
percentage_threshold = 10  # 颜色像素占比阈值

result = check_color_percentage(image_path, color_range, percentage_threshold)
print(result)



##c++ code
# #include <iostream>
# #include <opencv2/opencv.hpp>

# std::string check_color_percentage(const std::string& image, const std::vector<cv::Range>& color_range, double percentage_threshold) {
#     cv::Mat img = cv::imread(image);
#     cv::Rect roi = cv::selectROI(img, false);
#     cv::Mat roi_img = img(roi);
#     cv::Mat hsv_roi;
#     cv::cvtColor(roi_img, hsv_roi, cv::COLOR_BGR2HSV);
#     cv::Mat mask;
#     cv::inRange(hsv_roi, cv::Scalar(color_range[0].start, color_range[1].start, color_range[2].start), cv::Scalar(color_range[0].end, color_range[1].end, color_range[2].end), mask);
#     int total_pixels = mask.size().area();
#     int colored_pixels = cv::countNonZero(mask);
#     double color_percentage = (colored_pixels / static_cast<double>(total_pixels)) * 100;
#     if (color_percentage >= percentage_threshold) {
#         return "识别成功";
#     } else {
#         return "识别失败";
#     }
# }

# int main() {
#     std::string image_path = "D:/hjl/thinking/my_tools/AI_CLUB/data/image/warn4.jpg";
#     std::vector<cv::Range> color_range = { cv::Range(0, 50), cv::Range(50, 255), cv::Range(50, 255) };
#     double percentage_threshold = 50;

#     std::string result = check_color_percentage(image_path, color_range, percentage_threshold);
#     std::cout << result << std::endl;

#     return 0;
# }