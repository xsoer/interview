# python装饰器

- 作者：codehackfox@gmail.com
- 时间：2019-03-08 10:56:37


>## 0x00、装饰器

- 在函数调用前后想添加功能，但又不希望修改原函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
- 本质上，decorator就是一个返回函数的高阶函数。

```python
def deco1(func):
    print("func  before")
    start = datetime.datetime.now()
    ret = func()
    print("func after")
    end = datetime.datetime.now()
    return ret

def func():
    print("my name is func")
```

- 带了装饰器的函数会自动运行。

>## 0x01、复杂的装饰器

