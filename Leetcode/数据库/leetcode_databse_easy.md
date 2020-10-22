#### Easy：

##### [175. 组合两个表](https://leetcode-cn.com/problems/combine-two-tables/)

表1: Person

| 列名      | 类型    |
| --------- | ------- |
| PersonId  | int     |
| FirstName | varchar |
| LastName  | varchar |

PersonId 是上表主键

表2: Address


| 列名      | 类型    |
| --------- | ------- |
| AddressId | int     |
| PersonId  | int     |
| City      | varchar |
| State     | varchar |

AddressId 是上表主键


编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：

FirstName, LastName, City, State

```mysql
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
```

因为根据题目要求 不论是否person有没有 都要有person的相关信息 因此为外连接 



##### [176. 第二高的薪水](https://leetcode-cn.com/problems/second-highest-salary/)

编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

| Id   | Salary |
| ---- | ------ |
| 1    | 100    |
| 2    | 200    |
| 3    | 300    |

例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

| SecondHighestSalary |
| ------------------- |
| 200                 |

Using the OFF SET in the LIMIT query

The **OFFSET** value is also most often used together with the LIMIT keyword. The OFF SET value allows us to specify which row to start from retrieving data

```mysql
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```

IFNULL 关键字 判断 如果前一个为空 则返回结果为后一个

OFFSET关键字 定义从第几个结果开始返回



##### [181. 超过经理收入的员工](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/)

Employee 表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。

| Id   | Name  | Salary | ManagerId |
| ---- | ----- | ------ | --------- |
| 1    | Joe   | 70000  | 3         |
| 2    | Henry | 80000  | 4         |
| 3    | Sam   | 60000  | NULL      |
| 4    | Max   | 90000  | NULL      |

给定 Employee 表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。

```mysql
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
```





##### [182. 查找重复的电子邮箱](https://leetcode-cn.com/problems/duplicate-emails/)

编写一个 SQL 查询，查找 `Person` 表中所有重复的电子邮箱。

| Id   | Email   |
| ---- | ------- |
| 1    | a@b.com |
| 2    | c@d.com |
| 3    | a@b.com |

```mysql
select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
```



##### [183. 从不订购的客户](https://leetcode-cn.com/problems/customers-who-never-order/)

某网站包含两个表，`Customers` 表和 `Orders` 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

Customers 表：

| Id   | Name  |
| ---- | ----- |
| 1    | Joe   |
| 2    | Henry |
| 3    | Sam   |
| 4    | Max   |



Orders 表：

| Id   | CustomerId |
| ---- | ---------- |
| 1    | 3          |
| 2    | 1          |

```mysql
select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);
```



##### [196. 删除重复的电子邮箱](https://leetcode-cn.com/problems/delete-duplicate-emails/)

编写一个 SQL 查询，来删除 `Person` 表中所有重复的电子邮箱，重复的邮箱里只保留 **Id** *最小* 的那个。

| Id   | Email            |
| ---- | ---------------- |
| 1    | john@example.com |
| 2    | bob@example.com  |
| 3    | john@example.com |

例如，在运行你的查询语句之后，上面的 `Person` 表应返回以下几行:

| Id   | Email            |
| ---- | ---------------- |
| 1    | john@example.com |
| 2    | bob@example.com  |



```mysql
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
```



##### [197. 上升的温度](https://leetcode-cn.com/problems/rising-temperature/)

给定一个 `Weather` 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。

| Id(INT) | RecordDate(DATE) | Temperature(INT) |
| ------- | ---------------- | ---------------- |
| 1       | 2015-01-01       | 10               |
| 2       | 2015-01-02       | 25               |
| 3       | 2015-01-03       | 20               |
| 4       | 2015-01-04       | 30               |

```mysql
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.RecordDate, w.RecordDate) = 1
        AND weather.Temperature > w.Temperature
```



##### [511. 游戏I:第一次登陆日期](https://leetcode-cn.com/problems/game-play-analysis-i/)

