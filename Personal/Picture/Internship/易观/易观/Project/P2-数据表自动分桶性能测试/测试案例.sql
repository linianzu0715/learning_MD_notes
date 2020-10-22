--案例6：6个hash用户桶
/*@平台管理员#retention-1*/ 
select 
	"profile_$city" as attrValue,
	cast(state[1] as integer)*1 as totalUserCount , 
	cast(state[2] as integer)*1 as dayUserCount0, 
	cast(state[3] as integer)*1 as dayUserCount1, 
	cast(state[4] as integer)*1 as dayUserCount2, 
	cast(state[5] as integer)*1 as dayUserCount3, 
	cast(state[6] as integer)*1 as dayUserCount4, 
	cast(state[7] as integer)*1 as dayUserCount5, 
	cast(state[8] as integer)*1 as dayUserCount6, 
	cast(state[9] as integer)*1 as dayUserCount7, 
	cast(state[10] as integer)*1 as dayUserCount8, 
	cast(state[11] as integer)*1 as dayUserCount9, 
	cast(state[12] as integer)*1 as dayUserCount10, 
	cast(state[13] as integer)*1 as dayUserCount11, 
	cast(state[14] as integer)*1 as dayUserCount12, 
	cast(state[15] as integer)*1 as dayUserCount13, 
	cast(state[16] as integer)*1 as dayUserCount14, 
	cast(state[17] as integer)*1 as dayUserCount15, 
	cast(state[18] as integer)*1 as dayUserCount16, 
	cast(state[19] as integer)*1 as dayUserCount17, 
	cast(state[20] as integer)*1 as dayUserCount18, 
	cast(state[21] as integer)*1 as dayUserCount19, 
	cast(state[22] as integer)*1 as dayUserCount20, 
	cast(state[23] as integer)*1 as dayUserCount21, 
	cast(state[24] as integer)*1 as dayUserCount22, 
	cast(state[25] as integer)*1 as dayUserCount23, 
	cast(state[26] as integer)*1 as dayUserCount24, 
	cast(state[27] as integer)*1 as dayUserCount25, 
	cast(state[28] as integer)*1 as dayUserCount26, 
	cast(state[29] as integer)*1 as dayUserCount27, 
	cast(state[30] as integer)*1 as dayUserCount28, 
	cast(state[31] as integer)*1 as dayUserCount29, 
	cast(state[32] as integer)*1 as dayUserCount30  
from 
	( select 
		"profile_$city",
		retention_sum_grouping(distinct_id_state,60,30,-1) as state  
	from 
		( select 
			event.distinct_id,
			cast(  COALESCE(profile."$city",'(无值)')  as varchar) as "profile_$city" , 
			retention_count_grouping(
				array[ case when ( (event.xwhat_id=7)  and event."$channel" in ('今日头条','百度')) and  event.ds between 20200303 and 20200501 then 0 else -1 end ,  
						case when ( (event.xwhat_id=1)  and event."$app_version" in ('V1.0')) then 1 else -1 end ,  -1 ],
				cast( event.xwhen/1000 - 1583164800 as integer),
				cast(date_diff('day', from_iso8601_timestamp('2020-03-03'), parse_datetime(CAST(event.ds AS varchar),'YYYYMMdd')) as integer),
				60,
				30,
				-1,
				-1,
				-1,
				-1) as distinct_id_state  
		from hive.db_514fec3bdc58ccad.event event  left join hive.db_514fec3bdc58ccad.profile_vd profile  on event.distinct_id = profile.distinct_id  
		where (event.xwhat_id=7 or event.xwhat_id=1) and ( event.ds between 20200303 and 20200531) group by  event.distinct_id , COALESCE(profile."$city",'(无值)') )  
	where distinct_id_state is not null group by 1 )  
order by   totalUserCount desc  limit 50















