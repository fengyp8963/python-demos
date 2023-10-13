print(198 / 4)

sites = ["Baidu", "Google", "Qzxdp", "Taobao"]
for item in sites:
    print(item)

flag = 1
while flag:
    print('欢迎访问全栈教程!')
    flag = 0

print("Good bye!")

count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

listdemo = ['Google', 'Qzxdp', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对


list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")


def max(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(max(a, b))


def max1(a, b):
    if a > b:
        return a
    else:
        return b


print(max1(a, b))

import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

import time

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import calendar

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

print(eval('3 * x'))
print(3 * x)

import operator

a = 12
b = 13

print(operator.lt(a, b))
operator.le(a, b)
operator.eq(a, b)
operator.ne(a, b)
operator.ge(a, b)
operator.gt(a, b)
print(operator.__lt__(a, b))
operator.__le__(a, b)
operator.__eq__(a, b)
operator.__ne__(a, b)
operator.__ge__(a, b)
operator.__gt__(a, b)

people = {x: 1 for x in range(1, 32)}  # 创建一个字典，表示31个人的状态，1表示在船上，0表示已下船
check = 0  # 计数器，记录数到第几个人
i = 1  # 当前数到的人的编号
j = 0  # 记录已经下船的人数

while j < 15:  # 循环直到有15个人下船
    if people[i] == 0:  # 如果当前人已经下船，则继续下一个人
        i += 1
        continue

    check += 1  # 计数器加1
    if check == 9:  # 如果数到第9个人
        people[i] = 0  # 将当前人标记为已下船
        check = 0  # 重置计数器
        print("{}号下船了".format(i))  # 输出当前下船的人的编号
        j += 1  # 已下船的人数加1

    i += 1  # 继续下一个人
    if i == 32:  # 如果已经数到最后一个人，则从头开始数
        i = 1

print(people)

tup1 = ('Google', 'Qzxdp', 1997, 2000)

for item1 in tup1:
    print(item1)

print(tup1[1])

list1 = ['Google', 'Qzxdp', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print(list4)

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

tinydict = {'name': 'qzxdp', 'likes': 123, 'url': 'www.qzxdp.cn'}

for key, value in tinydict.items():
    print(key, value)

listdemo = ['Google', 'Qzxdp', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key: len(key) for key in listdemo}
print(newdict)


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self, b):
        return 'hello world' + b


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f('12312'))

print(len(x.f('12312')))
fruits = {'苹果': 1, '香蕉': 2, '梨': 3}
print(fruits)

aaa = [1, 2, 3]
aaa.reverse()
print(aaa)

print({ele: ele for ele in reversed([1, 2, 3, 4, 5, 6])})

print('sdsfsd'.format())

name = "Alice"
age = 25
message = "我的名字是{}，我今年{}岁。".format(name, age)
print(message)

print(1, 2, 3, 4, 6, 7, 8, 9, 10)

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

for i in range(5):
    print(i)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

setnew = {i ** 2 for i in (1, 2, 3)}
print(setnew)

import pyqrcode

# 设置二维码信息
s = "https://www.baidu.com"

# 生成二维码
url = pyqrcode.create(s)

# 保存二维码
url.svg("baidu.svg", scale=8)

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(1, 2, 3, 4, 5, 6, 7, 8)

print(1, 2, 3)
print(1, 2, 3, 4, 5, 6)

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup4 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

print(tup1)
print(tup2)

# 元组不可以修改
print(tup3)
print(type(tup1) == type(tup4))
print(type(tup1) == type(tup2))

var1 = 'Hello World!'
var2 = "Qzxdp"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

name = 'Qzxdp'
f'Hello {name}'  # 替换变量
f'{1 + 2}'  # 使用表达式

w = {'name': 'Qzxdp', 'url': 'www.qzxdp.cn'}
f'{w["name"]}: {w["url"]}'

x = 1
print(f'{x + 1}')  # Python 3.6
print(f'{x+1=}')  # Python 3.8

str = "       "
print(str.isspace())
str.capitalize()

str = "Qzxdp example....wow!!!"
print(str.isspace())
print(str.isspace())

print(str.islower())


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("小明", 10)

person1.say_hello()

import math

print("radians(90) : ", math.radians(90))  # 1 弧度等于大概 57.3°
print("radians(45) : ", math.radians(45))
print("radians(30) : ", math.radians(30))
print("radians(180) : ", math.radians(180))  # 180 度的弧度为 π

print("180 / pi : ", end="")
print(math.radians(180 / math.pi))
print(math.radians(180 / math.pi))
print(math.radians(180 / math.pi))

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Qzxdp',
    'url': 'http://www.qzxdp.cn'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

import random

print(dir(random))

random_number = random.randint(1, 10)

print(random_number, random_number)

print(random_number, random_number)

x = None  # 给变量x赋值为None
# 在后续的代码中为x赋值
x = 10
print(x + 1)  # 输出: 10

print(operator.eq((), ()))

# 模型定义
# 模型训练
# 输出模型
# 模型预测
import numpy as np

# 已经训练好的模型参数
model_coef = np.array([3.5, 2.8])  # 系数
model_intercept = 5.2  # 截距

# 待预测的特征数据
feature = np.array([2.3, 4.2])  # 特征数据，比如房屋的面积和卧室数量

# 将特征数据进行预处理，比如归一化等
preprocessed_feature = (feature - np.mean(feature)) / np.std(feature)

# 将特征数据转换为矩阵形式
feature_matrix = np.array([preprocessed_feature])

# 使用训练好的模型进行预测
predicted_price = np.dot(feature_matrix, model_coef) + model_intercept

# 输出预测结果
print("预测的房屋价格为:", predicted_price)

from datetime import datetime

print(datetime.today())

print(1.5 * 60 * 60)
