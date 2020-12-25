## Bash shell

[toc]

### 创建Bash脚本

使用`cd`命令进入将要保存脚本的目录。使用文本编辑器（如`gedit`/`vi`/`vim`命令），并键入shell命令

**脚本的第一行一般如下：**

```shell
#!/bin/bash
echo "Hello World!"
```



### Bash脚本的运行

作为可执行程序。

```sh
chmod +x ./file_name.sh
./file_name.sh
```



### 变量和函数：

#### 变量定义和求值：

```sh
SSH_HOME_DIR = "$HOME/.ssh"
TEMO_FILE = "$SSH_HOME_DIR/.temp_authorized_keys"
```



#### 函数定义和调用

```shell
function help{
		echo "Usage: $0 host user password [port, default 22]"
		return 1
}
help 
echo $?
```





