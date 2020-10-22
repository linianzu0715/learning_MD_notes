[toc]

#### Medium：

##### [177. 第N高的薪水](https://leetcode-cn.com/problems/nth-highest-salary/)

编写一个 SQL 查询，获取 `Employee` 表中第 *n* 高的薪水（Salary）。

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
	SET N := N-1;
  RETURN (
    SELECT
        IFNULL(
        (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
            LIMIT 1 OFFSET N),
        NULL) AS SecondHighestSalary
      
  );
END
```



##### [178. 分数排名](https://leetcode-cn.com/problems/rank-scores/)

编写一个 SQL 查询来实现分数排名。

如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。

| Id   | Score |
| ---- | ----- |
| 1    | 3.50  |
| 2    | 3.65  |
| 3    | 4.00  |
| 4    | 3.85  |
| 5    | 4.00  |
| 6    | 3.65  |

例如，根据上述给定的 Scores 表，你的查询应该返回（按分数从高到低排列）：

| Score | Rank |
| ----- | ---- |
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |



最后的结果包含两个部分，第一部分是降序排列的分数，第二部分是每个分数对应的排名。

第一部分不难写：

```mysql
select a.Score as Score
from Scores a
order by a.Score DESC
```

比较难的是第二部分。假设现在给你一个分数X，如何算出它的排名Rank呢？
我们可以先提取出大于等于X的所有分数集合H，将H去重后的元素个数就是X的排名。比如你考了99分，但最高的就只有99分，那么去重之后集合H里就只有99一个元素，个数为1，因此你的Rank为1。
先提取集合H：

```mysql
select b.Score from Scores b where b.Score >= X;
```


我们要的是集合H去重之后的元素个数，因此升级为：

```mysql
select count(distinct b.Score) from Scores b where b.Score >= X as Rank;
```


而从结果的角度来看，第二部分的Rank是对应第一部分的分数来的，所以这里的X就是上面的a.Score，把两部分结合在一起为：

```mysql
select a.Score as Score,
(select count(distinct b.Score) from Scores b where b.Score >= a.Score) as 'Rank'
from Scores a
order by a.Score DESC
```

Rank关键字被占用了 用引号括起来





##### [180. 连续出现的数字](https://leetcode-cn.com/problems/consecutive-numbers/)

方法：用 DISTINCT 和 WHERE 语句
算法

连续出现的意味着相同数字的 Id 是连着的，由于这题问的是至少连续出现 3 次，我们使用 Logs 并检查是否有 3 个连续的相同数字。

```mysql
SELECT *
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;
```

| Id   | Num  | Id   | Num  | Id   | Num  |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | 1    | 2    | 1    | 3    | 1    |

注意：前两列来自 l1 ，接下来两列来自 l2 ，最后两列来自 l3 。

然后我们从上表中选择任意的 Num 获得想要的答案。同时我们需要添加关键字 DISTINCT ，因为如果一个数字连续出现超过 3 次，会返回重复元素。

```mysql
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;
```



##### [184. 部门工资最高的员工](https://leetcode-cn.com/problems/department-highest-salary/)

Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。

| Id   | Name  | Salary | DepartmentId |
| ---- | ----- | ------ | ------------ |
| 1    | Joe   | 70000  | 1            |
| 2    | Henry | 80000  | 2            |
| 3    | Sam   | 60000  | 2            |
| 4    | Max   | 90000  | 1            |


Department 表包含公司所有部门的信息。

| Id   | Name  |
| ---- | ----- |
| 1    | IT    |
| 2    | Sales |


编写一个 SQL 查询，找出每个部门工资最高的员工。例如，根据上述给定的表格，Max 在 IT 部门有最高工资，Henry 在 Sales 部门有最高工资。

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |



因为 **Employee** 表包含 *Salary* 和 *DepartmentId* 字段，我们可以以此在部门内查询最高工资。然后，我们可以把表 **Employee** 和 **Department** 连接，再在这张临时表里用 `IN` 语句查询部门名字和工资的关系。

```mysql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
```

窗口函数

```sql
select Department.Name Department, t1.Name Employee, Salary
from (
select *, dense_rank() over (partition by DepartmentId order by Salary desc) rnk
from Employee) t1 join Department
on t1.DepartmentId = Department.Id
where t1.rnk = 1

