import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置使用宋体字体

# 创建一个示例数据集
data = {
    '日期': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    '销售额': [100, 120, 90, 110, 130]
}

# 将数据集转换为DataFrame
df = pd.DataFrame(data)

# 打印数据集的前几行
print("数据集的前几行:")
print(df.head())

# 绘制销售额的折线图
plt.figure(figsize=(8, 5))
plt.plot(df['日期'], df['销售额'], marker='o', linestyle='-')
plt.title('销售额趋势')
plt.xlabel('日期')
plt.ylabel('销售额')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()
