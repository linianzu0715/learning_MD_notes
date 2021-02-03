## @Repository注解帮助持久化

[toc]

## 结算池的持久化：

今天在研究通用结算中的结算池和流水的数据是如何被持久化的。  

代码块

Java

```
@Repository
@DataSource("commonDbMoneyScan")
public interface TspCommonSettlePoolDao {

    String POOL_SELECT_FIELDS = "id, partner_id, partner_type, source_type, out_id, settle_type, " +
            "amount, ctime, utime, out_create_time, out_confirm_time, " +
            "status, cdate, comment, extra_json, other_id";
    String POOL_INSERT_KEYS = "id, partner_id, partner_type, source_type, out_id, settle_type, " +
            "amount, ctime, utime, out_create_time, out_confirm_time, cdate, " +
            "status, extra_json, other_id, cc";
    String POOL_INSERT_VALUES = "#{id}, #{partner_id}, #{partner_type}, #{source_type}, #{out_id}, #{settle_type}, " +
            "#{amount}, unix_timestamp(), #{utime}, #{out_create_time}, #{out_confirm_time}, #{cdate}, " +
            "#{status}, #{extra_json}, #{other_id}, #{cc}";

    List<TspMiniMoneySettlePool> getPoolInfoByUnique(@Param("out_id") String out_id, @Param("settleTypeList") List<Integer> settleTypeList, @Param("source_type") int source_type, @Param("other_id") String other_id,@Param("partner_id") long partner_id);

    @Select("select " + POOL_SELECT_FIELDS + " from wm_common_settle_pool where cdate=#{cdate} and status=0 and unix_timestamp()-ctime>=60 limit 500")
    List<TspMiniMoneySettlePool> getPoolInfoByCdate4Fix(@Param("cdate") int cdate);

    @Select("select " + POOL_SELECT_FIELDS + " from wm_common_settle_pool where id=#{id}")
    TspMiniMoneySettlePool getPoolInfoById(@Param("id") long id);

    @Insert("insert into wm_common_settle_pool(" + POOL_INSERT_KEYS + ") values(" + POOL_INSERT_VALUES + ")")
    void insertCommonSettlePool(TspMiniMoneySettlePool tspMiniMoneySettlePool);

    @Update("update wm_common_settle_pool set status=1, utime=unix_timestamp() where id=#{id}")
    int updateCommonSettlePoolSplit(long id);

    /**
     * 为数据回放提供的查pool接口
     * @return
     */
    List<TspMiniMoneySettlePool> querySelective(@Param("query") TspMiniMoneySettlePoolQuery query);
}
```

我们在对结算池进行持久化的时候，调用的方法是 insertCommonSettlePool 。这个方法会接受一个 TspMiniMoneySettlePool ，一个结算池对象。

我们要注意@Insert 注解。这个注解是表示这个方法会向数据库中插入一些数据。但是具体是插入的什么数据呢，这个就需要看看 @Insert 注解中的内容了

代码块

Java

```
 @Insert("insert into wm_common_settle_pool(" + POOL_INSERT_KEYS + ") values(" + POOL_INSERT_VALUES + ")")
这里是引用了两个变量 POOL_INSERT_KEYS， POOL_INSERT_VALUES。当我们把这两个拼接起来，就是一个完整的SQL语句。我们就是通过这个sql语句向数据库中插入数据的
```

这样的方式向数据库中插入数据是非常直观的。实际上就是执行了一个sql语句。但是这样的方式有一个缺陷，就是一次方法调用只会新增一条数据。



## 流水的持久化

流水在持久化时候的代码就相对简单了很多。

代码块

Java