```



##### [534. 游戏III：目前玩了多少游戏](https://leetcode-cn.com/problems/game-play-analysis-iii/)

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

编写一个 SQL 查询，同时报告每组玩家和日期，以及玩家到目前为止玩了多少游戏。也就是说，在此日期之前玩家所玩的游戏总数。详细情况请查看示例。

```
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 1         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+------------+---------------------+
| player_id | event_date | games_played_so_far |
+-----------+------------+---------------------+
| 1         | 2016-03-01 | 5                   |
| 1         | 2016-05-02 | 11                  |
| 1         | 2017-06-25 | 12                  |
| 3         | 2016-03-02 | 0                   |
| 3         | 2018-07-03 | 5                   |
+-----------+------------+---------------------+
对于 ID 为 1 的玩家，2016-05-02 共玩了 5+6=11 个游戏，2017-06-25 共玩了 5+6+1=12 个游戏。
对于 ID 为 3 的玩家，2018-07-03 共玩了 0+5=5 个游戏。
请注意，对于每个玩家，我们只关心玩家的登录日期。
```

###### Answer:

窗口函数

```sql
select 
    player_id,
    event_date,
    sum(games_played) over(partition by player_id order by event_date) games_played_so_far
from Activity;
```

自连接

```sql
select 
    a1.player_id,
    a1.event_date,
    sum(a2.games_played) games_played_so_far
from Activity a1,Activity a2
where a1.player_id=a2.player_id and 
      a1.event_date>=a2.event_date
group by 1,2;
```



##### [550. 游戏 IV:首次登陆之后第二天再登陆的比例](https://leetcode-cn.com/problems/game-play-analysis-iv/)

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

编写一个 SQL 查询，报告在首次登录的第二天再次登录的玩家的分数，四舍五入到小数点后两位。换句话说，您需要计算从首次登录日期开始至少连续两天登录的玩家的数量，然后除以玩家总数。

查询结果格式如下所示：

```
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
只有 ID 为 1 的玩家在第一天登录后才重新登录，所以答案是 1/3 = 0.33
```

###### Answer:

子查询

1. 求出所有玩家首次登陆数据

```sql
select player_id,min(event_date) first_date from activity group by player_id
```

2. 将所有玩家首次登陆数据作为临时表，并和所有数据表activity进行关联

```sql
select *
from activity a,
(select player_id,min(event_date) first_date from activity group by player_id) b
where a.player_id=b.player_id
```

3. 使用datediff函数计算玩家每次登陆和首次登陆的日期差，使用count+distinct函数获取所有玩家数

```sql
select datediff(a.event_date,b.first_date),(select count(distinct(player_id)) from activity)
from activity a,
(select player_id,min(event_date) first_date from activity group by player_id) b
where a.player_id=b.player_id
```

4. 使用case when then else过滤出所有符合条件的玩家，然后使用sum求和，计算出符合条件的玩家数目

```sql
select sum(case when datediff(a.event_date,b.first_date)=1 then 1 else 0 end),(select count(distinct(player_id)) from activity)
from activity a,
(select player_id,min(event_date) first_date from activity group by player_id) b
where a.player_id=b.player_id
```

5. 最后将符合条件的玩家数除以所有玩家数，并使用round函数，保留两位小数,并且按照例子上面的输出结果给列名取个别名即可

```sql
select round(sum(case when datediff(a.event_date,b.first_date)=1 then 1 else 0 end)/(select count(distinct(player_id)) from activity),2) as fraction
from activity a,
(select player_id,min(event_date) first_date from activity group by player_id) b
where a.player_id=b.player_id
```



##### [570. 至少有5名直接下属的经理](https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports/)

`Employee` 表包含所有员工和他们的经理。每个员工都有一个 Id，并且还有一列是经理的 Id。

```
+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
```

给定 `Employee` 表，请编写一个SQL查询来查找至少有5名直接下属的经理。对于上表，您的SQL查询应该返回：

```
+-------+
| Name  |
+-------+
| John  |
+-------+
```



###### Answer:

```sql
select Name
from Employee 
join (
    select e1.Id, case when COUNT(1) >= 5 then 1 else 0 end result
    from Employee e1 JOIN Employee e2 ON e1.Id = e2.ManagerId
    group by e1.Id ) a
