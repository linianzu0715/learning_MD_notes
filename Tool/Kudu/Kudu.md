## Kudu

Apache Kudu是一个由Cloudera开源的存储引擎，可以同时提供低延迟的随机读写和高效的数据分析能力。Kudu支持水平拓展，使用Raft协议进行一致性保证，摒弃额呵Cloudera Impala 和 Apache Spark等流行的大数据查询和分析工具结合紧密。

**为什么需要Kudu**

提起大数据存储，我们能够想到的技术很多，比如HDFS，以及在HDFS上的列式存储技术Apache Parquet，Apache ORC，以及以KV姓氏存储半结构化数据的Apache Hbase和Apache Cassandra。

事实上，当前的这些存储技术都存在着一定的局限性。对于会被用来进行分析的静态数据集来说，使用Parquet或者ORC存储是一个明智的选择。但是目前列式存储技术都不能更新数据，而且随机读写的性能比较差。而可以进行高效随机读写的HBase，Cassandra等数据库，不适用于基于SQL的数据分析方向。所以在现在的企业中，常常会存储两套数据分别用于实时读写和数据分析。先将数据写入到Hbase中，再定期通过ETL到Parquet进行数据同步。但是这样有很多缺点：

1. 用户需要在两套系统间编写和维护复杂的ETL逻辑
2. 时效性较差。因为ETL通常是一个小时，几个小时或者是一天一次，那么可供分析的数据就需要一个小时甚至是一天的时间才进入到可用状态，就是说，从数据到达到可被分析之间会存在一个空档期。
3. 更新需求难以满足。在实际情况中可能会有一些对已经写入的数据的更新的需求，这种情况下就需要对历史数据进行更新，而对Parquet这种静态数据集的更新操作，代价是很大的。
4. 存储资源浪费。两套存储系统意味着占用的磁盘资源翻倍了，造成了成本的提升。

我们知道，基于HDFS的存储技术，比如Parquet，具有高吞吐量连续读取数据的能力。而HBase和Cassandra等技术适用于低延迟的随机读写场景。现在就是需要一种技术能够同时具备这两种有点。

Kudu不但是提供了行级别的插入，更新，删除API，同时也提供了接近Parquet性能的批量扫描操作。使用同一份存储，既可以进行随机读写，也可以满足数据分析的要求。

**Kudu纵览**

Tables和Schemas

从用户角度来看，kudu是一个存储结构化数据表的存储系统。在一个kudu集群中可以定义任意数量的table，每个table都需要预先定义好schema。每个table的列数是确定的，每一列都需要有名字和类型，每个表中可以把其中的一列或者多列定义为主键。这么看来，kudu更像是关系型数据库，而不是HBase，Cassandra和MangoDB这些Nosql数据库。不过Kudu目前还是不能像关系型数据库一样支持二级索引。

kudu使用确定的列类型，而不是类似于Nosql的"everything is byte"。好处：

1. 确定的列类型使Kudu可以进行类型特有的编码
2. 可以提供SQL-like元数据给其他上层查询工具，比如BI工具

**读写操作**

用户可以使用 *Insert*，*Update*和*Delete* API对表进行写操作。不论使用哪种API，都必须指定主键。但批量的删除和更新操作需要依赖更高层次的组件（比如Impala、Spark）。Kudu目前还不支持多行事务。而在读操作方面，Kudu只提供了*Scan*操作来获取数据。用户可以通过指定过滤条件来获取自己想要读取的数据，但目前只提供了两种类型的过滤条件：主键范围和列值与常数的比较。由于Kudu在硬盘中的数据采用列式存储，所以只扫描需要的列将极大地提高读取性能。

**一致性模型**

Kudu为用户提供了两种一致性模型。默认的一致性模型是*snapshot consistency*（快照一致性）。这种一致性模型保证用户每次读取出来的都是一个可用的快照，但这种一致性模型只能保证单个client可以看到最新的数据，但不能保证多个client每次取出的都是最新的数据。另一种一致性模型*external consistency*可以在多个client之间保证每次取到的都是最新数据，但是Kudu没有提供默认的实现，需要用户做一些额外工作。为了实现*external consistency*，Kudu提供了两种方式：

