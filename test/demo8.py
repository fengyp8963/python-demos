import numpy as np

# 输入层-隐藏层的权重
weights_input_hidden = np.array([[1, 2, 3, 4],
                                 [2, 3, 4, 5],
                                 [3, 4, 5, 6]])
# 隐藏层-输出层的权重
weights_hidden_output = np.array([[1, 2],
                                  [2, 3],
                                  [3, 4],
                                  [4, 5]])
# 输入值
input_data = np.array([2, 3, 4])


# 定义激活函数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# 计算隐藏层的输出
hidden_layer_input = np.dot(input_data, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)
# 计算输出层的输出
output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
output = sigmoid(output_layer_input)
print(output)
