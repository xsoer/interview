# docker基础文档
- 作者：codehackfox@gmail.com
- 时间：2019-03-10 18:06:12


>## 0x00、命令

- Management Commands:
  * config      Manage Docker configs
  * container   Manage containers
  * image       Manage images
  * network     Manage networks
  * node        Manage Swarm nodes
  * plugin      Manage plugins
  * secret      Manage Docker secrets
  * service     Manage services
  * stack       Manage Docker stacks
  * swarm       Manage Swarm
  * system      Manage Docker
  * volume      Manage volumes

- Commands:
  * attach      Attach local standard input, output, and error streams to a running container
  * build       Build an image from a Dockerfile
  * commit      Create a new image from a container's changes
  * cp          Copy files/folders between a container and the local filesystem
  * create      Create a new container
  * diff        Inspect changes to files or directories on a container's filesystem
  * events      Get real time events from the server
  * exec        Run a command in a running container
  * export      Export a container's filesystem as a tar archive
  * history     Show the history of an image
  * images      List images
  * import      Import the contents from a tarball to create a filesystem image
  * info        Display system-wide information
  * inspect     Return low-level information on Docker objects
  * kill        Kill one or more running containers
  * load        Load an image from a tar archive or STDIN
  * login       Log in to a Docker registry
  * logout      Log out from a Docker registry
  * logs        Fetch the logs of a container
  * pause       Pause all processes within one or more containers
  * port        List port mappings or a specific mapping for the container
  * ps          List containers
  * pull        Pull an image or a repository from a registry
  * push        Push an image or a repository to a registry
  * rename      Rename a container
  * restart     Restart one or more containers
  * rm          Remove one or more containers
  * rmi         Remove one or more images
  * run         Run a command in a new container
  * save        Save one or more images to a tar archive (streamed to STDOUT by default)
  * search      Search the Docker Hub for images
  * start       Start one or more stopped containers
  * stats       Display a live stream of container(s) resource usage statistics
  * stop        Stop one or more running containers
  * tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  * top         Display the running processes of a container
  * unpause     Unpause all processes within one or more containers
  * update      Update configuration of one or more containers
  * version     Show the Docker version information
  * wait        Block until one or more containers stop, then print their exit codes

- docker images      // 查看存在多少镜像
- docker ps         // 查看镜像运行情况
- docker run -t -i  // 运行镜像。并进行交互模式。
- docker stop     // 停止运行镜像，后边跟镜像ID或name
- docker search   // 搜索镜像仓库
- docker pull     // 拉取镜像
- docker inspect  // 查看镜像的json文件，即全部详细信息
- docker port     // 查看docker与宿主机的端口映射关系
- docker commit   // 用来生成新的版本
- docker build    // 用docker file来创建镜像
- docker tag      // 设置镜像标签

- 容器生命周期管理
  * run
  * start/stop/restart
  * kill
  * rm
  * pause/unpause·
  * create
  * exec

- 容器操作
  * ps
  * inspect
  * top
  * attach
  * events
  * logs
  * wait
  * export
  * port

- 容器rootfs命令
  * commit
  * cp
  * diff

- 镜像仓库
  * login
  * pull
  * push
  * search

- 本地镜像管理
  * images
  * rmi
  * tag
  * build
  * history
  * save
  * import

- info|version
  * info
  * version

>## 0x01、简介

### 链接映射
- docker有一个连接系统允许将多个容器连接在一起，共享连接信息。docker连接会创建一个父子关系，其中父容器可以看到子容器的信息。·

### 容器与虚拟机是互补的。
- 虚拟机是用来进行硬件资源划分的完美解决方案，它利用了硬件虚拟化技术，例如VT-x、AMD-V或者privilege level（权限等级）会同时通过一个hypervisor层来实现对资源的彻底隔离；而容器则是操作系统级别的虚拟化，利用的是内核的Cgroup和Namespace特性，此功能完全通过软件来实现，仅仅是进程本身就可以与其他进程隔离开，不需要任何辅助。
- Docker容器与主机共享操作系统内核，不同的容器之间可以共享部分系统资源，因此容器更加轻量级，消耗的资源也更少。而虚拟机会独占分配给自己的资源，几乎不存在资源共享，各个虚拟机实例之间近乎完全隔离，因此虚拟机更加重量级，也会消耗更多的资源。\

### 最小组成
- 对于Linux容器的最小组成，可以由以下公式来表示：
容器=cgroup+namespace+rootfs+容器引擎（用户态工具）
- 其中各项的功能分别为：
  - Cgroup：资源控制。
  - Namespace：访问隔离。
  - rootfs：文件系统隔离。
  - 容器引擎：生命周期控制。