活动表 `Activity`：

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
表的主键是 (player_id, event_date)。
这张表展示了一些游戏玩家在游戏平台上的行为活动。
每行数据记录了一名玩家在退出平台之前，当天使用同一台设备登录平台后打开的游戏的数目（可能是 0 个）。
```

写一条 SQL 查询语句获取每位玩家 **第一次登陆平台的日期**。

```
Activity 表：
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result 表：
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
```

###### Answer

```sql
select player_id, min(event_date) `first_login` from Activity group by player_id order by player_id asc
```



##### [512. 游戏II：第一次登陆的时间](https://leetcode-cn.com/problems/game-play-analysis-ii/)

Table: `Activity`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) 是这个表的两个主键
这个表显示的是某些游戏玩家的游戏活动情况
每一行是在某天使用某个设备登出之前登录并玩多个游戏（可能为0）的玩家的记录
```

请编写一个 SQL 查询，描述每一个玩家首次登陆的设备名称

查询结果格式在以下示例中：

```
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+-----------+
| player_id | device_id |
+-----------+-----------+
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |
+-----------+-----------+
```

###### Answer:

```sql
select a.player_id ,a.device_id from Activity a where (a.player_id ,a.event_date) in 
(select player_id,min(event_date) as first_login from Activity group by player_id)
```

为什么下面的sql命令是不对的：

```sql
select player_id ,device_id from ( select player_id,device_id,min(event_date) from Activity group by player_id ) s
```

因为使用GROUP之后，SELECT之中只能出现聚合字段或者聚合函数。device_id出现就是错的。

##### [577. 员工奖金](https://leetcode-cn.com/problems/employee-bonus/)

选出所有 bonus < 1000 的员工的 name 及其 bonus。

`Employee` 表单

```sql
+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId 是这张表单的主关键字
```

`Bonus` 表单

```
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId 是这张表单的主关键字
```

输出示例：

```sql
+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+
```



```sql
["EmpId", "Name", "Supervisor", "Salary", "EmpId", "Bonus"], 
[[3, "Brad", null, 4000, null, null], 
 [1, "John", 3, 1000, null, null], 
 [2, "Dan", 3, 2000, 2, 500], 
 [4, "Thomas", 3, 4000, 4, 2000]]}
```

######  Answer:

```sql
select e.name, b.bonus
from Employee e left join Bonus b
on e.empId = b.empId
where b.bonus is null or b.bonus < 1000
```



##### [580. 统计各专业学生人数](https://leetcode-cn.com/problems/count-student-number-in-departments/)

一所大学有 2 个数据表，分别是 student 和 department ，这两个表保存着每个专业的学生数据和院系数据。

写一个查询语句，查询 department 表中每个专业的学生人数 （即使没有学生的专业也需列出）。

将你的查询结果按照学生人数降序排列。 如果有两个或两个以上专业有相同的学生数目，将这些部门按照部门名字的字典序从小到大排列。

**student** 表格如下：

| Column Name  | Type      |
| ------------ | --------- |
| student_id   | Integer   |
| student_name | String    |
| gender       | Character |
| dept_id      | Integer   |

其中， student_id 是学生的学号， student_name 是学生的姓名， gender 是学生的性别， dept_id 是学生所属专业的专业编号。

**department**表格如下：

| Column Name | Type    |
| ----------- | ------- |
| dept_id     | Integer |
| dept_name   | String  |

dept_id 是专业编号， dept_name 是专业名字。

这里是一个示例输入：
**student** 表格：

| student_id | student_name | gender | dept_id |
| ---------- | ------------ | ------ | ------- |
| 1          | Jack         | M      | 1       |
| 2          | Jane         | F      | 1       |
| 3          | Mark         | M      | 2       |

**department** 表格：

| dept_id | dept_name   |
| ------- | ----------- |
| 1       | Engineering |
| 2       | Science     |
| 3       | Law         |

示例输出为：

| dept_name   | student_number |
| ----------- | -------------- |
| Engineering | 2              |
| Science     | 1              |
| Law         | 0              |

###### Answer：

```sql
--运行时间：650ms
--击败30%

select dept_name, case when total is null then 0 else total end as student_number
from department d left join 
    (select dept_id, count(1) total
    from student
    group by dept_id) b
on d.dept_id = b.dept_id
order by student_number desc
```



##### [584. 寻找用户推荐人](https://leetcode-cn.com/problems/find-customer-referee/)

给定表 `customer` ，里面保存了所有客户信息和他们的推荐人。

```sql
+------+------+-----------+
| id   | name | referee_id|
+------+------+-----------+
|    1 | Will |      NULL |
|    2 | Jane |      NULL |
|    3 | Alex |         2 |
|    4 | Bill |      NULL |
|    5 | Zack |         1 |
|    6 | Mark |         2 |
+------+------+-----------+
```

