### 自定义问题

##### 分组查找最早(大)或最晚(小)记录建立表格，插入数据

```sql
CREATE TABLE `test`.`player_login` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `uid` VARCHAR(45) NOT NULL,
  `time` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `player_login_uid` (`uid` ASC),
  INDEX `player_login_time` (`time` ASC));
 
insert into test.player_login(uid,`time`) values('1',unix_timestamp('2018-09-10 08:10:30'));
insert into test.player_login(uid,`time`) values('2',unix_timestamp('2018-09-10 08:11:10'));
insert into test.player_login(uid,`time`) values('3',unix_timestamp('2018-09-10 08:15:01'));
insert into test.player_login(uid,`time`) values('4',unix_timestamp('2018-09-10 08:20:05'));
 
insert into test.player_login(uid,`time`) values('1',unix_timestamp('2018-09-10 10:10:30'));
insert into test.player_login(uid,`time`) values('2',unix_timestamp('2018-09-10 10:20:15'));
insert into test.player_login(uid,`time`) values('3',unix_timestamp('2018-09-10 11:05:30'));
insert into test.player_login(uid,`time`) values('4',unix_timestamp('2018-09-10 10:30:45'));
 
insert into test.player_login(uid,`time`) values('2',unix_timestamp('2018-09-11 07:20:15'));
insert into test.player_login(uid,`time`) values('3',unix_timestamp('2018-09-11 09:05:30'));
insert into test.player_login(uid,`time`) values('4',unix_timestamp('2018-09-11 10:30:45'));
 
insert into test.player_login(uid,`time`) values('3',unix_timestamp('2018-09-11 20:05:30'));
insert into test.player_login(uid,`time`) values('4',unix_timestamp('2018-09-11 21:30:45'));
 
insert into test.player_login(uid,`time`) values('4',unix_timestamp('2018-09-12 20:30:45'));
insert into test.player_login(uid,`time`) values('4',unix_timestamp('2018-09-12 23:30:45'));
```

找到用户的第一个记录：

```sql
select uid, min(date_format(from_unixtime(`time`), '%Y-%m-%d')) d from player_login group by uid order by uid;
```

找到用户的最后一个记录：

```sql
select uid, max(date_format(from_unixtime(`time`), '%Y-%m-%d')) d from player_login group by uid order by uid;
```













