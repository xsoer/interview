"""
author: codehackfox@gmail.com
datetime: 2019-03-08 11:09:26
"""
import datetime


def deco1(func):
    print("func  before")
    start = datetime.datetime.now()
    ret = func()
    print("func after")
    end = datetime.datetime.now()
    print('func call time:', end-start)
    return ret


@deco1
def func():
    print("my name is func")

# 第一种，作为参数
# deco(func)

# 第二种，用@符号
# func()


def deco2(func):
    def wapper(*args, **kwargs):
        print("func  before")
        start = datetime.datetime.now()
        ret = func(*args, **kwargs)
        print("func after")
        end = datetime.datetime.now()
        print('func call time:', end-start)
        return ret
    return wapper


def func2():
    print("my name is func2")

deco2(func2)