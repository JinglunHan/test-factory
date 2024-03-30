'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-02-20 19:22:43
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-02-20 20:00:10
FilePath: \my_tools\AI_CLUB\project\pose\show_struct.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torch
from torchvision.models import detection

# 加载模型
model = torch.load(r'D:\hjl\thinking\my_tools\AI_CLUB\project\pose\last.pt',map_location=torch.device('cpu'))


# 打印模型结构
print(model)
