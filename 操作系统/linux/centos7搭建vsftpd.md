1.首先看看vsftpd装了没有
    ->rpm  -q  vsftpd

2.没装的话就先安装吧
    ->yum -y install vsftpd

3.设置开机启动vsftpd ftp服务
    ->systemctl enable vsftpd

4.启动vsftpd服务
    ->service vsftpd start
    ps:管理vsftpd相关命令：
    停止vsftpd:  systemctl  stop  vsftpd
    重启vsftpd:  systemctl  restart  vsftpd

5.配置vsftpd服务器
    ->vim  /etc/vsftpd/vsftpd.conf
    #将下面
    ->anonymous_enable=YES
    ->#chroot_list_enable=YES
    -># (default follows)
    ->#chroot_list_file=/etc/vsftpd/chroot_list
    #改为
    ->anonymous_enable=NO
    ->chroot_list_enable=YES
    -># (default follows)
    ->chroot_list_file=/etc/vsftpd/chroot_list
#添加
    ->allow_writeable_chroot=YES
7.在/etc/vsftpd下新建文件chroot_list

8.用adduser增加用户ftpuser，用-d指定目录。显示的用法看adduser.
    ->useradd  -d  /var/www/html  -g ftp  ftpuser

9.用passwd设置用户的密码
    ->passwd ftpuser

10.重新启动vsftpd
    ->service vsftpd restart

11.开通telnet服务
    ->rpm -q xinetd
    ->yum -y install xinetd
    ->systemctl  enable  xinetd
    ->systemctl  start   xinetd
    #这样就开通了telnet了。
12.配置防火墙
    ->firewall-cmd --zone=public --add-port=21/tcp --permanent
    ->firewall-cmd --zone=public --add-port=23/tcp --permanent
    ps:命令含义：
     --zone #作用域
     --add-port=80/tcp  #添加端口，格式为：端口/通讯协议
     --permanent   #永久生效，没有此参数重启后失效
    ->firewall-cmd --reload   #重启防火墙
13.修改目录权限
    #这个目录的权限应该是770，owner是root，group是ftp
    ->chmod 770 /var/www/html
    ->chown root:ftp /var/www/html

问题：
1.解决用户无法进入目录问题：
    打开终端，输入：setsebool  -P  ftpd_disable_trans  1
