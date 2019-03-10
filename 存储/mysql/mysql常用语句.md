# mysql常用语句

- 作者：codehackfox@gmail.com
- 时间：2019-03-10 18:20:48

>## 0x00、常用语句

- 1.授权用户
```
mysql>GRANT ALL PRIVILEGES ON *.* TO 'zxc'@'%' IDENTIFIED BY 'ydp#2015$Z!!!' WITH GRANT OPTION;
mysql>FLUSH PRIVILEGES;
```
- 2.远程连接
```
shell>mysql -h127.0.0.1 -P3306 -uroot -p
```
- 3.导出数据库
```
shell>mysqldump -h127.0.0.1 -P3306 -uroot -p sqsx > sqsx.sql
```
- 4.导入数据库
```
shell>mysql -uroot -p sqsx < sqsx.sql
```
- 5.分析查询
```
mysql>explain select * from user;
```
- 6.查询所有的进程
```
mysql>show procelist;
```
- 7.建数据库语句
```
mysql>create database dbname default character set utf8 collate utf8_general_ci;
```
- 8.创建数据表语句
```
mysql>create table dbname.tablename () engine=Innodb charset=utf8;
```
- 9.删除数据库
```
mysql>drop database dbname;
```
- 10.查看数据库状态
```
mysql>use dbname;
mysql>status;
```
- 11.查看参数
```
mysql>show variables like “%sql%”;
```
- 12.查看事件
```
mysql>show events;
```
- 13.查看触发器
```
mysql>show triggers;
```
- 14.查看所有参数
```
mysql>show status;
```
- 15.查看打开表
```
mysql>show open tables;
```
- 16.查看表状态
```
mysql>show table status;
```
- 17.查看主数据状态
```
mysql>show master status;
```
- 18.查看从数据库状态
```
mysql>show slave status;
```
- 19.查看函数状态
```
mysql>show function status;
```
- 20.查看插件
```
mysql>show plugins;
```
- 21.查看某用户的授权
```
mysql>show grants for username;
```
- 22.查看错误
```
mysql>show errors;
```
- 23.查看创建表语句
```
mysql>show create table tablename;
```
- 24.查看表头
```
mysql>show columns from tablename;
```
- 25.查看存储引擎
```
mysql>show engines;
```
- 26.查看表状态
```
mysql>show table status;
```
