# 导入必要的库
import numpy as np
from sklearn import linear_model

# 创建一些示例数据（特征和目标）
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # 特征（这里是一维特征）
y = np.array([2, 4, 6, 8, 10])  # 目标

# 创建一个线性回归模型
model = linear_model.LinearRegression()

# 训练模型
model.fit(X, y)

# 进行预测
new_data = np.array([6, 7, 8]).reshape(-1, 1)  # 新的特征数据
predictions = model.predict(new_data)

# 打印预测结果
for x, y_pred in zip(new_data, predictions):
    print(f"特征：{x[0]}, 预测值：{y_pred:.2f}")
