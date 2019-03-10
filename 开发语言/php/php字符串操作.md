# PHP字符串操作

- 作者：codehackfox@gmail.com
- 时间：2015-06-12 13:24:35

> ## 0x00、字符串操作

- 1.print 有返回值、只能输出一个、可以用在表达式中
 * echo 无返回值、能输出多个、不能用于表达式中

- 2.trim($strs) //去除两边的空格
 * rtrim($strs)  //去除右边的空格
 * ltrim($strs)  //去除左边的空格

- 3.点链接字符串(.)

- 4.strlen($strs)  //求字符串长度

- 5.explode(',',$strs)  //分割字符串为数组

- 6.implode(',',$arr)  //分割数组为字符串

- 7.strtoupper($strs),strtolower($strs)  //转换字符串大小写

- 8.!=、==  //比较两个对象是否相等

- 9.!== 、===   //比较两个对象及值是否相等

- 10.strcmp($str1,$str2)  //区分大小写比较字符串，前者大于后者返回大于零的数，小于返回小于零的数，相等则返回零

- 11.strcasecmp($str1,$str2) //不区分大小写比较字符串

- 12.strncmp($str1,$str2,n)  //区分大小写比较前n个字符串

- 13.strncasecmp($str1,$str2,n)  //不区分大小写比较前n个字符串

- 14.str_replace($oldstr,$newstr,$strs)  //区分大小写替换字符串内的字符

- 15.strstr($strs,$findstr)  //字符串查找

- 16.htmlspecialchars($str)  //将字符串内特殊的字符转换为html内的字符

- 17.md5($str)  //md5加密

- 18.strrev($str)  //反转字符串
