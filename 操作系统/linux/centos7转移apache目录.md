1.假设转移目录为/mnt/www
    ->mkdir /mnt/www	   #创建www目录
2.停止apache服务
    ->systemctl  stop  httpd
3.编辑apache配置文件
    ->vim  /etc/httpd/conf/httpd.conf
    ->#DocumentRoot  “/var/www/html”   #旧目录
    ->DocumentRoot “/mnt/www”     #新目录
    ->#<Directory  “/var/www/html”>  #旧目录
    -><Directory  “/mnt/www”>
4.修改www下文件的权限
    ->chown -R apache:ftp /mnt/www   #修改为apache用户，否则不允许访问
    ->chmod -R  755 /mnt/www    #或者这样改
5.重启apache服务
    ->systemctl  start  httpd
