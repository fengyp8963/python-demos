import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# 步骤1: 准备数据
data = pd.read_csv('emotion_dataset.csv')
X = data['text']
y = data['sentiment']

# 步骤2: 划分数据为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 步骤3: 特征提取
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# 步骤4: 训练情感分类模型
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 步骤5: 进行情感预测
y_pred = model.predict(X_test_tfidf)

# 步骤6: 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确度：{accuracy:.2f}")
