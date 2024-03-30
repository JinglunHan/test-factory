'''
Author: hanjinglun 1870685625@qq.com
Date: 2024-02-23 10:03:32
LastEditors: hanjinglun 1870685625@qq.com
LastEditTime: 2024-03-13 14:53:49
FilePath: \my_tools\AI_CLUB\project\pose\change_onnx.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import onnx
from onnx import numpy_helper
from onnx import helper
from onnx import TensorProto
import numpy as np

# 加载ONNX模型
model_path = "yolov8m-pose-sim.onnx"
#model_path = r"yolov8s-pose-sim.onnx"
model = onnx.load(model_path)



# 定义张量形状
shape = [1, 2, 8400]
print(np.prod(shape))
value = [-1] * np.prod(shape)
# 将numpy数组转换为raw_data格式
raw_data = np.array(value, dtype=np.float32).tobytes()
# 创建所有值为-1的张量
tensor_data = np.full(shape, -1, dtype=np.float32)

# 创建ONNX张量
#tensor = onnx.helper.make_tensor(name="/model.22/Constant_7_output_0", data_type=onnx.TensorProto.FLOAT, dims=shape, vals=tensor_data.flatten().tolist())
tensor = onnx.helper.make_tensor(name="/model.sub/Constant_7_output_0", data_type=onnx.TensorProto.FLOAT, dims=shape, vals=raw_data,raw=True)
for i, t in enumerate(model.graph.initializer):
    if t.name == "model.15.m.0.cv1.conv.weight":
        print(t.name)
        model.graph.initializer.insert(i+1, tensor)

# 记录有冲突的constant输入，修改其name并添加新的初始化器
print("_____________________________________constant____________________________________________________")
target_constant = ["/model.22/Constant_9_output_0","/model.22/Constant_10_output_0"]
store_constant_another = {"/model.22/Slice_output_0":[1,17,2,8400],
                          "/model.22/Add_1_output_0":[1,2,8400],
                          "/model.22/Concat_5_output_0":[1,4,8400],
                          "/model.22/Add_2_output_0":[1,17,2,8400]}
key_list = [x for x in store_constant_another.keys()]
print(key_list)
# #####验证如何修改constant的数组
# for j in model.graph.initializer:
#     t_shape = store_constant_another[key_list[3]]
#     if j.name == target_constant[1]:
#         t_value = np.frombuffer(j.raw_data, dtype=np.float32)
#         print(t_value)
#         print(t_value.shape)
#         print(j.dims)
#         # t_value = np.repeat(t_value,4)
#         # t_value = t_value.reshape(t_shape)
#         t_value = t_value.reshape(1,1,1,8400)
#         # t_value = np.concatenate((t_value,t_value,t_value,t_value),axis=1)
#         t_value = np.repeat(t_value,2,axis=2)
#         t_value = np.repeat(t_value,17,axis=1)
#         print(t_value)
#         print(t_value.shape)
#         t_raw_data = np.array(t_value).astype(np.float32).tobytes()
#         t_tensor = onnx.helper.make_tensor(name="sssssssssss", data_type=onnx.TensorProto.FLOAT, dims=t_shape, vals=t_raw_data,raw=True)
#         print(np.frombuffer(t_tensor.raw_data).shape)
#         # model.graph.initializer.insert(3,t_tensor)
#         print(t_tensor)
# print(sf)
def change_tensor(another_input_name,an_input_name):
    if another_input_name == key_list[0]:
        t_shape = store_constant_another[key_list[0]]
        t_value = [2]* np.prod(t_shape)
        t_raw_data = np.array(t_value).astype(np.float32).tobytes()
        t_tensor = onnx.helper.make_tensor(name=an_input_name, data_type=onnx.TensorProto.FLOAT, dims=t_shape, vals=t_raw_data,raw=True)
        model.graph.initializer.insert(1, t_tensor)
    elif another_input_name == key_list[1]:
        t_shape = store_constant_another[key_list[1]]
        t_value = [2]* np.prod(t_shape)
        t_raw_data = np.array(t_value).astype(np.float32).tobytes()
        t_tensor = onnx.helper.make_tensor(name=an_input_name, data_type=onnx.TensorProto.FLOAT, dims=t_shape, vals=t_raw_data,raw=True)
        model.graph.initializer.insert(2, t_tensor)
    elif another_input_name == key_list[2]:
        t_shape = store_constant_another[key_list[2]]
        for j in model.graph.initializer:
            if j.name == target_constant[1]:
                t_value = np.frombuffer(j.raw_data, dtype=np.float32)
                t_shape = j.dims
                # t_value = t_value.reshape(1,1,8400)
                # t_value = np.repeat(t_value, 4,axis=1)
                t_raw_data = np.array(t_value).astype(np.float32).tobytes()
                t_tensor = onnx.helper.make_tensor(name=an_input_name, data_type=onnx.TensorProto.FLOAT, dims=t_shape, vals=t_raw_data,raw=True)
                model.graph.initializer.insert(3,t_tensor)
                break
                
    elif another_input_name == key_list[3]:
        t_shape = store_constant_another[key_list[3]]
        for j in model.graph.initializer:
            if j.name == target_constant[1]:
                t_value = np.frombuffer(j.raw_data, dtype=np.float32)
                t_shape = j.dims
                # t_value = t_value.reshape(1,1,1,8400)   #根据字典中的shape进行修改
                # t_value = np.repeat(t_value, 2,axis=2)
                # t_value = np.repeat(t_value, 17,axis=1)
                t_raw_data = np.array(t_value).astype(np.float32).tobytes()
                t_tensor = onnx.helper.make_tensor(name=an_input_name, data_type=onnx.TensorProto.FLOAT, dims=t_shape, vals=t_raw_data,raw=True)
                model.graph.initializer.insert(4,t_tensor)
                break
                
    
for i, node in enumerate(model.graph.node):

    if node.input[0] == target_constant[0]:
        node.input[0] = target_constant[0]+str(i)
        an_input_name = node.input[0]
        another_input_name = node.input[1]
        change_tensor(another_input_name,an_input_name)
    elif len(node.input) > 1:
        if node.input[1] == target_constant[0]:
            node.input[1] = target_constant[0]+str(i)
            an_input_name = node.input[1]
            another_input_name = node.input[0]
            change_tensor(another_input_name,an_input_name)
    if node.input[0] == target_constant[1]:
        node.input[0] = target_constant[1]+str(i)
        an_input_name = node.input[0]
        another_input_name = node.input[1]
        change_tensor(another_input_name,an_input_name)
    elif len(node.input) > 1:
        if node.input[1] == target_constant[1]:
            node.input[1] = target_constant[1]+str(i)
            an_input_name = node.input[1]
            another_input_name = node.input[0]
            change_tensor(another_input_name,an_input_name)



print("_____________________________________constant_____________________________________________________")

# print("_____________________________________input_shape____________________________________________________")
# print(model.graph.input)
# for node in model.graph.node:
#     print("Node:", node.name)
    
#     # 遍历每个输入张量
#     for input_name in node.input:
#         input_shape = None
#         for value_info in model.graph.value_info:
#             if value_info.name == input_name:
#                 input_shape = value_info.type.tensor_type.shape
#                 break
        
#         if input_shape:
#             print("Input:", input_name, "Shape:", [d.dim_value for d in input_shape.dim])
#         else:
#             print("Input:", input_name, "Shape: Unknown")
# print("_____________________________________input_shape____________________________________________________")
    


    



# 遍历所有节点，找到Sub节点并替换为Mul和Add节点的组合
for i, node in enumerate(model.graph.node):
    print('-----------------  '+str(i)+str(node.name)+'  -----------------')
    if i == 334:
        print(node.output)
        print(node)
    if node.op_type == 'Sub':
        
        input_x = node.input[0]
        input_y = node.input[1]
        output_name = node.output[0]
        print(node.input)
        print("Inputs:")

        mul_out_tensor = onnx.helper.make_tensor_value_info("/model.22/Mul_output_"+str(i), onnx.TensorProto.FLOAT, shape)
        # 定义新的节点类型
        mul_node = onnx.helper.make_node('Mul',[input_y,tensor.name ], [mul_out_tensor.name])
        add_node = onnx.helper.make_node('Add', [mul_node.output[0], input_x], [node.output[0]])
        mul_node.name = '/model.22/Mul_' + str(i)
        add_node.name = '/model.22/Add_' + str(i+5)
        # i += 1
        # # 添加新节点到图中
        # model.graph.node.extend([mul_node, add_node])
        model.graph.node.insert(i, mul_node)
        model.graph.node.insert(i+1, add_node)
        model.graph.node.remove(node)
        # 更新节点之间的连接关系
for i, node in enumerate(model.graph.output):
    print('-----------------  '+str(i)+str(node.name)+'  -----------------')
    print(node.name)
    print(node)
        
try:
    onnx.checker.check_model(model)
except onnx.checker.ValidationError as e:
    print('The model is invalid: %s' % e)
else:
    print('The model is valid!')

# 保存修改后的ONNX模型
#onnx.save(model, "x_yolov8_pose.onnx")
onnx.save(model, "x_yolov8m-pose.onnx")