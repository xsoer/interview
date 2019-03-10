# mysql技术

- 作者：codehackfox@gmail.com
- 时间：2015-10-12 12:23:00

> ## 0x00、数据库基本概念

- 1.数据模型：描述数据、数据关系、数据语义及一致性约束的概念工具集
    - 1）网络模型
    - 2）层次模型
    - 3）关系模型*
- 2.关系模型：用表来描述数据与数据间的关系
- 3.数据完整性和数据保护
- 4.mysql 1.0诞生于1995年
- 5.mysql以守护进程运行

> ## 0x01、结构体系

- 1.连接器
    mysql> show variables like "%connection%";
    进行身份验证、线程重用,连接限制,检查内存,数据缓存；管理用户的连接，线程处理等需要缓存的需求。
- 2.连接池组件
- 3.缓存
    全局和引擎特定的缓存和缓冲区
    mysql> show variables like '%query_cache%';
- 4.权限
- 5.表管理器
- 6.日志管理
- 7.sql接口组件
    进行DML、DDL,存储过程、视图、触发器等操作和管理；用户通过SQL命令来查询所需结果。
- 8.插件式存储引擎
    mysql> show engines;
- 9.解析器
    查询翻译对象的特权；SQL命令传递到解析器的时候会被解析器验证和解析
- 10.优化器
    访问路径的统计数据
    mysql> select @@optimizer_switch;
- 11.管理服务与工具组件
    备份和恢复的安全性，复制，集群，管理，配置，迁移和元数据
- 12.物理文件
    #1.日志文件
        1)错误日志：errorlog
        2)二进制日志：binlog
        3)更新日志：update log
        4)查询日志：query log
        5)慢查询日志：slow query log
        6)innodb在线redo日志：innodb redo log
    #2.数据文件
        1).frm:任何存储引擎都有一个，存储表结构定义信息
        2).MYD:MYISAM存储引擎专用，存储数据
        3).MYI:MYISAM存储引擎专用，存储索引信息
        4).idb和idbdata:innodb存储引擎存储数据，.idb存储独享表空间数据，idbdata存储共享表空间数据
    #3.replication相关文件：
        1)master.info文件：存在于slave端的数据目录下，存放master端的ip，用户，连接密码和接口等数据
        2)relay log和relay log index
        3)relay-log.info文件
    #4.其他文件
        1)system config file:my.cnf
        2)pid file:存放mysql进程
        3)socket file:unix\linux环境下才有，可以不用tcp协议连接而用unix的socket来连接mysql



> ## 0x02、系统架构

1.逻辑模块
    #1.SQL Layer:权限判断、sql解析、执行计划优化、query cache的处理
        1)初始化模块：在mysql server启动时，对整个系统做各种各样的优化，如：各种buffer、cache结构的初始化和内存空间申请，各种系统变量初始化，各种存储引擎初始化等
        2)核心API:提供一些需要非常高效的底层操作功能的优化实现,包括各种底层数据结构的实现，特殊算法的实现，字符串处理，数字处理等，小文件I/O，格式化输出，以及最重要的内存管理部分
        3)网络交换模块：抽象出底层网络交互所使用的接口api， 实现底层网络数据的接收与发送，以方便其他各个模块调用，以及对这一部分的维护。
        4)Client&Server 交换协议模块：任何C/S结构的软件系统， 都肯定会有自己独有的信息交互协议，MySQL也不例外。MySQL的Client & Server 交互协议模块部分，实现了客户端与MySQL交互过程中的所有协议。
                当然这些协议都是建立在现有的OS和网络协议之上的，如TCP/IP以及Unix Socket
        5)用户模块：主要包括用户的登录连接权限控制和用户的授权管理
        6)访问控制模块：根据用户模块中各用户的授权信息， 以及数据库自身特有的各种约束， 来控制用户对数据的访问。 用户模块和访问控制模块两者结合起来， 组成了MySQL整个数据库系统的权限安全管理的功能
        7)连接管理、连接线程和线程管理：负责监听对MySQL Server的各种请求，接收连接请求，转发所有连接请求到线程管理模块。每一个连接上MySQL Server的客户端请求都会被分配（或创建）一个
                连接线程为其单独服务。而连接线程的主要工作就是负责 MySQL Server与客户端的通信，接受客户端的命令请求，传递Server端的结果信息等。线程管理模块则负责管理维护这些
                连接线程。包括线程的创建，线程的cache等
        8)Query解析和转发模块：MySQL中我们习惯将所有Client端发送给Server端的命令都称为query， 在 MySQL Server里面，连接线程接收到客户端的一个 Query后，会直接将该 query传递给专门负责
                将各种Query进行分类然后转发给各个对应的处理模块， 这个模块就是query解析和转发模块。 其主要工作就是将query语句进行语义和语法的分析， 然后按照不同的操作类型进行分
                类，然后做出针对性的转发。
        9)Query Cache模块：主要功能是将客户端提交给MySQL的Select类query请求的返回结果集cache到内存中， 与该query的一个hash值做一个对应。该Query所取数据的基表发生任何数据的变化之后， MySQL会自动使该query的
                Cache 失效。在读写比例非常高的应用系统中， Query Cache对性能的提高是非常显著的。当然它对内存的消耗也是非常大的。
        10)Query优化器模块：根据客户端请求的query语句，和数据库中的一些统计信息，在一系列算法的基础上进行分析，得出一个最优的策略，告诉后面的程序如何取得这个query语句的结果。
        11)表变更管理模块：主要是负责完成一些DML和 DDL的query，如： update， delte， insert，create table， alter table等语句的处理
        12)表维护模块：表的状态检查，错误修复，以及优化和分析等工作都是表维护模块需要做的事情。
        13)系统状态管理模块：负责在客户端请求系统状态的时候， 将各种状态数据返回给用户， 像DBA常用的各种show status命令， show variables命令等， 所得到的结果都是由这个模块返回的
        14)表管理器：表管理器的工作主要就是维护.frm等文件，以及一个cache，该cache中的主要内容是各个表的结构信息。此外它还维护table级别的锁管理。
        15)日志记录模块：日志记录模块主要负责整个系统级别的逻辑层的日志的记录，包括error log， binary log， slow query log等
        16)复制模块：可分为 Master 模块和 Slave 模块两部分， Master 模块主要负责在Replication环境中读取Master端的binary日志， 以及与 Slave端的I/O线程交互等工作。
                Slave模块比Master模块所要做的事情稍多一些，在系统中主要体现在两个线程上面。一个是负责从Master请求和接受binary日志， 并写入本地relay log中的I/O线程。 另外一
                个是负责从relay log中读取相关日志事件， 然后解析成可以在Slave端正确执行并得到和Master端完全相同的结果的命令并再交给Slave执行的SQL线程。
        17)存储引擎接口模块：
    #2.Storage Engine Layer
        1)MYISAM
            *支持三种索引：B-tree索引、R-tree索引、Full-text索引
            *数据存放格式：静态固定长度(FIXED)、动态可变长度(DYNAMIC)、压缩格式(COMPRESSED)三种格式，同过创建表时指定ROW_FORMAT指定
            *不支持事务，表级锁
        2)innodb
            *支持事务安装：四个级别READ UNCOMMITTED， READ COMMITTED， REPEATABLE READ和SERIALIZABLE。
            *数据多版本读取：
            *锁定机制的改进：实现了行级锁
            *支持外键
            *存在表空间概念：
                共享表空间：必须存在，innodb的undo信息和其他一些元数据信息都是存放在共享表空间里面的。 共享表空间的数据文件是可以设置为固定大小和可自动扩展大小两种形式
                独享表空间
        3)NDB Cluster
            *负责管理各个节点的Manage节点主机
            *SQL 层的SQL服务器节点
            *Storage层的NDB数据节点，也就是上面说的NDB Cluster


