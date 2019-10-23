* Spark 算子有哪些，项目用到哪些算子
    *
* Spark 广播变量
    *
* Spark内存溢出
    *
* Spark OOM问题解决办法
    *
* Spark 任务执行速度倾斜问题解决方案
    *
* Spark与Hadoop MapReduce的异同
    * 首先Spark是借鉴了mapreduce并在其基础上发展起来的，继承了其分布式计算的优点并改进了mapreduce明显的缺陷，但是二者也有不少的差异具体如下：
        * 1、spark把运算的中间数据存放在内存，迭代计算效率更高；mapreduce的中间结果需要落地，需要保存到磁盘，这样必然会有磁盘io操做，影响性能。
        * 2、spark容错性高，它通过弹性分布式数据集RDD来实现高效容错，RDD是一组分布式的存储在节点内存中的只读性质的数据集，这些集合是弹性的，某一部分丢失或者出错，可以通过整个数据集的计算流程的血缘关系来实现重建；mapreduce的话容错可能只能重新计算了，成本较高。
        * 3、spark更加通用，spark提供了transformation和action这两大类的多个功能api，另外还有流式处理sparkstreaming模块、图计算GraphX等等；mapreduce只提供了map和reduce两种操作，流计算以及其他模块的支持比较缺乏。
        * 4、spark框架和生态更为复杂，首先有RDD、血缘lineage、执行时的有向无环图DAG、stage划分等等，
        * 很多时候spark作业都需要根据不同业务场景的需要进行调优已达到性能要求；mapreduce框架及其生态相对较为简单，对性能的要求也相对较弱，但是运行较为稳定，适合长期后台运行。
    * 最后总结：
        * spark生态更为丰富，功能更为强大、性能更佳，适用范围更广；mapreduce更简单、稳定性好、适合离线海量数据挖掘计算。
* Spark streaming的数据来源
    *
* Spark与hadoop的shuffle有何异同
    *
* Spark RDD操作map与flatmap的区别
    * map：对RDD每个元素转换，文件中的每一行数据返回一个数组对象
    * flatMap：对RDD每个元素转换，然后再扁平化将所有的对象合并为一个对象，文件中的所有行数据仅返回一个数组对象，会抛弃值为null的值
* Spark  RDD的理解
    *
* Spark 有哪些算子
    *
* Spark 的stage的理解
    *
* Spark 宽依赖和窄依赖
    *
* Sparkcore 的广播变量
    *
* Spark 累加变量
    *
* Spark 二次排序
    *
* Spark reduceByKey和groupByKey区别
    *
* 为什么要进行序列化
    * 序列化可以减少数据的体积，减少存储空间，高效存储和传输数据，不好的是使用的时候要反序列化，非常消耗CPU
* 介绍一下join操作优化经验？
    * join其实常见的就分为两类： map-side join 和  reduce-side join。当大表和小表join时，用map-side join能显著提高效率。将多份数据进行关联是数据处理过程中非常普遍的用法，不过在分布式计算系统中，这个问题往往会变的非常麻烦，因为框架提供的 join 操作一般会将所有数据根据 key 发送到所有的 reduce 分区中去，也就是 shuffle 的过程。造成大量的网络以及磁盘IO消耗，运行效率极其低下，这个过程一般被称为 reduce-side-join。如果其中有张表较小的话，我们则可以自己实现在 map 端实现数据关联，跳过大量数据进行 shuffle 的过程，运行时间得到大量缩短，根据不同数据可能会有几倍到数十倍的性能提升。
    * 备注：这个题目面试中非常非常大概率见到，务必搜索相关资料掌握，这里抛砖引玉。
* collect功能是什么，其底层是怎么实现的？
    * driver通过collect把集群中各个节点的内容收集过来汇总成结果，collect返回结果是Array类型的，collect把各个节点上的数据抓过来，抓过来数据是Array型，collect对Array抓过来的结果进行合并，合并后Array中只有一个元素，是tuple类型（KV类型的）的。
* rdd有几种操作类型？
    * 1）transformation，rdd由一种转为另一种rdd
    * 2）action，
    * 3）cronroller，crontroller是控制算子,cache,persist，对性能和效率的有很好的支持
