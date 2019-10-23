* Hive 原理
    * 1. 用户提交查询等任务给Driver。
    * 2. 编译器获得该用户的任务Plan。
    * 3. 编译器Compiler根据用户任务去MetaStore中获取需要的Hive的元数据信息。
    * 4. 编译器Compiler得到元数据信息，对任务进行编译，先将HiveQL转换为抽象语法树，然后将抽象语法树转换成查询块，将查询块转化为逻辑的查询计划，重写逻辑查询计划，将逻辑计划转化为物理的计划（MapReduce）, 最后选择最佳的策略。
    * 5. 将最终的计划提交给Driver。
    * 6. Driver将计划Plan转交给ExecutionEngine去执行，获取元数据信息，提交给JobTracker或者SourceManager执行该任务，任务会直接读取HDFS中文件进行相应的操作。
    * 7. 获取执行的结果。
    * 8. 取得并返回执行结果。
* Hive数据倾斜问题
    * 1.1)key分布不均匀
    * 1.2)业务数据本身的
    * 1.3)SQL语句造成数据倾斜
    * 1>参数调节：
        * hive.map.aggr=true
        * hive.groupby.skewindata=true
    * 2>SQL语句调节：
        * 1)选用join key 分布最均匀的表作为驱动表。做好列裁剪和filter操作，以达到两表join的时候，数据量相对变小的效果。
        * 2)大小表Join： 使用map join让小的维度表（1000条以下的记录条数）先进内存。在Map端完成Reduce。
        * 3)大表Join大表：把空值的Key变成一个字符串加上一个随机数，把倾斜的数据分到不同的reduce上，由于null值关联不上，处理后并不影响最终的结果。
        * 4)count distinct大量相同特殊值：count distinct时，将值为空的情况单独处理，如果是计算count distinct，可以不用处理，直接过滤，在做后结果中加1。如果还有其他计算，需要进行group by，可以先将值为空的记录单独处理，再和其他计算结果进行union.
* Mapreduce和hive的区别和联系
    * hive是基于hadoop的数据仓库
    * 那么为什么说hive是基于Hadoop的呢？
        *  之所以说hive是构建在Hadoop之上的数据仓库，简单的说是因为：
        *  ①数据存储在hdfs上
        * ②数据计算用mapreduce
    * Hive是一种建立在Hadoop文件系统上的数据仓库架构，并对存储在HDFS中的数据进行分析和管理；它可以将结构化的数据文件映射为一张数据库表，并提供完整的 SQL 查询功能，可以将 SQL 语句转换为 MapReduce 任务进行运行，通过自己的 SQL 去查询分析需要的内容，这套 SQL 简称 Hive SQL（HQL），使不熟悉MapReduce 的用户也能很方便地利用 SQL 语言对数据进行查询、汇总、分析。
    * Hive不支持更改数据的操作，Hive基于数据仓库，提供静态数据的动态查询。其使用类SQL语言，底层经过编译转为MapReduce程序，在hadoop上运行，数据存储在HDFS上。
* HIVE与RDBMS关系数据库的区别
    * 1、hive存储的数据量比较大，适合海量数据，适合存储轨迹类历史数据，适合用来做离线分析、数据挖掘运算，事务性较差，实时性较差 ;rdbms一般数据量相对来说不会太大，适合事务性计算，实时性较好，更加接近上层业务
    * 2、hive的计算引擎是hadoop的mapreduce，存储是hadoop的hdfs文件系统;rdbms的引擎由数据库自己设计实现例如mysql的innoDB，存储用的是数据库服务器本地的文件系统
    * 3、hive由于基于hadoop所以存储和计算的扩展能力都很好;rdbms在这方面比较弱，比如orcale的分表和扩容就很头疼
    * 4、hive表格没有主键、没有索引、不支持对具体某一行的操作，适合对批量数据的操作，不支持对数据的update操作，更新的话一般是先删除表然后重新落数据；rdbms事务性强，有主键、索引，支持对具体某一行的增删改查等操作
    * 5、hive的SQL为HQL，与标准的RDBMS的SQL存在有不少的区别，相对来说功能有限；rdbms的SQL为标准SQL，功能较为强大。
* hive中的存储方式
    * 1.textfile
        * Hive的默认存储格式
            * 存储方式：行存储
            * 磁盘开销大数据解析开销大
            * 压缩的text文件 hive无法进行合并和拆分
    * 2.SequenceFile
        * 二进制文件以key,value的形式序列化到文件中
        * 存储方式：行存储
        * 可分割压缩
        * 一般选择block压缩
        * 优势是文件和Hadoop api中的mapfile是相互兼容的
    * 3.rcfile
        * 存储方式：数据按行分块每块按照列存储
        * 压缩快快速列存取
        * 读记录尽量涉及到的block最少
        * 读取需要的列只需要读取每个row group 的头部定义。
        * 读取全量数据的操作性能可能比sequencefile没有明显的优势
    * 4.orc
        * 存储方式：数据按行分块每块按照列存储
        * 压缩快快速列存取
        * 效率比rcfile高,是rcfile的改良版本
    * 5.自定义格式
        * 用户可以通过实现inputformat和 outputformat来自定义输入输出格式