>## 0x03、安全
- 1.网络
- 2.主机
- 3.数据库
- 4.代码
- 5.权限
    * 1.有关权限信息主要存储在几个被称为 grant tables 的系统表中，即： mysql.User， mysql.db， mysql.Host， mysql.table_priv和mysql.column_priv
    * 2.由于权限信息数据量比较小，而且访问又非常频繁，所以Mysql在启动的时候，就会将所有的权限信息都Load到内存中保存在几个特定的结构中。
    * 3.议读者一般情况下尽量使用GRANT， REVOKE， CREATE USER以及DROP USER命令来进行用户和权限的变更操作， 尽量减少直接修改grant tables来实现用户和权限变更的操作
    * 4.查询权限：SHOW GRANTS FOR 'username'@'hostname'
    * 5.权限级别：分为五个级别
        1)Global Level:称为全局权限控制， 所有权限信息都保存在mysql.user表中。 Global Level的所有权限都是针对整个mysqld的，对所有的数据库下的所有表及所有
                字段都有效。如果一个权限是以Global Level来授予的，则会覆盖其他所有级别的相同权限设置。
                只需要在执行GRANT命令的时候，用“ *.*”来指定适用范围是Global的即可，当有多个权限需要授予的时候，也并不需要多次重复执行GRANT命令，只需要一次将所有需要的权限名称通过逗号（ “ ,”）分隔开即可，
        2)Database Level:Database Level是在Global Level之下，其他三个Level之上的权限级别，其作用域即为所指定整个数据库中的所有对象。与Global Level的权限相比， Database Level主要
                少了以下几个权限：CREATE USER，FILE，PROCESS，RELOAD，REPLICATION CLIENT，REPLICATION SLAVE， SHOW DATABASES， SHUTDOWN， SUPER和USAGE这几个权限，没有增加任何权限。
                *1.执行GRANT命令的时候，通过“ database.*”来限定权限作用域为database整个数据库
                *2.先通过USE命令选定需要授权的数据库，然后通过“ *”来限定作用域，这样授权的作用域实际上就是当前选定的整个数据库
        3)Table Level:Database Level之下就是 Table Level的权限了， Table Level的权限可以被 GlobalLevel和Database Level的权限所覆盖， 同时也能覆盖Column Level和Routine Level的
                权限.权限作用范围是授权语句中所指定数据库的指定表。
                仅有ALTER， CREATE， DELETE， DROP， INDEX， INSERT， SELECT UPDATE这八种权限
        4)Column Level： 权限作用范围就更小了，仅仅是某个表的指定的某个（活某些）列。
                *由于权限的覆盖原则， Column Level的权限同样可以被 Global， Database， Table这三个级别的权限中的相同级别所覆盖
                *而且由于 Column Level所针对的权限和 Routine Level的权限作用域没有重合部分，所以不会有覆盖与被覆盖的关系。
                *针对Column Level级别的权限仅有INSERT， SELECT和UPDATE这三种。
                *Column Level的权限授权语句语法基本和Table Level差不多，只是需要在权限名称后面将需要授权的列名列表通过括号括起来
                *某个用户在向某个表插入（ INSERT）数据的时候，如果该用户在该表中某列上面没有INSERT权限，则该列的数据将以默认值填充。这一点和很多其他的数据库都有一些
                 区别，是MySQL自己在SQL上面所做的扩展
        5)Routine Level:权限主要只有 EXECUTE和 ALTER ROUTINE两种
                *主要针对的对象是procedure和function这两种对象
                *在授予 Routine Level权限的时候，需要指定数据库和相关对象
        6)GRANT权限:拥有GRANT权限的用户可以将自身所拥有的任何权限全部授予其他任何用户是一个非常特殊也非常重要的权限。
                *GRANT权限的授予方式也和其他任何权限都不太一样，通常都是通过在执行GRANT授权语句的时候在最后添加WITH GRANT OPTION子句达到授予GRANT权限的目的
        7)以上五个Level的权限中， Table、 Column和Routine三者在授权中所依赖（或者引用）的对象必须是已经存在的，而不像Database Level的权限授予，
                可以在当前不存在该数据库的时候就完成授权
6.访问控制原理
    #1.两个模块：用户管理模块和访问控制模块
    #2.用户管理模块：
        1)主要是有user表
        2)如果指定用户访问，需有-h选项指定连接ip，mysql默认用localhost指定连接
        3)权限更新：FLUSH PRIVILEGES会强行让MySQL更新Load到内存中的权限信息；
                *GRANT、 REVOKE或者CREATE USER和DROP USER操作会直接更新内存中俄权限信息；
                *重启MySQL会让MySQL完全从grant tables中读取权限信息
                *于Global Level的权限信息的修改，仅仅只有更改之后新建连接才会用到，对于已经连接上的session并不会受到影响。
                *而对于Database Level的权限信息的修改，只有当客户端请求执行了“ USE database_name” 命令之后，才会在重新校验中使用到新的权限信息。
                *所以有些时候如果在做了比较紧急的Global和Database这两个Level的权限变更之后，可能需要通过“ KILL” 命令将已经连接在MySQL中的session 杀掉强迫他们重新连接以使用更新后的权限。
                *对于Table Level和Column Level的权限，则会在下一次需要使用到该权限的Query被请求的时候生效，也就是说，对于应用来讲，这两个Level的权限，更新之后立刻就生效了，而不会需要执行“ KILL” 命令

    #3.访问控制模块：
        1) MySQL 接收到客户端的请求之后， 访问控制模块是需要校验该用户是否满足提交的请求所需要的权限。 权限校验过程是从最大范围的权限往最小范围的权限开始依次校验所涉及到的每个对象的每个权限
        2)MySQL首先会查找存储在内存结构中的权限数据，首先查找 Global Level 权限，如果所需权限在 Global Level 都有定义（ GRANT或者 REVOKE），
                则完成权限校验（通过或者拒绝） ，如果没有找到所有权限的定义，则会继续往后查找Database Level 权限，进行 Global Level 未定义的所需权限的校验，如果仍然没有能够
                找到所有所需权限的定义， MySQL 会继续往更小范围的权限定义域查找，也就是 Table Level，最后则是 Column Level 或者 Routine Level
        3) MySQL的权限是授予“ username@hostname” 的，也就是说，至少需要用户名和主机名二者才能确定一个访问者的权限。又由于hostname可以是一个含有通配符
                的域名，也可以是一个含有通配符的IP地址段。那么如果同一个用户有两条权限信息，一条是针对特定域名的， 另外一个是含有通配符的域名， 而且前者属于后者包含。 这时候MySQL
                如何来确定权限信息呢？实际上MySQL永远优先考虑更精确范围的权限。 在MySQL内部会按照username和hostname作一个排序， 对于相同username的权限， 其host信息越接近访问
                者的来源host， 则排序位置越靠前， 则越早被校验使用到。 而且， MySQL在权限校验过程中，只要找到匹配的权限之后， 就不会再继续往后查找是否还有匹配的权限信息， 而直接完成校验过程
7.访问授权策略
    #1.了解来访主机：
    #2.了解用户需求：
    #3.要用工作分类
    #4.确保只有绝对必要者拥有Grant Option权限
8.安全设置注意项
    #1.确认mysql是否需要联网，通过使用“ --skip-networking” 参数选项，让MySQL不通过TCP/IP监听网络请求，而仅仅通过命名管道或共享内存(在Windows中)或Unix套接字文件(在Unix中)来和客户端连接交互
    #2.通过使用“ --skip-networking” 参数选项，让MySQL不通过TCP/IP监听网络请求，而仅仅通过命名管道或共享内存(在Windows中)或Unix套接字文件(在Unix中)来和客户端连接交互
    #3.使用SSL加密通道。
    #4.访问授权限定来访主机信息。

    #5.OS安全方面：关闭MySQL Server主机上面任何不需要的服务，这不仅能从安全方面减少潜在隐患，还能减轻主机的部分负担，尽可能提高性能。
    #6.用非root用户运行MySQL
    #7.文件和进程安全。MySQL相关的数据和日志文件和所在的文件夹属主和所属组都设置为mysql，且禁用其他所有用户（除了拥有超级权限的用户，如root）的读写权限。以防止数据或者日志文件被窃取或破坏。
    #8.确保MySQL Server所在的主机上所必要运行的其他应用或者服务足够安全，避免因为其他应用或者服务存在安全漏洞而被入侵者攻破防线

    #9.用户设置：密码复杂
    #10.安全参数：不需要使用的功能模块尽量都不要启用
            如，如果不需要使用用户自定义函数，就不要在启动的时候使用“ --allow-suspicious-udfs” 参数选项，以防止被别有居心的潜在威胁者利用此功能而对MySQL的安全造成威胁；
            *不需要从本地文件中Load数据到数据库中，就使用“ --local-infile=0” 禁用掉可以从客户端机器上Load文件到数据库中；
            *使用新的密码规则和校验规则（不要使用“ --old-passwords”启动数据库） ，这项功能是为了兼容旧版本的密码校验方式的，如无额数必要，不要使用该功能，旧版本的密码加密方式要比新的方式在安全方面弱很多



