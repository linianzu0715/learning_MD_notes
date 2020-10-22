# /usr/bin/env python
# -*- coding: UTF-8 -*-

import prestodb
import argparse
import time
import sys
import threading
from threading import Lock

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--l", type=int, default=1)
parser.add_argument("--t", type=int, default=1)
#parser.add_argument("--h", type=str, default="10.9.76.169")
parser.add_argument("--h", type=str, default="ark2")
parser.add_argument("--c", type=str, default="ckudu")
parser.add_argument("--p", type=int, default=8285)
parser.add_argument("--s", type=int, default=2)
args = parser.parse_args()


sqlNames = []
sqls = []
sqlName = str
queries = []

lock = Lock()
# 定义类
class Query:
    queryName = str
    querySqls = []

    def __init__(self, name, sqls):
        self.queryName = name
        self.querySqls = sqls

    def getQueryName(self):
        return self.queryName

    def getQuerySql(self):
        return self.querySqls


# 加载sql
firstQueryName = 0
for line in open('sqls'):
    strLine = line.strip()
    if strLine.__len__() <= 0:
        continue

    if strLine.startswith("--"):
        if firstQueryName == 0:
            firstQueryName = 1
            sqlName = strLine[2:]
        else:
            queries.append(Query(sqlName, sqls))
            sqlName = strLine[2:]
            sqls = []
    else:
        sqls.append(strLine)

if sqlName.__len__() > 0 and sqls.__len__() > 0:
    queries.append(Query(sqlName, sqls))

# 读取session 参数配置
params = []
for line in open('params'):
    params.append(line)

#  读取Python 脚本配置参数
threadsNum = args.__getattribute__("t")
loopsNum = args.__getattribute__("l")
hostName = args.__getattribute__("h")
catalogName = args.__getattribute__("c")
portNum = args.__getattribute__("p")
sleepTime = args.__getattribute__("s")
finished = 0

def RunQuery():
    # 创建连接
    conn = prestodb.dbapi.connect(
        host=hostName,
        port=portNum,
        user='isuhadoop',
        catalog=catalogName,
    )
    cur = conn.cursor()

    # 设置session 参数
    for paramIndex in range(params.__len__()):
        cur.execute(params[paramIndex])
        cur.fetchall()

    # 执行sql
    for loopIndex in range(loopsNum):
        queryLenth = queries.__len__()
        for queryIndex in range(queryLenth):
            que = queries.__getitem__(queryIndex)
            queName = que.getQueryName()
            queSqls = list(que.getQuerySql())
            starttime = int(round(1000 * time.time()))
            global sleepTime
            if sleepTime > 0:
                time.sleep(sleepTime)
            for sqlIndex in range(queSqls.__len__()):
                try:
                    cur.execute(queSqls[sqlIndex])
                    cur.fetchall()
                    endTime = int(round(1000 * time.time()))
                    print('{:^20s}'.format(bytes(queName)) + "\t" + '{:^20s}'.format(bytes(endTime - starttime)) + "\t" + '{:^20s}'.format("ms"))

                except Exception as e:
                    print('{:^20s}'.format(bytes(queName)) + '{:^20s}'.format("interruptted"))
                pass

            
            # 保证一个场景并发跑完，再跑下一个场景
            lock.acquire()
            global finished
            finished += 1
            lock.release()

            global threadsNum
            while finished % threadsNum != 0:
                time.sleep(1)
    cur.close()

# 打印输出文件头
print('{:^20s}'.format("场景名称")+ "\t" + '{:^20s}'.format("执行时间") + "\t" + '{:^20s}'.format("时间单位"))

# 创建指定个数线程
for threadsSeq in range(threadsNum):
    print("threadsSeq: "+ str(threadsSeq))
    t = threading.Thread(target=RunQuery)
    t.start()
    if sleepTime > 0:
        time.sleep(sleepTime)



