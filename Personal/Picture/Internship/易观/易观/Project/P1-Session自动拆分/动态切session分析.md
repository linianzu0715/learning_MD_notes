##### [动态切割session分析](https://con.analysys.cn/pages/viewpage.action?pageId=13804129)

```
需要支持的切割规则
task1:0点切割(跨天切割，暂时不支持修改时间)
task2:超时(默认30分钟，可由客户指定)
task3:指定事件切割-当前事件(包括指定事件的指定属性)
task4:指定事件-上条记录(包括事件以及属性)
```



**lead over 语法：**

lead(expression,offset,default) over(partition by ... order by ...)

**Lag over 语法：**

lag(expression,offset,default) over(partition by ... order by ... )



Example 1:

```sql
---提取前一周和后一周的数据

select
　　year,week,sale,
　　lead(sale,1,NULL) over(					--前一周sale 
      partition by product,country,region order by year,week) lead_week_sale,
　　lag(sale,1,NULL) over(					--后一周sale 
      partition by product,country,region order by year,week) lag_week_sale

from sales_fact a
where a.country='country1' and a.product='product1' and region='region1'
order by product,country,year,week
```



Example 2:

```sql
SELECT　　
　　created_at create_time,
　　operator,
　　bridge_duration,
　　lead(created_at, 1) OVER (PARTITION BY operator ORDER BY created_at ASC) next_create_time
FROM ods.ods_call_ctob_auction_call_recording
WHERE substr(created_at,1,10)= '${date_y_m_d}'
```



实际代码：

第一层：

```sql
from (
   select
      t1.*,                              -- 根据参数补充属性，属性+session属性对应的属性
      lag(xwhen,1,-0) over(partition by distinct_id order by xwhen,xwhat) as "$$last_xwhen",  -- 固定写法，取上个事件的xwhen-
      lag(xwhat,1,'') over(partition by distinct_id order by xwhen,xwhat) as "$$last_xwhat",  -- 固定写法，上个事件的xwhat
      lead(xwhen,1) over(partition by distinct_id order by xwhen,xwhat) as "$$next_xwhen"  ,      -- 固定写法，取上个事件的xwhen
      lead(xwhat,1) over(partition by distinct_id order by xwhen,xwhat) as "$$next_xwhat"  ,      -- 固定写法，取下个事件的xwhat
      lag("$os",1) over(partition by distinct_id order by xwhen,xwhat) as "$$last_$os"        -- 取上一条记录的$$os属性，根据前台参数可变化           
   from hive.db_1234qwer.vd_event t1
   where ds between '20180410' and '20180416'  -- 日期条件
   ) t2
```



第二层：

```sql
select
     t2.*,
     case 
     when xwhen - "$$last_xwhen" >= 30*60*1000 then ARRAY[0,1]    
     -- 如果当前session的时间和上一个相比，超出了30mins，就根据超时切割策略进行切割
     -- 使用标记数组array进行标记
     -- array 第一位: 标记切割方式：0:超时切割
     --       第二位: 标记是否first_event 1:是
     
     when date_diff('day', from_unixtime("$$last_xwhen"/1000), from_unixtime(xwhen/1000)) >=1 then ARRAY[1,1]   
     -- 如果当前session的时间和上一个相比，是不同的两天，就根据跨天切割策略进行切割
     -- array 第一位: 标记切割方式：1:跨天
     
     when xwhat = 'start' then array[2,1]   
     -- 如果当前session的所做的事情为“start”，则意味着开启了一个新的会话，因此需要切割。
     -- array 第一位: 标记切割方式：2：当前事件或者属性达标，如当前事件为打开事件
     
     when "$$last_xwhat"='end' then array[3,1]   
     -- 如果前一个session的所做的事情为“END”，则意味着当前需要切割。
     -- array 第一位: 标记切割方式：3: 当前事件与上一条事件对比，或者上一条事件属性，如 上一条事件为结束事件 
     
     when "$$last_$os"<>"os" then array[4,1]
     -- 如果上一个session的os属性和当前session记录的os属性不相同。则标记切割。
     
     else array[-1,0] 
     -- 否则标记为不切割
     end  as "$$if_frist_evnet_info",    
     -- 标记session是否为开始页信息   
     
     
     case 
     when "$$next_xwhen"-xwhen>=30*60*1000
                or "$$next_xwhen" = 0
                or date_diff('day', from_unixtime(xwhen/1000), from_unixtime("$$next_xwhen"/1000)) >=1
                or "$$next_xwhat" = 'start'
                or xwhat = 'start'
                or "os"="nest_$os"
     then array[1,0]
     -- 标记当前session记录为结束页
     -- session结束页时为0
     else array[0,"$$next_xwhen"-xwhen]   end  as "$$if_end_event_info"            
   from (...) t3

```