> ## 0x04、存储管理器
1.权限及完整性管理器
2.事务管理器
    1)原子性
    2)一致性
    3)持久性
    4)
3.文件管理器
4.缓冲管理器
5.数据文件
6.数据字典
7.索引


> ## 0x05、查询处理器

- 1.DDL解释器
- 2.DML编译器
- 3.查询计算引擎
- 4.预处理


> ## 0x06、关系型数据库

- 1.数据库
- 2.表、元组、类型、主键、外键、码、关系、属性
- 3.范式
- 4.数据抽象：物理层、逻辑层、视图层
- 5.关系运算：选择、投影、并、差、笛卡儿积、交、自然连接、除
- 6.外连接：左外连接、右外连接


> ## 0x07、关键字(SQL)
create,delete,drop,select,insert,update,set
database,table,index,function,process,trigger
show,status,processlist
where,distinct,as,with,or,and,like,not like,between and,order by(DESE,ASE),group by,having
union,union all,except,except all,unique,check
in,not in
primary key,foreign key,not null,default,auto increment
grant,revoke


> ## 0x08、SQL语句
1.DDL和DML
2.创建操作
3.权限操作
    0)grant <权限列表> on <关系名或视图> to <用户或角色>
    1)revoke <权限列表> on <关系名或试图> from <用户或角色>
    1)grant all privileges on *.* to 'root'@'%' identify by "password";flush privileges;
2.DDL：
    create database\table\index\function\view\processor\trigger\user
    alter,drop
3.DML: select,update,delete,insert
4.between and:是包含两端的值
5.is null,is not null:不能用=或!=号
6.unknown:也是一种值，在参与运算时
7.嵌套子查询
    1)in,not in;=some等价于in,但!=some却不等价与not in;any;all
    2)exists;not exists
8.创建视图
    1)create view view_name as <查询表达式>
9.删除操作
    1)delete from r [where p]
10.插入操作
    1)insert into r[(row_name,...)] values()
11.更新操作
    1)update r set q where p
12.创建新类型
    create type Dollar as numberic(12,2) final
13.完整性约束
    1)not null,check,unique
14.参照完整性
    1)foreign key
15.where中用in比用or效率更快
16.在已知返回函数时，添加limit
17.在sql语句执行时，进行解析、优化、执行、结果几个步骤
18.在做更新是，用id来标记更新，否则会全表扫描
19.desc table_name  查看表结构



> ## 0x09、内置函数(聚集函数)：不能组合使用
max(),min(),count(),avg(),sum()
now(),curdate(),datetime(),timestamp(),curtime(),year()
concat(),




> ## 0x10、基本类型

- 1.int(-2,147,483,648--2,147,483,647,4字节),samllint(-32,768--32,767,2字节),tinyint(-128--127,1字节),unsigned,bigint(-9223372036854775808--9223372036854775807,8字节)
- 2.char,varchar
- 3.data,time,timestamp
- 4.double,float,numberic
- 5.tiny text,text,medium text,long text
- 6.blob,medium blob,long blob
- 7.enum,set


> ## 0x11、匹配

- %：匹配任意
- _：匹配任意一个字符


> ## 0x12、存储过程


> ## 0x13、索引

- 1.最适合索引的是在where之后的
- 2.使用唯一索引
- 3.使用短索引
- 4.利用最左前缀
- 5.不要过度索引



> ## 0x14、数据库设计问题

1.数据冗余与不一致
2.数据访问困难
3.数据孤立
4.并发访问异常·
5.安全性问题
    原则：
    1.完整性：完整性约束、参照完整性、断言、授权
    2.原子性
6.实体集、联系集、属性
7.区分实体集内实体的方法：主键
8.适度冗余---减少join使用（查询频繁，更新较少字段）
9.大字段垂直拆分---（summary表优化）：字段大，访问少
10.大表水平拆分---基于类型的分拆优化
11.优化数据类型
    #1.用更小的数据类型，减小存储空间和io资源
    #2.选择合适的数据库类型加速比较
12.规范的对象命名





> ## 0x15、数据库设计步骤

- 1.刻画未来数据库用户的需求：需求规格说明书
- 2.概念设计阶段：实体-联系模型图(确保数据需求都被满足，并且不互相冲突),重点是如何描述数据及其相互关系
- 3.功能需求规则说明书：确保设计模式满足功能需求
- 4.逻辑设计阶段
- 5.物理设计阶段


> ## 0x16、mysql存储引擎

1.Innodb:事务安全
2.Myisam：非事务安全



> ## 0x17、事务/锁

1.在同一个事务中，最好不使用不同存储引擎的表
2.DDL语句不能回滚
3.锁定机制直接影响数据库的并发处理能力和性能
    #1.三种锁：行级锁、页级锁和表级锁
    #2.行级锁：锁定粒度最小，支持并发量大，消耗资源多，容易发生死锁。有Innodb，，NDB Cluster存储引擎
    #3.页级锁：处于行级锁和表级锁之间。有BerkeleyDB存储引擎
    #4.表级锁：最大粒度锁，实现逻辑简单，负面影响小，获取和释放锁速度很快，极少死锁，并发量小。有Myisam，Memory，csv存储引擎
        1)分为读锁定和写锁定，通过四个队列来维护两种锁定：
                Current  read-lock queue
                Pending  read-lock queue
                Current  write-lock queue
                Pending  write-lock queue
        2)读锁定：满足下面条件后会立即通过，如果任何一个没有满足，都会被迫进入等待队列
                *1.请求锁定的资源当前没有被写锁定
                *2.写锁定等待队列（ Pending write-lock queue）中没有更高优先级的写锁定等待



> ## 0x18、备份/复制

1.逻辑备份
    #1.用mysqldump导出sql文件
    #2.生成特定分割文件
2.物理备份
    #1.备份物理数据文件，日志文件及配置文件等





> ## 0x19、优化建议
1.如果opened_tables太大,应该把my.cnf中的table_cache变大
2.如果Key_reads太大,则应该把my.cnf中key_buffer_size变大.可以用Key_reads/Key_read_requests计算出cache失败率
3.如果Handler_read_rnd太大,则你写的SQL语句里很多查询都是要扫描整个表,而没有发挥索引的键的作用
4.如果Threads_created太大,就要增加my.cnf中thread_cache_size的值.可以用Threads_created/Connections计算cache命中率
5.如果Created_tmp_disk_tables太大,就要增加my.cnf中tmp_table_size的值,用基于内存的临时表代替基于磁盘的


