[toc]

### SQL优化：

1. 在表中建立索引，优先考虑where、group by使用到的字段。

2. 尽量避免使用select *，返回无用的字段会降低查询效率。如下：

   ```sql
   SELECT * FROM t 
   ```

   优化方式：使用具体的字段代替*，只返回使用到的字段。

3. 尽量避免使用in 和not in，会导致数据库引擎放弃索引进行全表扫描。如下：

   ```sql
   SELECT * FROM t WHERE id IN (2,3)
   
   SELECT * FROM t1 WHERE username IN (SELECT username FROM t2)
   ```

   优化方式：如果是连续数值，可以用between代替。如下：

   ```sql
   SELECT * FROM t WHERE id BETWEEN 2 AND 3
   ```

   如果是子查询，可以用exists代替。如下：

   ```sql
   SELECT * FROM t1 WHERE EXISTS (SELECT * FROM t2 WHERE t1.username = t2.username)
   ```

4. 尽量避免使用or，会导致数据库引擎放弃索引进行全表扫描。如下：

   ```sql
   SELECT * FROM t WHERE id = 1 OR id = 3
   ```

   优化方式：可以用union代替or。如下：

   ```sql
   SELECT * FROM t WHERE id = 1
   UNION
   SELECT * FROM t WHERE id = 3
   （PS：如果or两边的字段是同一个，如例子中这样。貌似两种方式效率差不多，即使union扫描的是索引，or扫描的是全表）
   ```

5. 尽量避免在字段开头模糊查询，会导致数据库引擎放弃索引进行全表扫描。如下：

   ```sql
   SELECT * FROM t WHERE username LIKE '%li%'
   优化方式：尽量在字段后面使用模糊查询。如下：
   SELECT * FROM t WHERE username LIKE 'li%'
   ```

6. 尽量避免在where条件中等号的左侧进行表达式、函数操作，会导致数据库引擎放弃索引进行全表扫描。如下：

   ```sql
   SELECT * FROM t2 WHERE score/10 = 9
   SELECT * FROM t2 WHERE SUBSTR(username,1,2) = 'li'
   优化方式：可以将表达式、函数操作移动到等号右侧。如下：
   SELECT * FROM t2 WHERE score = 10*9
   SELECT * FROM t2 WHERE username LIKE 'li%'
   ```

7. 当数据量大时，避免使用where 1=1的条件。通常为了方便拼装查询条件，我们会默认使用该条件，数据库引擎会放弃索引进行全表扫描。如下：

   ```sql
   SELECT * FROM t WHERE 1=1
   ```

   优化方式：用代码拼装sql时进行判断，没where加where，有where加and。



### 创建数据库：

```sql
CREATE DATABASE 数据库名;
```

### 删除数据库：

```sql
drop database <数据库名>;
```

### 使用数据库：

```sql
USE RUNOOB;
```

### 创建数据表：

```sql
CREATE TABLE table_name (column_name column_type);

#example:
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```



### 删除数据表：

```sql
DROP TABLE table_name;
```



### 插入数据：

```sql
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```



### UPDATE 更新:

如果我们需要修改或更新 MySQL 中的数据，我们可以使用 SQL UPDATE 命令来操作。

```sql
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]

UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;
```



### DELETE 语句

```
DELETE FROM table_name [WHERE Clause]
```



### LIKE语句：

```sql
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
```

MySQL提供两个通配符，用于与`LIKE`运算符一起使用，它们分别是：百分比符号 `%`和下划线  `_`。

- 百分比(`%`)通配符允许匹配任何字符串的零个或多个字符。
- 下划线(`_`)通配符允许匹配任何单个字符



### MySQL 事务

MySQL 事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，你既需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务！

- 在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
- 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
- 事务用来管理 insert,update,delete 语句

MySQL 事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，你既需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务！

- 在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
- 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
- 事务用来管理 insert,update,delete 语句

MYSQL 事务处理主要有两种方法：

1、用 BEGIN, ROLLBACK, COMMIT来实现

- **BEGIN** 开始一个事务
- **ROLLBACK** 事务回滚
- **COMMIT** 事务确认

2、直接用 SET 来改变 MySQL 的自动提交模式: 

- **SET AUTOCOMMIT=0** 禁止自动提交
- **SET AUTOCOMMIT=1** 开启自动提交



### MySQL ALTER命令

当我们需要修改数据表名或者修改数据表字段时，就需要使用到MySQL ALTER命令。

**删除字段**

```sql
ALTER TABLE testalter_tbl  DROP i;
```

**添加表字段**

```sql
ALTER TABLE testalter_tbl ADD i INT;
```

**修改表字段**

修改字段c的类型

```
ALTER TABLE testalter_tbl MODIFY c CHAR(10);
```

**ALTER TABLE 对 Null 值和默认值的影响**

当你修改字段时，你可以指定是否包含值或者是否设置默认值。以下实例，指定字段 j 为 NOT NULL 且默认值为100 。

```sql
mysql> ALTER TABLE testalter_tbl 
    -> MODIFY j BIGINT NOT NULL DEFAULT 100;
```