**CONCAT函数**

CONCAT函数用于将两个字符串连接起来，形成一个单一的字符串。

Example1：

假设表中有当前记录

```
SQL> SELECT * FROM employee_tbl;
+------+------+------------+--------------------+
| id   | name | work_date  | daily_typing_pages |
+------+------+------------+--------------------+
|    1 | John | 2007-01-24 |                250 |
|    2 | Ram  | 2007-05-27 |                220 |
|    3 | Jack | 2007-05-06 |                170 |
|    3 | Jack | 2007-04-06 |                100 |
|    4 | Jill | 2007-04-06 |                220 |
|    5 | Zara | 2007-06-06 |                300 |
|    5 | Zara | 2007-02-06 |                350 |
+------+------+------------+--------------------+
7 rows in set (0.00 sec)
```

使用concat函数进行字段合并

```
SQL> SELECT CONCAT(id, name, work_date)
    -> FROM employee_tbl;
+-----------------------------+
| CONCAT(id, name, work_date) |
+-----------------------------+
| 1John2007-01-24             |
| 2Ram2007-05-27              |
| 3Jack2007-05-06             |
| 3Jack2007-04-06             |
| 4Jill2007-04-06             |
| 5Zara2007-06-06             |
| 5Zara2007-02-06             |
+-----------------------------+
7 rows in set (0.00 sec)
```





**BETWEEN函数：**

指定测试范围。

##### 语法：

*test_expression* [ NOT ] BETWEEN *begin_expression* AND *end_expression*

*test_expression*：是用来在由 *begin_expression* 和 *end_expression* 定义的范围内进行测试的表达式。*test_expression* 必须与 *begin_expression* 和 *end_expression* 具有相同的数据类型。

NOT：指定谓词的结果被取反

*begin_expression*：是任何有效的 Microsoft® SQL Server™ 表达式。*begin_expression* 必须与 *test_expression* 和 *end_expression* 具有相同的数据类型。

*end_expression*：是任何有效的 SQL Server 表达式。

AND：作为一个占位符，表示 *test_expression* 应该处于由 *begin_expression* 和 *end_expression* 指定的范围内。

##### 结果类型

Boolean

##### 结果值

如果 *test_expression* 的值大于或等于 *begin_expression* 的值并且小于或等于 *end_expression* 的值，则 BETWEEN 返回 TRUE。

如果 *test_expression* 的值小于 *begin_expression* 的值或者大于 *end_expression* 的值，则 NOT BETWEEN 返回 TRUE。

##### 注释

若要指定排除范围，请使用大于 (>) 和小于 (<) 运算符。如果任何 BETWEEN 或 NOT BETWEEN 谓词的输入为 NULL，则结果是 UNKNOWN。



Example：

```sql
SELECT title_id, ytd_sales
FROM titles
WHERE ytd_sales BETWEEN 4095 AND 12000
```

```
title_id ytd_sales 
-------- ----------- 
BU1032   4095        
BU7832   4095        
PC1035   8780        
PC8888   4095        
TC7777   4095        
(5 row(s) affected)
```



**Cast()函数：**

用于数据类型转换

语法：

CAST (expression AS data_type)

将某个字段的数据转化为特定的类型

UNBOUNDED PRECEDING：表示最前一行



第三层

