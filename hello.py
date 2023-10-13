# 第一个注释
# 第二个注释

"""
第三注释
第四注释
"""

"""
第五注释
第六注释
"""
print("Hello, Python!")

if True:
    print("True")
else:
    print("False")

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

print(total)

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nqzxdp')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nqzxdp')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input("\n\n按下 enter 键后退出。")

import sys;

x = 'qzxdp';
sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.pat

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "qzxdp"  # 字符串

print(counter)
print(miles)
print(name)

# a = b = c = 1
a, b, c = 1, 2, "qzxdp"

print(a)
print(b)
print(c)

print(type(a), type(b), type(c))

a = 111
print(isinstance(a, int))

print(True == 1)

str = 'Qzxdp'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TEST")  # 连接字符串

a = True
b = False

# 比较运算符
print(2 < 3)  # True
print(2 == 3)  # False

# 逻辑运算符
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

# 类型转换
print(int(a))  # 1
print(float(b))  # 0.0

list = ['abcd', 786, 2.23, 'qzxdp', 70.2]
tinylist = [123, 'qzxdp']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

sites = {'Google', 'Taobao', 'Qzxdp', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Qzxdp' in sites:
    print('Qzxdp 在集合中')
else:
    print('Qzxdp 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

dict = {}
dict['one'] = "1 - 全栈教程"
dict[2] = "2 - 全栈工具箱"

tinydict = {'name': 'qzxdp', 'code': 1, 'site': 'www.qzxdp.cn'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素

str = "Hello World"
list2 = tuple(str)
print("列表元素 : ", list2)

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")


def max(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(max(a, b))



