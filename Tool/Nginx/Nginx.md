## Nginx

[toc]



基本介绍：

https://mp.weixin.qq.com/s/C8ktgIgUUnhDcNsTnLS3SA

Nginx是一个高性能的HTTP和反向代理服务器，特点是占用内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好

nginx专为性能优化而开发，性能是其最重要的要求，十分注重效率，有报告nginx能支持高达50000个并发连接数。

### 反向代理

#### 正向代理

正向代理：局域网中的电脑用户想要直接访问网络是不可行的，只能通过代理服务器来访问，这种代理服务就被称为正向代理。

![img](https://mmbiz.qpic.cn/mmbiz_png/Fb60NIoTYzZADdBv0lRYWM1rn20IjSlIsPxfM8y0kJT22N2zdlSGJNY59cHpuAMm0PNCHjF0roOz9Y37HKgNFw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

#### 反向代理

反向代理：客户端无法感知代理，因为客户端访问网络不需要配置，只要把请求发送到反向代理服务器，由反向代理服务器去选择目标服务器获取数据，然后再返回到客户端，此时反向代理服务器和目标服务器对外就是一个服务器，暴露的是代理服务器地址，隐藏了真实服务器IP地址

![img](https://mmbiz.qpic.cn/mmbiz_png/Fb60NIoTYzZADdBv0lRYWM1rn20IjSlIic0Xsvobh9XPnepLcMESDK43WdPzlPGibEr9PbZhU50ibehP5HrX7ByIg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

### 负载均衡

客户端发送多个请求到服务器，服务器处理请求，有一些可能要与数据库进行狡猾，服务器处理完毕之后，再将结果返回给客户端

普通请求和响应过程

![img](https://mmbiz.qpic.cn/mmbiz_png/Fb60NIoTYzZADdBv0lRYWM1rn20IjSlI72hXhvshuBhCVsWS6k6PTAUs8XiaGwiaSIluaxzKNIALIGa6SoZngmEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

但是随着信息数量增长，访问量和数据量飞速增长，普通架构无法满足现在的需求

我们首先想到的是升级服务器配置，可以由于摩尔定律的日益失效，单纯从硬件提升性能已经逐渐不可取了，怎么解决这种需求呢？

我们可以增加服务器的数量，构建集群，将请求分发到各个服务器上，将原来请求集中到单个服务器的情况改为请求分发到多个服务器，也就是我们说的负载均衡

图解负载均衡

![img](https://mmbiz.qpic.cn/mmbiz_png/Fb60NIoTYzZADdBv0lRYWM1rn20IjSlID8mdx2496fWNr3KVL7UrJwiczATcMfiasAuiaFXKJZkrFHrN805HgRCibA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

假设有15个请求发送到代理服务器，那么由代理服务器根据服务器数量，平均分配，每个服务器处理5个请求，这个过程就叫做负载均衡

### 动静分离

为了加快网站的解析速度，可以把动态页面和静态页面交给不同的服务器来解析，加快解析的速度，降低由单个服务器的压力.

动静分离之前的状态

![img](https://mmbiz.qpic.cn/mmbiz_png/Fb60NIoTYzZADdBv0lRYWM1rn20IjSlI7wRompicLqR8cPic0EjC6u8kXQgrtzk0Le9xJPpkoCWD7MTqnh3YHzAw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

动静分离之后

![img](https://mmbiz.qpic.cn/mmbiz_png/Fb60NIoTYzZADdBv0lRYWM1rn20IjSlIY5yH2SswGRUNCwGNzWseucquvCLLfykMR8uVkpicDKkXoCdCEoNtwXA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

### nginx常用命令

查看版本

```
./nginx -v
```

启动

```
./nginx
```

关闭（有两种方式，推荐使用 ./nginx -s quit）

```
./nginx -s stop
./nginx -s quit
```

重新加载nginx配置

```
./nginx -s reload
```



### nginx的配置文件

配置文件分三部分组成

从配置文件开始到events块之间，主要是设置一些影响nginx服务器整体运行的配置指令

并发处理服务的配置，值越大，可以支持的并发处理量越多，但是会受到硬件、软件等设备的制约

```
worker_processes 1;
```



#### events块

影响nginx服务器与用户的网络连接，常用的设置包括是否开启对多workprocess下的网络连接进行序列化，是否允许同时接收多个网络连接等等

支持的最大连接数

```
events{
		worker_connection 1024;
}
```



#### http块

诸如反向代理和负载均衡都在此配置

location指令说明

- 该语法用来匹配url，语法如下

```
location[ = | ~ | ~* | ^~] url{
}
```

1. =:用于不含正则表达式的url前，要求字符串与url严格匹配，匹配成功就停止向下搜索并处理请求
2. ~：用于表示url包含正则表达式，并且区分大小写。
3. ~*：用于表示url包含正则表达式，并且不区分大瞎写
4. ^~：用于不含正则表达式的url前，要求ngin服务器找到表示url和字符串匹配度最高的location后，立即使用此location处理请求，而不再匹配
5. 如果有url包含正则表达式，不需要有~开头标识。



## 反向代理实战

目标：

Tomcat绑定的是 localhost 的 8080 端口。我们希望当我们访问本机的 80 端口的时候，也会自动跳转到 8080 端口。

首先我们需要打开 tomcat 服务。这个时候我们就能从 8080 端口访问到 tomcat 的页面。

然后我们再打开 Ningx 的配置 config 文件：

```
 server {
        listen       80; #监听的端口
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            proxy_pass http://127.0.0.1:8080; #要被代理到的地方
            index  index.html index.htm;
        }
```



## 负载均衡实战

## 动静分离实战



## mac下nginx的安装和配置

https://www.jianshu.com/p/026d67cc6cb1



## nginx文件目录

**5.1 nginx安装文件目录**
/usr/local/Cellar/nginx
**5.2 nginx配置文件目录**
/usr/local/etc/nginx
**5.3 config文件目录**
/usr/local/etc/nginx/nginx.conf
**5.4 系统hosts位置**
/private/etc/hosts



## nginx常用命令

```
nginx  #启动nginx
nginx -s quit  #快速停止nginx
nginx -V #查看版本，以及配置文件地址
nginx -v #查看版本
nginx -s reload|reopen|stop|quit   #重新加载配置|重启|快速停止|安全关闭nginx
nginx -h #帮助
```

```
$ nginx -h #帮助
nginx version: nginx/1.10.1
Usage: nginx [-?hvVtTq] [-s signal] [-c filename] [-p prefix] [-g directives]

Options:
  -?,-h         : this help
  -v            : show version and exit
  -V            : show version and configure options then exit
  -t            : test configuration and exit
  -T            : test configuration, dump it and exit
  -q            : suppress non-error messages during configuration testing
  -s signal     : send signal to a master process: stop, quit, reopen, reload
  -p prefix     : set prefix path (default: /usr/local/Cellar/nginx/1.10.1/)
  -c filename   : set configuration file (default: /usr/local/etc/nginx/nginx.conf)
  -g directives : set global directives out of configuration file
```



## 卸载：

```
brew uninstall nginx
```