```
@Repository
@DataSource("commonDbMoneyScan")
public interface TspCommonSettleFlowDao {

    void commonFlowBatchInsert(@Param("tspMiniMoneySettleFlows") List<TspMiniMoneySettleFlow> tspMiniMoneySettleFlows);

    List<TspMiniMoneySettleFlow> querySelective(@Param("query") TspMiniMoneySettleFlowQuery query);

    List<TspMiniMoneySettleFlow> queryFlowByOutIdSettleType(@Param("outId") String outId, @Param("sourceType") long sourceType);

    Integer countCommonSettleFlow(@Param("dailyBillId") long dailyBillId, @Param("settleTypeList") List<Integer> settleTypeList);

    List<TspMiniMoneySettleFlow> queryCommonSettleFlow(@Param("dailyBillId") long dailyBillId, @Param("settleTypeList") List<Integer> settleTypeList, @Param("offset") int offset, @Param("pageSize") int pageSize);
}
```

我们在持久化流水的时候，使用的是 commonFlowBatchInsert 方法。这个方法没有加上 @Insert。那么这个方法是如何来进行持久化的呢。我们要持久化的信息存储在这个方法传入的 tspMiniMoneySettleFlows 对象。



是想要说的时候，我们这声明的都是两个接口。而我们不许要为这两个接口提供实现类。因为我们在这个接口上面加上了@Repository 注解。这个Spring注解会帮助我们在执行的时候，自动生成一个实现类。



但是我们这里是具体如何将tspMiniMoneySettleFlows中的数据持久化的呢？

我们进行了全局搜索。最后找到了一个xml文件中有相应的记录。

代码块

XML

```
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.sankuai.meituan.tsp.minimoney.settle.dao.TspCommonSettleFlowDao">

    <sql id="insertKeys">
        id, common_settle_pool_id, settle_type, partner_a_type, partner_a_id, partner_b_id, partner_b_type, partner_type, partner_id, source_type, fee_type,
        direction, amount, out_id, out_create_time, out_confirm_time, ctime, utime, daily_bill_date, daily_bill_id, other_id,ext_json,settle_way
    </sql>

    <sql id="selectKeys">
        id, common_settle_pool_id, settle_type, partner_a_type, partner_a_id, partner_b_id, partner_b_type, partner_type, partner_id, source_type, fee_type,
        direction, amount, out_id, out_create_time, out_confirm_time, ctime, utime, daily_bill_date, daily_bill_id, other_id,ext_json,settle_way
    </sql>

    <insert id="commonFlowBatchInsert" useGeneratedKeys="false" parameterType="java.util.List">
        insert into wm_common_settle_flow (<include refid="insertKeys"/>)
        value
        <foreach collection="tspMiniMoneySettleFlows" item="item" index="index" separator=",">
            (#{item.id}, #{item.common_settle_pool_id}, #{item.settle_type}, #{item.partner_a_type}, #{item.partner_a_id},#{item.partner_b_id}, #{item.partner_b_type}, #{item.partner_type}, #{item.partner_id}, #{item.source_type}, #{item.fee_type},
            #{item.direction}, #{item.amount}, #{item.out_id}, #{item.out_create_time}, #{item.out_confirm_time}, unix_timestamp(), #{item.utime}, #{item.daily_bill_date}, #{item.daily_bill_id}, #{item.other_id}, #{item.ext_json}, #{item.settle_way})
        </foreach>
    </insert>
```

我们首先是要看到第一行这个mapper

代码块

XML

```
<mapper namespace="com.sankuai.meituan.tsp.minimoney.settle.dao.TspCommonSettleFlowDao"> 这个设置了我们要map的interface的位置保存在哪里。
```

然后我们能看到这个 insert 标签里面，第一个就是 id="commonFlowBatchInsert"。 这个意味着我们对应的方法的名字是 commonFlowBatchInsert。

后面连接上的是一个sql语句。在这个sql语句上面还有一个  <foreach> 标签。这意味着我们会循环一个对象。然后把对象中的内容查分出来，填写到相关位置上。

这样就生成了一系列完整的 sql。 我们循环执行这一系列的sql，就会向数据库中插入一系列的数据。