1. 在client之间传播timestamp token。在一个client完成一次写入后，会得到一个timestamp token，然后这个client把这个token传播到其他client，这样其他client就可以通过token取到最新数据了。不过这个方式的复杂度很高。
2. 通过*commit-wait*方式，这有些类似于Google的Spanner。但是目前基于NTP的*commit-wait*方式延迟实在有点高。不过Kudu相信，随着Spanner的出现，未来几年内基于real-time clock的技术将会逐渐成熟。

**kudu架构**

与HDFS和HBase相似，Kudu使用单个的Master节点，用来管理集群的元数据，并且使用任意数量的Tablet Server节点用来存储实际数据。可以部署多个Master节点来提高容错性。

**Master**

Kudu的master节点负责整个集群的元数据管理和服务协调。它承担着以下功能：

1. 作为*catalog manager*，master节点管理着集群中所有table和tablet的schema及一些其他的元数据。
2. 作为*cluster coordinator*，master节点追踪着所有server节点是否存活，并且当server节点挂掉后协调数据的重新分布。
3. 作为*tablet directory*，master跟踪每个tablet的位置。

**Catalog Manager**

Kudu的master节点会持有一个单tablet的table——catalog table，但是用户是不能直接访问的。master将内部的catalog信息写入该tablet，并且将整个catalog的信息缓存到内存中。随着现在商用服务器上的内存越来越大，并且元数据信息占用的空间其实并不大，所以master不容易存在性能瓶颈。catalog table保存了所有table的schema的版本以及table的状态（创建、运行、删除等）。

**Cluster Coordination**

Kudu集群中的每个tablet server都需要配置master的主机名列表。当集群启动时，tablet server会向master注册，并发送所有tablet的信息。tablet server第一次向master发送信息时会发送所有tablet的全量信息，后续每次发送则只会发送增量信息，仅包含新创建、删除或修改的tablet的信息。

作为cluster coordination，master只是集群状态的观察者。对于tablet server中tablet的副本位置、Raft配置和schema版本等信息的控制和修改由tablet server自身完成。master只需要下发命令，tablet server执行成功后会自动上报处理的结果。

**Tablet Directory**

因为master上缓存了集群的元数据，所以client读写数据的时候，肯定是要通过master才能获取到tablet的位置等信息。但是如果每次读写都要通过master节点的话，那master就会变成这个集群的性能瓶颈，所以client会在本地缓存一份它需要访问的tablet的位置信息，这样就不用每次读写都从master中获取。

因为tablet的位置可能也会发生变化（比如某个tablet server节点crash掉了），所以当tablet的位置发生变化的时候，client会收到相应的通知，然后再去master上获取一份新的元数据信息。

**Tablet存储**

在数据存储方面，Kudu选择完全由自己实现，而没有借助于已有的开源方案。tablet存储主要想要实现的目标为：

1. 快速的列扫描
2. 低延迟的随机读写
3. 一致性的性能

**RowSets**

在Kudu中，tablet被细分为更小的单元，叫做*RowSets*。一些RowSet仅存在于内存中，被称为*MemRowSets*，而另一些则同时使用内存和硬盘，被称为*DiskRowSets*。任何一行未被删除的数据都只能存在于一个RowSet中。

无论任何时候，一个tablet仅有一个MemRowSet用来保存最新插入的数据，并且有一个后台线程会定期把内存中的数据flush到硬盘上。

当一个MemRowSet被flush到硬盘上以后，一个新的MemRowSet会替代它。而原有的MemRowSet会变成一到多个DiskRowSet。flush操作是完全同步进行的，在进行flush时，client同样可以进行读写操作。

#### MemRowSets

MemRowSets是一个可以被并发访问并进行过锁优化的B-tree，主要是基于MassTree来设计的，但存在几点不同：