写一个查询语句，返回一个编号列表，列表中编号的推荐人的编号都 **不是** 2。

对于上面的示例数据，结果为：

```sql
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```



###### Answer:

```sql
-- run time: 450ms
-- beat 15% competitors

SELECT name
FROM customer
where customer.referee_id <> 2 or customer.referee_id is null
```



##### [586. 订单最多的客户](https://leetcode-cn.com/problems/customer-placing-the-largest-number-of-orders/)

在表 **orders** 中找到订单数最多客户对应的 **customer_number** 。

数据保证订单数最多的顾客恰好只有一位。

表 **orders** 定义如下：

```
| Column            | Type      |
|-------------------|-----------|
| order_number (PK) | int       |
| customer_number   | int       |
| order_date        | date      |
| required_date     | date      |
| shipped_date      | date      |
| status            | char(15)  |
| comment           | char(200) |
```

**样例输入**

```
| order_number | customer_number | order_date | required_date | shipped_date | status | comment |
|--------------|-----------------|------------|---------------|--------------|--------|---------|
| 1            | 1               | 2017-04-09 | 2017-04-13    | 2017-04-12   | Closed |         |
| 2            | 2               | 2017-04-15 | 2017-04-20    | 2017-04-18   | Closed |         |
| 3            | 3               | 2017-04-16 | 2017-04-25    | 2017-04-20   | Closed |         |
| 4            | 3               | 2017-04-18 | 2017-04-28    | 2017-04-25   | Closed |         |
```

**样例输出**

```
| customer_number |
|-----------------|
| 3               |
```

###### Answer:

```sql
select customer_number
from (
    select customer_number, count(1) cnt
    from orders
    group by customer_number) a 
order by cnt desc
limit 1
```



##### [595. 大的国家](https://leetcode-cn.com/problems/big-countries/)

这里有张 `World` 表

```
+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
```

如果一个国家的面积超过300万平方公里，或者人口超过2500万，那么这个国家就是大国家。

编写一个SQL查询，输出表中所有大国家的名称、人口和面积。

例如，根据上表，我们应该输出:

```
+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+
```

###### Answer:

```sql
select name, population, area
from World
where area > 3000000 or population > 25000000
```



##### [596. 超过5名学生的课](https://leetcode-cn.com/problems/classes-more-than-5-students/)

有一个`courses` 表 ，有: **student (学生)** 和 **class (课程)**。

请列出所有超过或等于5名学生的课。

例如,表:

```sql
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
```

应该输出:

```
+---------+
| class   |
+---------+
| Math    |
+---------+
```

###### Answer：

```sql
select class
from (
    select class, count(1) cnt from (
        select distinct student, class from courses) a
    group by class
) b
where cnt > 4
```



##### [597. 好友申请 I ：总体通过率](https://leetcode-cn.com/problems/friend-requests-i-overall-acceptance-rate/)

在 Facebook 或者 Twitter 这样的社交应用中，人们经常会发好友申请也会收到其他人的好友申请。

现在给如下两个表：

表： `friend_request`

```
| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |
```

表： `request_accepted`

```
| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |
```

写一个查询语句，求出好友申请的通过率，用 2 位小数表示。通过率由接受好友申请的数目除以申请总数。

对于上面的样例数据，你的查询语句应该返回如下结果。

```
|accept_rate|
|-----------|
|       0.80|
```

注意:

* 通过的好友申请不一定都在表 friend_request 中。在这种情况下，你只需要统计总的被通过的申请数（不管它们在不在原来的申请中），并将它除以申请总数，得到通过率
* 一个好友申请发送者有可能会给接受者发几条好友申请，也有可能一个好友申请会被通过好几次。这种情况下，重复的好友申请只统计一次。
* 如果一个好友申请都没有，通过率为 0.00 。

###### Answer:

```sql
select case when round(all_accepted/all_request,2) is null then 0.00 else round(all_accepted/all_request,2) end accept_rate
from (select count(*) all_request 
      from (select distinct sender_id,send_to_id from friend_request) new_friend_request) all_request
     ,(select count(*) all_accepted
from (select distinct requester_id,accepter_id from request_accepted) new_request_accepted) all_accepted

```



##### [603. 连续空余座位](https://leetcode-cn.com/problems/consecutive-available-seats/)

几个朋友来到电影院的售票处，准备预约连续空余座位。