* RDD创建有哪几种方式？
    * 1).使用程序中的集合创建rdd
    * 2).使用本地文件系统创建rdd
    * 3).使用hdfs创建rdd，
    * 4).基于数据库db创建rdd
    * 5).基于Nosql创建rdd，如hbase
    * 6).基于s3创建rdd，
    * 7).基于数据流，如socket创建rdd
* RDD有哪些缺陷？
    * 1）不支持细粒度的写和更新操作（如网络爬虫），spark写数据是粗粒度的所谓粗粒度，就是批量写入数据，为了提高效率。但是读数据是细粒度的也就是说可以一条条的读
    * 2）不支持增量迭代计算，Flink支持
* RDD的弹性表现在哪几点？
    * 1）自动的进行内存和磁盘的存储切换；
    * 2）基于Lingage的高效容错；
    * 3）task如果失败会自动进行特定次数的重试；
    * 4）stage如果失败会自动进行特定次数的重试，而且只会计算失败的分片；
    * 5）checkpoint和persist，数据计算之后持久化缓存
    * 6）数据调度弹性，DAG TASK调度和资源无关
    * 7）数据分片的高度弹性，a.分片很多碎片可以合并成大的，b.par
*  对于Spark中的数据倾斜问题你有什么好的方案？
    * 1前提是定位数据倾斜，是OOM了，还是任务执行缓慢，看日志，看WebUI
    * 2解决方法，有多个方面
        * 避免不必要的shuffle，如使用广播小表的方式，将reduce-side-join提升为map-side-join
        * 分拆发生数据倾斜的记录，分成几个部分进行，然后合并join后的结果
        * 改变并行度，可能并行度太少了，导致个别task数据压力大
        * 两阶段聚合，先局部聚合，再全局聚合
        * 自定义paritioner，分散key的分布，使其更加均匀
        * 详细解决方案参考博文《Spark数据倾斜优化方法》
* 你所理解的Spark的shuffle过程？
    * 1）shuffle过程的划分
    * 2）shuffle的中间结果如何存储
    * 3）shuffle的数据如何拉取过来
    * 可以参考这篇博文：http://www.cnblogs.com/jxhd1/p/6528540.html
* spark的有几种部署模式，每种模式特点？
    * 1）本地模式Spark不一定非要跑在hadoop集群，可以在本地，起多个线程的方式来指定。将Spark应用以多线程的方式直接运行在本地，一般都是为了方便调试，本地模式分三类
        * local：只启动一个executor
        * local[k]:启动k个executor
        * local启动跟cpu数目相同的 executor
    * 2)standalone模式
        * 分布式部署集群， 自带完整的服务，资源管理和任务监控是Spark自己监控，这个模式也是其他模式的基础，
    * 3)Spark on yarn模式
        * 分布式部署集群，资源和任务监控交给yarn管理，但是目前仅支持粗粒度资源分配方式，包含cluster和client运行模式，cluster适合生产，driver运行在集群子节点，具有容错功能，client适合调试，dirver运行在客户端
    * 4）Spark On Mesos模式。官方推荐这种模式（当然，原因之一是血缘关系）。正是由于Spark开发之初就考虑到支持Mesos，因此，目前而言，Spark运行在Mesos上会比运行在YARN上更加灵活，更加自然。用户可选择两种调度模式之一运行自己的应用程序：
        * 1)   粗粒度模式（Coarse-grained Mode）：每个应用程序的运行环境由一个Dirver和若干个Executor组成，其中，每个Executor占用若干资源，内部可运行多个Task（对应多少个“slot”）。应用程序的各个任务正式运行之前，需要将运行环境中的资源全部申请好，且运行过程中要一直占用这些资源，即使不用，最后程序运行结束后，回收这些资源。
        * 2)   细粒度模式（Fine-grained Mode）：鉴于粗粒度模式会造成大量资源浪费，Spark On Mesos还提供了另外一种调度模式：细粒度模式，这种模式类似于现在的云计算，思想是按需分配。
