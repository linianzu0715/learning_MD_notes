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



1. 用户名和邮箱地址的作用：

用户名和邮箱地址是本地 git 客户端的一个变量，不随git库而改变。每次commit都会用用户名和邮箱纪录。github的 contributions 统计就是按邮箱来统计的。

2. 查看用户名和邮箱地址：

```java
$ git config user.name
$ git config user.email
```

3. 修改用户名和邮箱地址：

```shell
$ git config --global user.name "username"
$ git config --global user.email "email"
```



## 查看配置信息

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



## GIT修改用户名和邮箱：

- 修改当前project
  用户名的命令为：git config user.name 你的目标用户名;
  提交邮箱命令为：git config user.email 你的目标邮箱名;
- git修改全局项目
  git config --global user.name你的目标用户名；
  git config --global user.email 你的目标邮箱名;





```
PlatformOrderMsgListener

PlatformPayFinishProcessor
```