如果你不设置默认值，MySQL会自动设置该字段默认为 NULL。



### MySQL 索引

MySQL索引的建立对于MySQL的高效运行是很重要的，索引可以大大提高MySQL的检索速度。拿汉语字典的目录页（索引）打比方，我们可以按拼音、笔画、偏旁部首等排序的目录（索引）快速查找到需要的字。

索引分单列索引和组合索引。单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。组合索引，即一个索引包含多个列。创建索引时，你需要确保该索引是应用在 SQL 查询语句的条件(一般作为 WHERE 子句的条件)。实际上，索引也是一张表，该表保存了主键与索引字段，并指向实体表的记录。

上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。建立索引会占用磁盘空间的索引文件。

**创建索引**

```sql
CREATE INDEX index_name ON table_name;
```



**单列索引**：单列索引基于单一的字段创建，其基本语法如下所示：

```sql
CREATE INDEX index_name ON table_name (column_name);
```



**唯一索引**：唯一索引不止用于提升查询性能，还用于保证数据完整性。唯一索引不允许向表中插入任何重复值。其基本语法如下所示：

```sql
CREATE UNIQUE INDEX index_name on table_name (column_name);
```

创建唯一索引的目的不是为了提高访问速度，而只是为了避免数据出现重复。唯一索引可以有多个但索引列的值必须唯一，索引列的值允许有空值。如果能确定某个数据列将只包含彼此各不相同的值，在为这个数据列创建索引的时候就应该使用关键字UNIQUE把它定义为一个唯一索引。



**聚簇索引**：聚簇索引在表中两个或更多的列的基础上建立。其基本语法如下所示：

```sql
CREATE INDEX index_name on table_name (column1, column2);
```

创建单列索引还是聚簇索引，要看每次查询中，哪些列在作为过滤条件的 WHERE 子句中最常出现。如果只需要一列，那么就应当创建单列索引。如果作为过滤条件的 WHERE 子句用到了两个或者更多的列，那么聚簇索引就是最好的选择。



**隐式索引**：隐式索引由数据库服务器在创建某些对象的时候自动生成。例如，对于主键约束和唯一约束，数据库服务器就会自动创建索引。



**DROP INDEX 命令：**

索引可以用 SQL **DROP** 命令删除。删除索引时应当特别小心，数据库的性能可能会因此而降低或者提高。

```sql
DROP INDEX table_name.index_name;
```



**什么时候应当避免使用索引？**

尽管创建索引的目的是提升数据库的性能，但是还是有一些情况应当避免使用索引。下面几条指导原则给出了何时应当重新考虑是否使用索引：

- 小的数据表不应当使用索引；
- 需要频繁进行大批量的更新或者插入操作的表；
- 如果列中包含大数或者 NULL 值，不宜创建索引；
- 频繁操作的列不宜创建索引。

### EXPLAIN关键词

在日常工作中，我们会有时会开慢查询去记录一些执行时间比较久的SQL语句，找出这些SQL语句并不意味着完事了，些时我们常常用到explain这个命令来查看一个这些SQL语句的执行计划，查看该SQL语句有没有使用上了索引，有没有做全表扫描，这都可以通过explain命令来查看。所以我们深入了解MySQL的基于开销的优化器，还可以获得很多可能被优化器考虑到的访问策略的细节，以及当运行SQL语句时哪种策略预计会被优化器采用。（QEP：sql生成一个执行计划query Execution plan）

```sql
mysql> explain select * from servers;
+----+-------------+---------+------+---------------+------+---------+------+------+-------+
| id | select_type | table   | type | possible_keys | key  | key_len | ref  | rows | Extra |
+----+-------------+---------+------+---------------+------+---------+------+------+-------+
|  1 | SIMPLE      | servers | ALL  | NULL          | NULL | NULL    | NULL |    1 | NULL  |
+----+-------------+---------+------+---------------+------+---------+------+------+-------+
1 row in set (0.03 sec)
```

expain出来的信息有10列，分别是id、select_type、table、type、possible_keys、key、key_len、ref、rows、Extra,下面对这些字段出现的可能进行解释：

一、 **id**

我的理解是SQL执行的顺序的标识,SQL从大到小的执行

1. id相同时，执行顺序由上至下
2. 如果是子查询，id的序号会递增，id值越大优先级越高，越先被执行
3. id如果相同，可以认为是一组，从上往下顺序执行；在所有组中，id值越大，优先级越高，越先执行

**二、select_type**

表示查询中每个select子句的类型

1. SIMPLE(简单SELECT,不使用UNION或子查询等)
2. PRIMARY(查询中若包含任何复杂的子部分,最外层的select被标记为PRIMARY)
3. UNION(UNION中的第二个或后面的SELECT语句)
4. DEPENDENT UNION(UNION中的第二个或后面的SELECT语句，取决于外面的查询)
5. UNION RESULT(UNION的结果)
6. SUBQUERY(子查询中的第一个SELECT)
7. DEPENDENT SUBQUERY(子查询中的第一个SELECT，取决于外面的查询)
8. DERIVED(派生表的SELECT, FROM子句的子查询)
9. UNCACHEABLE SUBQUERY(一个子查询的结果不能被缓存，必须重新评估外链接的第一行)

