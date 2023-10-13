import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置使用宋体字体

# 步骤 2: 准备数据
# 假设我们有一些历史气温数据，X 是日期（从1到365），y 是气温
# 这里使用随机生成数据作为示例
np.random.seed(0)
X = np.arange(1, 366, 1)
y = 20 + 10 * np.sin(2 * np.pi * (X - 1) / 365) + np.random.normal(0, 5, 365)

# 步骤 3: 数据预处理
# 将数据分为训练集和测试集
X = X.reshape(-1, 1)  # 将X转换为二维数组
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 步骤 4: 构建和训练模型
# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 步骤 5: 预测并评估模型
# 预测气温
y_pred = model.predict(X_test)

# 评估模型性能
score = model.score(X_test, y_test)
print(f"模型性能：{score}")

# 可视化预测结果
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='black', label='实际气温')
plt.plot(X_test, y_pred, color='blue', linewidth=2, label='预测气温')
plt.xlabel('日期')
plt.ylabel('气温')
plt.title('天气预测')
plt.legend()
plt.show()
