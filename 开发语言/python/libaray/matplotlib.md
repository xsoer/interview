# matplotlib库分析

- 作者：codehackfox@gmail.com
- 时间：2019-03-08 15:57:42


>## 0x00、pyplot

```python
plot.hist(data, density=None, bins=30, range=(0, 100), label=dts)
plot.title('followers_count')
plot.legend(prop={'size': 10})
plot.savefig('followers_count.png')
plot.close()
```

- hist
- title
- legend
- savefig
- close

- matplotlib使用numpy进行数组运算，并调用一系列其他的Python库来实现硬件交互。matplotlib的核心是一套由对象构成的绘图API。
- Python中的函数式编程是通过封装对象实现的

