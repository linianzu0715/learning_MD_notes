### Introduce:

Presto是一个运行在多台服务器上的分布式系统。 完整安装包括一个coordinator和多个worker。 由客户端提交查询，从Presto命令行CLI提交到coordinator。coordinator进行解析，分析并执行查询计划，然后分发处理队列到worker。![presto-overview](C:\Users\59584\OneDrive\新建文件夹\易观\pic\presto-overview.png)

### Demand

Presto的基本需求

- Linux or Mac OS X
- Java 8, 64-bit
- Python 2.4+

### Connector

#### HADOOP / HIVE

Presto支持从以下版本的Hadoop中读取Hive数据：

- Apache Hadoop 1.x
- Apache Hadoop 2.x
- Cloudera CDH 4
- Cloudera CDH 5

支持以下文件类型：Text, SequenceFile, RCFile, ORC

此外，需要有远程的Hive元数据。 不支持本地或嵌入模式。 Presto不使用MapReduce，只需要HDFS。

#### CASSANDRA

必须有Cassandra 2.x。 这种连接器完全不依赖Hive连接器，只需要一个安装好的Cassandra。

#### TPC-H

TPC-H连接器动态生成数据，可以用于实验与测试Presto。 此连接器没有额外要求。





### Deployment



