#### Hard：

##### [185. 部门工资前三高的所有员工](https://leetcode-cn.com/problems/department-top-three-salaries/)

`Employee` 表包含所有员工信息，每个员工有其对应的工号 `Id`，姓名 `Name`，工资 `Salary` 和部门编号 `DepartmentId` 。

| Id   | Name  | Salary | DepartmentId |
| ---- | ----- | ------ | ------------ |
| 1    | Joe   | 85000  | 1            |
| 2    | Henry | 80000  | 2            |
| 3    | Sam   | 60000  | 2            |
| 4    | Max   | 90000  | 1            |
| 5    | Janet | 69000  | 1            |
| 6    | Randy | 85000  | 1            |
| 7    | Will  | 70000  | 1            |

`Department` 表包含公司所有部门的信息。

| Id   | Name  |
| ---- | ----- |
| 1    | IT    |
| 2    | Sales |

编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。例如，根据上述给定的表，查询结果应返回：

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |

IT 部门中，Max 获得了最高的工资，Randy 和 Joe 都拿到了第二高的工资，Will 的工资排第三。销售部门（Sales）只有两名员工，Henry 的工资最高，Sam 的工资排第二。



```mysql
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;

```





##### [262. 行程和用户](https://leetcode-cn.com/problems/trips-and-users/)

Trips 表中存所有出租车的行程信息。每段行程有唯一键 Id，Client_Id 和 Driver_Id 是 Users 表中 Users_Id 的外键。Status 是枚举类型，枚举成员为 (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’)。

| Id   | Client_Id | Driver_Id | City_Id | Status              | Request_at |
| ---- | --------- | --------- | ------- | ------------------- | ---------- |
| 1    | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2    | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3    | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4    | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5    | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6    | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7    | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8    | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9    | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10   | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |



Users 表存所有用户。每个用户有唯一键 Users_Id。Banned 表示这个用户是否被禁止，Role 则是一个表示（‘client’, ‘driver’, ‘partner’）的枚举类型。

| Users_Id | Banned | Role   |
| -------- | ------ | ------ |
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |

写一段 SQL 语句查出 2013年10月1日 至 2013年10月3日 期间非禁止用户的取消率。基于上表，你的 SQL 语句应返回如下结果，取消率（Cancellation Rate）保留两位小数。

| Day        | Cancellation Rate |
| ---------- | ----------------- |
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |



```mysql
SELECT
    request_at 'Day', round(avg(Status!='completed'), 2) 'Cancellation Rate'
FROM 
    trips t JOIN users u1 ON (t.client_id = u1.users_id AND u1.banned = 'No')
    JOIN users u2 ON (t.driver_id = u2.users_id AND u2.banned = 'No')
WHERE	
    request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    request_at
```







##### [569. 薪水中位数](https://leetcode-cn.com/problems/median-employee-salary/)

`Employee` 表包含所有员工。`Employee` 表有三列：员工Id，公司名和薪水。

```
+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+
```

请编写SQL查询来查找每个公司的薪水中位数。挑战点：你是否可以在不使用任何内置的SQL函数的情况下解决此问题。

```
+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|5    | A          | 451    |
|6    | A          | 513    |
|12   | B          | 234    |
|9    | B          | 1154   |
|14   | C          | 2645   |
+-----+------------+--------+
```

######  Answer:

不使用窗口函数

```sql
select b.id,b.company,b.salary
from (
    -- 1. 按 company 分组排序，记为 `rk`
    select id,company,salary,
    case @com when company then @rk:=@rk+1 else @rk:=1 end rk, 
    --最开始的@rk变量为0，@com变量为“”，如果当前@com变量和当前的company不相同，设置@rk变量为1
    --如果@com变量和company字段相同，则把@rk变量+1
    --当前字段输出rk变量
    @com:=company
    --@com变量设置为当前company字段值
    from employee,(select @rk:=0, @com:='') a --初始化两个变量@rk和@com
    order by company,salary) b
left join 
    (-- 2. 计算各 company 的记录数除以2，记为 `cnt`
    select company,count(1)/2 cnt from employee group by company) c
on b.company=c.company
-- 4. 找出符合中位数要求的记录
where b.rk in (cnt+0.5,cnt+1,cnt); --同时符合奇数和偶数情况
```

窗口函数

```sql
select id, Company, salary
from
(
    select Id, Company, row_number()over(partition by Company order by Salary, Id) as rn, cnt, salary
    from 
    (
        select a.*, b.cnt
        from Employee a
        join 
        (
            select  Company, count(id) as cnt from Employee 
            group by Company
        )b
        on a.Company = b.Company 
    )a
)a
where rn >= cnt/2 and rn <= cnt/2 + 1 

```





##### [571. 给定数字的频率查询中位数](https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers/)

`Numbers` 表保存数字的值及其频率。

```
+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
```

在此表中，数字为 `0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3`，所以中位数是 `(0 + 0) / 2 = 0`。

```
+--------+
| median |
+--------|
| 0.0000 |
+--------+
```

###### Answer:

