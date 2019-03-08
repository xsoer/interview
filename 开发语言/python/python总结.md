> 基本概念



> 基本类型
- 1.数字:numbers
  int,double,float,bool,complex
    1)可同时为多个变量赋值
    2)一个变量可以通过赋值指向不同类型的对象
    3)数值的除法(/)总时返回浮点数，要获得整数用(//)
- 2.字符串:string
    1)可以用''或""
    2)可以使用(\)转义
    3)不想转义需要字符串前加r
    4)可以使用(+)号连接，用(*)可以重复
    5)可以使用(\)连接上下行，也可以用'''...'''或"""..."""
    6)没有单独的字符，一个字符就是长度为1的字符串
    7)可对字符串切片，用冒号切割，形式为：变量[头下标:尾下标]，从左向右以0开始，从右向左以-1开始
    8)字符串不能改变
- 3.列表:list->[]
    1)写在方括号内，并用逗号隔开
    2)元素类型可以不同
    3)可以被索引和切片
    4)支持串联操作，用(+)操作符
    5)列表元素可以改变
    6)内置很多方法：如append(i),pop(i),len(),insert(i,x),remove(x),index(i),count(i),sort(),reverse(),copy()
- 4.元组:tuple->()
    1)写在圆括号内，用逗号隔开
    2)元素类型可以不同
    3)可以被索引和切片
    4)支持串联操作，用(+)操作符
    5)元素不可改变
- 5.集合：set->{}
    1)无序不重复元素集
    2)基本功能是进行成员关系测试和消除重复元素
    3)可以使用大括号或set()函数创建集合；但创建空集合必须用set()函数，因为{}是用来创建字典的
- 6.字典：Dictionary->{'':'',...}
    1)一种映射类型，一个无序的键:值对的集合
    2)dict()函数直接从键值对序列中构造，也可以进行推导
    3)内置很多方法：如clear(),keys(),values()等
    4)字典的关键字必须是不可变类型，且不能重复


- list,string和tuple都属于sequence(序列)


### 注释
- 1.#号单行注释
- 2.'''或"""多行注释


### 格式
- 1.使用缩进来划分语句，相同缩进数的语句在一起组成一个语句块
- 2.没有switch-case语句
- 3.每个条件后都要是用(:)，表示接下来满足条件后要执行的语句


### 关键字
while,if,else,elif,pass,True,False,None,for,in,do
break,continue,as,del,from,global,import,is,lambda,not,or
class,def,self,return,with,yield,nonlocal
try,except,raise,finally



### 操作符
<,>,<=,>=,==,!=


### 函数
1.range(begin,end,step):
2.input("some word"):
3.len()
4.dir()
5.format()
6.open()
    1)f.read()
    2)f.write()
    3)f.readlines()
    4)f.tell()
    5)f.feek()
    6)f.close()
7.__str__
8.__init__
9.__del__
10.__repr__
11.__setitem__
12.__getitem__
13.__len__
14.__cmp__
15.__call__
16.__add__
17.__sub__
18.__mul__
19.__div__
20.__mod__
21.__pow__


### 模块
1.conllections
    1)deque
2.sys
3.fibo
4.math
5.os
    1)getcwd()
    2)get_exec_path()
    3)getenv('varname')
6.re
7.glob
8.urllib
9.smtplib
10.datetime
11.zlib
12.timeit
13.doctest
14.unittest
15.keyword
    1)kwlist
    2)iskeyword('word')

__name__属性


### 包


### 特性
- 1.自动检测递归深度，如果无限太深，会自动停止并抛出异常。