```sql
select
      t3.*,
      "$$if_frist_evnet_info"[1] as "$$session_Division_type",  -- 切割方式
      "$$if_frist_evnet_info"[2] as "$$if_frist_event",   -- 是否首页面
      "$$if_end_event_info"[1] as "$$if_end_event",       -- 是否尾页面
      "$$if_end_event_info"[2] as "$$session_dua",        -- 事件时间
      
      
      concat
      (cast
      (max
      (case when "$$if_frist_evnet_info"[2]=1 then xwhen else -1 end) 			   
      over
      (partition by distinct_id order by xwhen rows between UNBOUNDED PRECEDING and current row) 
       -- 选取从最前一行到当前行
       -- 选取出所有为会话开始的行中 时间最长 也就是最晚的那一条记录
       as varchar)
       -- 选取从上一个断点到当前行的最大的session时间，前提是当前行是新会话第一行
       ,distinct_id) as "$$session_id" -- 所有事件标记session号，该处需要算法支撑更好
   from () t4
```







**first_value()和last_value():**

首尾记录值:

Example:

查询部门最早发生销售记录日期和最近发生的销售记录日期

SQL> select * from criss_sales order by dept_id,sale_date

```
DEPT_ID SALE_DATE   GOODS_TYPE    SALE_CNT
------- ----------- ---------- -----------
D01     2014/3/4    G00                700
D01     2014/4/8    G01                200
D01     2014/4/30   G03                800
D01     2014/5/4    G02                 80
D01     2014/6/12   G01        
D02     2014/3/6    G00                500
D02     2014/4/8    G02                100
D02     2014/4/27   G01                300
D02     2014/5/2    G03                900
```

```sql
SQL> select
  2     dept_id
  3    ,sale_date
  4    ,goods_type
  5    ,sale_cnt
  6    ,first_value(sale_date) over (partition by dept_id order by sale_date) first_value
  7    ,last_value(sale_date) over (partition by dept_id order by sale_date desc) last_value
  8  from criss_sales;
```

```
DEPT_ID SALE_DATE   GOODS_TYPE    SALE_CNT FIRST_VALUE LAST_VALUE
------- ----------- ---------- ----------- ----------- -----------
D01     2014/3/4    G00                700 2014/3/4    2014/3/4
D01     2014/4/8    G01                200 2014/3/4    2014/4/8
D01     2014/4/30   G03                800 2014/3/4    2014/4/30
D01     2014/5/4    G02                 80 2014/3/4    2014/5/4
D01     2014/6/12   G01                    2014/3/4    2014/6/12
D02     2014/3/6    G00                500 2014/3/6    2014/3/6
D02     2014/4/8    G02                100 2014/3/6    2014/4/8
D02     2014/4/27   G01                300 2014/3/6    2014/4/27
D02     2014/5/2    G03                900 2014/3/6    2014/5/2
```

last_value()默认统计范围是

```sql
rows between unbounded preceding and current row
```



第四层：

```sql
select
    t4.*,
    ds as cycle,  -- 周期转换
    sum("$$session_dua") over(partition by distinct_id,"$$session_id") as "$$session_dua_tot",
    count(distinct_id) over(partition by distinct_id,"$$session_id") as "$$session_detailCount",
    first_value(xwhat) over(partition by distinct_id,"$$session_id" order by "$$if_frist_event") as "$$session_xwhat" -- session_属性
    /*0209：直接罗列需要的事件属性
       注意命名 不冲突，后面sql部分直接使用
        注意子查询透传属性，这一点与 session属性处理逻辑相同，特别 注意 透传属性的时候，同时 选了session属性以及 事件属性，不要冲突重复
     */
```



##### 总结

* 第一层：

获取每条记录对应的上一条记录的时间和操作，下一条记录对应的时间和操作，和$$os值

* 第二层：

判断每条记录是否是session的开始或者是结尾。并且用数组记录两个新 段 "if_frist_evnet_info" 和 "if_end_event_info"

"if_frist_evnet_info"[1] 切割方式

"if_frist_evnet_info"[2] 是否session的开头

