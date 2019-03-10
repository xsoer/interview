# mysql数据库主从同步

- 作者：codehackfox@gmail.com
- 时间：2019-03-10 18:25:53

>## 0x00、同步步骤

- 1.主库和从库创建同步账户
```
mysql> grant replication slave, replication client on *.* to repl@'192.168.1.%' identified by '123456';
```
- 2.主库配置/etc/my.cnf
```
server-id=130	#保证唯一值
log-bin=mysql-bin
binlog_format=mixed
binlog-do-db=test2
binlog-ignore-db=mysql
log-error=/var/lib/mysql/mysql.err
```
- 3.重启主库
- 4.查看主库状态
```
    mysql>show master status;
    +-------------------------+-----------------+--------------------+-------------------------+
    | File            |	 Position | Binlog_Do_DB | Binlog_Ignore_DB |
    +-------------------------+----------------+--------------------+--------------------------+
    | mysql-bin.000002 |      120 |   test2      |   mysql        |
    +-------------------------+----------------+---------------------+------------------------+
    1 row in set (0.00 sec)
```
- 5.从库配置 /etc/my.cnf
```
server-id=131 #保证唯一值
log-bin=mysql-bin
binlog_format=mixed
replicate-do-db=test2
replicate-ignore-db=mysql
relay_log=/var/lib/mysql/mysql-relay-bin
log_slave_updates=1
read_only=1
```
- 6.重启从库
- 7.指向主库操作
```
mysql> change master to master_host='192.168.1.201',
master_user='repl',
master_password='123456',
master_log_file='mysql-bin.000002',
master_log_pos=120;
```
- 8.开始同步
```
mysql>start slave;
```
- 9.查看状态
```
mysql>show slave status;
```
- 10.双向主从的话，把主库按照从库在配置一遍即可

>## 0x01、备注：

- 1.两个数据库版本尽量一致，如果不一致，高版本做从库，此时不可双向主从
- 2.主库和从库的数据库名必须相同；
- 3.主库和从库的复制可以精确到表，但是在需要更改主库或从库的数据结构时需要立刻重启slave；
- 4.不能在mysql配置文件里直接写入master的配置信息，需要用change master命令来完成；
- 5.指定replicate_do_db必须在my.ini里配置，不能用change master命令来完成；
- 6.如果不及时清理，日积月累二进制日志文件可能会把磁盘空间占满，可以在配置文件里加上expire_logs_days=7，只保留最近7天的日志，建议当slave不再使用时，通过reset slave来取消relaylog；