* Spark技术栈有哪些组件，每个组件都有什么功能，适合什么应用场景？
    * 可以画一个这样的技术栈图先，然后分别解释下每个组件的功能和场景
    * 1）Spark core：是其它组件的基础，spark的内核，主要包含：有向循环图、RDD、Lingage、Cache、broadcast等，并封装了底层通讯框架，是Spark的基础。
    * 2）SparkStreaming是一个对实时数据流进行高通量、容错处理的流式处理系统，可以对多种数据源（如Kdfka、Flume、Twitter、Zero和TCP 套接字）进行类似Map、Reduce和Join等复杂操作，将流式计算分解成一系列短小的批处理作业。
    * 3）Spark sql：Shark是SparkSQL的前身，Spark SQL的一个重要特点是其能够统一处理关系表和RDD，使得开发人员可以轻松地使用SQL命令进行外部查询，同时进行更复杂的数据分析
    * 4）BlinkDB ：是一个用于在海量数据上运行交互式 SQL 查询的大规模并行查询引擎，它允许用户通过权衡数据精度来提升查询响应时间，其数据的精度被控制在允许的误差范围内。
    * 5）MLBase是Spark生态圈的一部分专注于机器学习，让机器学习的门槛更低，让一些可能并不了解机器学习的用户也能方便地使用MLbase。MLBase分为四部分：MLlib、MLI、ML Optimizer和MLRuntime。
    * 6）GraphX是Spark中用于图和图并行计算
* Spark中Work的主要工作是什么？
    * 主要功能：管理当前节点内存，CPU的使用状况，接收master分配过来的资源指令，通过ExecutorRunner启动程序分配任务，worker就类似于包工头，管理分配新进程，做计算的服务，相当于process服务。
    * 需要注意的是：1）worker会不会汇报当前信息给master，worker心跳给master主要只有workid，它不会发送资源信息以心跳的方式给mater，master分配的时候就知道work，只有出现故障的时候才会发送资源。
    * 2）worker不会运行代码，具体运行的是Executor是可以运行具体appliaction写的业务逻辑代码，操作代码的节点，它不会运行程序的代码的。
* Spark为什么比mapreduce快？
    * 1）基于内存计算，减少低效的磁盘交互；
    * 2）高效的调度算法，基于DAG；
    * 3)容错机制Linage，精华部分就是DAG和Lingae
* 简单说一下hadoop和spark的shuffle相同和差异？
    * 1）从 high-level 的角度来看，两者并没有大的差别。 都是将 mapper（Spark 里是 ShuffleMapTask）的输出进行 partition，不同的 partition 送到不同的 reducer（Spark 里 reducer 可能是下一个 stage 里的 ShuffleMapTask，也可能是 ResultTask）。Reducer 以内存作缓冲区，边 shuffle 边 aggregate 数据，等到数据 aggregate 好以后进行 reduce() （Spark 里可能是后续的一系列操作）。
    * 2）从 low-level 的角度来看，两者差别不小。 Hadoop MapReduce 是 sort-based，进入 combine() 和 reduce() 的 records 必须先 sort。这样的好处在于 combine/reduce() 可以处理大规模的数据，因为其输入数据可以通过外排得到（mapper 对每段数据先做排序，reducer 的 shuffle 对排好序的每段数据做归并）。目前的 Spark 默认选择的是 hash-based，通常使用 HashMap 来对 shuffle 来的数据进行 aggregate，不会对数据进行提前排序。如果用户需要经过排序的数据，那么需要自己调用类似 sortByKey() 的操作；如果你是Spark 1.1的用户，可以将spark.shuffle.manager设置为sort，则会对数据进行排序。在Spark 1.2中，sort将作为默认的Shuffle实现。
    * 3）从实现角度来看，两者也有不少差别。 Hadoop MapReduce 将处理流程划分出明显的几个阶段：map(), spill, merge, shuffle, sort, reduce() 等。每个阶段各司其职，可以按照过程式的编程思想来逐一实现每个阶段的功能。在 Spark 中，没有这样功能明确的阶段，只有不同的 stage 和一系列的 transformation()，所以 spill, merge, aggregate 等操作需要蕴含在 transformation() 中。
    * 如果我们将 map 端划分数据、持久化数据的过程称为 shuffle write，而将 reducer 读入数据、aggregate 数据的过程称为 shuffle read。那么在 Spark 中，问题就变为怎么在 job 的逻辑或者物理执行图中加入 shuffle write 和 shuffle read 的处理逻辑？以及两个处理逻辑应该怎么高效实现？
    * Shuffle write由于不要求数据有序，shuffle write 的任务很简单：将数据 partition 好，并持久化。之所以要持久化，一方面是要减少内存存储空间压力，另一方面也是为了 fault-tolerance。