> ## 0x20、information_schema表
CHARACTER_SETS — 关于字符集信息
COLLATIONS — 关于每个字符集的（排序）规则信息
COLLATION_CHARACTER_SET_APPLICABILITY — 关于字符集和每种（排序）规则的对应关系信息
COLUMNS — 关于表中的列信息
COLUMN_PRIVILEGES — 关于MySQL对应账号所有列权限信息
ENGINES — 关于存储引擎的信息
EVENTS — 关于计划事件信息
FILES — 从7.8版本（未使用MySQL Cluster版本的情况下）开始，此表会显示关于InnoDB数据文件信息。早前的版本中此表都显示的是关于NDB数据文件的存储信息。
GLOBAL_STATUS — 关于服务端状态信息，7.6版本之后此表开始将被存放在PERFORMANCE_SCHEMA数据库中
GLOBAL_VARIABLES — 关于服务端全局变量信息，7.6版本之后此表开始将被存放在PERFORMANCE_SCHEMA数据库中
KEY_COLUMN_USAGE — 关于含有约束的键值列信息
OPTIMIZER_TRACE — 关于内部优化器执行语句的追踪信息，启用相应追踪功能需要启动设置optimizer_trace变量
PARAMETERS — 提供关于存储过程和功能函数所使用的参数及功能函数返回值信息
PLUGINS — 关于服务端插件信息
PROCESSLIST — 关于正在运行的线程信息
REFERENTIAL_CONSTRAINTS — 关于外键信息
ROUTINES — 关于存储过程和功能函数的相关信息
SCHEMATA — 关于数据库的信息
SCHEMA_PRIVILEGES — 关于MySQL用户账号所有的数据库权限
SESSION_STATUS — 关于当前连接的状态信息，7.6版本之后此表开始将被存放在PERFORMANCE_SCHEMA数据库中
SESSION_VARIABLES — 关于当前连接的会话变量信息，7.6版本之后此表开始将被存放在PERFORMANCE_SCHEMA数据库中
STATISTICS – 关于表索引的统计信息
TABLES — 关于数据库中表的信息
TABLESPACES — 提供了活动的表空间的信息，注意此表不提供关于InnoDB表空间的元数据信息，你需要去INNODB_SYS_TABLESPACES和INNODB_SYS_DATAFILES下查看，当然MySQL 5.7.8以后，FILES表也提供了InnoDB表空间相关的元数据信息。
TABLE_CONSTRAINTS — 关于表上的约束信息
TABLE_PRIVILEGES — 关于由MySQL用户账号所有的对应表权限信息
TRIGGERS — 关于数据库中触发器信息
USER_PRIVILEGES — 关于MySQL用户账号所有的全局性的权限信息
VIEWS — 关于数据库中视图信息
INNODB_XXXX表 — 这些表被用于监控正在进行的InnoDB活动，可以用于在出现问题前探测到这些低效的性能及承载问题。





> ## 0x21、配置参数:show variables;
auto_increment_increment:自增长键的步长
auto_increment_offset:自增长键的起始值
autocommit:
automatic_sp_privileges:
back_log:指定MySQL可能的连接数量。指出在MySQL暂时停止响应新请求之前的短时间内多少个请求可以被存在堆栈中。如果系统在一个短时间内有很多连接，则需要增大该参数的值，该参数值指定到来的TCP/IP连接的侦听队列的大小。不同的操作系统在这个队列大小上有它自己的限制。 试图设定back_log高于你的操作系统的限制将是无效的。
basedir:MySQL主程序所在路径，即：–basedir参数的值。
big_tables:
bind_address:
binlog_cache_size:
binlog_checksum, CRC32
binlog_direct_non_transactional_updates
binlog_format, STATEMENT
binlog_max_flush_queue_time
binlog_order_commits, ON
binlog_row_image, FULL
binlog_rows_query_log_events
binlog_stmt_cache_size, 32768
block_encryption_mode, aes-128-ecb
bulk_insert_buffer_size, 8388608
character_set_client, utf8
character_set_connection, utf8
character_set_database, utf8
character_set_filesystem, binary
character_set_results, utf8
character_set_server, latin1
character_set_system：指定系统字符类型 utf8
character_sets_dir:指定字符集路径，如： f:\wamp\bin\mysql\mysql5.6.17\share\charsets\
collation_connection, utf8_general_ci
collation_database, utf8_general_ci
collation_server, latin1_swedish_ci
completion_type, NO_CHAIN
concurrent_insert：如果开启该参数，MySQL则允许在执行 SELECT 操作的同时进行 INSERT 操作。如果要关闭该参数，可以在启动 mysqld 时加载 –safe 选项，或者使用 –skip-new 选项。默认为： AUTO
connect_timeout：指定MySQL服务等待应答一个连接报文的最大秒数，超出该时间，MySQL向客户端返回 bad handshake。默认为10
core_file
datadir：指定数据库路径。即为 –datadir 选项的值，如： f:\wamp\bin\mysql\mysql5.6.17\data\
date_format, %Y-%m-%d
datetime_format, %Y-%m-%d %H:%i:%s
default_storage_engine, InnoDB
default_tmp_storage_engine, InnoDB
default_week_format
delay_key_write：该参数只对 MyISAM 类型数据表有效。有如下的取值种类：
    off: 如果在建表语句中使用 CREATE TABLE … DELAYED_KEY_WRITES，则全部忽略DELAYED_KEY_WRITES;
    on: 如果在建表语句中使用 CREATE TABLE … DELAYED_KEY_WRITES，则使用该选项(默认);
    all: 所有打开的数据表都将按照 DELAYED_KEY_WRITES 处理。
    如果 DELAYED_KEY_WRITES 开启，对于已经打开的数据表而言，在每次索引更新时都不刷新带有
    DELAYED_KEY_WRITES 选项的数据表的key buffer，除非该数据表关闭。该参数会大幅提升写入键值的速
    度。如果使用该参数，则应该检查所有数据表：myisamchk –fast –force 。默认为ON
