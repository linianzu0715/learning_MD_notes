#### shell

##### [192. 统计词频](https://leetcode-cn.com/problems/word-frequency/)

写一个 bash 脚本以统计一个文本文件 words.txt 中每个单词出现的频率。为了简单起见，你可以假设：

* words.txt只包括小写字母和 ' ' 。

* 每个单词只由小写字母组成。

* 单词间由一个或多个空格字符分隔。

  示例:

假设 words.txt 内容如下：

the day is sunny the the
the sunny is is
你的脚本应当输出（以词频降序排列）：

the 4
is 3
sunny 2
day 1



```bash
awk '{for(i=1;i<=NF;i++){asso_array[$i]++;}};END{for(w in asso_array){print w,asso_array[w];}}' words.txt | sort -rn -k2

# awk '{for(i=1;i<=NF;i++){asso_array[$i]++;}};END{for(w in asso_array){print w,asso_array[w];}}' words.txt
#取出每一个单词 然后加入到一个字典中  取出字典的key 和 value， -rn 按照降序排列 -k2 选择第二个为key
```



```bash
cat words.txt | xargs -n1 | sort | uniq -c | sort -rn | awk '{print $2,$1}'

#分割单词 然后计算每个单词出现的次数 然后按照次数降序排列
```



##### [195. 第十行](https://leetcode-cn.com/problems/tenth-line/)

给定一个文本文件 file.txt，请只打印这个文件中的第十行。

示例:

假设 file.txt 有如下内容：

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
你的脚本应当显示第十行：

Line 10

```bash
awk 'NR==10' file.txt
```



##### [194. 转置文件](https://leetcode-cn.com/problems/transpose-file/)

给定一个文件 `file.txt`，转置它的内容。

你可以假设每行列数相同，并且每个字段由 `' '` 分隔.



示例:

假设 file.txt 文件内容如下：

name age
alice 21
ryan 30

应当输出：

name alice ryan
age 21 30



awk是一行一行地处理文本文件，运行流程是：

* 先运行BEGIN后的{Action}，相当于表头
* 再运行{Action}中的文件处理主体命令
* 最后运行END后的{Action}中的命令

有几个经常用到的`awk`常量：`NF`是当前行的`field`字段数；`NR`是正在处理的当前行数。

注意到是转置，假如原始文本有m行n列（字段），那么转置后的文本应该有n行m列，即原始文本的每个字段都对应新文本的一行。我们可以用数组res来储存新文本，将新文本的每一行存为数组res的一个元素。

在END之前我们遍历file.txt的每一行，并做一个判断：在第一行时，每碰到一个字段就将其按顺序放在res数组中；从第二行开始起，每碰到一个字段就将其追加到对应元素的末尾（中间添加一个空格）。

文本处理完了，最后需要输出。在`END`后遍历数组，输出每一行。注意`printf`不会自动换行，而`print`会自动换行。



```bash
awk '{
    for (i=1;i<=NF;i++){
        if (NR==1){
            res[i]=$i
        }
        else{
            res[i]=res[i]" "$i
        }
    }
}END{
    for(j=1;j<=NF;j++){
        print res[j]
    }
}' file.txt

```



##### [193. 有效电话号码](https://leetcode-cn.com/problems/valid-phone-numbers/)

给定一个包含电话号码列表（一行一个电话号码）的文本文件 file.txt，写一个 bash 脚本输出所有有效的电话号码。

你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）

你也可以假设每行前后没有多余的空格字符。

假设 file.txt 内容如下：

987-123-4567
123 456 7890
(123) 456-7890
你的脚本应当输出下列有效的电话号码：

987-123-4567
(123) 456-7890

1. 思路：

题目的核心是匹配符合规则的字符串，因为规则比较单一，所以使用正则表达式来检索符合要求的字符串即可。

2. 规则分析
   (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）

从规则中可以看出，只要符合上述形势的数字组合即可。

分析 (xxx) xxx-xxxx
我们把其中的规律列出来，找出固定的字符位置与可变字符的规律

![image.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/94e28bb2dbe4b71358356b1e312b19bb76f9e088ea2889aaedb13a3e00ee4da1-image.png)

最终需要用正则表达式中的普通字符、特殊字符、限定符、定位符来描述对应的规律(如上图所示)

3. 使用正则表达式描述规律
   个人感觉，正则表达式的重点有三：特殊字符、限定字符、定位符
   熟练掌握这三点，大部分的正则表达都不在话下~

特殊字符：勿忘加上转义符'\'
限定字符：限定字符出现的次数，掌握它也就get了精华，麻麻再也不用担心我读不懂漂亮的表达式了。
定位符：稍加理解，就能get到的好技巧

3.1 使用正则表达式描述上面的内容

表达 (xxx) xxx-xxxx:

```
^\([0-9][0-9][0-9]\) [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$
```

使用限定符来限定数字出现的次数，优化为如下表达

```
^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$
```

表达 xxx-xxx-xxxx

```
[0-9]{3}-[0-9]{3}-[0-9]{4}$
```

同时表示xxx-xxx-xxxx和 (xxx) xxx-xxxx:

```
^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$
```



```
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
```