"if_end_event_info"[1] 是否session的结尾

"if_end_event_info"[2] 事件时间

* 第三层

找到到每条记录为止，上一个session开头的位置。然后存储为session_id

* 第四层

生成每个session的总共时间，记录为："session_dua_tot"

生成每个session的操作次数，记录为："session_detailCount"

生成每个session的操作属性，记录为："session_xwhat"





#### 新动态session切割算法：

```java
/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package window.dynamicsession;

import io.prestosql.spi.block.BlockBuilder;
import io.prestosql.spi.function.ValueWindowFunction;
import io.prestosql.spi.function.WindowFunctionSignature;

import java.util.List;

import static com.google.common.base.Preconditions.checkArgument;
import static window.dynamicsession.Utils.getAttrReadFunction;
import static window.dynamicsession.Utils.getAttribute;
import static window.dynamicsession.Utils.getSessionDivType;


/**
 *  此windows 用于计算session start attr
 *
 *  参数释义
 *      - 第1个参数固定输入：xwhat_id， 表示xwhat_id 列
 *      - 第2个参数固定输入：xwhen, 表示xwhen 列
 *      - 第3个参数： time-interval， 即指定切分事件间隔
 *      - 第4个参数： 表示是否需要跨天切割， 可选值0或者1， 其中  0 表示不需要， 1表示需要
 *      - 第5个参数： start-xwhat-id, 即按起始事件切割， 不使用这一规则，则填写-1
 *      - 第6个参数： end-xwhat-id，即按照结束事件切割， 不适用这一规则，则填写-1
 *      - 第7个参数： 是否需要基于属性切割， 0 表示不需要， 1表示需要
 *      - 第8个参数： 是否需要基于属性切割， 0 表示不需要， 1表示需要，且参数类型为double， 2 表示需要，且参数类型为varchar-
 *      - 第9个参数：需要计算的session start属性
 * @author pengdou
 */
@WindowFunctionSignature(
        name = "get_session_start_attr",
        typeVariable = "T",
        returnType = "T",
        argumentTypes = {"integer", "bigint", "integer", "integer", "integer", "integer", "integer","varchar", "T"}
        )
@WindowFunctionSignature(
        name = "get_session_start_attr",
        typeVariable = "T",
        returnType = "T",
        argumentTypes = {"integer", "bigint", "integer", "integer", "integer", "integer", "integer","double", "T"}
)
public class DynamicSessionStartAttrFunction
        extends ValueWindowFunction
{
    private final int tsChannel;
    private final int eventIdChannel;
    private final int  sessionIntervalChannel;
    private final int  enableDayDivChannel;
    private final int sessionStartXWhatId;
    private final int sessionEndXWhatId;
    private final int enableAttrDivChannel;
    private final int attrChannel;

    private int curEventId;
    private long curEventTs;
    private Object curEventAttr;

    private int nextEventId;
    private long nextEventTs;
    private Object nextEventAttr;
    private int startEventId = Integer.MIN_VALUE;
    private int endEventId = Integer.MIN_VALUE;
    private int interval = Integer.MIN_VALUE;
    private boolean enableDayDiv;
    private byte enableAttrDivFlag;
    private Utils.READ_FUNCTION readFunction;
    private int lastSessionStartPosition = 0;
    private int calculateChannel;

    public DynamicSessionStartAttrFunction(List<Integer> argumentChannels)
    {
        // 参数合法性检查：
        checkArgument(argumentChannels.size() == 9, "arguments size must be 9");
        this.eventIdChannel = argumentChannels.get(0);
        this.tsChannel = argumentChannels.get(1);
        this.sessionIntervalChannel = argumentChannels.get(2);
        this.enableDayDivChannel = argumentChannels.get(3);
        this.sessionStartXWhatId = argumentChannels.get(4);
        this.sessionEndXWhatId = argumentChannels.get(5);
        this.enableAttrDivChannel = argumentChannels.get(6);
        this.attrChannel = argumentChannels.get(7);
        this.calculateChannel = argumentChannels.get(8);
    }

    @Override
    public void processRow(BlockBuilder output, int frameStart, int frameEnd, int currentPosition)
    {
        int lastEventId;
        long lastEventTs;
        Object lastEventAttr;

        if (startEventId == Integer.MIN_VALUE) {
            startEventId = (int) (windowIndex.getLong(sessionStartXWhatId, 0));
            endEventId = (int) (windowIndex.getLong(sessionEndXWhatId, 0));
            interval = (int) (windowIndex.getLong(sessionIntervalChannel, 0));
            enableDayDiv = windowIndex.getLong(enableDayDivChannel, 0) == 1;
            enableAttrDivFlag = (byte) (windowIndex.getLong(enableAttrDivChannel, 0));
            checkArgument(enableAttrDivFlag == 0 || enableAttrDivFlag == 1 || enableAttrDivFlag == 2, "enableAttrDivFlag must in (0, 1, 2)");
            if (enableAttrDivFlag > 0) {
                readFunction = getAttrReadFunction(enableAttrDivFlag);
            }
        }

        if (currentPosition == 0) {
            lastEventId = 0;
            lastEventTs = 0;
            lastEventAttr = null;
            curEventId = (int) (windowIndex.getLong(eventIdChannel, currentPosition));
            curEventTs = windowIndex.getLong(tsChannel, currentPosition);
            curEventAttr = getAttribute(enableAttrDivFlag, windowIndex, attrChannel, currentPosition, readFunction);
        }
        else {
            lastEventId = curEventId;
            lastEventTs = curEventTs;
            lastEventAttr = curEventAttr;
            curEventId = nextEventId;
            curEventTs = nextEventTs;
            curEventAttr = nextEventAttr;
        }

        if (currentPosition + 1 < windowIndex.size()) {
            nextEventId = (int) (windowIndex.getLong(eventIdChannel, currentPosition + 1));
            nextEventTs = windowIndex.getLong(tsChannel, currentPosition + 1);
            curEventAttr = getAttribute(enableAttrDivFlag, windowIndex, attrChannel, currentPosition + 1, readFunction);
        }
        else {
            nextEventId = 0;
            nextEventTs = 0;
            nextEventAttr = null;
        }

        byte sessionDivType = getSessionDivType(interval, curEventTs,lastEventTs, enableDayDiv,
                startEventId, endEventId, curEventId, lastEventId,
                enableAttrDivFlag, curEventAttr, lastEventAttr);

        if (sessionDivType >= 0) {
            lastSessionStartPosition = currentPosition;
        }
        windowIndex.appendTo(calculateChannel, lastSessionStartPosition, output);
    }
}

```