* Mapreduce和Spark的都是并行计算，那么他们有什么相同和区别
    * 两者都是用mr模型来进行并行计算:
    * 1)hadoop的一个作业称为job，job里面分为map task和reduce task，每个task都是在自己的进程中运行的，当task结束时，进程也会结束。
    * 2)spark用户提交的任务成为application，一个application对应一个sparkcontext，app中存在多个job，每触发一次action操作就会产生一个job。这些job可以并行或串行执行，每个job中有多个stage，stage是shuffle过程中DAGSchaduler通过RDD之间的依赖关系划分job而来的，每个stage里面有多个task，组成taskset有TaskSchaduler分发到各个executor中执行，executor的生命周期是和app一样的，即使没有job运行也是存在的，所以task可以快速启动读取内存进行计算。
    * 3)hadoop的job只有map和reduce操作，表达能力比较欠缺而且在mr过程中会重复的读写hdfs，造成大量的io操作，多个job需要自己管理关系。spark的迭代计算都是在内存中进行的，API中提供了大量的RDD操作如join，groupby等，而且通过DAG图可以实现良好的容错。
* spark有哪些组件？
    * 1）master：管理集群和节点，不参与计算。
    * 2）worker：计算节点，进程本身不参与计算，和master汇报。
    * 3）Driver：运行程序的main方法，创建spark context对象。
    * 4）spark context：控制整个application的生命周期，包括dagsheduler和task scheduler等组件。
    * 5）client：用户提交程序的入口。
* spark工作机制？
    * 用户在client端提交作业后，会由Driver运行main方法并创建spark context上下文。
    * 执行add算子，形成dag图输入dagscheduler，按照add之间的依赖关系划分stage输入task scheduler。 task scheduler会将stage划分为task set分发到各个节点的executor中执行。
* spark的优化怎么做？
    * spark调优比较复杂，但是大体可以分为三个方面来进行，
    * 1）平台层面的调优：防止不必要的jar包分发，提高数据的本地性，选择高效的存储格式如parquet，
    * 2）应用程序层面的调优：过滤操作符的优化降低过多小任务，降低单条记录的资源开销，处理数据倾斜，复用RDD进行缓存，作业并行化执行等等，
    * 3）JVM层面的调优：设置合适的资源量，设置合理的JVM，启用高效的序列化方法如kyro，增大off head内存等等
* 简要描述Spark分布式集群搭建的步骤
    * 1）准备linux环境，设置集群搭建账号和用户组，设置ssh，关闭防火墙，关闭seLinux，配置host，hostname
    * 2）配置jdk到环境变量
    * 3）搭建hadoop集群，如果要做master ha，需要搭建zookeeper集群修改hdfs-site.xml,hadoop_env.sh,yarn-site.xml,slaves等配置文件
    * 4）启动hadoop集群，启动前要格式化namenode
    * 5）配置spark集群，修改spark-env.xml，slaves等配置文件，拷贝hadoop相关配置到spark conf目录下
    * 6)启动spark集群。
* 什么是RDD宽依赖和窄依赖？
    * RDD和它依赖的parent RDD(s)的关系有两种不同的类型，即窄依赖（narrow dependency）和宽依赖（wide dependency）。
    * 1）窄依赖指的是每一个parent RDD的Partition最多被子RDD的一个Partition使用
    * 2）宽依赖指的是多个子RDD的Partition会依赖同一个parent RDD的Partition
