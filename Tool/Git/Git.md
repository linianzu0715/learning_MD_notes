[toc]

```
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```



Git 工作流程：

https://www.runoob.com/git/git-workflow.html



# 1、查看配置信息

查看系统的配置信息：

```
git config --system --list
```

查看当前用户的配置信息：

```
git config --global  --list
```

查看当前仓库配置信息

```
git config --local  --list
```



# 2、GIT修改用户名和邮箱：

用户名和邮箱地址是本地 git 客户端的一个变量，不随git库而改变。每次commit都会用用户名和邮箱纪录。github的 contributions 统计就是按邮箱来统计的。



- 修改当前project
  用户名的命令为：git config user.name 你的目标用户名;
  提交邮箱命令为：git config user.email 你的目标邮箱名;
- git修改全局项目
  git config --global user.name你的目标用户名；
  git config --global user.email 你的目标邮箱名;



# 3、删除本地分支

通过 git branch -d \<branch> 删除一个分支，比如： git branch -d fix/authentication。 当一个分支被推送并合并到远程分支后， -d 才会在本地删除该分支。 如果一个分支还没有被推送或者合并，那么可以使用 -D 强制删除它。 这就是本地删除分支的方法。



# 4、git add

### 4.1 git add  指令的作用？

就改动的内容加入到暂存区。

### 4.2 指令执行的时候会发生什么？

当对工作区修改（或新增）的文件执行 **git add** 命令时，暂存区的目录树被更新，同时工作区修改（或新增）的文件内容被写入到对象库中的一个新的对象中，而该对象的ID被记录在暂存区的文件索引中。



# 5、git commit

### 5.1 git commit 指令的作用？

git commit 命令将暂存区内容添加到本地仓库中。



### 5.2 git commit -m [message]?

[message] 可以是一些备注信息，备注本次提交的改动。



# 6、git clone 

### 6.1 git clone复制代码？

```shell
git clone + (https link)
```



# 7、git push

### 7.1 git push 指令的作用？

**git push** 命用于从将本地的分支版本上传到远程并合并。



### 7.2 git push <远程主机名> <本地分支名>:<远程分支名>？

将本地分支代码上传到远程分支，本地分支名和远程分支名可能不同。



### 7.3 git push <远程主机名> <本地分支名>？

将本地分支代码上传到远程分支，本地分支名和远程分支名需要相同。