- 目前市场上所有Linux容器项目都包含以上组件。

>## 0x02、Cgroups
- Cgroup是control group的简写，属于Linux内核提供的一个特性，用于限制和隔离一组进程对系统资源的使用，也就是做资源QoS，这些资源主要包括CPU、内存、block I/O和网络带宽。
- 从实现的角度来看，Cgroup实现了一个通用的进程分组的框架，而不同资源的具体管理则是由各个Cgroup子系统实现的。
- Cgroup中实现的子系统及其作用如下：
  - devices：设备权限控制。
  - cpuset：分配指定的CPU和内存节点。
  - cpu：控制CPU占用率。
  - cpuacct：统计CPU使用情况。
  - memory：限制内存的使用上限。
  - freezer：冻结（暂停）Cgroup中的进程。
  - net_cls：配合tc（traffic controller）限制网络带宽。
  - net_prio：设置进程的网络流量优先级。
  - huge_tlb：限制HugeTLB的使用。
  - perf_event：允许Perf工具基于Cgroup分组   
  - 做性能监测。

#### Cgroups子系统
> cpuset子系统

- cpuset可以为一组进程分配指定的CPU和内存节点。

> cpu子系统

- 子系统用于限制进程的CPU占用率。实际上它有三个功能，分别通过不同的接口来提供。
  - CPU比重分配。这个特性使用的接口是cpu.shares。
  - CPU带宽限制。这个特性使用的接口是cpu.cfs_period_us和cpu.cfs_quota_us，这两个接口的单位是微秒
  - 实时进程的CPU带宽限制。以上两个特性都只能限制普通进程，若要限制实时进程，就要使用cpu.rt_period_us和cpu.rt_runtime_us这两个接口了。使用方法和上面类似。

> cpuacct子系统

- cpuacct子系统用来统计各个Cgroup的CPU使用情况

> memory子系统

- memory子系统用来限制Cgroup所能使用的内存上限

> blkio子系统

- blkio子系统用来限制Cgroup的block I/O带宽

> devices子系统

- devices子系统用来控制Cgroup的进程对哪些设备有访问权限


>## 0x03、Namespace
- Namespace是将内核的全局资源做封装，使得每个Namespace都有一份独立的资源，因此不同的进程在各自的Namespace内对同一种资源的使用不会互相干扰
- 目前Linux内核总共实现了6种Namespace：
  - IPC：隔离System V IPC和POSIX消息队列。
  - Network：隔离网络资源。
  - Mount：隔离文件系统挂载点。
  - PID：隔离进程ID。
  - UTS：隔离主机名和域名。
  - User：隔离用户ID和组ID。
- 对Namespace的操作，主要是通过clone、setns和unshare这3个系统调用来完成的。

> 子命名空间

- 1.UTS Namespace
  - UTS Namespace用于对主机名和域名进行隔离，也就是uname系统调用使用的结构体struct utsname里的nodename和domainname这两个字段，UTS这个名字也是由此而来的。
- 2.IPC Namespace
  - IPC是Inter-Process Communication的简写，也就是进程间通信。Linux提供了很多种进程间通信的机制，IPC Namespace针对的是SystemV IPC和Posix消息队列。
- 3.PID Namespace
  - PID Namespace用于隔离进程PID号，这样一来，不同的Namespace里的进程PID号就可以是一样的了。
- 4.Mount Namespace
  - Mount Namespace用来隔离文件系统挂载点，每个进程能看到的文件系统都记录在/proc/$$/mounts里。
- 5.Network Namespace
  - 这个Namespace会对网络相关的系统资源进行隔离，每个Network Namespace都有自己的网络设备、IP地址、路由表、/proc/net目录、端口号等。
- 6.User Namespace
  - User Namespace用来隔离用户和组ID，也就是说一个进程在Namespace里的用户和组ID与它在host里的ID可以不一样，这样说可能读者还不理解有什么实际的用处。

- Namespace和Cgroup的使用是很灵活的，同时这里面又有不少需要注意的地方，因此直接操作Namespace和Cgroup并不是很容易。正是因为这些原因，Docker通过Libcontainer来处理这些底层的事情。这样一来，Docker只需要简单地调用Libcontainer的API，就能将完整的容器搭建起来


>## 0x04、Images
- 是启动融资的rootfs,只读模版

#### 一、基本概念
> 创建镜像