```sql
--执行耗时：850～900ms
--耗时较长

select
avg(t.number) as median
from
(
select
n1.number,
n1.frequency,
(select sum(frequency) from numbers n2 where n2.number<=n1.number) as asc_frequency,
(select sum(frequency) from numbers n3 where n3.number>=n1.number) as desc_frequency
from numbers n1
) t
where t.asc_frequency>= (select sum(frequency) from numbers)/2
and t.desc_frequency>= (select sum(frequency) from numbers)/2

```

窗口函数

```sql
select 
    avg(cast(number as float)) median
from 
    (
        select 
            Number,
            Frequency,
            sum(Frequency) over(order by Number) - Frequency prev_sum,
            sum(Frequency) over(order by Number) curr_sum
        from Numbers
    ) t1,
    (
        select 
            sum(Frequency) total_sum
        from Numbers
    ) t2
where 
    t1.prev_sum <= (cast(t2.total_sum as float) / 2) and 
    t1.curr_sum >= (cast(t2.total_sum as float) / 2)
```









##### [579. 查询员工的累计薪水](https://leetcode-cn.com/problems/find-cumulative-salary-of-an-employee/)

Employee 表保存了一年内的薪水信息。

请你编写 SQL 语句，对于每个员工，查询他除最近一个月（即最大月）之外，剩下每个月的近三个月的累计薪水（不足三个月也要计算）。

结果请按 Id 升序，然后按 Month 降序显示。

**示例：**
**输入：**

```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
```

**输出：**

```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
```



###### Answer:

```sql
--用时360ms
--击败20%

select Id, Month, sum(month_total) over (partition by Id order by Month rows between 2 preceding and current row) Salary
from 
  (select Id, Month, Sum(Salary) over(partition by Id, Month) month_total
  from Employee 
  where (Employee.Id, Employee.Month) not in (select id,max(month)
  from Employee
  group by id)
  order by Id, Month) b
order by Id, Month desc
 
```



##### [601. 体育馆的人流量](https://leetcode-cn.com/problems/human-traffic-of-stadium/)

X 市建了一个新的体育馆，每日人流量信息被记录在这三列信息中：序号 (id)、日期 (visit_date)、 人流量 (people)。

请编写一个查询语句，找出人流量的高峰期。高峰期时，至少连续三行记录中的人流量不少于100。

例如，表 stadium：

```
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
```

对于上面的示例数据，输出为：

```
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
```

###### Answer:

方法一：

```sql
SELECT id, visit_date, people
FROM (
	SELECT r1.*, @flag := if((r1.countt >= 3 OR @flag = 1) AND r1.countt != 0, 1, 0) AS flag
	FROM (
		SELECT s.*, @count := if(s.people >= 100, @count + 1, 0) AS `countt`
		FROM stadium s, (SELECT @count := 0) b
	) r1, (SELECT @flag := 0) c
	ORDER BY id DESC
) result
WHERE flag = 1 ORDER BY id;
```

方法二：

```sql
--使用变量，分步骤计算

select id, visit_date, people
from 
(
select *
from
(
select 
t1.*, 
case when cnt = 1 and @y = 0 then @x := @x +1 
	 when cnt = 1 and @y = 1 then @x := @x else 0 end t1,
case when cnt = 1 and @y = 0 then @y := 1
     when cnt = 0 then @y := 0
     else 0 end tt2      
from
(
SELECT *, case when people > 99 then 1 else 0 end cnt
from stadium) t1, (select @x:= 0, @y:= 0) a
) temp1,
(
select t1_2, count(1) t2_2
from (
    select 
    t1_2.*, 
    case when cnt_2 = 1 and @y_2 = 0 then @x_2 := @x_2 +1 
        when cnt_2 = 1 and @y_2 = 1 then @x_2 := @x_2 else 0 end t1_2,
    case when cnt_2 = 1 and @y_2 = 0 then @y_2 := 1
        when cnt_2 = 0 then @y_2 := 0
        else 0 end tt2_2      
    from
    (
    SELECT *, case when people > 99 then 1 else 0 end cnt_2
    from stadium) t1_2, (select @x_2:= 0, @y_2:= 0) a_2 ) b_2
where t1_2 <> 0
group by t1_2
order by id
) temp2
where temp1.t1 = temp2.t1_2 ) temp_all
where t2_2 > 2
```



###### [615. 平均工资：部门与公司比较](https://leetcode-cn.com/problems/average-salary-departments-vs-company/)

给如下两个表，写一个查询语句，求出在每一个工资发放日，每个部门的平均工资与公司的平均工资的比较结果 （高 / 低 / 相同）。

表： `salary`

```
| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |
```

**employee_id** 字段是表 `employee` 中 **employee_id** 字段的外键。

```
| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |
```

对于如上样例数据，结果为：

```
| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |
```

###### Answer:

```
["pay_date", "department_id", "avg(s1.amount)"],
[["2017-03-31", 1, 9000.0000], 
["2017-03-31", 2, 8000.0000], 
["2017-02-28", 1, 7000.0000], 
["2017-02-28", 2, 7000.0000]]}
```



