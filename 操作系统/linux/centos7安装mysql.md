# centos7安装mysql

- 作者：
- 时间：


1.安裝 MySQL Repository:
    # rpm -Uvh  http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
                https://repo.mysql.com//mysql57-community-release-el6-7.noarch.rpm
                http://repo.mysql.com//mysql57-community-release-el7-7.noarch.rpm
2.安裝 MySQL Server, MySQL client 已經包括在 server 套件內:
    # yum install mysql-community-server
3.开机自动启动 MySQL
    # /usr/bin/systemctl enable mysqld
4.启动 MySQL
    # /usr/bin/systemctl start mysqld
5.MySQL 預設為空密碼, 執行以下指令修改:
    # /usr/bin/mysql_secure_installation
6.设置新密码
    #set password for root@localhost password=(“password”);