你能利用表 cinema ，帮他们写一个查询语句，获取所有空余座位，并将它们按照 seat_id 排序后返回吗？

```
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
```

对于如上样例，你的查询语句应该返回如下结果。

```
| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
```

seat_id 字段是一个自增的整数，free 字段是布尔类型（'1' 表示空余， '0' 表示已被占据）。
连续空余座位的定义是大于等于 2 个连续空余的座位。

###### Answer:

连续两个就可以使用自连接

```
select distinct(t1.seat_id)
from cinema t1 join cinema t2
on abs(t1.seat_id - t2.seat_id) = 1 and t1.free = true and t2.free = true
order by t1.seat_id
```



##### [607. 销售员](https://leetcode-cn.com/problems/sales-person/)

给定 3 个表： salesperson， company， orders。
输出所有表 salesperson 中，没有向公司 'RED' 销售任何东西的销售员。

**输入**

表： `salesperson`

```
+----------+------+--------+-----------------+-----------+
| sales_id | name | salary | commission_rate | hire_date |
+----------+------+--------+-----------------+-----------+
|   1      | John | 100000 |     6           | 4/1/2006  |
|   2      | Amy  | 120000 |     5           | 5/1/2010  |
|   3      | Mark | 65000  |     12          | 12/25/2008|
|   4      | Pam  | 25000  |     25          | 1/1/2005  |
|   5      | Alex | 50000  |     10          | 2/3/2007  |
+----------+------+--------+-----------------+-----------+
```

表 `salesperson` 存储了所有销售员的信息。每个销售员都有一个销售员编号 **sales_id** 和他的名字 **name** 。

表： `company`

```
+---------+--------+------------+
| com_id  |  name  |    city    |
+---------+--------+------------+
|   1     |  RED   |   Boston   |
|   2     | ORANGE |   New York |
|   3     | YELLOW |   Boston   |
|   4     | GREEN  |   Austin   |
+---------+--------+------------+
```

表 `company` 存储了所有公司的信息。每个公司都有一个公司编号 **com_id** 和它的名字 **name** 。

表： `orders`

```
+----------+------------+---------+----------+--------+
| order_id | order_date | com_id  | sales_id | amount |
+----------+------------+---------+----------+--------+
| 1        |   1/1/2014 |    3    |    4     | 100000 |
| 2        |   2/1/2014 |    4    |    5     | 5000   |
| 3        |   3/1/2014 |    1    |    1     | 50000  |
| 4        |   4/1/2014 |    1    |    4     | 25000  |
+----------+----------+---------+----------+--------+
```

表 `orders` 存储了所有的销售数据，包括销售员编号 **sales_id** 和公司编号 **com_id** 。

**输出**

```
+------+
| name | 
+------+
| Amy  | 
| Mark | 
| Alex |
+------+
```

###### Answer:

```sql
select name
from salesperson s
where s.sales_id not in 
(select orders.sales_id
from orders, company
where orders.com_id = company.com_id and company.name = "RED")
```





##### [610. 判断三角形](https://leetcode-cn.com/problems/triangle-judgement/)

一个小学生 Tim 的作业是判断三条线段是否能形成一个三角形。

然而，这个作业非常繁重，因为有几百组线段需要判断。

假设表 triangle 保存了所有三条线段的三元组 x, y, z ，你能帮 Tim 写一个查询语句，来判断每个三元组是否可以组成一个三角形吗？

```
| x  | y  | z  |
|----|----|----|
| 13 | 15 | 30 |
| 10 | 20 | 15 |
```

对于如上样例数据，你的查询语句应该返回如下结果：

```sql
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
```

###### Answer:

```sql
SELECT t.x, t.y, t.z,
CASE WHEN  t.x + t.y > t.z and t.x + t.z > t.y and t.y + t.z > t.x then "Yes"
ELSE "No"
END AS triangle
FROM triangle t
```



##### [619. 只出现一次的最大数字](https://leetcode-cn.com/problems/biggest-single-number/)

表 `my_numbers` 的 **num** 字段包含很多数字，其中包括很多重复的数字。

你能写一个 SQL 查询语句，找到只出现过一次的数字中，最大的一个数字吗？

###### Answer：

```sql
SELECT
    MAX(num) AS num
FROM
    (SELECT
        num
    FROM
        my_numbers
    GROUP BY num
    HAVING COUNT(num) = 1) AS t
```



##### [620. 有趣的电影](https://leetcode-cn.com/problems/not-boring-movies/)

