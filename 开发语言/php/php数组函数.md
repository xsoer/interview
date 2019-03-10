# PHP数组函数

- 作者：codehackfox@gmail.com
- 时间：2015-07-05 01:53:37

> ## 0x00、函数

- 1.array()  []   //生成数组
- 2.isset($arr[$i])//判断该值是否存在
- 3.is_array($arr)  //判断是否是数组、
- 4.array_push($arr,$a)  //从尾部往数组内添加值
- 5.array_unshift  //从头部往数组内插入
- 6.array_pop  //弹出数组最后一个
- 7.array_shift  //弹出数组第一个
- 8.range(0,6)  //产生一个从0到6的数组
- 9.in_array($a,$arr)  //检验是否在数组内
- 10.array_keys()  //返回数组的所有键值
- 11.array_change_key_case($arr1,CASE_UPPER)  //改变键值为大写 或者CASE_LOWER 小写
- 12.array_merge()  //合并两个或多个数组
- 13.sort($arr)  //给数组排序，升序  
- 14.count()  //查询数组内元素的个数
- 15.array_filter($arr,$fun)  //用一个函数过滤数组
- 16.print_r()  //输出数组
- 17.foreach($arr as $k)  //遍历数组
- 18.while(list($key,$value)==each($arr))  //list遍历数组
- 19.explode(',',$arr)  //去除字符串中的逗号，转为数组
- 20.implode(',',$arr)  //将数组转为字符串
- 21.ksort()  //按键排序
- 22.asort()  //按值排序
- 23.rsort($arr)  //降序排序
