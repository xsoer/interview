

* docker进入到内部，停止内部启动docker时的进程，则docker会自动退出，然后docker停止。

### docker的run、create、start的区别。
* docker run相当于执行了两步操作：将镜像放入容器中（docker create）,然后将容器启动，使之变成运行时容器（docker start）。
* docker start的作用是，重新启动已存在的镜像。也就是说，如果使用这个命令，我们必须事先知道这个容器的ID，或者这个容器的名字，我们可以使用docker ps找到这个容器的信息。
* docker create是只创建容器，不启动。create不能后台运行，也就是不能有`-d`参数

### 写出一条创建容器运行的命令，并解释其参数
```
docker run -d --mount type=bind,src=/data/logs/project,dst=/home/log --name service_name -e token=token_str image_name /bin/sh -c "python main.py"
```

* -d:表示后台运行
* --mount:挂在目录，让容器和主机共享目录
* --name:运行的容器的名称
* -e:添加环境变量

### 显示正在运行的容器
* docker ps


### 重命名容器
* docker rename old_name new_name
* 无论容器是运行还是停止，都可以进行重命名。过后就用新名称来操作就可用了。

### 启动中的容器可以直接删除吗
* 启动中的容器不允许直接删除，必须要先停止，在删除。

### docker service是干什么的？
* docker swarm集群的管理工具

### 列出所有容器ID
docker ps -aq

### 查看所有运行或者不运行容器

docker ps -a

### 停止所有的container（容器），这样才能够删除其中的images：

docker stop $(docker ps -a -q) 或者 docker stop $(docker ps -aq)

### 删除container（容器）：
* 删除停止运行的容器
    docker rm $(docker ps -a -q) 或者 docker rm $(docker ps -aq)
* 删除运行中的容器
    docker rm -f $(docker ps -a -q) 或者 docker rm -f $(docker ps -aq)

### 查看当前有些什么images

docker images

### 删除images（镜像），通过image的id来指定删除谁
docker rmi <image id>

### 想要删除untagged images，也就是那些id为的image的话可以用

docker rmi $(docker images | grep "^<none>" | awk "{print $3}")

### 要删除全部image（镜像）的话

docker rmi $(docker images -q)

### 强制删除全部image的话

docker rmi -f $(docker images -q)

### 从容器到宿主机复制

 docker cp tomcat：/webapps/js/text.js /home/admin
 docker  cp 容器名:  容器路径       宿主机路径

### 从宿主机到容器复制

 docker cp /home/admin/text.js tomcat：/webapps/js
 docker cp 宿主路径中文件      容器名  容器路径

### 删除所有停止的容器

docker container prune

### 删除所有不使用的镜像

docker image prune --force --all
docker image prune -f -a

### 停止、启动、杀死、重启一个容器

docker stop Name或者ID
docker start Name或者ID
docker kill Name或者ID
docker restart name或者ID

### docker进入容器，查看配置文件

docker exec ：在运行的容器中执行命令
        -d :分离模式: 在后台运行
        -i :即使没有附加也保持STDIN（标准输入） 打开,以交互模式运行容器，通常与 -t 同时使用；
        -t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
docker exec -it  容器id或容器名称 /bin/bash