on Employee.Id = a.Id
Where a.result = 1
```



##### [574. 当选者](https://leetcode-cn.com/problems/winning-candidate/)

表: `Candidate`

```sql
+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
```

表: `Vote`

```
+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id 是自动递增的主键，
CandidateId 是 Candidate 表中的 id.
```

请编写 sql 语句来找到当选者的名字，上面的例子将返回当选者 `B`.

```
+------+
| Name |
+------+
| B    |
+------+
```

###### Answer：

1. 获得每个人被投票的次数
2. 通过ID将两个表连接
3. 按照投票次数排序
4. 选取从上到下第一名

```sql
--运行时间350毫秒
--性能一般
select c.name
from
(
select candidateid,count(*) as votes
from vote
group by candidateid
) v
left join candidate c
on c.id=v.candidateid
order by votes desc
limit 1
```



##### [578. 查询回答率最高的问题](https://leetcode-cn.com/problems/get-highest-answer-rate-question/)

从 survey_log 表中获得回答率最高的问题，survey_log 表包含这些列：id, action, question_id, answer_id, q_num, timestamp。

id 表示用户 id；action 有以下几种值："show"，"answer"，"skip"；当 action 值为 "answer" 时 answer_id 非空，而 action 值为 "show" 或者 "skip" 时 answer_id 为空；q_num 表示当前会话中问题的编号。

请编写 SQL 查询来找到具有最高回答率的问题。

**示例：**

```sql
输入：
+------+-----------+--------------+------------+-----------+------------+
| id   | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
输出：
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+
解释：
问题 285 的回答率为 1/1，而问题 369 回答率为 0/1，因此输出 285 。

```



###### Answer：

```sql
select question_id as survey_log
from survey_log
group by question_id
order by sum(if(action = 'answer', 1, 0)) / sum(if(action = 'show', 1, 0)) desc
limit 1
```



##### [585. 2016年的投资](https://leetcode-cn.com/problems/investments-in-2016/)

写一个查询语句，将 2016 年 (TIV_2016) 所有成功投资的金额加起来，保留 2 位小数。

对于一个投保人，他在 2016 年成功投资的条件是：

他在 2015 年的投保额 (TIV_2015) 至少跟一个其他投保人在 2015 年的投保额相同。
他所在的城市必须与其他投保人都不同（也就是说维度和经度不能跟其他任何一个投保人完全相同）。

**输入格式:**
表 **insurance** 格式如下：

```
| Column Name | Type          |
|-------------|---------------|
| PID         | INTEGER(11)   |
| TIV_2015    | NUMERIC(15,2) |
| TIV_2016    | NUMERIC(15,2) |
| LAT         | NUMERIC(5,2)  |
| LON         | NUMERIC(5,2)  |
```

PID 字段是投保人的投保编号， TIV_2015 是该投保人在2015年的总投保金额， TIV_2016 是该投保人在2016年的投保金额， LAT 是投保人所在城市的维度， LON 是投保人所在城市的经度。、

**样例输入**

```
| PID | TIV_2015 | TIV_2016 | LAT | LON |
|-----|----------|----------|-----|-----|
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
```

**样例输出**

```
| TIV_2016 |
|----------|
| 45.00    |
```

就如最后一个投保人，第一个投保人同时满足两个条件：

1. 他在 2015 年的投保金额 TIV_2015 为 '10' ，与第三个和第四个投保人在 2015 年的投保金额相同。
2. 他所在城市的经纬度是独一无二的。

第二个投保人两个条件都不满足。他在 2015 年的投资 TIV_2015 与其他任何投保人都不相同。
且他所在城市的经纬度与第三个投保人相同。基于同样的原因，第三个投保人投资失败。

所以返回的结果是第一个投保人和最后一个投保人的 TIV_2016 之和，结果是 45 。

###### Answer:

```sql
--run time: 460ms
--beat 20% competitors