某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个 LED显示板做电影推荐，上面公布着影评和相关电影描述。

作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。

例如，下表 `cinema`:

```
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
```

对于上面的例子，则正确的输出是为：

```
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
```

###### Answer:

```
select *
from cinema
where mod(id, 2) = 1 and description != 'boring'
order by rating DESC
```



##### [627. 交换工资](https://leetcode-cn.com/problems/swap-salary/)

给定一个 salary 表，如下所示，有 m = 男性 和 f = 女性 的值。交换所有的 f 和 m 值（例如，将所有 f 值更改为 m，反之亦然）。要求只使用一个更新（Update）语句，并且没有中间的临时表。

注意，您必只能写一个 Update 语句，请不要编写任何 Select 语句。

```
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
```

运行你所编写的更新语句之后，将会得到以下表:

```
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
```

###### Answer:

```sql
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
```



##### [1050. 合作过至少三次的演员和导演](https://leetcode-cn.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)

`ActorDirector` 表：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp 是这张表的主键.
```

写一条SQL查询语句获取合作过至少三次的演员和导演的 id 对 `(actor_id, director_id)`

**示例：**

```
ActorDirector 表：
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+

Result 表：
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
唯一的 id 对是 (1, 1)，他们恰好合作了 3 次。
```

###### Answer:

```
select actor_id, director_id
from
(select actor_id, director_id, count(1) cnt
from ActorDirector
group by actor_id, director_id) t1
where cnt > 2
```



##### [1068. 产品销售分析 I](https://leetcode-cn.com/problems/product-sales-analysis-i/)

销售表 `Sales`：

```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) 是销售表 Sales 的主键.
product_id 是产品表 Product 的外键.
注意: price 表示每单位价格
```

产品表 `Product`：

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id 是表的主键.
```

写一条SQL 查询语句获取产品表 Product 中所有的 产品名称 product name 以及 该产品在 Sales 表中相对应的 上市年份 year 和 价格 price。

```
Sales 表：
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product 表：
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Result 表：
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
```

###### Answer:

```sql
select Product.product_name, Sales.year, Sales.price
from Sales, Product
where Sales.product_id = Product.product_id
```



##### [1069. 产品销售分析 II](https://leetcode-cn.com/problems/product-sales-analysis-ii/)

销售表：`Sales`

```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
sale_id 是这个表的主键。
product_id 是 Product 表的外键。
```

产品表：`Product`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id 是这个表的主键。
```

编写一个 SQL 查询，按产品 id `product_id` 来统计每个产品的销售总量。

```
Sales 表：
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product 表：
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Result 表：
+--------------+----------------+
| product_id   | total_quantity |
+--------------+----------------+
| 100          | 22             |
| 200          | 15             |
+--------------+----------------+
```

###### Answer:

```
select product_id, sum(quantity) total_quantity
from Sales
group by product_id
```





##### [1075. 项目员工 I](https://leetcode-cn.com/problems/project-employees-i/)

项目表 `Project`： 

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
主键为 (project_id, employee_id)。
employee_id 是员工表 Employee 表的外键。
```

员工表 `Employee`：

```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
主键是 employee_id。
```

请写一个 SQL 语句，查询每一个项目中员工的 **平均** 工作年限，**精确到小数点后两位**。

查询结果的格式如下：

```
Project 表：
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee 表：
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Result 表：
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50
```

###### Answer:

```sql
select p.project_id, round(avg(e.experience_years),2) as average_years
from Project p, Employee e
where p.employee_id = e.employee_id
group by p.project_id
```



##### [1076. 项目员工II](https://leetcode-cn.com/problems/project-employees-ii/)

Table: `Project`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
主键为 (project_id, employee_id)。
employee_id 是员工表 Employee 表的外键。
```

Table: `Employee`

```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
主键是 employee_id。
```

编写一个SQL查询，报告所有雇员最多的项目。可能有多个项目同时排名第一

查询结果格式如下所示：

```
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Result table:
+-------------+
| project_id  |
+-------------+
| 1           |
+-------------+
第一个项目有3名员工，第二个项目有2名员工。
```

###### Answer:

```sql
select t2.project_id
from 
(
select t.project_id, dense_rank() over (order by cnt desc) as dese_rank
from
(
select p1.project_id, count(1) cnt
from Project p1
group by p1.project_id) t) t2
where dese_rank = 1
```

