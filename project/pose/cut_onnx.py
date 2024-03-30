import onnx
from onnx import numpy_helper
from onnx import helper
from onnx import TensorProto
import numpy as np

# 加载ONNX模型
model_path = "x_yolov8m-pose.onnx"
#model_path = r"yolov8s-pose-sim.onnx"
model = onnx.load(model_path)

# first cut node
node1_all = []
# second cut node
node2_all = []
node_list = []

for i, node in enumerate(model.graph.node):
    print('-----------------  '+str(i)+str(node.name)+'  -----------------')
    if node.name == '/model.22/Concat':
        node1_all.append(node.output[0])
    if node.name == '/model.22/Concat_4':
        node2_all.append(node.output[0])
    if i <= 306:
        node_list.append(node.name)
print(node_list)
##======================================== PART 1 ===========================================##

# while True:
#     if len(model.graph.node)<=307:
#         break
#     else:
#         print(len(model.graph.node))
#         model.graph.node.pop()

# new_concat_node = helper.make_node('Concat',[node1_all[0], node2_all[0]],['output'], axis=1)
# new_concat_node.name = 'output_concat'
# model.graph.node.extend([new_concat_node])
# # new_reshape_node = helper.make_node('Reshape',['output_concat'],['output'],shape=[1,1,116,8400])
# # new_reshape_node.name = 'output_reshape'
# # model.graph.node.extend([new_reshape_node])
# model.graph.output.remove(model.graph.output[0])
# output_node = helper.make_tensor_value_info('output', TensorProto.FLOAT, [1, 1, 116, 8400])
# model.graph.output.extend([output_node])
# print(model.graph.output)
# for i, node in enumerate(model.graph.node):
#     print('-----------------  '+str(i)+str(node.name)+'  -----------------')
##=============================================================================================##    

##======================================== PART 2 ===========================================##

input_node = helper.make_tensor_value_info('input', TensorProto.FLOAT, [1, 1, 116, 8400])
model.graph.input.remove(model.graph.input[0])
model.graph.input.extend([input_node])
print(model.graph.input)

while True:
    if len(model.graph.node)<29:
        break
    else:
        print(len(model.graph.node))
        model.graph.node.remove(model.graph.node[0])
reshape_trensor = numpy_helper.from_array(np.array([1,116,8400]), name='reshape_trensor')
model.graph.initializer.extend([reshape_trensor])
new_reshape_node = helper.make_node('Reshape',['input','reshape_trensor'],['input_reshape'])
new_reshape_node.name = 'input_reshape'
model.graph.node.insert(0,new_reshape_node)
new_split_node = helper.make_node('Split',['input_reshape'],[node1_all[0], node2_all[0]], axis=1, split=[51,65])
new_split_node.name = 'input_split'
model.graph.node.insert(1,new_split_node)
for i, node in enumerate(model.graph.node):
    print('-----------------  '+str(i)+str(node.name)+'  -----------------')
##=============================================================================================##

        
try:
    onnx.checker.check_model(model)
except onnx.checker.ValidationError as e:
    print('The model is invalid: %s' % e)
else:
    print('The model is valid!')

# 保存修改后的ONNX模型
#onnx.save(model, "x_yolov8_pose.onnx")
onnx.save(model, "x_yolov8m-pose_p2.onnx")