select sum(A.TIV_2016) as `TIV_2016`
from insurance as A
where exists(
    select *
    from insurance as B
    where B.PID != A.PID and B.TIV_2015 = A.TIV_2015 
) and not exists(
    select *
    from insurance as B
    where B.PID != A.PID and B.LAT = A.LAT and B.LON = A.LON
)
```



##### [602. 好友申请 II ：谁有最多的好友](https://leetcode-cn.com/problems/friend-requests-ii-who-has-the-most-friends/)

在 Facebook 或者 Twitter 这样的社交应用中，人们经常会发好友申请也会收到其他人的好友申请。

表 request_accepted 存储了所有好友申请通过的数据记录，其中， requester_id 和 accepter_id 都是用户的编号。

```
| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
```

写一个查询语句，求出谁拥有最多的好友和他拥有的好友数目。对于上面的样例数据，结果为：

```
| id | num |
|----|-----|
| 3  | 3   |
```

- 保证拥有最多好友数目的只有 1 个人。
- 好友申请只会被接受一次，所以不会有 **requester_id** 和 **accepter_id** 值都相同的重复记录。

###### Answer:

```sql
--run time 182 ms
--beat 77% competitors

select requester_id id, sum(cnt1) num
from 
(
select requester_id , count(1) cnt1
from request_accepted
group by requester_id
UNION ALL
select accepter_id, count(1) cnt2
from request_accepted
group by accepter_id
) temp3
group by requester_id
order by num desc
limit 1


```



##### [608. 树节点](https://leetcode-cn.com/problems/tree-node/)

给定一个表 `tree`，**id** 是树节点的编号， **p_id** 是它父节点的 **id 。**

```
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
```

树中每个节点属于以下三种类型之一：

叶子：如果这个节点没有任何孩子节点。
根：如果这个节点是整棵树的根，即没有父节点。
内部节点：如果这个节点既不是叶子节点也不是根节点。

写一个查询语句，输出所有节点的编号和节点的类型，并将结果按照节点编号排序。上面样例的结果为：

```
+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
```

###### Answer:

```sql
SELECT
    id AS `Id`,
    CASE
        WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
          THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
          THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM
    tree
ORDER BY `Id`

```



##### [612. 平面上的最近距离](https://leetcode-cn.com/problems/shortest-distance-in-a-plane/)

表 `point_2d` 保存了所有点（多于 2 个点）的坐标 (x,y) ，这些点在平面上两两不重合。写一个查询语句找到两点之间的最近距离，保留 2 位小数。

```
| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
```

最近距离在点 (-1,-1) 和(-1,2) 之间，距离为 1.00 。所以输出应该为：

```
| shortest |
|----------|
| 1.00     |
```

###### Answer:

```sql
select round(min(t1.abstract),2) shortest
from (
select sqrt(pow(abs(p1.x - p2.x),2) + pow(abs(p1.y -p2.y),2)) as abstract
from point_2d p1 join point_2d p2
) t1
where abstract <> 0
```



##### [613. 直线上的最近距离](https://leetcode-cn.com/problems/shortest-distance-in-a-line/)

表 `point` 保存了一些点在 x 轴上的坐标，这些坐标都是整数。

写一个查询语句，找到这些点中最近两个点之间的距离。

```
| x   |
|-----|
| -1  |
| 0   |
| 2   |
```

最近距离显然是 '1' ，是点 '-1' 和 '0' 之间的距离。所以输出应该如下：

```
| shortest|
|---------|
| 1       |
```

Answer:

```sql
select min(dis) as shortest
from (
select abs(p1.x - p2.x) dis
from point p1 join point p2
) t1
where dis <> 0
```



##### [614. 二级关注者](https://leetcode-cn.com/problems/second-degree-follower/)

在 facebook 中，表 follow 会有 2 个字段： followee, follower ，分别表示被关注者和关注者。 请写一个 sql 查询语句，对每一个关注者，查询关注他的关注者的数目。

比方说：

```
+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+
```

应该输出：

```
+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+
```

###### Answer:

```sql
# Write your MySQL query statement below
select f.followee follower, count(distinct f.follower) num
from follow f  
where f.followee in (
    select f1.follower
    from follow f1 
)
group by f.followee
order by f.followee
```



##### [626. 换座位](https://leetcode-cn.com/problems/exchange-seats/)

小美是一所中学的信息科技老师，她有一张 seat 座位表，平时用来储存学生名字和与他们相对应的座位 id。

其中纵列的 id 是连续递增的

小美想改变相邻俩学生的座位。

你能不能帮她写一个 SQL query 来输出小美想要的结果呢？

```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
```

变成：

```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
```

###### Answer:

```
SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;
```



##### [1045. 买下所有产品的客户](https://leetcode-cn.com/problems/customers-who-bought-all-products/)

`Customer` 表：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
product_key 是 Product 表的外键。
```

