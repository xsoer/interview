[TOC]

## 0x00、设计思想
##### 语言设计原则
* python设计之蝉
```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
##### 语言特点
* 面向对象
* 解释性和编译性结合的
* 动态的：动态属性、动态方法
* 免费
* 开源
* 可移植
* 功能强大
* 可混合
* 简单易用
* 生态丰富
* 标准库强大

##### 语言适用场景
* 用户图形接口
* web开发
* 爬虫开发
* Internet脚本
* 组件集成
* 数据库编程
* 数值计算和科学计算
* 游戏
* 图像
* 人工智能
* 机器人
* 系统运维
* 微服务

##### 编程规范有哪些

##### 注释、文档如何实现


## 0x01、基础操作
##### 关键字有哪些，有什么作用
```python
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
```

##### 关键字赋值
* 关键字不可以赋值，会报`invalid syntax`错误
```python
>>> if=123
  File "<stdin>", line 1
    if=123
      ^
SyntaxError: invalid syntax
>>> while='abc'
  File "<stdin>", line 1
    while='abc'
         ^
SyntaxError: invalid syntax
```

##### 基础数据类型

##### 变量作用域

##### 普通打印
* 数字、字符串、函数、类、结构体、枚举值、关键字、未定义值
* 多个变量同时打印
* 换行打印，同行打印
* 以不同的结尾符打印
```python
>>> print(123)
123
>>> print('aaa')
aaa
>>> print(123,456)
123 456
>>> print("abc",123)
abc 123
>>> print(print)
<built-in function print>
>>> print(dir)
<built-in function dir>
>>> print(print())

None
>>> print(dir())
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```
##### 结构化打印
* 把数据按照可读的方式打印出来
```python
>>> import pprint
>>> pprint.pprint({'a':123,'b':['abc','def'],'c':{'x':456,'y':789}},width=30)
{'a': 123,
 'b': ['abc', 'def'],
 'c': {'x': 456, 'y': 789}}
```

* 如何区别可变数据类型和不可变数据类型
* 变量作用域
* 判断变量是否相等
* 是否有常量？常量如何定义？常量特性？
* 普通打印
* 结构化打印
* 字符填充为固定宽度
* 字符串带变量拼接
* 对象打印
* 条件判断有哪些？
* 循环遍历有哪些？各有什么好用处？循环遍历时改变遍历对象的值
* 路径如何做到穷举、全覆盖
* 操作符可否重载？哪些情况可以重载？为什么要有重载？
* 变量重新赋值给另一个变量，原变量如何？修改新赋值的变量，原变量又如何？修改原变量，新变量如何？
* 字符串截取成数组，数组拼接成字符串
* 数组去重，数组内某个值的数量，数组排序，数组反转，两个数组合并，两个数组求并集和差集
* 字符串是否包含某个值，是否以某个值开始、结尾，字符串长度，字符串前后去除无效字符(比如空格)，字符串大小写转换，获取字符的某几位，
* 字符串转json，json转成列表或字典
* 是否有深浅拷贝，都是做什么的，适用场景是什么？
    * 浅拷贝：不管多么复杂的数据结构，只copy对象最外层本身，该对象引用的其他对象不copy， 内存里两个变量的地址是一样的，一个改变另一个也改变。
    * 深拷贝：完全复制原变量的所有数据，内存中生成一套完全一样的内容；只是值一样，内存地址不一样，一方修改另一方不受影响

## 0x02、常用数据结构
* 动态列表
* hash
* 字典
* 队列
* 堆栈

## 0x03、系统操作
* 获取用户输入
* 获取命令行参数
* 命令参数化
* 获取系统环境变量
* 获取文件路径

## 0x04、文件操作
* 创建文件夹
* 递归创建文件夹
* 创建文件
##### 读文件
```python

# 全部读出，为字符串
with open('a.txt') as f:
    content = f.read()

# 全部读出，按行分割的列表
with open('a.txt') as f:
    content = f.readlines()

# 一行一行的读
with open('a.txt') as f:
    line = f.readline()
    if line:
        content += line
    else:
        break
#
with open('a.txt') as f:
```
* 写文件
* 读大文件
* 移动文件夹及文件
* 重命名文件夹及文件

## 0x05、时间操作
* 获取当前时间
* 获取当前日期
* 获取前天、30天前、上个季度、一年前日期
* 字符串日期时间转时间类型
* 时间类型转字符串时间日期
* 日期时间中获取日期
* 获取整分、整时的时间
* 时间戳转时间、转字符串
* 字符串时间转时间戳
*

## 0x06、正则操作
* 匹配数字、小数
* 匹配字母，区分、不区分大小写
* 匹配汉字
* 匹配url
* 匹配邮箱
* 匹配手机号
* 匹配域名
* url截取成协议、域名、path、params

## 0x07、上传下载
* 上传、下载文件
* 上传、下载图像

## 0x08、线程/进程
* 线程与进程的区别
* 多线程执行
* 多进程执行
* 多进程共享变量
* 多线程锁如何使用

## 0x09、网络操作
* http请求
* socket编程

## 0x10、面向对象
* 继承
* 多态
* 封装
* 对象序列化传输，反序列化执行
* 判断某个实例是不是属于某个类

## 0x11、异常处理
* 错误、异常处理

## 0x12、工程
* 包管理
* 装饰器是什么，如何实现
* 编程模式是什么，都有哪些，作用是什么，如何实现？

## 0x13、常用方法实现
* 递归
* 排序
* 查找
* 数学库
* 随机数
* 加密算法

* 装饰器的写法，并打印出方法名
* b树，b+树
* GIL
* 协程
* grpc
* https://github.com/leeguandong/Interview-code-practice-python
* https://github.com/princewen/leetcode_python
* http://bookshadow.com/leetcode/