1. Kudu并不支持直接删除操作，由于使用了MVCC，所以在Kudu中删除操作其实是插入一条标志着删除的数据，这样就可以推迟删除操作。
2. 类似删除操作，Kudu也不支持原地更新操作。
3. 将tree的leaf链接起来，就像B+-tree。这一步关键的操作可以明显地提升scan操作的性能。
4. 没有实现字典树（trie树），而是只用了单个tree，因为Kudu并不适用于极高的随机读写的场景。

与Kudu中其他模块中的数据结构不同，MemRowSet中的数据使用行式存储。因为数据都在内存中，所以性能也是可以接受的，而且Kudu对在MemRowSet中的数据结构进行了一定的优化。

**DiskRowSet**

当MemRowSet被flush到硬盘上，就变成了DiskRowSet。当MemRowSet被flush到硬盘的时候，每32M就会形成一个新的DiskRowSet，这主要是为了保证每个DiskRowSet不会太大，便于后续的增量compaction操作。Kudu会将数据按列存储，数据被切分成多个page，并使用B-tree进行索引。除了用户写入的数据，Kudu还会将主键索引存入一个列中，并且提供布隆过滤器来进行高效查找。布隆过滤器（Bloom Filter）是1970年由布隆提出的。它实际上是一个很长的[二进制](https://baike.baidu.com/item/二进制/361457)向量和一系列随机映射[函数](https://baike.baidu.com/item/函数/301912)。布隆过滤器可以用于[检索](https://baike.baidu.com/item/检索/11003896)一个元素是否在一个[集合](https://baike.baidu.com/item/集合/2908117)中。它的优点是空间效率和查询时间都比一般的算法要好的多，缺点是有一定的误识别率和删除困难。

**Compaction**

为了提高查询性能，Kudu会定期进行compaction操作，合并delta data与base data，对标记了删除的数据进行删除，并且会合并一些DiskRowSet。

**分区**

和许多分布式存储系统一样，Kudu的table是水平分区的。BigTable只提供了range分区，Cassandra只提供hash分区，而Kudu提供了较为灵活的分区方式。当用户创建一个table时，可以同时指定table的的partition schema，partition schema会将primary key映射为partition key。一个partition schema包括0到多个hash-partitioning规则和一个range-partitioning规则。通过灵活地组合各种partition规则，用户可以创造适用于自己业务场景的分区方式。

**Kudu的应用**

Kudu的应用场景很广泛，比如可以进行实时的数据分析，用于数据可能会存在变化的时序数据应用等，甚至还有人探讨过使用Kudu替代Kafka的可行性（详情请戳[这里](https://link.jianshu.com/?t=http://blog.rodeo.io/2016/01/24/kudu-as-a-more-flexible-kafka.html)）。不过Kudu最有名和最成功的应用案例，还是国内的小米。小米公司不仅使用Kudu，还深度参与了Kudu的开发。Kudu项目在2012年10月由Cloudera公司发起，2015年10月对外公布，2015年12月进入Apache孵化器，但是小米公司早在2014年9月就加入到Kudu的开发中了。下面我们可以跟随Cloudera在宣传Kudu时使用的ppt来看一看Kudu在小米的使用。



**Introducing Apache Kudu**

Kudu is a columnar storage manager developed for the Apache Hadoop platform. Kudu shares the common technical properties of Hadoop ecosystem applications: it runs on commodity hardware, is horizontally scalable, and supports highly available operation.

Kudu’s design sets it apart. Some of Kudu’s benefits include:

1. Fast processing of OLAP workloads.
2. Integration with MapReduce, Spark and other Hadoop ecosystem components.
3. Tight integration with Apache Impala, making it a good, mutable alternative to using HDFS with Apache Parquet.
4. Strong but flexible consistency model, allowing you to choose consistency requirements on a per-request basis, including the option for strict-serializable consistency.
5. Strong performance for running sequential and random workloads simultaneously.
6. Easy to administer and manage.
7. High availability. Tablet Servers and Masters use the [Raft Consensus Algorithm](https://kudu.apache.org/docs/#raft), which ensures that as long as more than half the total number of replicas is available, the tablet is available for reads and writes. For instance, if 2 out of 3 replicas or 3 out of 5 replicas are available, the tablet is available.
8. Reads can be serviced by read-only follower tablets, even in the event of a leader tablet failure.
9. Structured data model.

By combining all of these properties, Kudu targets support for families of applications that are difficult or impossible to implement on current generation Hadoop storage technologies.  A few examples of applications for which Kudu is a great solution are:

1. Reporting applications where newly-arrived data needs to be immediately available for end users
2. Time-series applications that must simultaneously support: queries across large amounts of historic data. Granular queries about an individual entity that must return very quickly.
3. Applications that use predictive models to make real-time decisions with periodic refreshes of the predictive model based on all historic data

**Kudu-Impala Integration Features**

- `CREATE/ALTER/DROP TABLE`: Impala supports creating, altering, and dropping tables using Kudu as the persistence layer. The tables follow the same internal / external approach as other tables in Impala, allowing for flexible data ingestion and querying.
- `INSERT`:Data can be inserted into Kudu tables in Impala using the same syntax as any other Impala table like those using HDFS or HBase for persistence.
- `UPDATE` / `DELETE`: Impala supports the UPDATE and DELETE SQL commands to modify existing data in a Kudu table row-by-row or as a batch. The syntax of the SQL commands is chosen to be as compatible as possible with existing standards. In addition to simple DELETE or UPDATE commands, you can specify complex joins with a FROM clause in a subquery.
- Flexible Partitioning: Similar to partitioning of tables in Hive, Kudu allows you to dynamically pre-split tables by hash or range into a predefined number of tablets,  in order to distribute writes and queries evenly across your cluster. You can partition by any number of primary key columns, by any number of hashes, and an optional list of split rows. See [Schema Design](https://kudu.apache.org/docs/schema_design.html#schema_design).
- Parallel Scan: To achieve the highest possible performance on modern hardware, the Kudu client used by Impala parallelizes scans across multiple tablets.
- High-efficiency queries: Where possible, Impala pushes down predicate evaluation to Kudu, so that predicates are evaluated as close as possible to the data. Query performance is comparable to Parquet in many workloads.

For more details regarding querying data stored in Kudu using Impala, please refer to the Impala documentation.

**Concepts and terms**

Columnar Data Store: Kudu is a *columnar data store*. A columnar data store stores data in strongly-typed columns. With a proper design, it is superior for analytical or data warehousing workloads for several reasons.

Read Efficiency: For analytical queries, you can read a single column, or a portion of that column, while ignoring other columns. This means you can fulfill your query while reading a minimal number of blocks on disk. With a row-based store, you need to read the entire row, even if you only return values from a few columns.

Data Compression: Because a given column contains only one type of data, pattern-based compression can be orders of magnitude more efficient than compressing mixed data types, which are used in row-based solutions. Combined with the efficiencies of reading data from columns, compression allows you to fulfill your query while reading even fewer blocks from disk. See Data Compression.

Table: A *table* is where your data is stored in Kudu. A table has a schema and a totally ordered primary key. A table is split into segments called tablets.

Tablet: A *tablet* is a contiguous segment of a table, similar to a *partition* in other data storage engines or relational databases. A given tablet is replicated on multiple tablet servers, and at any given point in time, one of these replicas is considered the leader tablet.  Any replica can service reads, and writes require consensus among the set of tablet servers serving the tablet.

Tablet Server: A *tablet server* stores and serves tablets to clients. For a given tablet, one tablet server acts as a leader, and the others act as follower replicas of that tablet. Only leaders service write requests, while leaders or followers each service read requests. Leaders are elected using [Raft Consensus Algorithm](https://kudu.apache.org/docs/#raft). One tablet server can serve multiple tablets, and one tablet can be served by multiple tablet servers.

Master: The *master* keeps track of all the tablets, tablet servers, the [Catalog Table](https://kudu.apache.org/docs/#catalog_table), and other metadata related to the cluster. At a given point in time, there can only be one acting master (the leader). If the current leader disappears, a new master is elected using [Raft Consensus Algorithm](https://kudu.apache.org/docs/#raft). The master also coordinates metadata operations for clients. For example, when creating a new table, the client internally sends the request to the master. The master writes the metadata for the new table into the catalog table, and coordinates the process of creating tablets on the tablet servers.

All the master’s data is stored in a tablet, which can be replicated to all the other candidate masters.

Tablet servers heartbeat to the master at a set interval (the default is once per second).

Raft Consensus Algorithm: Kudu uses the [Raft consensus algorithm](https://raft.github.io/) as a means to guarantee fault-tolerance and consistency, both for regular tablets and for master data. Through Raft, multiple replicas of a tablet elect a *leader*, which is responsible for accepting and replicating writes to *follower* replicas. Once a write is persisted in a majority of replicas it is acknowledged to the client. A given group of `N` replicas (usually 3 or 5) is able to accept writes with at most `(N - 1)/2` faulty replicas.

Catalog Table: The *catalog table* is the central location for metadata of Kudu. It stores information about tables and tablets. The catalog table may not be read or written directly. Instead, it is accessible only via metadata operations exposed in the client API. The catalog table stores two categories of metadata:

1. Tables: table schemas, locations, and states
2. Tablets: the list of existing tablets, which tablet servers have replicas of each tablet, the tablet’s current state, and start and end keys.

**Logical Replication: 逻辑上的复制品**

Kudu replicates operations, not on-disk data. This is referred to as *logical replication*, as opposed to *physical replication*. This has several advantages: 

1. Although inserts and updates do transmit data over the network, deletes do not need to move any data. The delete operation is sent to each tablet server, which performs the delete locally.
2. Physical operations, such as compaction, do not need to transmit the data over the network in Kudu. This is different from storage systems that use HDFS, where the blocks need to be transmitted over the network to fulfill the required number of replicas.
3. Tablets do not need to perform compactions at the same time or on the same schedule, or otherwise remain in sync on the physical storage layer. This decreases the chances of all tablet servers experiencing high latency at the same time, due to compactions or heavy write loads.

Example use case:

**Streaming Input with Near Real Time Availability**

A common challenge in data analysis is one where new data arrives rapidly and constantly, and the same data needs to be available in near real time for reads, scans, and updates. Kudu offers the powerful combination of fast inserts and updates  with efficient columnar scans to enable real-time analytics use cases on a single storage layer.

**Time-series application with widely varying access patterns**

A time-series schema is one in which data points are organized and keyed according to the time at which they occurred.  This can be useful for investigating the performance of metrics over time or attempting to predict future behavior based on past data. For instance, time-series customer data might be used both to store purchase click-stream history and to predict future purchases, or for use by a customer support representative. While these different types of analysis are occurring, inserts and mutations may also be occurring individually and in bulk, and become available immediately to read workloads.  Kudu can handle all of these access patterns simultaneously in a scalable and efficient manner.

Kudu is a good fit for time-series workloads for several reasons. With Kudu’s support for hash-based partitioning, combined with its native support for compound row keys,  it is simple to set up a table spread across many servers without the risk of "hotspotting" that is commonly observed when range partitioning is used. Kudu’s columnar storage engine is also beneficial in this context, because many time-series workloads read only a few columns, as opposed to the whole row.

设计不好的行键是导致 hotspotting 的常见原因。当大量的客户端流量（ traffic ）被定向在集群上的一个或几个节点时，就会发生 hotspotting。这些流量可能代表着读、写或其他操作。流量超过了承载该region的单个机器所能负荷的量，这就会导致性能下降并有可能造成region的不可用。在同一 RegionServer 上的其他region也可能会受到其不良影响，因为主机无法提供服务所请求的负载。设计使集群能被充分均匀地使用的数据访问模式是至关重要的。

In the past, you might have needed to use multiple data stores to handle different data access patterns. This practice adds complexity to your application and operations, 

**Combining Data In Kudu With Legacy Systems**

