

* docker进入到内部，停止内部启动docker时的进程，则docker会自动退出，然后docker停止。

### docker的run、create、start的区别。
* docker run相当于执行了两步操作：将镜像放入容器中（docker create）,然后将容器启动，使之变成运行时容器（docker start）。
* docker start的作用是，重新启动已存在的镜像。也就是说，如果使用这个命令，我们必须事先知道这个容器的ID，或者这个容器的名字，我们可以使用docker ps找到这个容器的信息。
* docker create是只创建容器，不启动。

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

### 显示所有的容器
* docker ps -a