##### [615. 平均工资：部门与公司比较](https://leetcode-cn.com/problems/average-salary-departments-vs-company/)

给如下两个表，写一个查询语句，求出在每一个工资发放日，每个部门的平均工资与公司的平均工资的比较结果 （高 / 低 / 相同）。

表： `salary`

```
| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |
```

**employee_id** 字段是表 `employee` 中 **employee_id** 字段的外键。

```
| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |
```

对于如上样例数据，结果为：

```
| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |
```



###### Answer:

```sql
select temp3.s1_pay_date as pay_month,
temp3.s1_department_id as department_id,
case when temp3.avg_comp_month = temp3.avg_month then "same"
     when temp3.avg_comp_month > temp3.avg_month then "higher"
     else "lower" end as comparison
from
(select *
from (select date_format(s1.pay_date, '%Y-%m') as s1_pay_date, e1.department_id as s1_department_id, avg(s1.amount) as avg_comp_month
from salary s1, employee e1
where s1.employee_id = e1.employee_id
group by date_format(s1.pay_date, '%Y-%m'), e1.department_id) temp1,
(select date_format(s2.pay_date, '%Y-%m') as s2_pay_date, round(avg(s2.amount),4) as avg_month
from salary s2
group by date_format(s2.pay_date, '%Y-%m')) temp2
where temp1.s1_pay_date = temp2.s2_pay_date) temp3
```



##### [618. 学生地理信息报告](https://leetcode-cn.com/problems/students-report-by-geography/)

一所美国大学有来自亚洲、欧洲和美洲的学生，他们的地理信息存放在如下 `student` 表中。

```
| name   | continent |
|--------|-----------|
| Jack   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jane   | America   |
```

写一个查询语句实现对大洲（continent）列的 透视表 操作，使得每个学生按照姓名的字母顺序依次排列在对应的大洲下面。输出的标题应依次为美洲（America）、亚洲（Asia）和欧洲（Europe）。数据保证来自美洲的学生不少于来自亚洲或者欧洲的学生。

对于样例输入，它的对应输出是：

```
| America | Asia | Europe |
|---------|------|--------|
| Jack    | Xi   | Pascal |
| Jane    |      |        |
```



###### Answer：

```sql
select America,Asia,Europe 
from(
    select row_number() over(order by name) as rn,name as America from student
    where continent='America'
) a
left join(
    select row_number() over(order by name) as rn,name as Asia from student
    where continent='Asia'
) b on a.rn=b.rn
left join(
    select row_number() over(order by name) as rn,name as Europe from student
    where continent='Europe'
) c on a.rn=c.rn
```



##### [1097. 游戏玩法分析 V](https://leetcode-cn.com/problems/game-play-analysis-v/)

`Activity` 活动记录表

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
（player_id，event_date）是此表的主键
这张表显示了某些游戏的玩家的活动情况
每一行是一个玩家的记录，他在某一天使用某个设备注销之前登录并玩了很多游戏（可能是 0）
```

我们将玩家的安装日期定义为该玩家的第一个登录日。

我们还将某个日期 X 的第 1 天留存时间定义为安装日期为 X 的玩家的数量，他们在 X 之后的一天重新登录，除以安装日期为 X 的玩家的数量，四舍五入到小数点后两位。

编写一个 SQL 查询，报告每个安装日期、当天安装游戏的玩家数量和第一天的留存时间。

查询结果格式如下所示：

```
Activity 表：
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-01 | 0            |
| 3         | 4         | 2016-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result 表：
+------------+----------+----------------+
| install_dt | installs | Day1_retention |
+------------+----------+----------------+
| 2016-03-01 | 2        | 0.50           |
| 2017-06-25 | 1        | 0.00           |
+------------+----------+----------------+
玩家 1 和 3 在 2016-03-01 安装了游戏，但只有玩家 1 在 2016-03-02 重新登录，所以 2016-03-01 的第一天留存时间是 1/2=0.50
玩家 2 在 2017-06-25 安装了游戏，但在 2017-06-26 没有重新登录，因此 2017-06-25 的第一天留存时间为 0/1=0.00
```

###### Answer:

```sql
select t3.first_date as install_dt, 
sum(case when t3.symbol = -1 then 1 else 0 end) as installs, 
round(sum(case when t3.symbol = 1 then 1 else 0 end)/sum(case when t3.symbol = -1 then 1 else 0 end),2) as Day1_retention
from 
    (select t2.first_date, 
    case when DATEDIFF(a2.event_date,t2.first_date) = 0 then -1
        when DATEDIFF(a2.event_date,t2.first_date) = 1 then 1
        else 0 end as symbol
    from Activity a2 left join 
    (select t1.player_id, t1.event_date as first_date
    from 
        (select a1.player_id, a1.event_date, dense_rank()  over (partition by a1.player_id order by a1.event_date) as rnk
        from Activity a1) t1
        where t1.rnk = 1) t2
    on a2.player_id = t2.player_id) t3
group by t3.first_date

```