**三、table**

显示这一行的数据是关于哪张表的，有时不是真实的表名字,看到的是derivedx(x是个数字,我的理解是第几步执行的结果)

**四、type**

表示MySQL在表中找到所需行的方式，又称“访问类型”。

常用的类型有： **ALL, index, range, ref, eq_ref, const, system, NULL（从左到右，性能从差到好）**

1. ALL：Full Table Scan， MySQL将遍历全表以找到匹配的行
2. index: Full Index Scan，index与ALL区别为index类型只遍历索引树
3. range:只检索给定范围的行，使用一个索引来选择行
4. ref: 表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值
5. eq_ref: 类似ref，区别就在使用的索引是唯一索引，对于每个索引键值，表中只有一条记录匹配，简单来说，就是多表连接中使用primary key或者 unique key作为关联条件
6. const、system: 当MySQL对查询某部分进行优化，并转换为一个常量时，使用这些类型访问。如将主键置于where列表中，MySQL就能将该查询转换为一个常量,system是const类型的特例，当查询的表只有一行的情况下，使用system
7. NULL: MySQL在优化过程中分解语句，执行时甚至不用访问表或索引，例如从一个索引列里选取最小值可以通过单独索引查找完成。

**五、possible_keys**

**指出MySQL能使用哪个索引在表中找到记录，查询涉及到的字段上若存在索引，则该索引将被列出，但不一定被查询使用**

该列完全独立于EXPLAIN输出所示的表的次序。这意味着在possible_keys中的某些键实际上不能按生成的表次序使用。
如果该列是NULL，则没有相关的索引。在这种情况下，可以通过检查WHERE子句看是否它引用某些列或适合索引的列来提高你的查询性能。如果是这样，创造一个适当的索引并且再次用EXPLAIN检查查询。

**六、Key**

**key列显示MySQL实际决定使用的键（索引）**

如果没有选择索引，键是NULL。要想强制MySQL使用或忽视possible_keys列中的索引，在查询中使用FORCE INDEX、USE INDEX或者IGNORE INDEX。

**六、Key**

**key列显示MySQL实际决定使用的键（索引）**

如果没有选择索引，键是NULL。要想强制MySQL使用或忽视possible_keys列中的索引，在查询中使用FORCE INDEX、USE INDEX或者IGNORE INDEX。

**七、key_len**

***\*表示索引中使用的字节数，可通过该列计算查询中使用的索引的长度（key_len显示的值为索引字段的最大可能长度，并非实际使用长度，即key_len是根据表定义计算而得，不是通过表内检索出的）\****

不损失精确性的情况下，长度越短越好 

**八、ref**

**表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值**。

**九、rows**

 **表示MySQL根据表统计信息及索引选用情况，估算的找到所需的记录所需要读取的行数**

**十、Extra**

**该列包含MySQL解决查询的详细信息,有以下几种情况：**

1. Using where:列数据是从仅仅使用了索引中的信息而没有读取实际的行动的表返回的，这发生在对表的全部的请求列都是同一个索引的部分的时候，表示mysql服务器将在存储引擎检索行后再进行过滤
2. Using temporary：表示MySQL需要使用临时表来存储结果集，常见于排序和分组查询
3. Using filesort：MySQL中无法利用索引完成的排序操作称为“文件排序”
4. Using join buffer：改值强调了在获取连接条件时没有使用索引，并且需要连接缓冲区来存储中间结果。如果出现了这个值，那应该注意，根据查询的具体情况可能需要添加索引来改进能。
5. Impossible where：这个值强调了where语句会导致没有符合条件的行。
6. Select tables optimized away：这个值意味着仅通过使用索引，优化器可能仅从聚合函数结果中返回一行

**总结：**
• EXPLAIN不会告诉你关于触发器、存储过程的信息或用户自定义函数对查询的影响情况
• EXPLAIN不考虑各种Cache
• EXPLAIN不能显示MySQL在执行查询时所作的优化工作
• 部分统计信息是估算的，并非精确值
• EXPALIN只能解释SELECT操作，其他操作要重写为SELECT后查看执行计划。**



### NVL关键词

**NVL(expr1, expr2)** : In SQL, NVL() converts a null value to an actual value. Data types that can be used are date, character and number. Data type must match with each other i.e. expr1 and expr2 must of same data type.
**Syntax –**

```
NVL (expr1, expr2)
```

**expr1** is the source value or expression that may contain a null.
**expr2** is the target value for converting the null.

```sql
SELECT  salary, NVL(commission_pct, 0),
    (salary*12) + (salary*12*NVL(commission_pct, 0))
      annual_salary FROM employees;
```

NVL(commission_pct, 0) 如果commission_pct字段中出现了空值null，则把空值转化为0。



### COALESCE关键词

**COALESCE()** :返回列表中第一个非null的值，如果列表中所有的值都是null，则返回null。

**Syntax –**

```
COALESCE (expr_1, expr_2, ... expr_n)
```