`Product` 表：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key 是这张表的主键。
```

写一条 SQL 查询语句，从 `Customer` 表中查询购买了 `Product` 表中所有产品的客户的 id。

```
Customer 表：
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+

Product 表：
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+

Result 表：
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
购买了所有产品（5 和 6）的客户的 id 是 1 和 3 。
```

###### Answer:

```
select t2.customer_id
from 
(select t1.customer_id, count(1) cnt
from 
(select distinct c1.customer_id, c1.product_key
from Customer c1) t1
group by t1.customer_id) t2,
(select count(*) cnt_all
from Product) t3
where t3.cnt_all = t2.cnt
```



##### [1070. 产品销售分析 III](https://leetcode-cn.com/problems/product-sales-analysis-iii/)

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
sale_id 是此表的主键。
product_id 是产品表的外键。
请注意，价格是按每单位计的。
```

产品表 `Product`：

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id 是此表的主键。
```

编写一个 SQL 查询，选出每个销售产品的 **第一年** 的 **产品 id**、**年份**、**数量** 和 **价格**。查询结果格式如下：

```
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Result table:
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
```

###### Answer:

```sql
select product_id, year as first_year, quantity, price
from Sales
where (product_id, year) in (
select s1.product_id, min(s1.year)
from Sales s1
group by s1.product_id)
```



##### [1077. 项目员工 III](https://leetcode-cn.com/problems/project-employees-iii/)

项目表 `Project`：

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) 是这个表的主键
employee_id 是员工表 Employee 的外键
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
employee_id 是这个表的主键
```

写 一个 SQL 查询语句，报告在每一个项目中经验最丰富的雇员是谁。如果出现经验年数相同的情况，请报告所有具有最大经验年数的员工。

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
| 3           | John   | 3                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Result 表：
+-------------+---------------+
| project_id  | employee_id   |
+-------------+---------------+
| 1           | 1             |
| 1           | 3             |
| 2           | 1             |
+-------------+---------------+
employee_id 为 1 和 3 的员工在 project_id 为 1 的项目中拥有最丰富的经验。在 project_id 为 2 的项目中，employee_id 为 1 的员工拥有最丰富的经验。
```

###### Answer:

```sql
select t2.project_id, t2.employee_id
from 
(select t.project_id, t.employee_id, dense_rank() over (partition by t.project_id order by t.experience_years desc) rnk
from 
(select p.project_id, p.employee_id, e.name, e.experience_years
from Project p left join Employee e
on p.employee_id = e.employee_id) t)t2
where t2.rnk = 1
```



##### [1098. 小众书籍](https://leetcode-cn.com/problems/unpopular-books/)

书籍表 `Books`：

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| name           | varchar |
| available_from | date    |
+----------------+---------+
book_id 是这个表的主键。
```

订单表 `Orders`：

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| order_id       | int     |
| book_id        | int     |
| quantity       | int     |
| dispatch_date  | date    |
+----------------+---------+
order_id 是这个表的主键。
book_id  是 Books 表的外键。
```

你需要写一段 SQL 命令，筛选出过去一年中订单总量 少于10本 的 书籍 。

注意：不考虑 上架（available from）距今 不满一个月 的书籍。并且 假设今天是 2019-06-23 。

下面是样例输出结果：

```
Books 表：
+---------+--------------------+----------------+
| book_id | name               | available_from |
+---------+--------------------+----------------+
| 1       | "Kalila And Demna" | 2010-01-01     |
| 2       | "28 Letters"       | 2012-05-12     |
| 3       | "The Hobbit"       | 2019-06-10     |
| 4       | "13 Reasons Why"   | 2019-06-01     |
| 5       | "The Hunger Games" | 2008-09-21     |
+---------+--------------------+----------------+