delayed_insert_limit：在插入delayed_insert_limit行后，INSERT DELAYED处理模块将检查是否有未执行的SELECT语句。如果有，在继续处理前执行允许这些语句。默认为 100
delayed_insert_timeout：一个INSERT DELAYED线程应该在终止之前等待INSERT语句的时间。默认为300
delayed_queue_size：为处理INSERT DELAYED分配的队列大小(以行为单位)。如果排队满了，任何进行INSERT DELAYED的客户必须等待队列空间释放后才能继续。默认为1000
disconnect_on_expired_password, ON
div_precision_increment, 4
end_markers_in_json
enforce_gtid_consistency
eq_range_index_dive_limit, 10
error_count
event_scheduler
expire_logs_days
explicit_defaults_for_timestamp, ON
external_user,
flush：在启动MySQL时加载 –flush 参数打开该功能。默认为 OFF
flush_time：如果该设置为非0值，那么每flush_time秒，所有打开的表将被关，以释放资源和sync到磁盘。注意：只建议在使用 Windows9x/Me 或者当前操作系统资源严重不足时才使用该参数!默认为 0
foreign_key_checks， ON
ft_boolean_syntax：搜索引擎维护员希望更改允许用于逻辑全文搜索的操作符。这些则由变量 ft_boolean_syntax 控制。默认为 + -><()~*:""&|
ft_max_word_len：指定被索引的关键词的最大长度。注意：在更改该参数值后，索引必须重建! 默认为84
ft_min_word_len：指定被索引的关键词的最小长度。注意：在更改该参数值后，索引必须重建! 默认为4
ft_query_expansion_limit, 20
ft_stopword_file：从 ft_stopword_file 变量指定的文件中读取列表。在修改了 stopword 列表后，必须重建 FULLTEXT 索引。默认为 (built-in)
general_log
general_log_file, f:\wamp\bin\mysql\mysql5.6.17\data\zxc-PC.log
group_concat_max_len, 1024
gtid_executed,
gtid_mode
gtid_next, AUTOMATIC
gtid_owned,
gtid_purged,
have_compress, YES
have_crypt, NO
have_dynamic_loading, YES
have_geometry, YES
have_openssl：YES， 使MySQL支持SSL加密协议。 DISABLED，则不支持
have_profiling, YES
have_query_cache, YES
have_rtree_keys, YES
have_ssl, DISABLED
have_symlink, YES
host_cache_size, 279
hostname, zxc-PC
identity
ignore_builtin_innodb
ignore_db_dirs,
init_connect,
init_file：指定一个包含SQL查询语句的文件，该文件在MySQL启动时将被加载，文件中的SQL语句也会被执行。
init_slave,
innodb_adaptive_flushing, ON
innodb_adaptive_flushing_lwm, 10
innodb_adaptive_hash_index, ON
innodb_adaptive_max_sleep_delay, 150000
innodb_additional_mem_pool_size, 8388608
innodb_api_bk_commit_interval, 5
innodb_api_disable_rowlock
innodb_api_enable_binlog
innodb_api_enable_mdl
innodb_api_trx_level
innodb_autoextend_increment, 64
innodb_autoinc_lock_mode, 1
innodb_buffer_pool_dump_at_shutdown
innodb_buffer_pool_dump_now
innodb_buffer_pool_filename, ib_buffer_pool
innodb_buffer_pool_instances, 8
innodb_buffer_pool_load_abort
innodb_buffer_pool_load_at_startup
innodb_buffer_pool_load_now
innodb_buffer_pool_size, 134217728
innodb_change_buffer_max_size, 25
innodb_change_buffering, all
innodb_checksum_algorithm, innodb
innodb_checksums, ON
innodb_cmp_per_index_enabled
innodb_commit_concurrency
innodb_compression_failure_threshold_pct, 5
innodb_compression_level, 6
innodb_compression_pad_pct_max, 50
innodb_concurrency_tickets, 5000
innodb_data_file_path, ibdata1:12M:autoextend
innodb_data_home_dir,
innodb_disable_sort_file_cache
innodb_doublewrite, ON
innodb_fast_shutdown, 1
innodb_file_format, Antelope
innodb_file_format_check, ON
innodb_file_format_max, Antelope
innodb_file_per_table, ON
innodb_flush_log_at_timeout, 1
innodb_flush_log_at_trx_commit, 1
innodb_flush_method,
innodb_flush_neighbors, 1
innodb_flushing_avg_loops, 30
innodb_force_load_corrupted
innodb_force_recovery
innodb_ft_aux_table,
innodb_ft_cache_size, 8000000
innodb_ft_enable_diag_print
innodb_ft_enable_stopword, ON
innodb_ft_max_token_size, 84
innodb_ft_min_token_size, 3
innodb_ft_num_word_optimize, 2000
innodb_ft_result_cache_limit, 2000000000
innodb_ft_server_stopword_table,
innodb_ft_sort_pll_degree, 2
innodb_ft_total_cache_size, 640000000
innodb_ft_user_stopword_table,
innodb_io_capacity, 200
innodb_io_capacity_max, 2000
innodb_large_prefix
innodb_lock_wait_timeout, 50
innodb_locks_unsafe_for_binlog
innodb_log_buffer_size, 8388608
innodb_log_compressed_pages, ON
innodb_log_file_size, 50331648
innodb_log_files_in_group, 2
innodb_log_group_home_dir, .\
innodb_lru_scan_depth, 1024
innodb_max_dirty_pages_pct, 75
innodb_max_dirty_pages_pct_lwm
innodb_max_purge_lag
innodb_max_purge_lag_delay
innodb_mirrored_log_groups, 1
innodb_monitor_disable,
innodb_monitor_enable,
innodb_monitor_reset,
innodb_monitor_reset_all,
innodb_old_blocks_pct, 37
innodb_old_blocks_time, 1000
innodb_online_alter_log_max_size, 134217728
innodb_open_files, 2000
innodb_optimize_fulltext_only
innodb_page_size, 16384
innodb_print_all_deadlocks
innodb_purge_batch_size, 300
innodb_purge_threads, 1
innodb_random_read_ahead
innodb_read_ahead_threshold, 56
innodb_read_io_threads, 4
innodb_read_only
innodb_replication_delay
innodb_rollback_on_timeout
innodb_rollback_segments, 128
innodb_sort_buffer_size, 1048576
innodb_spin_wait_delay, 6
innodb_stats_auto_recalc, ON
innodb_stats_method, nulls_equal
innodb_stats_on_metadata
innodb_stats_persistent, ON
innodb_stats_persistent_sample_pages, 20
innodb_stats_sample_pages, 8
innodb_stats_transient_sample_pages, 8
innodb_status_output
innodb_status_output_locks
innodb_strict_mode
innodb_support_xa, ON
innodb_sync_array_size, 1
innodb_sync_spin_loops, 30
innodb_table_locks, ON
innodb_thread_concurrency
innodb_thread_sleep_delay, 10000
innodb_undo_directory, .
innodb_undo_logs, 128
innodb_undo_tablespaces
innodb_use_native_aio, ON
innodb_use_sys_malloc, ON
innodb_version, 5.6.17
innodb_write_io_threads, 4
insert_id
interactive_timeout：服务器在关上它前在一个交互连接上等待行动的秒数。一个交互的客户被定义为对mysql_real_connect()使用CLIENT_INTERACTIVE选项的客户。也可见wait_timeout。默认为 28800
join_buffer_size：用于全部联合(join)的缓冲区大小(不是用索引的联结)。缓冲区对2个表间的每个全部联结分配一次缓冲区，当增加索引不可能时，增加该值可得到一个更快的全部联结。(通常得到快速联结的最佳方法是增加索引。)默认为 262144
keep_files_on_create
key_buffer_size：用于索引块的缓冲区大小，增加它可得到更好处理的索引(对所有读和多重写)，到你能负担得起那样多。如果你使它太大，系统将开始变慢慢。必须为OS文件系统缓存留下一些空间。为了在写入多个行时得到更多的速度。默认为 8388608
key_cache_age_threshold, 300
key_cache_block_size, 1024
key_cache_division_limit, 100
large_files_support：开启大文件支持。默认为 ON
large_page_size
large_pages
last_insert_id
lc_messages, en_US
lc_messages_dir, f:\wamp\bin\mysql\mysql5.6.17\share\
lc_time_names, en_US
license, GPL
local_infile, ON
lock_wait_timeout, 31536000
log_bin：开启 binary log。默认为 OFF
log_bin_basename,
log_bin_index,
log_bin_trust_function_creators
log_bin_use_v1_row_events
log_error, f:\wamp\bin\mysql\mysql5.6.17\data\zxc-PC.err
log_output, FILE
log_queries_not_using_indexes
log_slave_updates：如果使用链状同步或者多台Slave之间进行同步则需要开启此参数。默认为 OFF
log_slow_admin_statements
log_slow_slave_statements
log_throttle_queries_not_using_indexes
log_warnings, 1
long_query_time：如果一个查询所用时间超过该参数值，则该查询操作将被记录在Slow_queries中。默认为 10.000000
low_priority_updates
lower_case_file_system, ON
lower_case_table_names：1: MySQL总使用小写字母进行SQL操作;0: 关闭该功能。默认为 1
master_info_repository, FILE
master_verify_checksum
max_allowed_packet：一个查询语句包的最大尺寸。消息缓冲区被初始化为net_buffer_length字节，但是可在需要时增加到max_allowed_packet个字节。该值太小则会在处理大包时产生错误。如果使用大的BLOB列，必须增加该值。默认为 4194304
max_binlog_cache_size：指定binary log缓存的最大容量，如果设置的过小，则在执行复杂查询语句时MySQL会出错。默认为 18446744073709547520
max_binlog_size：指定binary log文件的最大容量。默认为 1073741824
max_binlog_stmt_cache_size, 18446744073709547520
max_connect_errors：对于同一主机，如果有超出该参数值个数的中断错误连接，则该主机将被禁止连接。如需对该主机进行解禁，执行：FLUSH HOST。默认为 100
max_connections：允许同时连接MySQL服务器的客户数量。如果超出该值，MySQL会返回Too many connections错误，但通常情况下，MySQL能够自行解决。默认为 151
max_delayed_threads：不要启动多于的这个数字的线程来处理INSERT DELAYED语句。如果你试图在所有INSERT DELAYED线程在用后向一张新表插入数据，行将被插入，就像DELAYED属性没被指定那样。默认为 20
max_error_count, 64
max_heap_table_size：内存表所能使用的最大容量。默认为 16777216
max_insert_delayed_threads, 20
max_join_size：如果要查询多于max_join_size个记录的联合将返回一个错误。如果要执行没有一个WHERE的语句并且耗费大量时间，且返回上百万行的联结，则需要加大该参数值。默认为 18446744073709551615
max_length_for_sort_data, 1024
max_prepared_stmt_count, 16382
max_relay_log_size
max_seeks_for_key, 4294967295
max_sort_length：在排序BLOB或TEXT值时使用的字节数(每个值仅头max_sort_length个字节被使用;其余的被忽略)。默认为 1024
max_sp_recursion_depth
max_tmp_tables：(该参数目前还没有作用)。一个客户能同时保持打开的临时表的最大数量。默认为 32
max_user_connections：指定来自同一用户的最多连接数。设置为0则代表不限制。默认为 0
max_write_lock_count：当出现max_write_lock_count个写入锁定数量后，开始允许一些被锁定的读操作开始执行。避免写入锁定过多，读取操作处于长时间等待状态。默认为 4294967295
metadata_locks_cache_size, 1024
metadata_locks_hash_instances, 8
min_examined_row_limit
multi_range_count, 256
myisam_data_pointer_size, 6
myisam_max_sort_file_size, 2146435072
myisam_mmap_size, 18446744073709551615
myisam_recover_options
myisam_repair_threads, 1
myisam_sort_buffer_size, 8388608
myisam_stats_method, nulls_unequal
myisam_use_mmap
named_pipe
net_buffer_length, 16384
net_read_timeout, 30
net_retry_count, 10
net_write_timeout, 60
new
old
old_alter_table
old_passwords
open_files_limit, 7048
optimizer_prune_level, 1
optimizer_search_depth, 62
optimizer_switch, index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,subquery_materialization_cost_based=on,use_index_extensions=on
optimizer_trace, enabled=off,one_line=off
optimizer_trace_features, greedy_search=on,range_optimizer=on,dynamic_range=on,repeated_subselect=on
optimizer_trace_limit, 1
optimizer_trace_max_mem_size, 16384
optimizer_trace_offset, -1
performance_schema, ON
performance_schema_accounts_size, 100
performance_schema_digests_size, 10000
performance_schema_events_stages_history_long_size, 10000
performance_schema_events_stages_history_size, 10
performance_schema_events_statements_history_long_size, 10000
performance_schema_events_statements_history_size, 10
performance_schema_events_waits_history_long_size, 10000
performance_schema_events_waits_history_size, 10
performance_schema_hosts_size, 100
performance_schema_max_cond_classes, 80
performance_schema_max_cond_instances, 3504
performance_schema_max_file_classes, 50
performance_schema_max_file_handles, 32768
performance_schema_max_file_instances, 7693
performance_schema_max_mutex_classes, 200
performance_schema_max_mutex_instances, 15906
performance_schema_max_rwlock_classes, 40
performance_schema_max_rwlock_instances, 9102
performance_schema_max_socket_classes, 10
performance_schema_max_socket_instances, 322
performance_schema_max_stage_classes, 150
performance_schema_max_statement_classes, 168
performance_schema_max_table_handles, 4000
performance_schema_max_table_instances, 12500
performance_schema_max_thread_classes, 50
performance_schema_max_thread_instances, 402
performance_schema_session_connect_attrs_size, 512
performance_schema_setup_actors_size, 100
performance_schema_setup_objects_size, 100
performance_schema_users_size, 100
pid_file, f:\wamp\bin\mysql\mysql5.6.17\data\zxc-PC.pid
plugin_dir, f:\wamp\bin\mysql\mysql5.6.17\lib\plugin\
port, 3306
preload_buffer_size, 32768
profiling
profiling_history_size, 15
protocol_version, 10
proxy_user,
pseudo_slave_mode
pseudo_thread_id, 2
query_alloc_block_size, 8192
query_cache_limit, 1048576
query_cache_min_res_unit, 4096
query_cache_size, 1048576
query_cache_type
query_cache_wlock_invalidate
query_prealloc_size, 8192
rand_seed1
rand_seed2
range_alloc_block_size, 4096
read_buffer_size, 131072
read_only
read_rnd_buffer_size, 262144
relay_log,
relay_log_basename,
relay_log_index,
relay_log_info_file, relay-log.info
relay_log_info_repository, FILE
relay_log_purge, ON
relay_log_recovery
relay_log_space_limit
report_host,
report_password,
report_port, 3306
report_user,
rpl_stop_slave_timeout, 31536000
secure_auth, ON
secure_file_priv,
server_id
server_id_bits, 32
server_uuid, 5c0971e1-3985-11e5-849c-dc0ea17af70f
shared_memory
shared_memory_base_name, MYSQL
skip_external_locking, ON
skip_name_resolve
skip_networking
skip_show_database
slave_allow_batching
slave_checkpoint_group, 512
slave_checkpoint_period, 300
slave_compressed_protocol
slave_exec_mode, STRICT
slave_load_tmpdir, C:\WINDOWS\TEMP
slave_max_allowed_packet, 1073741824
slave_net_timeout, 3600
slave_parallel_workers
slave_pending_jobs_size_max, 16777216
slave_rows_search_algorithms, TABLE_SCAN,INDEX_SCAN
slave_skip_errors
slave_sql_verify_checksum, ON
slave_transaction_retries, 10
slave_type_conversions,
slow_launch_time, 2
slow_query_log
slow_query_log_file, f:\wamp\bin\mysql\mysql5.6.17\data\zxc-PC-slow.log
socket, MySQL
sort_buffer_size, 262144
sql_auto_is_null
sql_big_selects, ON
sql_buffer_result
sql_log_bin, ON
sql_log_off
sql_mode, NO_ENGINE_SUBSTITUTION
sql_notes, ON
sql_quote_show_create, ON
sql_safe_updates, ON
sql_select_limit, 18446744073709551615
sql_slave_skip_counter
sql_warnings
ssl_ca,
ssl_capath,
ssl_cert,
ssl_cipher,
ssl_crl,
ssl_crlpath,
ssl_key,
storage_engine, InnoDB
stored_program_cache, 256
sync_binlog
sync_frm, ON
sync_master_info, 10000
sync_relay_log, 10000
sync_relay_log_info, 10000
system_time_zone,
table_definition_cache, 1400
table_open_cache, 2000
table_open_cache_instances, 1
thread_cache_size, 9
thread_concurrency, 10
thread_handling, one-thread-per-connection
thread_stack, 262144
time_format, %H:%i:%s
time_zone, SYSTEM
timed_mutexes
timestamp, 1449802723.239825
tmp_table_size, 16777216
tmpdir, C:\WINDOWS\TEMP
transaction_alloc_block_size, 8192
transaction_allow_batching
transaction_prealloc_size, 4096
tx_isolation, REPEATABLE-READ
tx_read_only
unique_checks, ON
updatable_views_with_limit, YES
version, 5.6.17
version_comment, MySQL Community Server (GPL)
version_compile_machine, x86_64
version_compile_os, Win64
wait_timeout, 28800
warning_count, 1