##### 性能提升的原因：

1. 之前用sql命令嵌套了四层才能实现得到每个记录的sessionID，但是我们现在使用自定义窗口函数之后，相当于展开了4层嵌套的sql。我们用一个新的窗口函数来代替原有的sql命令。这样提升了系统的效率。
2. 之前使用的是最早是使用时间戳和distinctID通过使用concat方法合成sessionID。但是这样的效率是很差的。因为我们在concat的时候先是将两个字段转化为字符串，然后将两个字符串进行拼接，成为一个新的字符串。然后sessionID是以这个字符串的形式储存的。这种形式效率是很低的。首先处理的时候就需要消耗很多的内存。但是



动态分桶项目：

1. 批量执行脚本，完成。之前遇到了一个问题  在启动多线程的时候主线程卡死。 原因：参数传递。总结。把已经完成了的更新的脚本我都写好了新的脚本说明放在了confluence上面
2. 更近一步： 需求就是：
3. 三并发结果：执行时间比较长。现在还差最后一批结果 今天能完成  看已经完成的结果可以看到分桶确实有性能的提升。但是具体性能提升了多少还是需要所有的结果出来了之后再总结一下。 今天完成了数据的采集之后我也会仿照成为的单并发一样出一个可视化图表







动态切割session：

和彭哥成为重点研究了这个  当要获取新的属性之后  有两种方式。但是还是有性能提升的空间