- 1.直接下载镜像
```
docker pull centos
```
- 2.导入镜像
```
docker save -o centos.tar centos
docker load -i centos.tar
```
- 3.制作新镜像
  - docker import 用于导入包含根文件系统的归档，并将之变成docker镜像
  - docker commit 可以增量的生成镜像，可以把容器保存为一个镜像
  - docker build 可以用Dockerfile来制作镜像

> 传输镜像

- 1.用Docker镜像仓库做中转
- 2.docker export/docker save生成tar包
- 3.Dockerfile文件

> 运行镜像

- docker run 来运营一个镜像成为容器

#### 二、组织结构

> 数据内容

- 包含着数据和元数据。
  - 数据有一层一层的image layer组成，元数据则是一些JSON文件，用来描述数据之间的关系和容器配置信息。
- Docker对数据进行来完整性校验，这种完整性对凭证是有镜像仓库提供的。

```shell
ll /var/lab/docker
```
- 1.总体信息
  * 从repositories-overlay文件可以看到该存储目录下的所有image以及其对应的layer ID.
- 2.数据和元数据
  * graph和overlay目录包含本地镜像库中所有元数据和数据信息
  * 对于不同的存储驱动，数据的存储位置和存储结构是不同的。
  * 元数据包含json和layersize两个文件，其中json包含来必要的层次和配置信息，layersize文件包含来该层的大小。
  * 先通过repositories-overlay获取image对应的layer ID；在根据layer对应的元数据梳理出image包含的所有层，以及层之间的关系；在使用联合挂载技术还原出容器启动所需要的rootfs和一些基本配置信息。
- 3.数据组织
```
docker inspect dockerID
```

> 扩展知识

- docker引入的联合挂载(Union mount)使镜像分层成为可能；而git式管理，使基础镜像复用成为可能。
- 1.联合挂载
  * 把多个目录挂载到同一个目录，对外呈现这些目录的联合。·
- 2.写时复制

>## 0x05、仓库进阶

#### 什么是仓库
> 仓库的组成

- 仓库的名字通常有两部分组成，中间以斜线分隔。前边是用户名，后边是镜像名。
- 仓库有镜像存储系统和账户管理系统

```shell
docker login -u <user_name> -p <password> -e <email> <registry domain>

```

> 仓库镜像

- 仓库下面包含一组镜像，彼此之间用标签(tag)区分。一个完整的镜像地址通常有 服务器地址、仓库名称和标签组成。
- 1.上传镜像：push

```shell
// 表示向本地私有仓库上传镜像。如果不写服务器地址，默认上传到官方Docker Hub。一般需要先登陆在上传。
docker push localhost::5000/official/ubuntu:14.04
```

- 2.下载镜像：pull

```shell
docker pull ubuntu:14.04
```

- 3.搜索镜像：search

```shell
docker search ubuntu
```

  * 注：在上传、下载过程中是逐层进行的。下载和搜索不需要登陆

> restfulApi介绍

> 上传、下载、鉴权原理

> 私有仓库搭建


>## 0x06、docker网络


>## 0x07、容器卷管理
- 可以把本地文件目录挂载到容器内

>## 0x08、DockerAPI
- Docker Remote API
- Docker Registry API
- Docker Hub API

>## 0x09、Docker安全

> 包含内容

- 容器的安全性
- 镜像的安全性
- Docker daemon的安全性

> 容器安全

- Cgroup
  * 限制CPU：指定CPU权重、使用上限
  * 限制内存
  * 限制块设备I/O
- ulimit
  * core dump文件大小
  * 进程数据段大小
  * 可创建文件大小
  * 常驻内存集大小
  * 打开文件数量
  * 进程栈的大小
  * CPU时间
  * 单个用户的最大进程数
  * 进程的最大虚拟内存
- 容器组网
  * 将容器隔离在不同的网络内
- 容器+虚拟化
- 镜像签名
- 日志审计
- 监控
- 文件系统级保护
- capability
  * 可以作用在进程上；也可以作用在程序文件上
  * 与sudo不同，sudo可以配置某个用户可以执行某个命令或更改某个文件；而capablity则是让某个程序拥有某种能力
  * 每个进程有三个和能力有关的位图：Inheritable(I)、Permitted(P)和Effective(E)
- SELinux
- APPArmor
- Seccomp
- grsecurity

> 安全加固

> 安全遗留问题


>## 0x10、Libcontainer

- 容器引擎：一种驱动和管理容器生命周期的runtime工具

>## 0x11、Docker实战
- 部署web服务

>## 0x12、Docker集群
- Compose
- Machine
- Swarm

>## 0x13、Docker生态圈