> ## 0x22、性能指标:show status;
  Aborted_clients：由于客户端没有正确关闭连接导致客户端终止而中断的连接数。global
  Aborted_connects:试图连接到MySQL服务器而失败的连接数。global
  Binlog_cache_disk_use:使用临时二进制日志缓存但超过binlog_cache_size值并使用临时文件来保存事务中的语句的事务数量.global
  Binlog_cache_use:使用临时二进制日志缓存的事务数量.global
  Binlog_stmt_cache_disk_use:
  Binlog_stmt_cache_use:
  Bytes_received:从所有客户端接收到的字节数。both
  Bytes_sent:发送给所有客户端的字节数。both
  Com_admin_commands:
  Com_alter_db:
  Com_alter_db_upgrade:
  Com_alter_event:
  Com_alter_function:
  Com_alter_procedure
  Com_alter_server
  Com_alter_table
  Com_alter_tablespace
  Com_alter_user
  Com_analyze
  Com_assign_to_keycache
  Com_begin
  Com_binlog
  Com_call_procedure
  Com_change_db, 1
  Com_change_master
  Com_check
  Com_checksum
  Com_commit
  Com_create_db
  Com_create_event
  Com_create_function
  Com_create_index
  Com_create_procedure
  Com_create_server
  Com_create_table
  Com_create_trigger
  Com_create_udf
  Com_create_user
  Com_create_view
  Com_dealloc_sql
  Com_delete
  Com_delete_multi
  Com_do
  Com_drop_db
  Com_drop_event
  Com_drop_function
  Com_drop_index
  Com_drop_procedure
  Com_drop_server
  Com_drop_table
  Com_drop_trigger
  Com_drop_user
  Com_drop_view
  Com_empty_query
  Com_execute_sql
  Com_flush
  Com_get_diagnostics
  Com_grant
  Com_ha_close
  Com_ha_open
  Com_ha_read
  Com_help
  Com_insert
  Com_insert_select
  Com_install_plugin
  Com_kill
  Com_load
  Com_lock_tables
  Com_optimize
  Com_preload_keys
  Com_prepare_sql
  Com_purge
  Com_purge_before_date
  Com_release_savepoint
  Com_rename_table
  Com_rename_user
  Com_repair
  Com_replace
  Com_replace_select
  Com_reset
  Com_resignal
  Com_revoke
  Com_revoke_all
  Com_rollback
  Com_rollback_to_savepoint
  Com_savepoint
  Com_select, 3
  Com_set_option, 6
  Com_show_binlog_events
  Com_show_binlogs
  Com_show_charsets
  Com_show_collations
  Com_show_create_db
  Com_show_create_event
  Com_show_create_func
  Com_show_create_proc
  Com_show_create_table
  Com_show_create_trigger
  Com_show_databases
  Com_show_engine_logs
  Com_show_engine_mutex
  Com_show_engine_status
  Com_show_errors
  Com_show_events
  Com_show_fields
  Com_show_function_code
  Com_show_function_status
  Com_show_grants
  Com_show_keys
  Com_show_master_status
  Com_show_open_tables
  Com_show_plugins
  Com_show_privileges
  Com_show_procedure_code
  Com_show_procedure_status
  Com_show_processlist
  Com_show_profile
  Com_show_profiles
  Com_show_relaylog_events
  Com_show_slave_hosts
  Com_show_slave_status
  Com_show_status, 2
  Com_show_storage_engines
  Com_show_table_status
  Com_show_tables
  Com_show_triggers
  Com_show_variables, 6
  Com_show_warnings
  Com_signal
  Com_slave_start
  Com_slave_stop
  Com_stmt_close
  Com_stmt_execute
  Com_stmt_fetch
  Com_stmt_prepare
  Com_stmt_reprepare
  Com_stmt_reset
  Com_stmt_send_long_data
  Com_truncate
  Com_uninstall_plugin
  Com_unlock_tables
  Com_update
  Com_update_multi
  Com_xa_commit
  Com_xa_end
  Com_xa_prepare
  Com_xa_recover
  Com_xa_rollback
  Com_xa_start
  Compression
  Connection_errors_accept
  Connection_errors_internal
  Connection_errors_max_connections
  Connection_errors_peer_address
  Connection_errors_select
  Connection_errors_tcpwrap
  Connections:试图连接到(不管是否成功)MySQL服务器的连接数.global
  Created_tmp_disk_tables:服务器执行语句时在硬盘上自动创建的临时表的数量.both
  Created_tmp_files:mysqld已经创建的临时文件的数量.global
  Created_tmp_tables:服务器执行语句时自动创建的内存中的临时表的数量。如果Created_tmp_disk_tables较大，你可能要增加tmp_table_size值使临时 表基于内存而不基于硬盘.both
  Delayed_errors:用INSERT DELAYED写的出现错误的行数(可能为duplicate key)。global
  Delayed_insert_threads:使用的INSERT DELAYED处理器线程数.global
  Delayed_writes:写入的INSERT DELAYED行数.global
  Flush_commands:执行的FLUSH语句数.global
  Handler_commit:内部提交语句数.both
  Handler_delete:行从表中删除的次数.both
  Handler_discover:MySQL服务器可以问NDB CLUSTER存储引擎是否知道某一名字的表。这被称作发现。Handler_discover说明通过该方法发现的次数。both
  Handler_external_lock:
  Handler_mrr_init:
  Handler_prepare:A counter for the prepare phase of two-phase commit operations.both
  Handler_read_first:索引中第一条被读的次数。如果较高，它建议服务器正执行大量全索引扫描；例如，SELECT col1 FROM foo，假定col1有索引。both
  Handler_read_key:根据键读一行的请求数。如果较高，说明查询和表的索引正确。both
  Handler_read_last:
  Handler_read_next:按照键顺序读下一行的请求数。如果你用范围约束或如果执行索引扫描来查询索引列，该值增加.both
  Handler_read_prev:按照键顺序读前一行的请求数。该读方法主要用于优化ORDER BY … DESC.both
  Handler_read_rnd:根据固定位置读一行的请求数。如果你正执行大量查询并需要对结果进行排序该值较高。你可能使用了大量需要MySQL扫描整个表的查询或你的连接没有正确使用键.both
  Handler_read_rnd_next:在数据文件中读下一行的请求数。如果你正进行大量的表扫描，该值较高。通常说明你的表索引不正确或写入的查询没有利用索引。both
  Handler_rollback:内部ROLLBACK语句的数量.both
  Handler_savepoint:在一个存储引擎放置一个保存点的请求数量。both
  Handler_savepoint_rollback:在一个存储引擎的要求回滚到一个保存点数目。both
  Handler_update:在表内更新一行的请求数。both
  Handler_write:在表内插入一行的请求数。both
  Innodb_available_undo_logs:
  Innodb_buffer_pool_bytes_data:
  Innodb_buffer_pool_bytes_dirty
  Innodb_buffer_pool_dump_status, not started
  Innodb_buffer_pool_load_status, not started
  Innodb_buffer_pool_pages_data:包含数据的页数(脏或干净)。global
  Innodb_buffer_pool_pages_dirty:当前的脏页数。global
  Innodb_buffer_pool_pages_flushed:要求清空的缓冲池页数.global
  Innodb_buffer_pool_pages_free:空页数。global
  Innodb_buffer_pool_pages_misc:忙的页数，因为它们已经被分配优先用作管理，例如行锁定或适用的哈希索引。该值还可以计算为Innodb_buffer_pool_pages_total – Innodb_buffer_pool_pages_free – Innodb_buffer_pool_pages_data。global
  Innodb_buffer_pool_pages_total:缓冲池总大小（页数）。global
  Innodb_buffer_pool_read_ahead:
  Innodb_buffer_pool_read_ahead_evicted
  Innodb_buffer_pool_read_ahead_rnd:InnoDB初始化的“随机”read-aheads数。当查询以随机顺序扫描表的一大部分时发生。global
  Innodb_buffer_pool_read_requests:InnoDB已经完成的逻辑读请求数。global
  Innodb_buffer_pool_reads:不能满足InnoDB必须单页读取的缓冲池中的逻辑读数量。global
  Innodb_buffer_pool_wait_free:一般情况，通过后台向InnoDB缓冲池写。但是，如果需要读或创建页，并且没有干净的页可用，则它还需要先等待页面清空。该计数器对等待实例进行记数。如果已经适当设置缓冲池大小，该值应小。global
  Innodb_buffer_pool_write_requests:向InnoDB缓冲池的写数量。global
  Innodb_data_fsyncs:fsync()操作数。global
  Innodb_data_pending_fsyncs:当前挂起的fsync()操作数。global
  Innodb_data_pending_reads:当前挂起的读数。global
  Innodb_data_pending_writes:当前挂起的写数。global
  Innodb_data_read:	至此已经读取的数据数量（字节）。global
  Innodb_data_reads:数据读总数量。global
  Innodb_data_writes:数据读写数量。global
  Innodb_data_written:至此已经写入的数据量（字节）。global
  Innodb_dblwr_pages_written:已经执行的双写操作数量.global
  Innodb_dblwr_writes:双写操作已经写好的页数.global
  Innodb_have_atomic_builtins:
  Innodb_log_waits
  Innodb_log_write_requests:日志写请求数。global
  Innodb_log_writes:向日志文件的物理写数量。global
  Innodb_num_open_files:
  Innodb_os_log_fsyncs:向日志文件完成的fsync()写数量。global
  Innodb_os_log_pending_fsyncs:挂起的日志文件fsync()操作数量。global
  Innodb_os_log_pending_writes:挂起的日志文件写操作.global
  Innodb_os_log_written:写入日志文件的字节数。global
  Innodb_page_size:编译的InnoDB页大小(默认16KB)。许多值用页来记数；页的大小很容易转换为字节。global
  Innodb_pages_created:创建的页数。global
  Innodb_pages_read:读取的页数。global
  Innodb_pages_written:写入的页数。global
  Innodb_row_lock_current_waits:当前等待的待锁定的行数。global
  Innodb_row_lock_time:行锁定花费的总时间，单位毫秒。global
  Innodb_row_lock_time_avg:	行锁定的平均时间，单位毫秒。global
  Innodb_row_lock_time_max:行锁定的最长时间，单位毫秒。global
  Innodb_row_lock_waits:一行锁定必须等待的时间数。global
  Innodb_rows_deleted:从InnoDB表删除的行数。global
  Innodb_rows_inserted:插入到InnoDB表的行数。global
  Innodb_rows_read:	从InnoDB表读取的行数。global
  Innodb_rows_updated:	InnoDB表内更新的行数。global
  Innodb_truncated_status_writes:
  Key_blocks_not_flushed:键缓存内已经更改但还没有清空到硬盘上的键的数据块数量。global
  Key_blocks_unused:键缓存内未使用的块数量。你可以使用该值来确定使用了多少键缓存.global
  Key_blocks_used:键缓存内使用的块数量。该值为高水平线标记，说明已经同时最多使用了多少块。global
  Key_read_requests:从缓存读键的数据块的请求数。global
  Key_reads:从硬盘读取键的数据块的次数。如果Key_reads较大，则Key_buffer_size值可能太小。可以用Key_reads/Key_read_requests计算缓存损失率。global
  Key_write_requests:将键的数据块写入缓存的请求数。global
  Key_writes:向硬盘写入将键的数据块的物理写操作的次数。global
  Last_query_cost:用查询优化器计算的最后编译的查询的总成本。用于对比同一查询的不同查询方案的成本。默认值0表示还没有编译查询。 默认值是0。Last_query_cost具有会话范围。global
  Last_query_partial_plans:
  Max_used_connections:服务器启动后已经同时使用的连接的最大数量。global
  Not_flushed_delayed_rows
  Open_files:打开的文件的数目。global
  Open_streams:打开的流的数量(主要用于记录)。global
  Open_table_definitions:缓存的.frm文件数量.global
  Open_tables:当前打开的表的数量。both
  Opened_files:文件打开的数量。不包括诸如套接字或管道其他类型的文件。 也不包括存储引擎用来做自己的内部功能的文件。global
  Opened_table_definitions:已经缓存的.frm文件数量.both
  Opened_tables:已经打开的表的数量。如果Opened_tables较大，table_cache 值可能太小。both
  Performance_schema_accounts_lost:
  Performance_schema_cond_classes_lost:
  Performance_schema_cond_instances_lost:
  Performance_schema_digest_lost:
  Performance_schema_file_classes_lost:
  Performance_schema_file_handles_lost:
  Performance_schema_file_instances_lost:
  Performance_schema_hosts_lost:
  Performance_schema_locker_lost:
  Performance_schema_mutex_classes_lost:
  Performance_schema_mutex_instances_lost:
  Performance_schema_rwlock_classes_lost:
  Performance_schema_rwlock_instances_lost:
  Performance_schema_session_connect_attrs_lost:
  Performance_schema_socket_classes_lost:
  Performance_schema_socket_instances_lost:
  Performance_schema_stage_classes_lost:
  Performance_schema_statement_classes_lost:
  Performance_schema_table_handles_lost:
  Performance_schema_table_instances_lost:
  Performance_schema_thread_classes_lost:
  Performance_schema_thread_instances_lost:
  Performance_schema_users_lost:
  Prepared_stmt_count:当前的预处理语句的数量。 (最大数为系统变量: max_prepared_stmt_count).global
  Qcache_free_blocks:查询缓存内自由内存块的数量。global
  Qcache_free_memory:用于查询缓存的自由内存的数量。global
  Qcache_hits:查询缓存被访问的次数。global
  Qcache_inserts:加入到缓存的查询数量。global
  Qcache_lowmem_prunes:由于内存较少从缓存删除的查询数量。global
  Qcache_not_cached:非缓存查询数(不可缓存，或由于query_cache_type设定值未缓存)。global
  Qcache_queries_in_cache:登记到缓存内的查询的数量.global
  Qcache_total_blocks:查询缓存内的总块数。global
  Queries:服务器执行的请求个数，包含存储过程中的请求。global
  Questions:已经发送给服务器的查询的个数。global
  Select_full_join:没有使用索引的联接的数量。如果该值不为0,你应仔细检查表的索引.both
  Select_full_range_join:在引用的表中使用范围搜索的联接的数量。both
  Select_range:在第一个表中使用范围的联接的数量。一般情况不是关键问题，即使该值相当大。both
  Select_range_check:在每一行数据后对键值进行检查的不带键值的联接的数量。如果不为0，你应仔细检查表的索引。both
  Select_scan:对第一个表进行完全扫描的联接的数量。both
  Slave_heartbeat_period:复制的心跳间隔.global
  Slave_last_heartbeat:
  Slave_open_temp_tables:从服务器打开的临时表数量.global
  Slave_received_heartbeats:从服务器心跳数.global
  Slave_retried_transactions:本次启动以来从服务器复制线程重试次数.global
  Slave_running:如果该服务器是连接到主服务器的从服务器，则该值为ON。global
  Slow_launch_threads:创建时间超过slow_launch_time秒的线程数。both
  Slow_queries:查询时间超过long_query_time秒的查询的个数。both
  Sort_merge_passes:排序算法已经执行的合并的数量。如果这个变量值较大，应考虑增加sort_buffer_size系统变量的值。both
  Sort_range:在范围内执行的排序的数量.both
  Sort_rows:已经排序的行数。both
  Sort_scan:通过扫描表完成的排序的数量。both
  Ssl_accept_renegotiates:
  Ssl_accepts
  Ssl_callback_cache_hits
  Ssl_cipher
  Ssl_cipher_list
  Ssl_client_connects
  Ssl_connect_renegotiates
  Ssl_ctx_verify_depth
  Ssl_ctx_verify_mode
  Ssl_default_timeout
  Ssl_finished_accepts
  Ssl_finished_connects
  Ssl_server_not_after
  Ssl_server_not_before
  Ssl_session_cache_hits
  Ssl_session_cache_misses
  Ssl_session_cache_mode NONE
  Ssl_session_cache_overflows
  Ssl_session_cache_size
  Ssl_session_cache_timeouts
  Ssl_sessions_reused
  Ssl_used_session_cache_entries
  Ssl_verify_depth
  Ssl_verify_mode
  Ssl_version,
  Table_locks_immediate:立即获得的表的锁的次数。global
  Table_locks_waited:不能立即获得的表的锁的次数。如果该值较高，并且有性能问题，你应首先优化查询，然后拆分表或使用复制。global
  Table_open_cache_hits:
  Table_open_cache_misses
  Table_open_cache_overflows
  Tc_log_max_pages_used
  Tc_log_page_size
  Tc_log_page_waits
  Threads_cached:线程缓存内的线程的数量。global
  Threads_connected:当前打开的连接的数量。global
  Threads_created:创建用来处理连接的线程数。如果Threads_created较大，你可能要增加thread_cache_size值。缓存访问率的计算方法Threads_created/Connections。global
  Threads_running:激活的（非睡眠状态）线程数。global
  Uptime:服务器已经运行的时间（以秒为单位）。global
  Uptime_since_flush_status:最近一次使用FLUSH STATUS 的时间（以秒为单位）。global
