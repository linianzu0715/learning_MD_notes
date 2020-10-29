Mysql使用

登陆：

```shell
mysql -u root -p
```

然后会要求输入密码：

```shell
linianzu1996715
```



### 从csv文件向mysql插入数据

1. 首先我们启动mysql，并且使用我们的目标数据库

```mysql
mysql> use study
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```

2. 在我们的目标数据库中创建新的表

```mysql
CREATE TABLE IF NOT EXISTS study_test (
	user_number INT,
	user_name VARCHAR(30),
	user_address VARCHAR(30),
	user_phone INT,
	PRIMARY KEY (user_number)
)
```

创建完成表之后，里面是没有任何数据的

```mysql
mysql> select * from study_test;
Empty set (0.00 sec)
```

3. 我们准备好我们要插入的数据的csv格式文件

```
user_number,user_name,user_address,user_phone
1,li1,CS,121
2,li2,CS,122
3,li3,CS,123
4,li4,CS,124
5,li5,CS,125
```

4. 进入到 mysql workbench 中插入数据

![image-20201022153150467](/Users/linianzu/Documents/learning_MD_notes/Picture/image-20201022153150467.png)

![image-20201022153224573](/Users/linianzu/Documents/learning_MD_notes/Picture/image-20201022153224573.png)

![image-20201022153255844](/Users/linianzu/Documents/learning_MD_notes/Picture/image-20201022153255844.png)

![image-20201022153336583](/Users/linianzu/Documents/learning_MD_notes/Picture/image-20201022153336583.png)

最后就完成了数据的导入

5. 显示出导入的数据

```mysql
mysql> select * from study_test;
+-------------+-----------+--------------+------------+
| user_number | user_name | user_address | user_phone |
+-------------+-----------+--------------+------------+
|           1 | li1       | CS           |        121 |
|           2 | li2       | CS           |        122 |
|           3 | li3       | CS           |        123 |
|           4 | li4       | CS           |        124 |
|           5 | li5       | CS           |        125 |
+-------------+-----------+--------------+------------+
5 rows in set (0.00 sec)
```



