#### 常用命令

**1、启动hadoop所有进程**

start-all.sh等价于**start-dfs.sh + start-yarn.sh**

但是一般不推荐使用start-all.sh(因为开源框架中内部命令启动有很多问题)。



**2、单进程启动。**

```
sbin/start-dfs.sh
```

  **sbin/hadoop-daemons.sh --config .. --hostname .. start namenode ...**
  **sbin/hadoop-daemons.sh --config .. --hostname .. start datanode ...**
  **sbin/hadoop-daemons.sh --config .. --hostname .. start sescondarynamenode ...**
  **sbin/hadoop-daemons.sh --config .. --hostname .. start zkfc ...     **

```
sbin/start-yarn.sh
```

  **libexec/yarn-config.sh**
  **sbin/yarn-daemon.sh --config $YARN_CONF_DIR start resourcemanager**
  **sbin/yarn-daemons.sh --config $YARN_CONF_DIR start nodemanager**



**3、常用命令**

**1、查看指定目录下内容**

```
hdfs dfs –ls [文件目录]
hdfs dfs -ls -R   /                  //显式目录结构

eg: hdfs dfs –ls /user/wangkai.pt
```



 **2、打开某个已存在文件**

```
hdfs dfs –cat [file_path]

eg:hdfs dfs -cat /user/wangkai.pt/data.txt
```



**3、将本地文件存储至hadoop**

```
hdfs dfs –put [本地地址] [hadoop目录]

eg:
hdfs dfs –put /home/t/file.txt  /user/t
```



**4、将本地文件夹存储至hadoop**

```
hdfs dfs –put [本地目录] [hadoop目录] 

eg:
hdfs dfs –put /home/t/dir_name/user/t  (dir_name是文件夹名)
```



 **5、将hadoop上某个文件down至本地已有目录下**

```
hadoop dfs -get [文件目录] [本地目录]

eg:
hadoop dfs –get /user/t/ok.txt /home/t
```



 **6、删除hadoop上指定文件**

```
hdfs dfs –rm [文件地址]

eg:
hdfs dfs –rm /user/t/ok.txt
```



 **7、删除hadoop上指定文件夹（包含子目录等）**

```
hdfs dfs –rm [目录地址]

eg:
hdfs dfs –rmr /user/t
```



 **8、在hadoop指定目录内创建新目录**

```
hdfs dfs –mkdir /user/t

eg:
hdfs dfs -mkdir - p /user/centos/hadoop
```



 **9、在hadoop指定目录下新建一个空文件**

```
使用touchz命令：

hdfs dfs  -touchz  /user/new.txt
```



 **10、将hadoop上某个文件重命名**

```
使用mv命令：

hdfs dfs –mv  /user/test.txt  /user/ok.txt  （将test.txt重命名为ok.txt）
```



 **11、将hadoop指定目录下所有内容保存为一个文件，同时down至本地**

```
hdfs dfs –getmerge /user /home/t
```



**12、将正在运行的hadoop作业kill掉**

```
hadoop job –kill  [job-id]
```



**13.查看帮助**

```
hdfs dfs -help
```



#### **安全模式**

**(1)退出安全模式**

NameNode在启动时会自动进入安全模式。安全模式是NameNode的一种状态，在这个阶段，文件系统不允许有任何修改。

系统显示Name node in safe mode，说明系统正处于安全模式，这时只需要等待十几秒即可，也可通过下面的命令退出安全模式：**/usr/local/hadoop$bin/hadoop dfsadmin -safemode leave**



**(2) 进入安全模式**
  在必要情况下，可以通过以下命令把HDFS置于安全模式：

```
/usr/local/hadoop$bin/hadoop dfsadmin -safemode enter
```



#### **节点添加**

添加一个新的DataNode节点，先在新加节点上安装好Hadoop，要和NameNode使用相同的配置（可以直接从NameNode复制），修改HADOOPHOME/conf/master文件，加入NameNode主机名。然后在NameNode节点上修改HADOOP_HOME/conf/slaves文件，加入新节点名，再建立新加节点无密码的SSH连接，运行启动命令为：**/usr/local/hadoop$bin/start-all.sh**



#### **负载均衡**

HDFS的数据在各个DataNode中的分布可能很不均匀，尤其是在DataNode节点出现故障或新增DataNode节点时。新增数据块时NameNode对DataNode节点的选择策略也有可能导致数据块分布不均匀。用户可以使用命令重新平衡DataNode上的数据块的分布：**/usr/local/hadoop$bin/start-balancer.sh**

