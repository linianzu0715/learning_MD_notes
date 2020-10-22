### Sample

```sql
SELECT
    distinct_id,
    getSessionStartAttr("$$session_id", "$attr") over(partition  by distinct_id  order by xwhen, xwhat) as "$$session_start_attr",  -- 我们要实现的窗口函数
    "$$session_Division_type",
    "$$if_frist_event",
    "$$if_end_event",
    "$$session_dua",
    "$$session_id" 
FROM （
    SELECT
        distinct_id, 
        "$attr",
        getsessiondivtype(sessioninfo) as "$$session_Division_type", 
        issessionstart(sessioninfo) as "$$if_frist_event", 
        issessionend(sessioninfo) as "$$if_end_event", 
        getsessiondua(sessioninfo) "$$session_dua", 
        getsessionid(sessioninfo) as "$$session_id" 
    FROM ( 
        SELECT  ##
            distinct_id, 
            "$attr",    --- 代表任意选定属性
            dynamic_session2( xwhat_id, xwhen, 1800000,  0,  -1,  -1, 1,  "$os") over(partition  by distinct_id  order by xwhen, xwhat) as sessioninfo 
        FROM
            hive.db_1b1a8746b7dd77d5.event 
        WHERE
            ds between 20200201 and 20200207))
        
```



### Over(partition by)方法介绍

开窗函数，Oracle从8.1.6开始提供分析函数，分析函数用于计算基于组的某种聚合值，它和聚合函数的不同之处是：对于每个组返回多行，而聚合函数对于每个组只返回一行。

测试用例数据:

```sql
 1 create table T2_TEMP(
 2     NAME varchar2(10) primary key,
 3     CLASS varchar2(10),
 4     SROCE NUMBER 
 5 )
 6 
 7 insert into T2_TEMP (NAME, CLASS, SROCE)
 8 values ('cfe', '2', 74);
 9 
10 insert into T2_TEMP (NAME, CLASS, SROCE)
11 values ('dss', '1', 95);
12 
13 insert into T2_TEMP (NAME, CLASS, SROCE)
14 values ('ffd', '1', 95);
15 
16 insert into T2_TEMP (NAME, CLASS, SROCE)
17 values ('fda', '1', 80);
18 
19 insert into T2_TEMP (NAME, CLASS, SROCE)
20 values ('gds', '2', 92);
21 
22 insert into T2_TEMP (NAME, CLASS, SROCE)
23 values ('gf', '3', 99);
24 
25 insert into T2_TEMP (NAME, CLASS, SROCE)
26 values ('ddd', '3', 99);
27 
28 insert into T2_TEMP (NAME, CLASS, SROCE)
29 values ('adf', '3', 45);
30 
31 insert into T2_TEMP (NAME, CLASS, SROCE)
32 values ('asdf', '3', 55);
33 
34 insert into T2_TEMP (NAME, CLASS, SROCE)
35 values ('3dd', '3', 78);
```



#### 1、over函数的写法：

　　over（partition by class order by sroce） 按照sroce排序进行累计，order by是个默认的开窗函数，按照class分区。

#### 2、开窗的窗口范围：

　　over（order by sroce range between 5 preceding and 5 following）：窗口范围为当前行数据幅度减5加5后的范围内的。

　　over（order by sroce rows between 5 preceding and 5 following）：窗口范围为当前行前后各移动5行。

#### 3、与over()函数结合的函数的介绍

##### （1）、查询每个班的第一名的成绩

```sql
SELECT * 
FROM (
  select t.name,t.class,t.sroce,rank() over(partition by t.class order by t.sroce desc) mm 
  from T2_TEMP t) 
  where mm = 1;
```

```

1 得到的结果是:
2 dss        1        95        1
3 ffd        1        95        1
4 gds        2        92        1
5 gf         3        99        1
6 ddd        3        99        1
```

注意：在求第一名成绩的时候，不能用row_number()，因为如果同班有两个并列第一，row_number()只返回一个结果。

```sql
SELECT * 
FROM (
  select t.name,t.class,t.sroce,row_number() over(partition by t.class order by t.sroce desc) mm 
  from T2_TEMP t) 
  where mm = 1;
```

```
dss      1        95        1  
gfs      2        92        1
ddd      3        99        1 
```

可以看出，本来第一名是两个人的并列，结果只显示了一个。

##### （2）、rank()和dense_rank()

将所有的都查找出来，rank可以将并列第一名的都查找出来；rank()和dense_rank()区别：rank()是跳跃排序，有两个第二名时接下来就是第四名。

求班级成绩排名：

```sql
select t.name,t.class,t.sroce,rank() over(partition by t.class order by t.sroce desc) mm from T2_TEMP t;
```

```
dss        1        95        1
ffd        1        95        1
fda        1        80        3
gds        2        92        1
cfe        2        74        2
gf         3        99        1
ddd        3        99        1
3dd        3        78        3
asdf       3        55        4
adf        3        45        5
```

dense_rank()l是连续排序，有两个第二名时仍然跟着第三名.

```sql
select t.name,t.class,t.sroce,dense_rank() over(partition by t.class order by t.sroce desc) mm from T2_TEMP t;
```

```
dss        1        95        1
ffd        1        95        1
fda        1        80        2 
gds        2        92        1
cfe        2        74        2
gf         3        99        1
ddd        3        99        1
3dd        3        78        2
asdf       3        55        3
adf        3        45        4
```

##### （3）、sum() over() 的使用

根据班级进行分数求和

```sql
select t.name,t.class,t.sroce,sum(t.sroce) over(partition by t.class order by t.sroce desc) mm from T2_TEMP t;
```

```
dss        1        95        190  --由于两个95都是第一名，所以累加时是两个第一名的相加
ffd        1        95        190 
fda        1        80        270  --第一名加上第二名的
gds        2        92        92
cfe        2        74        166
gf         3        99        198
ddd        3        99        198
3dd        3        78        276
asdf       3        55        331
adf        3        45        376
```

##### （4）、first_value() over() 和 last_value() over()的使用 

```sql
1 select t.name,t.class,t.sroce,first_value(t.sroce) over(partition by t.class order by t.sroce desc) mm from T2_TEMP t;
2 select t.name,t.class,t.sroce,last_value(t.sroce) over(partition by t.class order by t.sroce desc) mm from T2_TEMP t;
```

分别求出第一个和最后一个成绩。

##### （5）其他用法

　　count() over(partition by ... order by ...)：求分组后的总数。
　　max() over(partition by ... order by ...)：求分组后的最大值。
　　min() over(partition by ... order by ...)：求分组后的最小值。
　　avg() over(partition by ... order by ...)：求分组后的平均值。
　　lag() over(partition by ... order by ...)：取出前n行数据。　　

　　lead() over(partition by ... order by ...)：取出后n行数据。

　　ratio_to_report() over(partition by ... order by ...)：Ratio_to_report() 括号中就是分子，over() 括号中就是分母。

　　percent_rank() over(partition by ... order by ...)：

##### （6）、over partition by与group by的区别：

group by是对检索结果的保留行进行单纯分组，一般和聚合函数一起使用例如max、min、sum、avg、count等一块用。partition by虽然也具有分组功能，但同时也具有其他的高级功能。