Orders 表：
+----------+---------+----------+---------------+
| order_id | book_id | quantity | dispatch_date |
+----------+---------+----------+---------------+
| 1        | 1       | 2        | 2018-07-26    |
| 2        | 1       | 1        | 2018-11-05    |
| 3        | 3       | 8        | 2019-06-11    |
| 4        | 4       | 6        | 2019-06-05    |
| 5        | 4       | 5        | 2019-06-20    |
| 6        | 5       | 9        | 2009-02-02    |
| 7        | 5       | 8        | 2010-04-13    |
+----------+---------+----------+---------------+

Result 表：
+-----------+--------------------+
| book_id   | name               |
+-----------+--------------------+
| 1         | "Kalila And Demna" |
| 2         | "28 Letters"       |
| 5         | "The Hunger Games" |
+-----------+--------------------+
```

###### Answer:

```sql
select book_id, name
from Books
where datediff("2019-06-23",available_from) > 30 and book_id not in (
    select t1.book_id
    from 
    (select book_id, sum(quantity) cnt
    from Orders 
    where datediff("2019-06-23",dispatch_date) < 366
    group by book_id
    ) t1
    where t1.cnt > 9
)
```



##### [1107. 每日新用户统计](https://leetcode-cn.com/problems/new-users-daily-count/)

`Traffic` 表：

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| activity      | enum    |
| activity_date | date    |
+---------------+---------+
该表没有主键，它可能有重复的行。
activity 列是 ENUM 类型，可能取 ('login', 'logout', 'jobs', 'groups', 'homepage') 几个值之一。
```

编写一个 SQL 查询，以查询从今天起最多 90 天内，每个日期该日期首次登录的用户数。假设今天是 **2019-06-30**.

```
Traffic 表：
+---------+----------+---------------+
| user_id | activity | activity_date |
+---------+----------+---------------+
| 1       | login    | 2019-05-01    |
| 1       | homepage | 2019-05-01    |
| 1       | logout   | 2019-05-01    |
| 2       | login    | 2019-06-21    |
| 2       | logout   | 2019-06-21    |
| 3       | login    | 2019-01-01    |
| 3       | jobs     | 2019-01-01    |
| 3       | logout   | 2019-01-01    |
| 4       | login    | 2019-06-21    |
| 4       | groups   | 2019-06-21    |
| 4       | logout   | 2019-06-21    |
| 5       | login    | 2019-03-01    |
| 5       | logout   | 2019-03-01    |
| 5       | login    | 2019-06-21    |
| 5       | logout   | 2019-06-21    |
+---------+----------+---------------+

Result 表：
+------------+-------------+
| login_date | user_count  |
+------------+-------------+
| 2019-05-01 | 1           |
| 2019-06-21 | 2           |
+------------+-------------+
请注意，我们只关心用户数非零的日期.
ID 为 5 的用户第一次登陆于 2019-03-01，因此他不算在 2019-06-21 的的统计内。
```

###### Answer:

```sql
 select t1.activity_date as login_date, count(1) user_count
 from 
   (select tra1.user_id, tra1.activity_date, row_number() over (partition by tra1.user_id order by tra1.activity_date) as rnk
    from Traffic tra1
    where tra1.activity = "login"
   ) t1
 where t1.rnk = 1 and datediff("2019-06-30" ,t1.activity_date) < 91
 group by t1.activity_date
```



##### [1112. 每位学生的最高成绩](https://leetcode-cn.com/problems/highest-grade-for-each-student/)

表：`Enrollments`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) 是该表的主键。
```

编写一个 SQL 查询，查询每位学生获得的最高成绩和它所对应的科目，若科目成绩并列，取 course_id 最小的一门。查询结果需按 student_id 增序进行排序。

查询结果格式如下所示：

```
Enrollments 表：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+

Result 表：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
```

###### Answer:

```sql
select student_id, course_id, grade
from
   (select student_id, course_id, grade, row_number() over (partition by student_id order by grade desc, course_id) as rnk
  from Enrollments
   ) t1
where t1.rnk = 1 
```

