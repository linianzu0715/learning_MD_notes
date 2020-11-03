## 目录

[toc]



## 方法覆盖和方法重写

1. 方法重载 (overload)：在一个类中有两个或者多个方法有相同的方法名称，但是是不同的参数列表

2. 方法重写 (override)：子类重新定义了父类的方法。方法覆盖要求是相同的方法名称，参数和返回值。



## 正则表达式

* 正则表达式定义了字符串的模式。

* 正则表达式可以用来搜索、编辑或处理文本。

* 正则表达式并不仅限于某一种语言，但是在每种语言中有细微的差别。



一个字符串其实就是一个简单的正则表达式，例如 **Hello World** 正则表达式匹配 "Hello World" 字符串。

**.**（点号）也是一个正则表达式，它匹配任何一个字符如："a" 或 "1"。

下表列出了一些正则表达式的实例及描述：

| 正则表达式       | 描述                                                         |
| :--------------- | :----------------------------------------------------------- |
| this is text     | 匹配字符串 "this is text"                                    |
| this\s+is\s+text | 注意字符串中的 **\s+**。匹配单词 "this" 后面的 **\s+** 可以匹配多个空格，之后匹配 is 字符串，再之后 **\s+** 匹配多个空格然后再跟上 text 字符串。可以匹配这个实例：this is text |
| ^\d+(\.\d+)?     | ^ 定义了以什么开始\d+ 匹配一个或多个数字? 设置括号内的选项是可选的\. 匹配 "."可以匹配的实例："5", "1.5" 和 "2.21"。 |

java.util.regex 包主要包括以下三个类：

- **Pattern 类：**

  pattern 对象是一个正则表达式的编译表示。Pattern 类没有公共构造方法。要创建一个 Pattern 对象，你必须首先调用其公共静态编译方法，它返回一个 Pattern 对象。该方法接受一个正则表达式作为它的第一个参数。

- **Matcher 类：**

  Matcher 对象是对输入字符串进行解释和匹配操作的引擎。与Pattern 类一样，Matcher 也没有公共构造方法。你需要调用 Pattern 对象的 matcher 方法来获得一个 Matcher 对象。

- **PatternSyntaxException：**

  PatternSyntaxException 是一个非强制异常类，它表示一个正则表达式模式中的语法错误。



**正则表达式语法**

在其他语言中，**\\** 表示：**我想要在正则表达式中插入一个普通的（字面上的）反斜杠，请不要给它任何特殊的意义。**

在 Java 中，**\\** 表示：**我要插入一个正则表达式的反斜线，所以其后的字符具有特殊的意义。**

所以，在其他的语言中（如Perl），一个反斜杠 \ 就足以具有转义的作用，而在 Java 中正则表达式中则需要有两个反斜杠才能被解析为其他语言中的转义作用。也可以简单的理解在 Java 的正则表达式中，两个 **\\** 代表其他语言中的一个 \，这也就是为什么表示一位数字的正则表达式是 \\\d，而表示一个普通的反斜杠是 \\\\\\\。

| 字符          | 说明                                                         |
| :------------ | :----------------------------------------------------------- |
| \             | 将下一字符标记为特殊字符、文本、反向引用或八进制转义符。例如，"n"匹配字符"n"。"\n"匹配换行符。序列"\\\\"匹配"\\"，"\\("匹配"("。 |
| ^             | 匹配输入字符串开始的位置。如果设置了 **RegExp** 对象的 **Multiline** 属性，^ 还会与"\n"或"\r"之后的位置匹配。 |
| $             | 匹配输入字符串结尾的位置。如果设置了 **RegExp** 对象的 **Multiline** 属性，$ 还会与"\n"或"\r"之前的位置匹配。 |
| *             | 零次或多次匹配前面的字符或子表达式。例如，zo* 匹配"z"和"zoo"。* 等效于 {0,}。 |
| +             | 一次或多次匹配前面的字符或子表达式。例如，"zo+"与"zo"和"zoo"匹配，但与"z"不匹配。+ 等效于 {1,}。 |
| ?             | 零次或一次匹配前面的字符或子表达式。例如，"do(es)?"匹配"do"或"does"中的"do"。? 等效于 {0,1}。 |
| {*n*}         | *n* 是非负整数。正好匹配 *n* 次。例如，"o{2}"与"Bob"中的"o"不匹配，但与"food"中的两个"o"匹配。 |
| {*n*,}        | *n* 是非负整数。至少匹配 *n* 次。例如，"o{2,}"不匹配"Bob"中的"o"，而匹配"foooood"中的所有 o。"o{1,}"等效于"o+"。"o{0,}"等效于"o*"。 |
| {*n*,*m*}     | *m* 和 *n* 是非负整数，其中 *n* <= *m*。匹配至少 *n* 次，至多 *m* 次。例如，"o{1,3}"匹配"fooooood"中的头三个 o。'o{0,1}' 等效于 'o?'。注意：您不能将空格插入逗号和数字之间。 |
| ?             | 当此字符紧随任何其他限定符（*、+、?、{*n*}、{*n*,}、{*n*,*m*}）之后时，匹配模式是"非贪心的"。"非贪心的"模式匹配搜索到的、尽可能短的字符串，而默认的"贪心的"模式匹配搜索到的、尽可能长的字符串。例如，在字符串"oooo"中，"o+?"只匹配单个"o"，而"o+"匹配所有"o"。 |
| .             | 匹配除"\r\n"之外的任何单个字符。若要匹配包括"\r\n"在内的任意字符，请使用诸如"[\s\S]"之类的模式。 |
| (*pattern*)   | 匹配 *pattern* 并捕获该匹配的子表达式。可以使用 **$0…$9** 属性从结果"匹配"集合中检索捕获的匹配。若要匹配括号字符 ( )，请使用"\("或者"\)"。 |
| (?:*pattern*) | 匹配 *pattern* 但不捕获该匹配的子表达式，即它是一个非捕获匹配，不存储供以后使用的匹配。这对于用"or"字符 (\|) 组合模式部件的情况很有用。例如，'industr(?:y\|ies) 是比 'industry\|industries' 更经济的表达式。 |
| (?=*pattern*) | 执行正向预测先行搜索的子表达式，该表达式匹配处于匹配 *pattern* 的字符串的起始点的字符串。它是一个非捕获匹配，即不能捕获供以后使用的匹配。例如，'Windows (?=95\|98\|NT\|2000)' 匹配"Windows 2000"中的"Windows"，但不匹配"Windows 3.1"中的"Windows"。预测先行不占用字符，即发生匹配后，下一匹配的搜索紧随上一匹配之后，而不是在组成预测先行的字符后。 |
| (?!*pattern*) | 执行反向预测先行搜索的子表达式，该表达式匹配不处于匹配 *pattern* 的字符串的起始点的搜索字符串。它是一个非捕获匹配，即不能捕获供以后使用的匹配。例如，'Windows (?!95\|98\|NT\|2000)' 匹配"Windows 3.1"中的 "Windows"，但不匹配"Windows 2000"中的"Windows"。预测先行不占用字符，即发生匹配后，下一匹配的搜索紧随上一匹配之后，而不是在组成预测先行的字符后。 |
| *x*\|*y*      | 匹配 *x* 或 *y*。例如，'z\|food' 匹配"z"或"food"。'(z\|f)ood' 匹配"zood"或"food"。 |
| [*xyz*]       | 字符集。匹配包含的任一字符。例如，"[abc]"匹配"plain"中的"a"。 |
| [^*xyz*]      | 反向字符集。匹配未包含的任何字符。例如，"[^abc]"匹配"plain"中"p"，"l"，"i"，"n"。 |
| [*a-z*]       | 字符范围。匹配指定范围内的任何字符。例如，"[a-z]"匹配"a"到"z"范围内的任何小写字母。 |
| [^*a-z*]      | 反向范围字符。匹配不在指定的范围内的任何字符。例如，"[^a-z]"匹配任何不在"a"到"z"范围内的任何字符。 |
| \b            | 匹配一个字边界，即字与空格间的位置。例如，"er\b"匹配"never"中的"er"，但不匹配"verb"中的"er"。 |
| \B            | 非字边界匹配。"er\B"匹配"verb"中的"er"，但不匹配"never"中的"er"。 |
| \c*x*         | 匹配 *x* 指示的控制字符。例如，\cM 匹配 Control-M 或回车符。*x* 的值必须在 A-Z 或 a-z 之间。如果不是这样，则假定 c 就是"c"字符本身。 |
| \d            | 数字字符匹配。等效于 [0-9]。                                 |
| \D            | 非数字字符匹配。等效于 [^0-9]。                              |
| \f            | 换页符匹配。等效于 \x0c 和 \cL。                             |
| \n            | 换行符匹配。等效于 \x0a 和 \cJ。                             |
| \r            | 匹配一个回车符。等效于 \x0d 和 \cM。                         |
| \s            | 匹配任何空白字符，包括空格、制表符、换页符等。与 [ \f\n\r\t\v] 等效。 |
| \S            | 匹配任何非空白字符。与 [^ \f\n\r\t\v] 等效。                 |
| \t            | 制表符匹配。与 \x09 和 \cI 等效。                            |
| \v            | 垂直制表符匹配。与 \x0b 和 \cK 等效。                        |
| \w            | 匹配任何字类字符，包括下划线。与"[A-Za-z0-9_]"等效。         |
| \W            | 与任何非单词字符匹配。与"[^A-Za-z0-9_]"等效。                |
| \x*n*         | 匹配 *n*，此处的 *n* 是一个十六进制转义码。十六进制转义码必须正好是两位数长。例如，"\x41"匹配"A"。"\x041"与"\x04"&"1"等效。允许在正则表达式中使用 ASCII 代码。 |
| \*num*        | 匹配 *num*，此处的 *num* 是一个正整数。到捕获匹配的反向引用。例如，"(.)\1"匹配两个连续的相同字符。 |
| \*n*          | 标识一个八进制转义码或反向引用。如果 \*n* 前面至少有 *n* 个捕获子表达式，那么 *n* 是反向引用。否则，如果 *n* 是八进制数 (0-7)，那么 *n* 是八进制转义码。 |
| \*nm*         | 标识一个八进制转义码或反向引用。如果 \*nm* 前面至少有 *nm* 个捕获子表达式，那么 *nm* 是反向引用。如果 \*nm* 前面至少有 *n* 个捕获，则 *n* 是反向引用，后面跟有字符 *m*。如果两种前面的情况都不存在，则 \*nm* 匹配八进制值 *nm*，其中 *n* 和 *m* 是八进制数字 (0-7)。 |
| \nml          | 当 *n* 是八进制数 (0-3)，*m* 和 *l* 是八进制数 (0-7) 时，匹配八进制转义码 *nml*。 |
| \u*n*         | 匹配 *n*，其中 *n* 是以四位十六进制数表示的 Unicode 字符。例如，\u00A9 匹配版权符号 (©)。 |

**Matcher 类的方法**

**索引方法**

索引方法提供了有用的索引值，精确表明输入字符串中在哪能找到匹配：

| **序号** | **方法及说明**                                               |
| :------- | :----------------------------------------------------------- |
| 1        | **public int start()** 返回以前匹配的初始索引。              |
| 2        | **public int start(int group)**  返回在以前的匹配操作期间，由给定组所捕获的子序列的初始索引 |
| 3        | **public int end()** 返回最后匹配字符之后的偏移量。          |
| 4        | **public int end(int group)** 返回在以前的匹配操作期间，由给定组所捕获子序列的最后字符之后的偏移量。 |

**查找方法**

查找方法用来检查输入字符串并返回一个布尔值，表示是否找到该模式：

| **序号** | **方法及说明**                                               |
| :------- | :----------------------------------------------------------- |
| 1        | **public boolean lookingAt()**  尝试将从区域开头开始的输入序列与该模式匹配。 |
| 2        | **public boolean find()** 尝试查找与该模式匹配的输入序列的下一个子序列。 |
| 3        | **public boolean find(int start****）** 重置此匹配器，然后尝试查找匹配该模式、从指定索引开始的输入序列的下一个子序列。 |
| 4        | **public boolean matches()** 尝试将整个区域与模式匹配。      |

**替换方法**

替换方法是替换输入字符串里文本的方法：

| **序号** | **方法及说明**                                               |
| :------- | :----------------------------------------------------------- |
| 1        | **public Matcher appendReplacement(StringBuffer sb, String replacement)** 实现非终端添加和替换步骤。 |
| 2        | **public StringBuffer appendTail(StringBuffer sb)** 实现终端添加和替换步骤。 |
| 3        | **public String replaceAll(String replacement)**  替换模式与给定替换字符串相匹配的输入序列的每个子序列。 |
| 4        | **public String replaceFirst(String replacement)**  替换模式与给定替换字符串匹配的输入序列的第一个子序列。 |
| 5        | **public static String quoteReplacement(String s)** 返回指定字符串的字面替换字符串。这个方法返回一个字符串，就像传递给Matcher类的appendReplacement 方法一个字面字符串一样工作。 |



**PatternSyntaxException 类的方法**

PatternSyntaxException 是一个非强制异常类，它指示一个正则表达式模式中的语法错误。

PatternSyntaxException 类提供了下面的方法来帮助我们查看发生了什么错误。

| **序号** | **方法及说明**                                               |
| :------- | :----------------------------------------------------------- |
| 1        | **public String getDescription()** 获取错误的描述。          |
| 2        | **public int getIndex()**  获取错误的索引。                  |
| 3        | **public String getPattern()** 获取错误的正则表达式模式。    |
| 4        | **public String getMessage()** 返回多行字符串，包含语法错误及其索引的描述、错误的正则表达式模式和模式中错误索引的可视化指示。 |



## 值传递引用传递

值传递是对基本类型变量而言的，传递的是一个变量的副本，改变副本不会改变原有变量

引用传递一般是对于对象型变量而言，传递的是对象地址的一个副本，而不是对象本身。所以对引用对象进行操作会同时改变原对象。

java中只有值传递。



## Lambda表达式

Lambda 表达式，也可称为闭包，它是推动 Java 8 发布的最重要新特性。

Lambda 允许把函数作为一个方法的参数（函数作为参数传递进方法中）。

使用 Lambda 表达式可以使代码变的更加简洁紧凑。

**语法**

(parameters) -> expression 或 (parameters) ->{ statements; }

以下是lambda表达式的重要特征:

- **可选类型声明：**不需要声明参数类型，编译器可以统一识别参数值。
- **可选的参数圆括号：**一个参数无需定义圆括号，但多个参数需要定义圆括号。
- **可选的大括号：**如果主体包含了一个语句，就不需要使用大括号。
- **可选的返回关键字：**如果主体只有一个表达式返回值则编译器会自动返回值，大括号需要指定明表达式返回了一个数值。

**Lambda 表达式实例**

```java
// 1. 不需要参数,返回值为 5  
() -> 5  
  
// 2. 接收一个参数(数字类型),返回其2倍的值  
x -> 2 * x  
  
// 3. 接受2个参数(数字),并返回他们的差值  
(x, y) -> x – y  
  
// 4. 接收2个int型整数,返回他们的和  
(int x, int y) -> x + y  
  
// 5. 接受一个 string 对象,并在控制台打印,不返回任何值(看起来像是返回void)  
(String s) -> System.out.print(s)
```



## Java跳出多重循环的方式：

1. 利用标识变量 定义一个标识变量，在每层循环中判断这个变量
2. break跳出内循环时，改变外循环的值
3. 利用抛出异常跳出循环
4. 给循环加上标签变量，利用标签变量来跳出。

```java
public class Test1 {
    public static boolean flag = true;   //标识变量
    public static int i = 1;
    public static int j = 1;
    public static void main(String[] args) {
        for (;i<10;i++){
            for(;j<10;j++){
                if(flag){
                    break;
                }
            }
            if(flag) {
                break;
            }
        }
        System.out.println("i="+i+"     j="+j);
    }
}
```

```java
public class Test1 {
    public static int i = 1;
    public static int j = 1;
    public static void main(String[] args) {
        for (;i<10;i++){
            for(;j<10;j++){
                if(j == 4){
                    i = 10;
                    break;
                	}
            	}
            }
        }
        System.out.println("i="+i+"     j="+j);
    }
}
```

```java
public class Test2 {
    public static int i=1;
    public static int j=1;
    public static int max = 10;

    public static void main(String[] args) {
        try {
            for (; i < max; i++) {
                for (; j < max; j++) {
                    throw new Exception("跳出循环");
                }
            }
        } catch (Exception e) {

        }
        System.out.println("i="+i+"     j="+j);
    }
}
```

```java
public class Test3 {
    public static int i = 1;
    public static int j = 1;
    public static int max = 10;

    public static void main(String[] args) {
        label: for (; i < max; i++) {
            for (; j < max; j++) {
                break label;
            }
        }
        System.out.println("i=" + i + "     j=" + j);
    }
}
```



## &和&&的区别

&&运算符是短路与运算。逻辑与和短路与的区别在于，虽然两者都要求左右两端都为True的情况下才能返回True，&&被成为短路与，在于左边的表达式的值为False时，右边的表达式会被短路掉，不会被执行。

&运算符有两种用法：

1. 按位与
2. 逻辑与



## 十进制存储在内存

二进制补码 

1. 负数的补码是将所有的二进制位取反，然后加上
2. 正数的补码就是原来的二进制数。



## 泛型

https://www.cnblogs.com/coprince/p/8603492.html

泛型，即“参数化类型”。顾名思义，就是将类型由原来的具体的类型参数化，类似于方法中的变量参数，此时类型也定义成参数形式（可以称之为类型形参），然后在使用/调用时传入具体的类型（类型实参）。 泛型的本质是为了参数化类型（在不创建新的类型的情况下，通过泛型指定的不同类型来控制形参具体限制的类型）。也就是说在泛型使用过程中，操作的数据类型被指定为一个参数，这种参数类型可以用在类、接口和方法中，分别被称为泛型类、泛型接口、泛型方法。

```java
List arrayList = new ArrayList();
arrayList.add("aaaa");
arrayList.add(100);

for(int i = 0; i< arrayList.size();i++){
    String item = (String)arrayList.get(i);
    Log.d("泛型测试","item = " + item);
}
```

毫无疑问，程序的运行结果会以崩溃结束：

```java
java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String
```

ArrayList可以存放任意类型，例子中添加了一个String类型，添加了一个Integer类型，再使用时都以String的方式使用，因此程序崩溃了。为了解决类似这样的问题（在编译阶段就可以解决），泛型应运而生。我们将第一行声明初始化list的代码更改一下，编译器会在编译阶段就能够帮我们发现类似这样的问题。

```java
List<String> arrayList = new ArrayList<String>();
...
//arrayList.add(100); 在编译阶段，编译器就会报错
```

**特性**

泛型只在编译阶段有效。看下面的代码：

```java
List<String> stringArrayList = new ArrayList<String>();
List<Integer> integerArrayList = new ArrayList<Integer>();

Class classStringArrayList = stringArrayList.getClass();
Class classIntegerArrayList = integerArrayList.getClass();

if(classStringArrayList.equals(classIntegerArrayList)){
    Log.d("泛型测试","类型相同");
}
```

输出结果：`D/泛型测试: 类型相同`。

通过上面的例子可以证明，在编译之后程序会采取去泛型化的措施。也就是说Java中的泛型，只在编译阶段有效。在编译过程中，正确检验泛型结果后，会将泛型的相关信息擦出，并且在对象进入和离开方法的边界处添加类型检查和类型转换的方法。也就是说，泛型信息不会进入到运行时阶段。

对此总结成一句话：泛型类型在逻辑上看以看成是多个不同的类型，实际上都是相同的基本类型。

**泛型的使用**

泛型有三种使用方式，分别为：泛型类、泛型接口、泛型方法。

泛型类

泛型类型用于类的定义中，被称为泛型类。通过泛型可以完成对一组类的操作对外开放相同的接口。最典型的就是各种容器类，如：List、Set、Map。

```java
//此处T可以随便写为任意标识，常见的如T、E、K、V等形式的参数常用于表示泛型
//在实例化泛型类时，必须指定T的具体类型
public class Generic<T>{ 
    //key这个成员变量的类型为T,T的类型由外部指定  
    private T key;

    public Generic(T key) { //泛型构造方法形参key的类型也为T，T的类型由外部指定
        this.key = key;
    }

    public T getKey(){ //泛型方法getKey的返回值类型为T，T的类型由外部指定
        return key;
    }
}
```

```java
//泛型的类型参数只能是类类型（包括自定义类），不能是简单类型
//传入的实参类型需与泛型的类型参数类型相同，即为Integer.
Generic<Integer> genericInteger = new Generic<Integer>(123456);

//传入的实参类型需与泛型的类型参数类型相同，即为String.
Generic<String> genericString = new Generic<String>("key_vlaue");
Log.d("泛型测试","key is " + genericInteger.getKey());
Log.d("泛型测试","key is " + genericString.getKey());
```

```java
12-27 09:20:04.432 13063-13063/? D/泛型测试: key is 123456
12-27 09:20:04.432 13063-13063/? D/泛型测试: key is key_vlaue
```

定义的泛型类，就一定要传入泛型类型实参么？并不是这样，在使用泛型的时候如果传入泛型实参，则会根据传入的泛型实参做相应的限制，此时泛型才会起到本应起到的限制作用。如果不传入泛型类型实参的话，在泛型类中使用泛型的方法或成员变量定义的类型可以为任何的类型。

```java
Generic generic = new Generic("111111");
Generic generic1 = new Generic(4444);
Generic generic2 = new Generic(55.55);
Generic generic3 = new Generic(false);

Log.d("泛型测试","key is " + generic.getKey());
Log.d("泛型测试","key is " + generic1.getKey());
Log.d("泛型测试","key is " + generic2.getKey());
Log.d("泛型测试","key is " + generic3.getKey());
```

```
D/泛型测试: key is 111111
D/泛型测试: key is 4444
D/泛型测试: key is 55.55
D/泛型测试: key is false
```



**泛型接口**

泛型接口与泛型类的定义及使用基本相同。泛型接口常被用在各种类的生产器中，可以看一个例子：

```java
//定义一个泛型接口
public interface Generator<T> {
    public T next();
}
```

当实现泛型接口的类，未传入泛型实参时：

```java
/**
 * 未传入泛型实参时，与泛型类的定义相同，在声明类的时候，需将泛型的声明也一起加到类中
 * 即：class FruitGenerator<T> implements Generator<T>{
 * 如果不声明泛型，如：class FruitGenerator implements Generator<T>，编译器会报错："Unknown class"
 */
class FruitGenerator<T> implements Generator<T>{
    @Override
    public T next() {
        return null;
    }
}
```

当实现泛型接口的类，传入泛型实参时：

```java
/**
 * 传入泛型实参时：
 * 定义一个生产器实现这个接口,虽然我们只创建了一个泛型接口Generator<T>
 * 但是我们可以为T传入无数个实参，形成无数种类型的Generator接口。
 * 在实现类实现泛型接口时，如已将泛型类型传入实参类型，则所有使用泛型的地方都要替换成传入的实参类型
 * 即：Generator<T>，public T next();中的的T都要替换成传入的String类型。
 */
public class FruitGenerator implements Generator<String> {

    private String[] fruits = new String[]{"Apple", "Banana", "Pear"};

    @Override
    public String next() {
        Random rand = new Random();
        return fruits[rand.nextInt(3)];
    }
}
```

**泛型通配符**

我们知道`Ingeter`是`Number`的一个子类，同时在特性章节中我们也验证过`Generic<Ingeter>`与`Generic<Number>`实际上是相同的一种基本类型。那么问题来了，在使用`Generic<Number>`作为形参的方法中，能否使用`Generic<Ingeter>`的实例传入呢？在逻辑上类似于`Generic<Number>`和`Generic<Ingeter>`是否可以看成具有父子关系的泛型类型呢？

为了弄清楚这个问题，我们使用`Generic<T>`这个泛型类继续看下面的例子：

```java
public void showKeyValue1(Generic<Number> obj){
    Log.d("泛型测试","key value is " + obj.getKey());
}
```

```java
Generic<Integer> gInteger = new Generic<Integer>(123);
Generic<Number> gNumber = new Generic<Number>(456);

showKeyValue(gNumber);

// showKeyValue这个方法编译器会为我们报错：Generic<java.lang.Integer> 
// cannot be applied to Generic<java.lang.Number>
// showKeyValue(gInteger);
```

通过提示信息我们可以看到`Generic<Integer>`不能被看作为``Generic<Number>`的子类。由此可以看出:同一种泛型可以对应多个版本（因为参数类型是不确定的），不同版本的泛型类实例是不兼容的。

回到上面的例子，如何解决上面的问题？总不能为了定义一个新的方法来处理`Generic<Integer>`类型的类，这显然与java中的多台理念相违背。因此我们需要一个在逻辑上可以表示同时是`Generic<Integer>`和`Generic<Number>`父类的引用类型。由此类型通配符应运而生。

我们可以将上面的方法改一下：

```java
public void showKeyValue1(Generic<?> obj){
    Log.d("泛型测试","key value is " + obj.getKey());
}
```

类型通配符一般是使用？代替具体的类型实参，注意了，此处’？’是类型实参，而不是类型形参 。重要说三遍！此处’？’是类型实参，而不是类型形参 ！ 此处’？’是类型实参，而不是类型形参 ！再直白点的意思就是，此处的？和Number、String、Integer一样都是一种实际的类型，可以把？看成所有类型的父类。是一种真实的类型。

可以解决当具体类型不确定的时候，这个通配符就是 ? ；当操作类型时，不需要使用类型的具体功能时，只使用Object类中的功能。那么可以用 ? 通配符来表未知类型。

**泛型方法**

在java中,泛型类的定义非常简单，但是泛型方法就比较复杂了。尤其是我们见到的大多数泛型类中的成员方法也都使用了泛型，有的甚至泛型类中也包含着泛型方法，这样在初学者中非常容易将泛型方法理解错了。

泛型类，是在实例化类的时候指明泛型的具体类型；泛型方法，是在调用方法的时候指明泛型的具体类型 。

```java
/**
 * 泛型方法的基本介绍
 * @param tClass 传入的泛型实参
 * @return T 返回值为T类型
 * 说明：
 *     1）public 与 返回值中间<T>非常重要，可以理解为声明此方法为泛型方法。
 *     2）只有声明了<T>的方法才是泛型方法，泛型类中的使用了泛型的成员方法并不是泛型方法。
 *     3）<T>表明该方法将使用泛型类型T，此时才可以在方法中使用泛型类型T。
 *     4）与泛型类的定义一样，此处T可以随便写为任意标识，常见的如T、E、K、V等形式的参数常用于表示泛型。
 */
public <T> T genericMethod(Class<T> tClass)throws InstantiationException ,
  IllegalAccessException{
        T instance = tClass.newInstance();
        return instance;
}
```

```java
Object obj = genericMethod(Class.forName("com.test.test"));
```

**泛型方法的基本用法**

光看上面的例子有的同学可能依然会非常迷糊，我们再通过一个例子，把我泛型方法再总结一下。

```java
public class GenericTest {
   //这个类是个泛型类，在上面已经介绍过
   public class Generic<T>{     
        private T key;

        public Generic(T key) {
            this.key = key;
        }

        //我想说的其实是这个，虽然在方法中使用了泛型，但是这并不是一个泛型方法。
        //这只是类中一个普通的成员方法，只不过他的返回值是在声明泛型类已经声明过的泛型。
        //所以在这个方法中才可以继续使用 T 这个泛型。
        public T getKey(){
            return key;
        }

        /**
         * 这个方法显然是有问题的，在编译器会给我们提示这样的错误信息"cannot reslove symbol E"
         * 因为在类的声明中并未声明泛型E，所以在使用E做形参和返回值类型时，编译器会无法识别。
        public E setKey(E key){
             this.key = keu
        }
        */
    }

    /** 
     * 这才是一个真正的泛型方法。
     * 首先在public与返回值之间的<T>必不可少，这表明这是一个泛型方法，并且声明了一个泛型T
     * 这个T可以出现在这个泛型方法的任意位置.
     * 泛型的数量也可以为任意多个 
     *    如：public <T,K> K showKeyName(Generic<T> container){
     *        ...
     *        }
     */
    public <T> T showKeyName(Generic<T> container){
        System.out.println("container key :" + container.getKey());
        //当然这个例子举的不太合适，只是为了说明泛型方法的特性。
        T test = container.getKey();
        return test;
    }

    //这也不是一个泛型方法，这就是一个普通的方法，只是使用了Generic<Number>这个泛型类做形参而已。
    public void showKeyValue1(Generic<Number> obj){
        Log.d("泛型测试","key value is " + obj.getKey());
    }

    //这也不是一个泛型方法，这也是一个普通的方法，只不过使用了泛型通配符?
    //同时这也印证了泛型通配符章节所描述的，?是一种类型实参，可以看做为Number等所有类的父类
    public void showKeyValue2(Generic<?> obj){
        Log.d("泛型测试","key value is " + obj.getKey());
    }

     /**
     * 这个方法是有问题的，编译器会为我们提示错误信息："UnKnown class 'E' "
     * 虽然我们声明了<T>,也表明了这是一个可以处理泛型的类型的泛型方法。
     * 但是只声明了泛型类型T，并未声明泛型类型E，因此编译器并不知道该如何处理E这个类型。
    public <T> T showKeyName(Generic<E> container){
        ...
    }  
    */

    /**
     * 这个方法也是有问题的，编译器会为我们提示错误信息："UnKnown class 'T' "
     * 对于编译器来说T这个类型并未项目中声明过，因此编译也不知道该如何编译这个类。
     * 所以这也不是一个正确的泛型方法声明。
    public void showkey(T genericObj){

    }
    */

    public static void main(String[] args) {
    }
}
```

**类中的泛型方法**

光看上面的例子有的同学可能依然会非常迷糊，我们再通过一个例子，把我泛型方法再总结一下。

```java
public class GenericFruit {
    class Fruit{
        @Override
        public String toString() {
            return "fruit";
        }
    }

    class Apple extends Fruit{
        @Override
        public String toString() {
            return "apple";
        }
    }

    class Person{
        @Override
        public String toString() {
            return "Person";
        }
    }

    class GenerateTest<T>{
        public void show_1(T t){
            System.out.println(t.toString());
        }

        //在泛型类中声明了一个泛型方法，使用泛型E，这种泛型E可以为任意类型。可以类型与T相同，也可以不同。
        //由于泛型方法在声明的时候会声明泛型<E>，因此即使在泛型类中并未声明泛型，编译器也能够正确识别泛型方法中识别的泛型。
        public <E> void show_3(E t){
            System.out.println(t.toString());
        }

        //在泛型类中声明了一个泛型方法，使用泛型T，注意这个T是一种全新的类型，可以与泛型类中声明的T不是同一种类型。
        public <T> void show_2(T t){
            System.out.println(t.toString());
        }
    }

    public static void main(String[] args) {
        Apple apple = new Apple();
        Person person = new Person();

        GenerateTest<Fruit> generateTest = new GenerateTest<Fruit>();
        //apple是Fruit的子类，所以这里可以
        generateTest.show_1(apple);
        //编译器会报错，因为泛型类型实参指定的是Fruit，而传入的实参类是Person
        //generateTest.show_1(person);

        //使用这两个方法都可以成功
        generateTest.show_2(apple);
        generateTest.show_2(person);

        //使用这两个方法也都可以成功
        generateTest.show_3(apple);
        generateTest.show_3(person);
    }
}
```

 **泛型方法与可变参数**

再看一个泛型方法和可变参数的例子：

```java
public <T> void printMsg( T... args){
    for(T t : args){
        Log.d("泛型测试","t is " + t);
    }
}
```

```
printMsg("111",222,"aaaa","2323.4",55.55);
```

**静态方法与泛型**

静态方法有一种情况需要注意一下，那就是在类中的静态方法使用泛型：静态方法无法访问类上定义的泛型；如果静态方法操作的引用数据类型不确定的时候，必须要将泛型定义在方法上。

即：如果静态方法要使用泛型的话，必须将静态方法也定义成泛型方法 。

```java
public class StaticGenerator<T> {
    ....
    ....
    /**
     * 如果在类中定义使用泛型的静态方法，需要添加额外的泛型声明（将这个方法定义成泛型方法）
     * 即使静态方法要使用泛型类中已经声明过的泛型也不可以。
     * 如：public static void show(T t){..},此时编译器会提示错误信息：
          "StaticGenerator cannot be refrenced from static context"
     */
    public static <T> void show(T t){

    }
}
```

 **泛型方法总结**

泛型方法能使方法独立于类而产生变化，以下是一个基本的指导原则：

```java
无论何时，如果你能做到，你就该尽量使用泛型方法。也就是说，如果使用泛型方法将整个类泛型化，

那么就应该使用泛型方法。另外对于一个static的方法而已，无法访问泛型类型的参数。

所以如果static方法要使用泛型能力，就必须使其成为泛型方法。
```

**泛型上下边界**

在使用泛型的时候，我们还可以为传入的泛型类型实参进行上下边界的限制，如：类型实参只准传入某种类型的父类或某种类型的子类.为泛型添加上边界，即传入的类型实参必须是指定类型的子类型

```java
public void showKeyValue1(Generic<? extends Number> obj){
    Log.d("泛型测试","key value is " + obj.getKey());
}
```

```java
Generic<String> generic1 = new Generic<String>("11111");
Generic<Integer> generic2 = new Generic<Integer>(2222);
Generic<Float> generic3 = new Generic<Float>(2.4f);
Generic<Double> generic4 = new Generic<Double>(2.56);

//这一行代码编译器会提示错误，因为String类型并不是Number类型的子类
//showKeyValue1(generic1);

showKeyValue1(generic2);
showKeyValue1(generic3);
showKeyValue1(generic4);
```

如果我们把泛型类的定义也改一下:

```java
public class Generic<T extends Number>{
    private T key;

    public Generic(T key) {
        this.key = key;
    }

    public T getKey(){
        return key;
    }
}
```

```java
//这一行代码也会报错，因为String不是Number的子类
Generic<String> generic1 = new Generic<String>("11111");
```

再来一个泛型方法的例子：

```java
//在泛型方法中添加上下边界限制的时候，必须在权限声明与返回值之间的<T>上添加上下边界，即在泛型声明的时候添加
//public <T> T showKeyName(Generic<T extends Number> container)，编译器会报错："Unexpected bound"
public <T extends Number> T showKeyName(Generic<T> container){
    System.out.println("container key :" + container.getKey());
    T test = container.getKey();
    return test;
}
```

通过上面的两个例子可以看出：泛型的上下边界添加，必须与泛型的声明在一起 。

**关于泛型数组要提一下**

看到了很多文章中都会提起泛型数组，经过查看sun的说明文档，在java中是”不能创建一个确切的泛型类型的数组”的。也就是说下面的这个例子是不可以的：

```java
List<String>[] ls = new ArrayList<String>[10];  
```

而使用通配符创建泛型数组是可以的，如下面这个例子：

```java
List<?>[] ls = new ArrayList<?>[10]; 
```

这样也是可以的：

```java
List<String>[] ls = new ArrayList[10];
```

下面使用[Sun](http://docs.oracle.com/javase/tutorial/extra/generics/fineprint.html)[的一篇文档](http://docs.oracle.com/javase/tutorial/extra/generics/fineprint.html)的一个例子来说明这个问题：

```java
List<String>[] lsa = new List<String>[10]; // Not really allowed.    
Object o = lsa;    
Object[] oa = (Object[]) o;    
List<Integer> li = new ArrayList<Integer>();    
li.add(new Integer(3));    
oa[1] = li; // Unsound, but passes run time store check    
String s = lsa[1].get(0); // Run-time error: ClassCastException.
```

```
这种情况下，由于JVM泛型的擦除机制，在运行时JVM是不知道泛型信息的，所以可以给oa[1]赋上一个ArrayList而不会出现异常，

但是在取出数据的时候却要做一次类型转换，所以就会出现ClassCastException，如果可以进行泛型数组的声明，

上面说的这种情况在编译期将不会出现任何的警告和错误，只有在运行时才会出错。

而对泛型数组的声明进行限制，对于这样的情况，可以在编译期提示代码有类型安全问题，比没有任何提示要强很多。
```

下面采用通配符的方式是被允许的:数组的类型不可以是类型变量，除非是采用通配符的方式，因为对于通配符的方式，最后取出数据是要做显式的类型转换的。





## 编程语言

### Java和Javascript

1. Java和Javascript没有任何关系。java是是由Sun 公司于1995年5月推出的，而javascript是于1995年由Netscape公司设计实现而成的，由于Netscape公司与Sun公司合作，Netscape高层希望它看上去能够像Java，因此取名为JavaScript。
2. java是一种可以撰写跨平台应用软件的面向对象的程序设计语言；而JavaScript是一种直译式脚本语言，它本身提供了非常丰富的内部对象供设计人员使用。
3. Java是介于解释型和编译型语言之间的一种语言。java的源代码在传递到客户端执行之前，必须经过编译，通过相应平台上的解释器，实现独立于某个特定的平台编译代码的束缚。JavaScript是一种解释性编程语言，其源代码在发往客户执行之前不需经过编译，而是将文本格式的字符代码发送给客户编由浏览器解释执行。
4. 用途也不一样。java广泛应用于个人PC、数据中心、游戏控制台、科学超级计算机、移动电话和互联网等，而Javascript的用途是:1.嵌入动态文本于HTML页面;2.对浏览器事件做出响应; 3.读写HTML元素;4.在数据被提交到服务器之前验证数据;5.检测访客的浏览器信息; 6.控制cookies，包括创建和修改等。



## 基本类型和拆装箱

### 基本类型

Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

**byte：**

- byte 数据类型是8位、有符号的，以二进制补码表示的整数；
- 最小值是 **-128（-2^7）**；
- 最大值是 **127（2^7-1）**；
- 默认值是 **0**；
- byte 类型用在大型数组中节约空间，主要代替整数，因为 byte 变量占用的空间只有 int 类型的四分之一；
- 例子：byte a = 100，byte b = -50。

**short：**

- short 数据类型是 16 位、有符号的以二进制补码表示的整数
- 最小值是 **-32768（-2^15）**；
- 最大值是 **32767（2^15 - 1）**；
- Short 数据类型也可以像 byte 那样节省空间。一个short变量是int型变量所占空间的二分之一；
- 默认值是 **0**；
- 例子：short s = 1000，short r = -20000。

**int：**

- int 数据类型是32位、有符号的以二进制补码表示的整数；
- 最小值是 **-2,147,483,648（-2^31）**；
- 最大值是 **2,147,483,647（2^31 - 1）**；
- 一般地整型变量默认为 int 类型；
- 默认值是 **0** ；
- 例子：int a = 100000, int b = -200000。

**long：**

- long 数据类型是 64 位、有符号的以二进制补码表示的整数；
- 最小值是 **-9,223,372,036,854,775,808（-2^63）**；
- 最大值是 **9,223,372,036,854,775,807（2^63 -1）**；
- 这种类型主要使用在需要比较大整数的系统上；
- 默认值是 **0L**；
- 例子： long a = 100000L，Long b = -200000L。 "L"理论上不分大小写，但是若写成"l"容易与数字"1"混淆，不容易分辩。所以最好大写。

**float：**

- float 数据类型是单精度、32位、符合IEEE 754标准的浮点数；
- float 在储存大型浮点数组的时候可节省内存空间；
- 默认值是 **0.0f**；
- 浮点数不能用来表示精确的值，如货币；
- 例子：float f1 = 234.5f。

**double：**

- double 数据类型是双精度、64 位、符合IEEE 754标准的浮点数；
- 浮点数的默认类型为double类型；
- double类型同样不能表示精确的值，如货币；
- 默认值是 **0.0d**；
- 例子：double d1 = 123.4。

**boolean：**

- boolean数据类型表示一位的信息；
- 只有两个取值：true 和 false；
- 这种类型只作为一种标志来记录 true/false 情况；
- 默认值是 **false**；
- 例子：boolean one = true。

**char：**

- char类型是一个单一的 16 位 Unicode 字符；
- 最小值是 **\u0000**（即为0）；
- 最大值是 **\uffff**（即为65,535）；
- char 数据类型可以储存任何字符；
- 例子：char letter = 'A';



### 基本类型在JVM中的存储位置：

基本数据类型一定存储在栈中的吗？不是。java中的基本数据类型可能存储在栈中，也可能存储在堆内存中。基本数据类型是放在栈中还是放在堆中，这取决于基本类型在何处声明，下面对数据类型在内存中的存储问题来解释一下：

**一：在方法中声明的变量，即该变量是局部变量，每当程序调用方法时，系统都会为该方法建立一个方法栈，其所在方法中声明的变量就放在方法栈中，当方法结束系统会释放方法栈，其对应在该方法中声明的变量随着栈的销毁而结束，这就局部变量只能在方法中有效的原因。**

在方法中声明的变量可以是基本类型的变量，也可以是引用类型的变量。

1. 当声明是基本类型的变量的时，其变量名及值（变量名及值是两个概念）是放在JAVA虚拟机栈中
2. 当声明的是引用变量时，所声明的变量（该变量实际上是在方法中存储的是内存地址值）是放在JAVA虚拟机的栈中，该变量所指向的对象是放在堆类存中的。

**二：在类中声明的变量是成员变量，也叫全局变量，放在堆中的（因为全局变量不会随着某个方法执行结束而销毁）。**

同样在类中声明的变量即可是基本类型的变量 也可是引用类型的变量

1. 当声明的是基本类型的变量其变量名及其值放在堆内存中的
2. 引用类型时，其声明的变量仍然会存储一个内存地址值，该内存地址值指向所引用的对象。引用变量名和对应的对象仍然存储在相应的堆中



### String非基本类型

不是，String是一个类，是java语言中的字符串。String对象是char的有序集合，并且该值是不可变得。因为java.lang.String类是final类型的，因此不能继承这个类，也不能修改。



### String的底层实现

string的底层是一个字符数组，并且保存了它的hash，用来比较相同性。

```java
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
    /** The value is used for character storage. */
    private final char value[];
  
    /** Cache the hash code for the string */
    private int hash; // Default to 0
  
    /**
     * 无参数构造器
     * Initializes a newly created {@code String} object so that it represents
     * an empty character sequence.  Note that use of this constructor is
     * unnecessary since Strings are immutable.
     */
    public String() {
        this.value = "".value;
    }
  
    /**
     * 带参数的构造器
     * Initializes a newly created {@code String} object so that it represents
     * the same sequence of characters as the argument; in other words, the
     * newly created string is a copy of the argument string. Unless an
     * explicit copy of {@code original} is needed, use of this constructor is
     * unnecessary since Strings are immutable.
     *
     * @param  original
     *         A {@code String}
     */
    public String(String original) {
        this.value = original.value;
        this.hash = original.hash;
    }
}
```



### 基本类型的优点，包装类的优点：

基本类型的优点：

1. 存储在栈中，存储速度比存储在堆中的包装类的实例快

包装类的优点：

1. 自带的方法丰富，集合的元素的对象类型，体检java中一切都是对象的思想
2. 基本类型的包装类都是使用final进行修饰的，无法继承



### 自动拆装箱的场景：

1. 函数参数与返回值

2. 将基本数据类型放入集合类：基本数据类型放入集合类中的时候，会进行自动装箱。
3. 包装类型和基本类型的大小比较：包装类与基本数据类型进行比较运算，是先将包装类进行拆箱成基本数据类型，然后进行比较的。
4. 包装类型的运算：两个包装类型之间的运算，会被自动拆箱成基本类型进行。
5. 三目运算符的使用：

涉及到对象的情形需要自动包装。涉及到运算的时候需要自动拆箱。



## 容器类

### 创建数组Array的三种方式

```java
public static void main(String args[])
    {
        // 测试创建数组的三种方式
        System.out.println("----test1----");
        Test1();

        System.out.println("----test2----");
        Test2();

        System.out.println("----test3----");
        Test3();
    }

    private static void Test1(){
        // 第一种
        int[] test1 = new int[5];
        for(int i = 0; i < 5; i++){
            test1[i] = i;
            System.out.println(test1[i]);
        }
    }

    private static void Test2(){
        // 第二种
        int[] test2 = {0,1,2,3,4};
        for(int i = 0; i < 5; i++){
            System.out.println(test2[i]);
        }
    }

    private static void Test3(){
        int[] test3;
        test3 = new int[5];
        for(int i = 0; i < 5; i++){
            test3[i] = i;
            System.out.println(test3[i]);
        }
    }
```



### 数组Array的底层实现

数组对于每一门编程语言来说都是重要的数据结构之一。Java 语言中提供的数组是用来存储固定大小的同类型元素。带有一个属性length。



### 继承架构

Collection接口：

* List接口: Arraylist, LInkedList, Vector
* Set接口: HashSet, TreeSet, LinkedHashSet

Map接口：

HashTable, HashMap, WeakHashMap



### collection和colletions的区别？

collection是集合类的上级接口，继承它的接口有set和list

collections是针对集合类的一个帮助类，它提供一系列静态方法实现对各种集合的搜索，排序，线程安全化的操作。



### List接口

Java 集合框架中有一个“List”接口，表示：**元素有序排列的集合序列（Sequence）**，也被称为**线性表**、**列表**。线性表内部的元素按先后顺序依次排列，相同元素可以重复出现。

Java 集合框架`List`接口继承了`Collection`接口，并添加了对列表元素以**索引方式**进行访问的方法，你可以将一枚元素添加到列表的指定位置，**列表索引从零开始（Zero-Based）**。



#### List接口实现类

Java 集合框架对`List`接口有两类实现：**数组（Resizable Array）**与**链表（Linked List）**。

- `ArrayList`：数组实现
- `LinkedList`：链表实现

两种实现各有优势，`ArrayList`在随机存/取元素（`get/set`）方面性能优异，但在添加/移除（`add/remove`）元素方面速度较慢；`LinkedList`在添加/移除（`add/remove`）元素方面性能出色，在随机存/取元素（`get/set`）方面速度较慢，根据实际使用场景，选择合适的实现类。



#### Arraylist的底层实现

**ArrayList概述**

ArrayList是基于数组实现的，是一个动态数组，其容量能自动增长，类似于C语言中的动态申请内存，动态增长内存。

ArrayList不是线程安全的，只能用在单线程环境下，多线程环境下可以考虑用Collections.synchronizedList(List l)函数返回一个线程安全的ArrayList类，也可以使用concurrent并发包下的CopyOnWriteArrayList类。

ArrayList实现了Serializable接口，因此它支持序列化，能够通过序列化传输，实现了RandomAccess接口，支持快速随机访问，实际上就是通过下标序号进行快速访问，实现了Cloneable接口，能被克隆.

每个ArrayList实例都有一个容量，该容量是指用来存储列表元素的数组的大小。它总是至少等于列表的大小。随着向ArrayList中不断添加元素，其容量也自动增长。自动增长会带来数据向新数组的重新拷贝，因此，如果可预知数据量的多少，可在构造ArrayList时指定其容量。在添加大量元素前，应用程序也可以使用ensureCapacity操作来增加ArrayList实例的容量，这可以减少递增式再分配的数量。


注意，此实现不是同步的。如果多个线程同时访问一个ArrayList实例，而其中至少一个线程从结构上修改了列表，那么它必须保持外部同步。

**ArrayList的实现：**

对于ArrayList而言，它实现List接口、底层使用数组保存所有元素。其操作基本上是对数组的操作。下面我们来分析ArrayList的源代码：

 1) 私有属性：

```java
    /** 
      * The array buffer into which the elements of the ArrayList are stored. 
      * The capacity of the ArrayList is the length of this array buffer. 
      */  
     private transient Object[] elementData;  
   
     /** 
      * The size of the ArrayList (the number of elements it contains). 
      * 
      * @serial 
      */  
     private int size;
```

数组 elementData 用来存储元素， size 记录大小。

有个关键字需要解释：transient。

 Java的serialization提供了一种持久化对象实例的机制。当持久化对象时，可能有一个特殊的对象数据成员，我们不想用serialization机制来保存它。为了在一个特定对象的一个域上关闭serialization，可以在这个域前加上关键字transient。

```java
public class UserInfo implements Serializable {  
     // 总共有三个私有变量，一个是序列化版本， 一个是对象的名称，一个是密码，这里的密码变量设置为transient
     private static final long serialVersionUID = 996890129747019948L;  
     private String name;  
     private transient String psw;  
   
     // 使用构造函数，输入名称和密码
     public UserInfo(String name, String psw) {  
         this.name = name;  
         this.psw = psw;  
     }  
   
     // 重写 toString 方法， 打印出对象的名字和密码
     public String toString() {  
         return "name=" + name + ", psw=" + psw;  
     }  
 }  
   
 public class TestTransient {  
     public static void main(String[] args) {  
         // 利用构造函数，创建一个 userInfo 对象
         UserInfo userInfo = new UserInfo("张三", "123456");  
         // 打印出对象信息
         System.out.println(userInfo);  
         try {  
             // 序列化，被设置为transient的属性没有被序列化  
             ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream(  
                     "UserInfo.out"));  
             o.writeObject(userInfo);  
             o.close();  
         } catch (Exception e) {  
             // TODO: handle exception  
             e.printStackTrace();  
         }  
         try {  
             // 重新读取内容  
             ObjectInputStream in = new ObjectInputStream(new FileInputStream( 
                     "UserInfo.out"));  
             UserInfo readUserInfo = (UserInfo) in.readObject();  
             //读取后psw的内容为null  
             System.out.println(readUserInfo.toString());  
         } catch (Exception e) {  
             // TODO: handle exception  
             e.printStackTrace();  
         }  
     }  
 }
```

被标记为transient的属性在对象被序列化的时候不会被保存。



**构造方法**： 

ArrayList提供了三种方式的构造器，可以构造一个默认初始容量为10的空列表、构造一个指定初始容量的空列表以及构造一个包含指定collection的元素的列表，这些元素按照该collection的迭代器返回它们的顺序排列的。

```java
    // ArrayList带容量大小的构造函数。    
    public ArrayList(int initialCapacity) {    
        super();    
        if (initialCapacity < 0)    
            throw new IllegalArgumentException("Illegal Capacity: "+    
                                               initialCapacity);    
        // 新建一个数组    
        this.elementData = new Object[initialCapacity];    
    }    
   
    // ArrayList无参构造函数。默认容量是10。    
    public ArrayList() {    
        this(10);    
    }    
   
    // 创建一个包含collection的ArrayList  ?????? 不太懂  
    public ArrayList(Collection<? extends E> c) {    
        elementData = c.toArray();    
        size = elementData.length;    
        if (elementData.getClass() != Object[].class)    
            elementData = Arrays.copyOf(elementData, size, Object[].class);    
    }
```



**元素存储：**

ArrayList提供了set(int index, E element)、add(E e)、add(int index, E element)、addAll(Collection<? extends E> c)、addAll(int index, Collection<? extends E> c)这些添加元素的方法。下面我们一一讲解：

```java
// 用指定的元素替代此列表中指定位置上的元素，并返回以前位于该位置上的元素。  
public E set(int index, E element) {  
   RangeCheck(index);  
 
   E oldValue = (E) elementData[index];  
   elementData[index] = element;  
   return oldValue;  
}    
// 将指定的元素添加到此列表的尾部。  
public boolean add(E e) {  
   ensureCapacity(size + 1);   
   elementData[size++] = e;  
   return true;  
}    
// 将指定的元素插入此列表中的指定位置。  
// 如果当前位置有元素，则向右移动当前位于该位置的元素以及所有后续元素（将其索引加1）。  
public void add(int index, E element) {  
   if (index > size || index < 0)  
       throw new IndexOutOfBoundsException("Index: "+index+", Size: "+size);  
   // 如果数组长度不足，将进行扩容。  
   ensureCapacity(size+1);  // Increments modCount!!  
   // 将 elementData中从Index位置开始、长度为size-index的元素，  
   // 拷贝到从下标为index+1位置开始的新的elementData数组中。  
   // 即将当前位于该位置的元素以及所有后续元素右移一个位置。  
   System.arraycopy(elementData, index, elementData, index + 1, size - index);  
   elementData[index] = element;  
   size++;  
}    
// 按照指定collection的迭代器所返回的元素顺序，将该collection中的所有元素添加到此列表的尾部。  
public boolean addAll(Collection<? extends E> c) {  
   Object[] a = c.toArray();  
   int numNew = a.length;  
   ensureCapacity(size + numNew);  // Increments modCount  
   System.arraycopy(a, 0, elementData, size, numNew);  
   size += numNew;  
   return numNew != 0;  
}    
// 从指定的位置开始，将指定collection中的所有元素插入到此列表中。  
public boolean addAll(int index, Collection<? extends E> c) {  
   if (index > size || index < 0)  
       throw new IndexOutOfBoundsException(  
           "Index: " + index + ", Size: " + size);  
 
   Object[] a = c.toArray();  
   int numNew = a.length;  
   ensureCapacity(size + numNew);  // Increments modCount   
   int numMoved = size - index;  
   if (numMoved > 0)  
       System.arraycopy(elementData, index, elementData, index + numNew, numMoved);  
 
   System.arraycopy(a, 0, elementData, index, numNew);  
   size += numNew;  
   return numNew != 0;  
   } 
```

书上都说ArrayList是基于数组实现的，属性中也看到了数组，具体是怎么实现的呢？比如就这个添加元素的方法，如果数组大，则在将某个位置的值设置为指定元素即可，如果数组容量不够了呢？

看到add(E e)中先调用了ensureCapacity(size+1)方法，之后将元素的索引赋给elementData[size]，而后size自增。例如初次添加时，size为0，add将elementData[0]赋值为e，然后size设置为1（类似执行以下两条语句elementData[0]=e;size=1）。将元素的索引赋给elementData[size]不是会出现数组越界的情况吗？这里关键就在ensureCapacity(size+1)中了。

**元素读取：**

```java
 // 返回此列表中指定位置上的元素。  
 public E get(int index) {  
    RangeCheck(index);  
    return (E) elementData[index];  
  }
```



**元素删除：**

ArrayList提供了根据下标或者指定对象两种方式的删除功能。如下：romove(int index):

```java
// 移除此列表中指定位置上的元素。  
public E remove(int index) {  
   RangeCheck(index);  
 
   modCount++;  
   E oldValue = (E) elementData[index];  
 
   int numMoved = size - index - 1;  
   if (numMoved > 0)  
       System.arraycopy(elementData, index+1, elementData, index, numMoved);  
   elementData[--size] = null; // Let gc do its work  
 
   return oldValue;  
}
```

首先是检查范围，修改modCount，保留将要被移除的元素，将移除位置之后的元素向前挪动一个位置，将list末尾元素置空（null），返回被移除的元素。

remove(Object o)

```java
// 移除此列表中首次出现的指定元素（如果存在）。这是应为ArrayList中允许存放重复的元素。  
public boolean remove(Object o) {  
   // 由于ArrayList中允许存放null，因此下面通过两种情况来分别处理。  
   if (o == null) {  
       for (int index = 0; index < size; index++)  
           if (elementData[index] == null) {  
               // 类似remove(int index)，移除列表中指定位置上的元素。  
               fastRemove(index);  
              return true;  
          }  
   } else {  
       for (int index = 0; index < size; index++)  
            if (o.equals(elementData[index])) {  
              fastRemove(index);  
              return true;  
          }  
       }  
       return false;  
   } 
} 
```

首先通过代码可以看到，当移除成功后返回true，否则返回false。remove(Object o)中通过遍历element寻找是否存在传入对象，一旦找到就调用fastRemove移除对象。为什么找到了元素就知道了index，不通过remove(index)来移除元素呢？因为fastRemove跳过了判断边界的处理，因为找到元素就相当于确定了index不会超过边界，而且fastRemove并不返回被移除的元素。下面是fastRemove的代码，基本和remove(index)一致。

```java
private void fastRemove(int index) {  
         modCount++;  
         int numMoved = size - index - 1;  
         if (numMoved > 0)  
             System.arraycopy(elementData, index+1, elementData, index,  
                              numMoved);  
         elementData[--size] = null; // Let gc do its work  
}
```

removeRange(int fromIndex,int toIndex)

```java
protected void removeRange(int fromIndex, int toIndex) {  
     modCount++;  
     int numMoved = size - toIndex;  
         System.arraycopy(elementData, toIndex, elementData, fromIndex,  
                          numMoved);  
   
     // Let gc do its work  
     int newSize = size - (toIndex-fromIndex);  
     while (size != newSize)  
         elementData[--size] = null;  
} 
```

执行过程是将elementData从toIndex位置开始的元素向前移动到fromIndex，然后将toIndex位置之后的元素全部置空顺便修改size。

  这个方法是protected，及受保护的方法，为什么这个方法被定义为protected呢？

  这是一个解释，但是可能不容易看明白。http://stackoverflow.com/questions/2289183/why-is-javas-abstractlists-removerange-method-protected

  先看下面这个例子.

```java
ArrayList<Integer> ints = new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3, 4, 5, 6));  
// fromIndex low endpoint (inclusive) of the subList  
// toIndex high endpoint (exclusive) of the subList  
ints.subList(2, 4).clear();  
System.out.println(ints); 
```

输出结果是[0, 1, 4, 5, 6]，结果是不是像调用了removeRange(int fromIndex,int toIndex)！哈哈哈，就是这样的。但是为什么效果相同呢？是不是调用了removeRange(int fromIndex,int toIndex)呢？



**调整数组容量ensureCapacity：**

从上面介绍的向ArrayList中存储元素的代码中，我们看到，每当向数组中添加元素时，都要去检查添加后元素的个数是否会超出当前数组的长度，如果超出，数组将会进行扩容，以满足添加数据的需求。数组扩容通过一个公开的方法ensureCapacity(int minCapacity)来实现。在实际添加大量元素前，我也可以使用ensureCapacity来手动增加ArrayList实例的容量，以减少递增式再分配的数量。

```java
public void ensureCapacity(int minCapacity) {  
    modCount++;  
    int oldCapacity = elementData.length;  
    if (minCapacity > oldCapacity) {  
        Object oldData[] = elementData;  
        int newCapacity = (oldCapacity * 3)/2 + 1;  //增加50%+1
            if (newCapacity < minCapacity)  
                newCapacity = minCapacity;  
      // minCapacity is usually close to size, so this is a win:  
      elementData = Arrays.copyOf(elementData, newCapacity);  
    }  
 }
```

从上述代码中可以看出，数组进行扩容时，会将老数组中的元素重新拷贝一份到新的数组中，每次数组容量的增长大约是其原容量的1.5倍。这种操作的代价是很高的，因此在实际使用时，我们应该尽量避免数组容量的扩张。当我们可预知要保存的元素的多少时，要在构造ArrayList实例时，就指定其容量，以避免数组扩容的发生。或者根据实际需求，通过调用ensureCapacity方法来手动增加ArrayList实例的容量。

Object oldData[] = elementData;//为什么要用到oldData[]
乍一看来后面并没有用到关于oldData， 这句话显得多此一举！但是这是一个牵涉到内存管理的类， 所以要了解内部的问题。 而且为什么这一句还在if的内部，这跟elementData = Arrays.copyOf(elementData, newCapacity); 这句是有关系的，下面这句Arrays.copyOf的实现时新创建了newCapacity大小的内存，然后把老的elementData放入。好像也没有用到oldData，有什么问题呢。问题就在于旧的内存的引用是elementData， elementData指向了新的内存块，如果有一个局部变量oldData变量引用旧的内存块的话，在copy的过程中就会比较安全，因为这样证明这块老的内存依然有引用，分配内存的时候就不会被侵占掉，然后copy完成后这个局部变量的生命期也过去了，然后释放才是安全的。不然在copy的的时候万一新的内存或其他线程的分配内存侵占了这块老的内存，而copy还没有结束，这将是个严重的事情。

 关于ArrayList和Vector区别如下：

- ArrayList在内存不够时默认是扩展50% + 1个，Vector是默认扩展1倍。
- Vector提供indexOf(obj, start)接口，ArrayList没有。
- Vector属于线程安全级别的，但是大多数情况下不使用Vector，因为线程安全需要更大的系统开销。

 ArrayList还给我们提供了将底层数组的容量调整为当前列表保存的实际元素的大小的功能。它可以通过trimToSize方法来实现。代码如下：

```java
public void trimToSize() {  
   modCount++;  
   int oldCapacity = elementData.length;  
   if (size < oldCapacity) {  
       elementData = Arrays.copyOf(elementData, size);  
   }  
}
```

由于elementData的长度会被拓展，size标记的是其中包含的元素的个数。所以会出现size很小 elementData.length 很大的情况，将出现空间的浪费。trimToSize将返回一个新的数组给elementData，元素内容保持不变，length和size相同，节省空间。

**转为静态数组toArray**

注意ArrayList的两个转化为静态数组的toArray方法。

第一个， 调用Arrays.copyOf将返回一个数组，数组内容是size个elementData的元素，即拷贝elementData从0至size-1位置的元素到新数组并返回。

```java
public Object[] toArray() {  
         return Arrays.copyOf(elementData, size);  
 } 
```

第二个，如果传入数组的长度小于size，返回一个新的数组，大小为size，类型与传入数组相同。所传入数组长度与size相等，则将 elementData 复制到传入数组中并返回传入的数组。若传入数组长度大于size，除了复制 elementData 外，还将把返回数组的第size个元素置为空。

```java
public <T> T[] toArray(T[] a) {
        if (a.length < size)
            // Make a new array of a's runtime type, but my contents:
            return (T[]) Arrays.copyOf(elementData, size, a.getClass());
    System.arraycopy(elementData, 0, a, 0, size);
        if (a.length > size)
            a[size] = null;
        return a;
    }
```

Fail-Fast机制： 
ArrayList也采用了快速失败的机制，通过记录modCount参数来实现。在面对并发的修改时，迭代器很快就会完全失败，而不是冒着在将来某个不确定时间发生任意不确定行为的风险。具体介绍请参考这篇文章[深入Java集合学习系列：HashMap的实现原理](http://zhangshixi.iteye.com/blog/672697) 中的Fail-Fast机制。



总结:

关于ArrayList的源码，给出几点比较重要的总结：

1、注意其三个不同的构造方法。无参构造方法构造的ArrayList的容量默认为10，带有Collection参数的构造方法，将Collection转化为数组赋给ArrayList的实现数组elementData。

2、注意扩充容量的方法ensureCapacity。ArrayList在每次增加元素（可能是1个，也可能是一组）时，都要调用该方法来确保足够的容量。当容量不足以容纳当前的元素个数时，就设置新的容量为旧的容量的1.5倍加1，如果设置后的新容量还不够，则直接新容量设置为传入的参数（也就是所需的容量），而后用Arrays.copyof()方法将元素拷贝到新的数组（详见下面的第3点）。从中可以看出，当容量不够时，每次增加元素，都要将原来的元素拷贝到一个新的数组中，非常之耗时，也因此建议在事先能确定元素数量的情况下，才使用ArrayList，否则建议使用LinkedList。

3、ArrayList的实现中大量地调用了Arrays.copyof()和System.arraycopy()方法。我们有必要对这两个方法的实现做下深入的了解。

首先来看Arrays.copyof()方法。它有很多个重载的方法，但实现思路都是一样的，我们来看泛型版本的源码：

```java
public static <T> T[] copyOf(T[] original, int newLength) {  
    return (T[]) copyOf(original, newLength, original.getClass());  
}
```

很明显调用了另一个copyof方法，该方法有三个参数，最后一个参数指明要转换的数据的类型，其源码如下：

```java
public static <T,U> T[] copyOf(U[] original, int newLength, Class<? extends T[]> newType) {  
    T[] copy = ((Object)newType == (Object)Object[].class)  
        ? (T[]) new Object[newLength]  
        : (T[]) Array.newInstance(newType.getComponentType(), newLength);  
    System.arraycopy(original, 0, copy, 0,  
                     Math.min(original.length, newLength));  
    return copy;  
}
```

这里可以很明显地看出，该方法实际上是在其内部又创建了一个长度为newlength的数组，调用System.arraycopy()方法，将原来数组中的元素复制到了新的数组中。

下面来看System.arraycopy()方法。该方法被标记了native，调用了系统的C/C++代码，在JDK中是看不到的，但在openJDK中可以看到其源码。该函数实际上最终调用了C语言的memmove()函数，因此它可以保证同一个数组内元素的正确复制和移动，比一般的复制方法的实现效率要高很多，很适合用来批量处理数组。Java强烈推荐在复制大量数组元素时用该方法，以取得更高的效率。

```java
public static void arraycopy(Object src,
                             int srcPos,
                             Object dest,
                             int destPos,
                             int length)
    src:源数组；	srcPos:源数组要复制的起始位置；
    dest:目的数组；	destPos:目的数组放置的起始位置；	
    length:复制的长度。
```





4、ArrayList基于数组实现，可以通过下标索引直接查找到指定位置的元素，因此查找效率高，但每次插入或删除元素，就要大量地移动元素，插入删除元素的效率低。

5、在查找给定元素索引值等的方法中，源码都将该元素的值分为null和不为null两种情况处理，ArrayList中允许元素为null。



#### ArrayList是否会越界，Array是否会越界

首先我们要知道Array数组中是有越界的现象的。当发生数组越界的时候，系统会抛出一个 java.lang.ArrayIndexOutOfBoundsException 异常。我们来测试一下。

```java
public static void main(String args[]){
        TestArrayOutOfIndex();
    }
private static void TestArrayOutOfIndex(){
        try{
            // 创建一个新的Array，长度为5，内容为{0,1,2,3,4}
            int[] test1 = {0,1,2,3,4};
            // 我们尝试访问7号位置上的元素，这肯定是超出了范围的
            System.out.println(test1[7]);
        }catch (Exception e){
            // 我们打印出抛出的异常是什么
            System.out.println(e);
            // 然后打印出异常中的信息
            System.out.println(e.getMessage());
        }
    }
```



ArrayList并发add()可能会出现数数组下标越界异常。或者我们在使用arraylist.add(int index, object temp)方法往arraylist中添加元素的时候，也有可能发生arraylist越界。

首先是第一种情况：并发add()可能会出现数数组下标越界异常

```java
import java.util.ArrayList;
import java.util.List;
public class TestArraylistOutOfIndex {
    /** 创建一个所有这个类的对象都共享的Arraylist，中间存储的是Integer */
    public static List<Integer> numberList = new ArrayList<Integer>();

    /** 创建一个实现了Runnable接口的内部类 */
    class AddToList implements Runnable{

        int startNum = 0;

        /** 默认构造函数，有一个参数， 为对象的成员变量赋值*/
        public AddToList(int startNum){
            this.startNum = startNum;
        }

        /** 实现接口中的run()方法 */
        public void run() {
            /** 循环一百次 */
            int count = 0;
            while(count < 100){
                /** 线程休眠100ms */
                try{
                    Thread.sleep(100);
                }catch(Exception e){
                    e.printStackTrace();
                }
                /** 将当前对象的成员变量加入到Arraylist */
                numberList.add(startNum);
                /** 打印出当前的结果 */
                System.out.println(Thread.currentThread().getName() + "--" + "第" + (count + 1) + "次进入，添加的数字是：" + numberList.get(numberList.size()-1) + "现在的集合的大小是：" + numberList.size());
                startNum += 2;
                count++;
            }
        }
    }

    public static void main(String[] args) {
        /** 创建两个线程，在线程中各自创建一个对象，这个对象会执行run（）方法 */
        Thread thread1 = new Thread( new TestArraylistOutOfIndex().new AddToList(0));
        Thread thread2 = new Thread( new TestArraylistOutOfIndex().new AddToList(1));
        thread1.start();
        thread2.start();
    }
}
```

在执行这个的时候，系统会抛出 ArrayIndexOutOfBoundsException 异常：

```java
Thread-0--第13次进入，添加的数字是：25现在的集合的大小是：21
Thread-1--第13次进入，添加的数字是：25现在的集合的大小是：21
Exception in thread "Thread-1" Exception in thread "Thread-0" java.lang.ArrayIndexOutOfBoundsException: 22
	at java.util.ArrayList.elementData(ArrayList.java:422)
	at java.util.ArrayList.get(ArrayList.java:435)
	at TestArraylistOutOfIndex$AddToList.run(TestArraylistOutOfIndex.java:32)
	at java.lang.Thread.run(Thread.java:748)
java.lang.ArrayIndexOutOfBoundsException: 22
	at java.util.ArrayList.add(ArrayList.java:463)
	at TestArraylistOutOfIndex$AddToList.run(TestArraylistOutOfIndex.java:30)
	at java.lang.Thread.run(Thread.java:748)
```

这个时候我们就需要看一下add()方法实现的具体的流程

首先，ArrayList是基于数组实现的，是一个动态数组，其容量能自动增长，类似于C语言中的动态申请内存，动态增长内存。对于ArrayList而言，它实现了List接口、底层使用数组保存所有元素。其操作基本上是对数组的操作。

首先我们看一下往Arraylist中加入元素的add方法具体是怎么写的，我们参考到的java jdk的版本为1.8.0_192：

```java
    /**
     * Appends the specified element to the end of this list.
     *
     * @param e element to be appended to this list
     * @return <tt>true</tt> (as specified by {@link Collection#add})
     */
    public boolean add(E e) {
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }
```

在方法中首先调用了ensureCapacityInternal(size + 1); 这个函数的目的是保证数组的容量始终够用，其中size是elementData数组中元组的个数，初始为0。方法中的e是输入的要加入的元素。方法中还有一个变量size，我们看看它是什么：

```java
		/**
     * The size of the ArrayList (the number of elements it contains).
     *
     * @serial
     */
    private int size;
```

这里说明这个变量是arraylist中的一个成员变量吗，这个变量记录着当前的这个arraylist中，保存了（使用了）多少个元素。

然后还是add方法，我们再深入看 ensureCapacityInternal() 的内部是怎么写的：

```java
    private void ensureCapacityInternal(int minCapacity) {
        ensureExplicitCapacity(calculateCapacity(elementData, minCapacity));
    }
```

首先我们将要加入元素的下一个位置作为参数 minCapacity 传入给了 ensureCapacityInternal 方法。这个方法中只有一行，首先要执行的是 calculateCapacity 这个方法。这个方法还有一个参数 elementData。我们需要看看这个全局的参数 elementData 是什么：

```java
     /**
     * The array buffer into which the elements of the ArrayList are stored.
     * The capacity of the ArrayList is the length of this array buffer. Any
     * empty ArrayList with elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA
     * will be expanded to DEFAULT_CAPACITY when the first element is added.
     */
    transient Object[] elementData; // non-private to simplify nested class access
```

来来来我们来翻译一下上面着一段话的介绍：1. elementData 这个数组保存了ArrayList中存储的所有的元素。2. ArrayList 的容量就是这个 elementData 的长度。 3. 一个空的 ArrayList（ elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA）会在它加入第一个元素的时候被扩充为 DEFAULT_CAPACITY。 好了，这下我们知道了，其实Arraylist的存储操作底层就是对这个 elementData 进行操作。 

这下我们知道了这个 elementData 是干什么的，我们可以研究一下 calculateCapacity 这个函数：

```java
		private static int calculateCapacity(Object[] elementData, int minCapacity) {
        if (elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA) {
            return Math.max(DEFAULT_CAPACITY, minCapacity);
        }
        return minCapacity;
    }
```

总结一下这个方法，如果当前的 Arraylist 是空的（ elementData 是初始时候的默认值），就返回当前要加入位置和第一次插入时候的位置和默认容量参数的较大值，如果 Arraylist 不是空的，就直接返回下一个插入的位置。

之后我们就可以看  ensureExplicitCapacity 这个函数的内容：

```java
		private void ensureExplicitCapacity(int minCapacity) {
        modCount++;

        // overflow-conscious code
        if (minCapacity - elementData.length > 0)
            grow(minCapacity);
    }
```

其中 modCount 记录的是数组发生size变化的次数。如果下一个要存储元素的位置超过了当前element的长度，我们就需要调用 grow() 函数来对 arraylist 的容量 （  elementData 的长度）拓展。

```java
    /**
     * Increases the capacity to ensure that it can hold at least the
     * number of elements specified by the minimum capacity argument.
     *
     * @param minCapacity the desired minimum capacity
     */
    private void grow(int minCapacity) {
        // overflow-conscious code
        int oldCapacity = elementData.length;
        int newCapacity = oldCapacity + (oldCapacity >> 1);
        if (newCapacity - minCapacity < 0)
            newCapacity = minCapacity;
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        // minCapacity is usually close to size, so this is a win:
        elementData = Arrays.copyOf(elementData, newCapacity);
    }
```

我们可以看到，oldCapacity 是存储的之前的容量， newCapacity 是存储的新的容量。新的容量的计算的方式是把原有的容量计算一个1.5倍。如果计算出来的新的容量比下一个位置还要少，那就把新的容量定义为下一个加入的位置。然后创建一个新的容量的 array 来创建一个新的 elementData。 到此为止就完成了 elementData 的增长和更新。

然后我们重新回到我们最开始的 add 函数。 elementData[size++] = e; 这一部分是往 elementData 中填充元素。这一行由两个部分组成。首先要在位置上加入这次的元素。然后把 size + 1。

在单线程的情况下，这一行是没有问题的。在单线程运行的情况下，如果 Size = 0，添加一个元素后，此元素在位置 0，而且 Size=1；

而如果是在多线程情况下，比如有两个线程，线程 A 先将元素存放在位置 0。但是此时 CPU 调度线程A暂停，线程 B 得到运行的机会。线程B也向此 ArrayList 添加元素，因为此时 Size 仍然等于 0 （注意哦，我们假设的是添加一个元素是要两个步骤哦，而线程A仅仅完成了步骤1），所以线程B也将元素存放在位置0。然后线程A和线程B都继续运行，都增加 Size 的值。那好，我们来看看 ArrayList 的情况，元素实际上只有一个，存放在位置 0，而 Size 却等于 2。这就是“线程不安全”了。这就解释了为何集合中会出现null。

但是数组下标越界还不能仅仅依靠这个来解释。我们观察发生越界时的数组下标，分别为10、15、22、33、49和73。结合前面讲的数组自动机制，数组初始长度为10，第一次扩容为15=10+10/2，第二次扩容22=15+15/2，第三次扩容33=22+22/2...以此类推，我们不难发现，越界异常都发生在数组扩容之时。

由此给了我想法，我猜想是，由于没有该方法没有同步，导致出现这样一种现象，用第一次异常，即下标为15时的异常举例。当集合中已经添加了14个元素时，一个线程率先进入add()方法，在执行ensureCapacityInternal(size + 1)时，发现还可以添加一个元素，故数组没有扩容，但随后该线程被阻塞在此处。接着另一线程进入add()方法，执行ensureCapacityInternal(size + 1)，由于前一个线程并没有添加元素，故size依然为14，依然不需要扩容，所以该线程就开始添加元素，使得size++，变为15，数组已经满了。而刚刚阻塞在elementData[size++] = e;语句之前的线程开始执行，它要在集合中添加第16个元素，而数组容量只有15个，所以就发生了数组下标越界异常！



**然后是第二种情况**：使用arraylist.add(int index, object temp)方法往arraylist中添加元素出现数数组下标越界异常

众所周知，Java中的arraylist的大小是随着我们添加的元素多少而变化的，于是我们习惯性的以为arraylist就是无限大的，其实不然，arraylist也是有边界的。只是Arraylist在我们加入元素的过程中会自动增加自己的容量，使得一般情况下是不会发生越界。但是如果我们使用arraylist.add(int index, object temp)方法的时候，方法要求我们输入一个索引值，但是arraylist可能还没有自动扩容到索引值那么多，因此这个时候就会发生下表越界的现象。具体arraylist是怎样进行自动扩容的需要参考arraylist的底层实现方式。

```java
     /**
     * Inserts the specified element at the specified position in this
     * list. Shifts the element currently at that position (if any) and
     * any subsequent elements to the right (adds one to their indices).
     *
     * @param index index at which the specified element is to be inserted
     * @param element element to be inserted
     * @throws IndexOutOfBoundsException {@inheritDoc}
     */
    public void add(int index, E element) {
        rangeCheckForAdd(index);

        ensureCapacityInternal(size + 1);  // Increments modCount!!
        System.arraycopy(elementData, index, elementData, index + 1,
                         size - index);
        elementData[index] = element;
        size++;
    }
```





#### ArrayList，Vector和Linkedlist的存储性能和特征

ArrayList和Vector都是使用数组方式存储数据，此数组元素数目大于实际存储的的数据，以便于增加和插入元素，他们都被允许按照序号索引元素，但是插入元素要设计数组元素移动等内存操作，所以索引数据快但是插入数据慢。Vector中的方法啊由于添加了synchronized修饰，因此Vector是线程安全的容器，但是性能上比ArrayList差，因此在java中是遗留容器。

Linkedlist使用双向链表实现存储（将内存中零散的内存单元通过附加的引用关联起来，形成一个可以按照序号索引的线性结构，这种链式存储的方式和数组的连续存储的方式相比，内存的利用率更高）按照序号索引数据需要进行前向和后向遍历，但是插入时只需要几率本项的前后项即可，所以插入的速度很快。

由于ArrayList和Linkedlist都是非线程安全的，如果遇到多个线程同时操作一个容器的情况下，可是使用工具类Collections中的synchronizedList方法将其转化为想线程安全的容器再使用。



#### Array和Arraylist的区别和相似性

首先要说什么是Array。它中文我们称之为“数组”。数组是一个用于存储固定长度的相同类型元素的数据结构。

然后我们再说什么是Arraylist。我们称之为“列表：。总结一下就是说：ArrayList想象成一种“会自动扩增容量的Array（数组）”。 

Array和ArrayList都是Java中两个重要的数据结构，在Java程序中经常使用。并且ArrayList在内部由Array支持，了解Java中的Array和ArrayList之间的差异对于成为一名优秀的Java开发人员也至关重要。

另一方面 ，ArrayList是Java Collection框架中的一个类，它是作为动态数组引入的。由于数组本质上是静态的，即一旦创建后就无法更改数组的大小，因此，如果需要一个可以调整自身大小的数组，则应使用ArrayList。这是Array和ArrayList之间的根本区别。 

------

最好在某些点上对比两者，这更易于理解。因此，让我们看一下可以Array与ArrayList有哪些区别吧。

**1、Implementation**

数组是基础编程组件或数据结构，但ArrayList是Java Collections框架(一个API)中的类。实际上，ArrayList是使用Java中的数组在内部实现的。因为ArrayList是一个类，所以它拥有类的所有属性，例如，您可以创建对象和调用方法，但是Array是Java中的对象，它不提供任何方法。它只提供一个公开的length属性来为您提供数组的长度，并且它长度是固定的。

**2、性能**

由于ArrayList基于数组，因此一定程度上两者性能相当。在某种程度上确实如此，但是由于ArrayList提供了额外的功能，因此ArrayList和数组的性能存在一些差异，主要是在内存使用和CPU时间方面。对于基于索引的访问，ArrayList和array均提供**O(1)**性能，但是如果添加新元素会触发调整大小，则添加在ArrayList中可以为**O(logN)**，因为这涉及在后台创建新并数组从旧数组中复制元素到新的数组。ArrayList中的内存需求也不仅仅是用于存储相同数量对象的数组，例如int[]与ArrayList中相比，int[] 存储20个INT变量所需的内存更少，这是因为ArrayList和wrapper类的对象元数据开销很大。

**3、类型安全性**

ArrayList是类型安全的，因为它支持泛型，泛型允许编译器检查ArrayList中存储的所有对象的类型正确正确。替换，但数组不支持Java中的Generic。这意味着无法进行编译时检查，但是如果您尝试将不正确的[对象存储](https://cloud.tencent.com/product/cos?from=10680)到数组中(例如：将字符串存储到int数组中)，则array通过引发ArrayStoreException来提供运行时类型检查。

**4、通用**

简而言之，ArrayList比普通的数组分散更灵活，因为它是动态的。它可以在需要时自行增长，而Array布局则无法实现。ArrayList中还允许您删除Array无法实现的元素。通过删除，我们的意思不仅是将零分配给相应的索引，还意味着将其余元素向下复制一个索引，而ArrayList中会自动为您完成。

**5、基础数据类型**

如果您首先开始使用ArrayList，那么您将无法在ArrayList上存储基元。这是array和ArrayList之间的关键区别，因为可以提供*存储基本类型和对象*。例如，int []数字有效，但int的ArrayList无效。您如何处理这个问题？假设您想将int原语存储到ArrayList中，那又如何呢？好了，在Java中您可以使用包装器类。因此，如果您只想将int 2存储到ArrayList中，其余的操作将由自动装箱完成。顺便说一句，由于自动装箱，这种差异从Java 5开始并不明显，因为您会看到ArrayList.add(21)完全有效并且可以正常工作。

**6、泛型**

ArrayList 和 Array的另一个重要区别是，前者支持Generic，但者来不支持Generic。由于是协变类型的，因此可以将泛型与它们一起使用。这意味着编译器不可能在编译时检查数组的类型安全性，但他们可以验证Array的类型安全性。那么在用Java编写类型安全的类时如何处理这个问题呢？好了，您可以查看《Effective Java》中内容，在其中可以声明一个像E []这样的副本，然后使用类型转换。

如果您对Java编码技巧与实践更感兴趣，请阅读Joshua Bloch撰写的《Effective Java 中文 第三版》 ，这是值得深读的一本书。在公众号【Java知己】，后台回复：Effective Java，可以获得该书籍。

**7、迭代性**

ArrayList提供了更多的迭代方式，即Array只能通过循环索引一一访问所有元素。例如：针对循环的增强和do-while来遍历数组，但ArrayList还可以使用Iterator和ListIterator类来遍历。

**8、支持的操作**

由于ArrayList在内部由数组支持，因此它公开了Array可能执行的操作，但是鉴于其动态特性，它还没有添加Array无法执行的操作，例如，您可以将元素存储在array和ArrayList中，但是只有ArrayList允许您删除元素。虽然您可以通过分配null使用数组来模拟到相应的索引，除非将多个中间该索引上方的所有元素都向下移动一级，否则它不会像删除。

ArrayList和Array都提供了检索元素的方法，例如ArrayList的get()方法使用索引从数组中获取元素，例如，Array0将返回第一个元素  

。ArrayList还提供了清除和重用的操作，例如clear()和removeAll()，Array不提供该操作，但是您可以循环遍历Array并为每个索引分配null以模拟它。

**9、size()与length**

数组仅提供一个length属性，该属性告诉您数组中的插槽数，即可以存储多少个元素，它不提供任何方法来找出已填充的元素数和多少个插槽为空，即元素。尽管ArrayList确实提供了size()方法，该方法告诉给定时间点存储在ArrayList中的对象数量。size()始终与length不同，这也是ArrayList的容量。

**10、维度**

数组和数组列表之间的另一个显着区别是，数组可以是多维的，例如，您可以具有二维数组或三维数组，这可以表示矩阵和2D地形的非常特殊的数据结构。

------

到目前为止，您已经看到了ArrayList和副本之间的区别，现在让我们集中讨论一些相似之处。由于ArrayList在内部使用数组，因此必然有很多相似之处，如下所示：

**1、数据结构**

两者都允许您将对象存储在Java中，并且彼此都是基于索引的数据结构，可提供O(1)性能来检索元素，但是，如果对进行了排序和使用了二进制搜索算法，则没有索引的搜索仍然是LOG(N) 。

**2、顺序**

Array和AArrayList都保持将元素添加到其中的顺序。

**3、搜索**

您可以使用索引搜索元素，即O(1)，否则，如果未对片段进行排序，则可以使用线性搜索，这大约需要O(n)的时间，也可以在对进行进行排序后使用二进制搜索Java，这是排序+ O(logN)。

**4、空值**

这两个数组和ArrayList允许空值，但请记住只有对象数组允许其存储为空，原始类型不能为空，原始类型为使用默认值。例如：int类型的0与 boolean类型的false 。

**5、复制**

array和ArrayList都允许复制。

**6、性能**

ArrayList模拟数组的性能，例如，如果您知道索引，则可以进行O(1)访问，但是它具有额外的内存开销，因为它是一个对象，并且还拥有其他数据以自动调整ArrayList的大小。

**7、从零开始的索引**

array和ArrayList都有从零开始的索引，即第一个元素从第零个索引开始。

这就是**Java中数组与ArrayList之间真正的区别**的全部。您应该记住的最重要的区别是，Array本质上是静态的，即创建后就无法更改其大小，但是ArrayList是动态数组，如果ArrayList中的元素数大于其阈值，则可以调整自身大小。基于这种差异，如果预先知道大小并确定它不会改变，则应该使用数组作为数据结构来存储对象；如果不确定，则只需使用ArrayList。

------



### Map接口

#### HashMap底层实现原理

哈希表（hash table）也叫散列表，是一种非常重要的数据结构，应用场景及其丰富，许多缓存技术（比如memcached）的核心其实就是在内存中维护一张大的哈希表。



**什么是哈希表**

在讨论哈希表之前，我们先大概了解下其他数据结构在新增，查找等基础操作执行性能

**数组**：采用一段连续的存储单元来存储数据。对于指定下标的查找，时间复杂度为O(1)；通过给定值进行查找，需要遍历数组，逐一比对给定关键字和数组元素，时间复杂度为O(n)，当然，对于有序数组，则可采用二分查找，插值查找，斐波那契查找等方式，可将查找复杂度提高为O(logn)；对于一般的插入删除操作，涉及到数组元素的移动，其平均复杂度也为O(n)

**线性链表**：对于链表的新增，删除等操作（在找到指定操作位置后），仅需处理结点间的引用即可，时间复杂度为O(1)，而查找操作需要遍历链表逐一进行比对，复杂度为O(n)

**二叉树**：对一棵相对平衡的有序二叉树，对其进行插入，查找，删除等操作，平均复杂度均为O(logn)。

**哈希表**：相比上述几种数据结构，在哈希表中进行添加，删除，查找等操作，性能十分之高，不考虑哈希冲突的情况下，仅需一次定位即可完成，时间复杂度为O(1)，接下来我们就来看看哈希表是如何实现达到惊艳的常数阶O(1)的。

我们知道，数据结构的物理存储结构只有两种：**顺序存储结构**和**链式存储结构**（像栈，队列，树，图等是从逻辑结构去抽象的，映射到内存中，也这两种物理组织形式），而在上面我们提到过，在数组中根据下标查找某个元素，一次定位就可以达到，哈希表利用了这种特性，**哈希表的主干就是数组**。

比如我们要新增或查找某个元素，我们通过把当前元素的关键字 通过某个函数映射到数组中的某个位置，通过数组下标一次定位就可完成操作。

**存储位置 = f(关键字)**

其中，这个函数f一般称为**哈希函数**，这个函数的设计好坏会直接影响到哈希表的优劣。举个例子，比如我们要在哈希表中执行插入操作：

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161113180447499-1953916974.png)

查找操作同理，先通过哈希函数计算出实际存储地址，然后从数组中对应地址取出即可。

**哈希冲突**

然而万事无完美，如果两个不同的元素，通过哈希函数得出的实际存储地址相同怎么办？也就是说，当我们对某个元素进行哈希运算，得到一个存储地址，然后要进行插入的时候，发现已经被其他元素占用了，其实这就是所谓的**哈希冲突**，也叫哈希碰撞。前面我们提到过，哈希函数的设计至关重要，好的哈希函数会尽可能地保证 **计算简单**和**散列地址分布均匀,**但是，我们需要清楚的是，数组是一块连续的固定长度的内存空间，再好的哈希函数也不能保证得到的存储地址绝对不发生冲突。那么哈希冲突如何解决呢？哈希冲突的解决方案有多种:开放定址法（发生冲突，继续寻找下一块未被占用的存储地址），再散列函数法，链地址法，而HashMap即是采用了链地址法，也就是**数组+链表**的方式。

**HashMap实现原理**

HashMap的主干是一个Entry数组。Entry是HashMap的基本组成单元，每一个Entry包含一个key-value键值对。

```java
//HashMap的主干数组，可以看到就是一个Entry数组，初始值为空数组{}，主干数组的长度一定是2的次幂，至于为什么这么做，后面会有详细分析。
transient Entry<K,V>[] table = (Entry<K,V>[]) EMPTY_TABLE;
```

 Entry是HashMap中的一个静态内部类。

```java
static class Entry<K,V> implements Map.Entry<K,V> {
    final K key;
    V value;
    Entry<K,V> next;//存储指向下一个Entry的引用，单链表结构
    int hash;//对key的hashcode值进行hash运算后得到的值，存储在Entry，避免重复计算

    /**
    * Creates new entry.
    */
    Entry(int h, K k, V v, Entry<K,V> n) {
        value = v;
        next = n;
        key = k;
        hash = h;
    } 
```

 所以，HashMap的整体结构如下

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161113235348670-746615111.png)

简单来说，HashMap由数组+链表组成的，数组是HashMap的主体，链表则是主要为了解决哈希冲突而存在的，如果定位到的数组位置不含链表（当前entry的next指向null）,那么对于查找，添加等操作很快，仅需一次寻址即可；如果定位到的数组包含链表，对于添加操作，其时间复杂度为O(n)，首先遍历链表，存在即覆盖，否则新增；对于查找操作来讲，仍需遍历链表，然后通过key对象的equals方法逐一比对查找。所以，性能考虑，HashMap中的链表出现越少，性能才会越好。

其他的一些字段：

```java
//实际存储的key-value键值对的个数
transient int size;
//阈值，当table == {}时，该值为初始容量（初始容量默认为16）；当table被填充了，也就是为table分配内存空间后，threshold一般为 capacity*loadFactory。HashMap在进行扩容时需要参考threshold，后面会详细谈到
int threshold;
//负载因子，代表了table的填充度有多少，默认是0.75
final float loadFactor;
//用于快速失败，由于HashMap非线程安全，在对HashMap进行迭代时，如果期间其他线程的参与导致HashMap的结构发生变化了（比如put，remove等操作），需要抛出异常ConcurrentModificationException
transient int modCount;
```

HashMap有4个构造器，其他构造器如果用户没有传入 initialCapacity 和 loadFactor 这两个参数，会使用默认值

initialCapacity 默认为 16 ，loadFactory 默认为 0.75.

```java
public HashMap(int initialCapacity, float loadFactor) {
　　　　　//此处对传入的初始容量进行校验，最大不能超过MAXIMUM_CAPACITY = 1<<30(230)
        if (initialCapacity < 0)
            throw new IllegalArgumentException("Illegal initial capacity: " +
                                               initialCapacity);
        if (initialCapacity > MAXIMUM_CAPACITY)
            initialCapacity = MAXIMUM_CAPACITY;
        if (loadFactor <= 0 || Float.isNaN(loadFactor))
            throw new IllegalArgumentException("Illegal load factor: " +
                                               loadFactor);

        this.loadFactor = loadFactor;
        threshold = initialCapacity;
　　　　　
        init();//init方法在HashMap中没有实际实现，不过在其子类如 linkedHashMap 中就会有对应实现
    }
```

从上面这段代码我们可以看出，在常规构造器中，没有为数组table分配内存空间（有一个入参为指定Map的构造器例外），而是在执行put操作的时候才真正构建table数组.

我们来看看put操作的实现吧

```java
    public V put(K key, V value) {
        //如果table数组为空数组{}，进行数组填充（为table分配实际内存空间），入参为threshold，此时threshold为initialCapacity 默认是1<<4(24=16)
        if (table == EMPTY_TABLE) {
            inflateTable(threshold);
        }
       //如果key为null，存储位置为table[0]或table[0]的冲突链上
        if (key == null)
            return putForNullKey(value);
        int hash = hash(key);//对key的hashcode进一步计算，确保散列均匀
        int i = indexFor(hash, table.length);//获取在table中的实际位置
        for (Entry<K,V> e = table[i]; e != null; e = e.next) {
        //如果该对应数据已存在，执行覆盖操作。用新value替换旧value，并返回旧value
            Object k;
            if (e.hash == hash && ((k = e.key) == key || key.equals(k))) {
                V oldValue = e.value;
                e.value = value;
                e.recordAccess(this);
                return oldValue;
            }
        }
        modCount++;//保证并发访问时，若HashMap内部结构发生变化，快速响应失败
        addEntry(hash, key, value, i);//新增一个entry
        return null;
    }
```

先来看看 inflateTable 这个方法

```java
private void inflateTable(int toSize) {
        // capacity一定是2的次幂
        int capacity = roundUpToPowerOf2(toSize);
        // 此处为threshold赋值，取capacity*loadFactor和MAXIMUM_CAPACITY+1的最小值，capaticy一定不会超过MAXIMUM_CAPACITY，除非loadFactor大于1
        threshold = (int) Math.min(capacity * loadFactor, MAXIMUM_CAPACITY + 1);
        table = new Entry[capacity];
        initHashSeedAsNeeded(capacity);
    }
```

inflateTable 这个方法用于为主干数组table在内存中分配存储空间，通过.roundUpToPowerOf2(toSize) 可以确保 capacity 为大于或等于toSize的最接近toSize的二次幂，比如 toSize=13 , capacity=16; to_size=16,capacity=16; to_size=17,capacity=32.

```java
 private static int roundUpToPowerOf2(int number) {
        // assert number >= 0 : "number must be non-negative";
        return number >= MAXIMUM_CAPACITY
                ? MAXIMUM_CAPACITY
                : (number > 1) ? Integer.highestOneBit((number - 1) << 1) : 1;
    }
```

roundUpToPowerOf2中的这段处理使得数组长度一定为2的次幂，Integer.highestOneBit是用来获取最左边的bit（其他bit位为0）所代表的数值.



hash函数/哈希函数

```java
//这是一个神奇的函数，用了很多的异或，移位等运算，对key的hashcode进一步进行计算以及二进制位的调整等来保证最终获取的存储位置尽量分布均匀
final int hash(Object k) {
        int h = hashSeed;
        if (0 != h && k instanceof String) {
            return sun.misc.Hashing.stringHash32((String) k);
        }

        h ^= k.hashCode();
        h ^= (h >>> 20) ^ (h >>> 12);
        return h ^ (h >>> 7) ^ (h >>> 4);
    }
```

以上hash函数计算出的值，通过indexFor进一步处理来获取实际的存储位置

```java
　　/**
     * 返回数组下标
     */
    static int indexFor(int h, int length) {
        return h & (length-1);
    }
```

h &（length-1）保证获取的index一定在数组范围内，举个例子，默认容量16，length-1=15，h=18,转换成二进制计算为

```java
        1  0  0  1  0
    &   0  1  1  1  1
    __________________
        0  0  0  1  0    = 2
```

最终计算出的index=2。有些版本的对于此处的计算会使用 取模运算，也能保证index一定在数组范围内，不过位运算对计算机来说，性能更高一些（HashMap中有大量位运算）

所以最终存储位置的确定流程是这样的：

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161115133556388-1098209938.png)

再来看看addEntry的实现：

```java
void addEntry(int hash, K key, V value, int bucketIndex) {
        if ((size >= threshold) && (null != table[bucketIndex])) {
            // 当size超过临界阈值threshold，并且即将发生哈希冲突时进行扩容
            resize(2 * table.length);
            hash = (null != key) ? hash(key) : 0;
            bucketIndex = indexFor(hash, table.length);
        }

        createEntry(hash, key, value, bucketIndex);
    }
```

通过以上代码能够得知，当发生哈希冲突并且size大于阈值的时候，需要进行数组扩容，扩容时，需要新建一个长度为之前数组2倍的新的数组，然后将当前的Entry数组中的元素全部传输过去，扩容后的新数组长度为之前的2倍，所以扩容相对来说是个耗资源的操作。



**为何HashMap的数组长度一定是2的次幂？**

我们来继续看上面提到的resize方法:

```java
 void resize(int newCapacity) {
        Entry[] oldTable = table;
        int oldCapacity = oldTable.length;
        if (oldCapacity == MAXIMUM_CAPACITY) {
            threshold = Integer.MAX_VALUE;
            return;
        }

        Entry[] newTable = new Entry[newCapacity];
        transfer(newTable, initHashSeedAsNeeded(newCapacity));
        table = newTable;
        threshold = (int)Math.min(newCapacity * loadFactor, MAXIMUM_CAPACITY + 1);
    }
```

如果数组进行扩容，数组长度发生变化，而存储位置 index = h&(length-1),index也可能会发生变化，需要重新计算index，我们先来看看transfer这个方法.

```java
void transfer(Entry[] newTable, boolean rehash) {
    int newCapacity = newTable.length;
    // for循环中的代码，逐一遍历链表，重新计算索引位置
    // 将老数组数据复制到新数组中去，数组中不存储实际数据，所以隐隐是拷贝引用而已
    for (Entry<K,V> e: table){
        while (null != e){
            Entry<K,V> next = e.next;
            if (rehash){
                // 如果需要重新哈希
                // 数组中的 entry 的属性hash
                // 当 e 的 key 为 null 的时候设置为0
                // 当 e 的 key 不是 null 的时候设置为 重新计算哈希的值
                e.hash = null == e.key ? 0 : hash(e.key);
            }
            int i = indexFor(e.hash, newCapacity);
            // 将当前 entry 的 next 链指向新的索引的位置，newTable[i]
            // 有可能为空。
            // 有可能也是个 entry 链， 如果是 entry 连，之间在链表头部插入
            e.next = newTable[i]
            newTable[i] = e;
            // 处理链表的下一个 entry 
            e = next;
        }
    }
}
```

这个方法将老数组中的数据逐个链表地遍历，扔到新的扩容后的数组中，我们的数组索引位置的计算是通过 对key值的hashcode进行hash扰乱运算后，再通过和 length-1进行位运算得到最终数组索引位置。

hashMap的数组长度一定保持2的次幂，比如16的二进制表示为 10000，那么length-1就是15，二进制为01111，同理扩容后的数组长度为32，二进制表示为100000，length-1为31，二进制表示为011111。从下图可以我们也能看到这样会保证低位全为1，而扩容后只有一位差异，也就是多出了最左位的1，这样在通过 h&(length-1)的时候，只要h对应的最左边的那一个差异位为0，就能保证得到的新的数组索引和老数组索引一致(大大减少了之前已经散列良好的老数组的数据位置重新调换)。

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161115215812138-679881037.png)

 还有，数组长度保持2的次幂，length-1的低位都为1，会使得获得的数组索引index更加均匀，比如：

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161116001404732-625340289.png)

我们看到，上面的&运算，高位是不会对结果产生影响的（hash函数采用各种位运算可能也是为了使得低位更加散列），我们只关注低位bit，如果低位全部为1，那么对于 h 低位部分来说，任何一位的变化都会对结果产生影响，也就是说，要得到index=21这个存储位置，h的低位只有这一种组合。这也是数组长度设计为必须为2的次幂的原因。

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161116001717560-1455096254.png)

如果不是2的次幂，也就是低位不是全为1此时，要使得index=21，h的低位部分不再具有唯一性了，哈希冲突的几率会变的更大，同时，index对应的这个bit位无论如何不会等于1了，而对应的那些数组位置也就被白白浪费了。

get方法:

```java
 public V get(Object key) {
　　　　 //如果key为null,则直接去table[0]处去检索即可。
        if (key == null)
            return getForNullKey();
        Entry<K,V> entry = getEntry(key);
        return null == entry ? null : entry.getValue();
 }
```

get方法通过key值返回对应value，如果key为null，直接去table[0]处检索。我们再看一下getEntry这个方法

```java
final Entry<K,V> getEntry(Object key) {
        if (size == 0) {
            return null;
        }
        //通过key的hashcode值计算hash值
        int hash = (key == null) ? 0 : hash(key);
        //indexFor (hash&length-1) 获取最终数组索引，然后遍历链表，通过equals方法比对找出对应记录
        for (Entry<K,V> e = table[indexFor(hash, table.length)];
             e != null;
             e = e.next) {
            Object k;
            if (e.hash == hash && 
                ((k = e.key) == key || (key != null && key.equals(k))))
                return e;
        }
        return null;
    }    
```

可以看出，get方法的实现相对简单，key(hashcode)-->hash-->indexFor-->最终索引位置，找到对应位置table[i]，再查看是否有链表，遍历链表，通过key的equals方法比对查找对应的记录。要注意的是，有人觉得上面在定位到数组位置之后然后遍历链表的时候，e.hash == hash这个判断没必要，仅通过equals判断就可以。其实不然，试想一下，如果传入的key对象重写了equals方法却没有重写hashCode，而恰巧此对象定位到这个数组位置，如果仅仅用equals判断可能是相等的，但其hashCode和当前对象不一致，这种情况，根据Object的hashCode的约定，不能返回当前对象，而应该返回null，后面的例子会做出进一步解释。



**重写 equals() 方法之后必须要重写 hashcode():**

如果重写了equals而不重写hashcode会发生什么样的问题.

```java
/**
 * Created by chengxiao on 2016/11/15.
 */
public class MyTest {
    private static class Person{
        int idCard;
        String name;

        public Person(int idCard, String name) {
            this.idCard = idCard;
            this.name = name;
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()){
                return false;
            }
            Person person = (Person) o;
            //两个对象是否等值，通过idCard来确定
            return this.idCard == person.idCard;
        }

    }
    public static void main(String []args){
        HashMap<Person,String> map = new HashMap<Person, String>();
        Person person = new Person(1234,"乔峰");
        //put到hashmap中去
        map.put(person,"天龙八部");
        //get取出，从逻辑上讲应该能输出“天龙八部”
        System.out.println("结果:"+map.get(new Person(1234,"萧峰")));
    }
}
```

实际输出结果：

```
结果：null
```

如果我们已经对HashMap的原理有了一定了解，这个结果就不难理解了。尽管我们在进行get和put操作的时候，使用的key从逻辑上讲是等值的（通过equals比较是相等的），但由于没有重写hashCode方法，所以put操作时，key(hashcode1)-->hash-->indexFor-->最终索引位置 ，而通过key取出value的时候 key(hashcode2)-->hash-->indexFor-->最终索引位置，由于hashcode1不等于hashcode2，导致没有定位到一个数组位置而返回逻辑上错误的值null（也有可能碰巧定位到一个数组位置，但是也会判断其entry的hash值是否相等，上面get方法中有提到。）

所以，在重写equals的方法的时候，必须注意重写hashCode方法，同时还要保证通过equals判断相等的两个对象，调用hashCode方法要返回同样的整数值。而如果equals判断不相等的两个对象，其hashCode可以相同（只不过会发生哈希冲突，应尽量避免)。





**hashmap的Hash算法**

在聊哈算法之前我们要知道在Java中所有对象都有hashcode（使用key的），如果使用object对象get hashcode的话会得到一个int类型的值，我们在hashmap中主要是用他的key去计算它的值的。

Hash值=（hashcode）^(hashcode >>> 16)

Hashcode予hashcode自己向右位移16位的异或运算。这样可以确保算出来的值足够随机。因为进行hash计算的时候足够分散，以便于计算数组下标的时候算的值足够分散。前面说过hashmap的底层是由数组组成，数组默认大小是16，那么数组下标是怎么计算出来的呢，那就是:

**数组下标：hash&(16-1) = hash%16**

对哈希计算得到的hash值进行16的求余，得到一个16的位数，比如说是1到15之间的一个数，hashmap会与hash值和15进行运算。这样可以效率会更高。计算机中会容易识别这种向右位移，向左位移。

**Hash冲突**

不同的对象算出来的数组下标是相同的这样就会产生hash冲突。

Hash冲突会产生单线链表。当单线链表达到一定长度后效率会非常低，那么在jdk1.8以后的话，加入了红黑树，也就是说单线列表达到一定长度后就会变成一个红黑树。

**Hashmap底层原理扩容**

数组存储比例达到75%时数组长度变成2倍 

**红黑树**

jdk1.8以后，在链表长度大于8的时候，将后面的数据存在二叉树中。

红黑树（Red Black Tree） 是一种自平衡二叉查找树

红黑树是每个节点都带有颜色属性的二叉查找树，颜色或红色或黑色。 在二叉查找树强制一般要求以外，对于任何有效的红黑树我们增加了如下的额外要求:

1. 节点是红色或黑色。
2. 根节点是黑色。
3. 所有叶子都是黑色。（叶子是NUIL节点）
4. 每个红色节点的两个子节点都是黑色。（从每个叶子到根的所有路径上不能有两个连续的红色节点）
5. 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。



#### Hashmap解决hash冲突的方法：

1. 开放定址法
2. 再哈希法
3. 链地址法
4. 建立公共溢出区



#### ConcurrentHashMap的基本原理

ConcurrentHashMap包含两个静态内部类 HashEntry和Segment。HashEntry用来封装映射表的键值对，Segment用来充当锁的角色，每个segment对象守护整个haxi映射表的若干个桶。每个桶是有若干个HashEntry对象连接起来的链表。



#### HashMap和HashTable的区别

HashMap和HashTable都实现了Map接口。

HashMap允许键和值是null，HashTable不允许。

HashTable是同步的，HashMap不是。因此HashMap适合于单线程环境，HashTable适合于多线程环境。

HashMap提供了可应用迭代的键的集合，因此HashMap是快速失败的。



#### Map分类和常见的使用情况

java为数据结构中的映射定义了一个接口java.util.Map。它有四个实现类,分别是HashMap、Hashtable、LinkedHashMap 和TreeMap。

Map接口：主要用于存储健值对，根据键得到值，因此不允许键重复(重复了覆盖了),但允许值重复。

HashMap ：它根据键的 HashCode 值存储数据，具有很快的访问速度，遍历时，取得数据的顺序是完全随机的。

Hashtable ：将HashMap内部方法大多使用synchronized的关键字修饰得到的，没有做并发相关的优化，目前主要使用concurrentHashMap替代。

LinkedHashMap 是 HashMap的一个子类，保存了记录的插入顺序，再使用Iterator遍历时，先得到的数据肯定是先插入的，也可以在构造时用带参数，按照应用次数排序。遍历时会比HashMap慢，但当HashMap容量很大，实际数据很少时，遍历起来可能会必LinkedHashMap慢，因为LinkedHashMap的遍历只和实际数据有关，和容量无关。

TreeMap 实现SortMap接口，能够把它保存的记录根据键排序，默认键值是升序排序的，也可以指定排序的比较器，当遍历时，得到的记录是排序的。



### 迭代器

#### 什么是迭代器？

迭代器提供了统一遍历操作集合元素的统一接口，collection接口实现iterable接口。

每个集合都通过实现iterable接口中的iterator()方法，返回iterator接口的实例，然后对集合中的元素进行迭代操作。



#### Iterator和ListIterator的区别：

Iterator可以用来遍历set和list集合，但是ListIterator只能用来遍历list集合。

Iterator对集合只能前向遍历，ListIterator可以前向遍历，也可以后向遍历。

ListIterator实现了Iterator接口，并包含其他的功能，比如：增加元素，替换元素，获取前一个和后一个元素的索引等等。



#### fail-fast和fail-safe的区别：

fail-fast:

当迭代器遍历一个集合对象时，如果遍历的过程中对集合对象的内容进行了修改，则会抛出 concurrent modification exception.

fail-safe:

在遍历时不是直接在集合内容上访问的，而是先复制原有集合内容，在副本上进行遍历。



## 继承类和实现接口

### 继承一个类有什么作用？

- 子类拥有父类非 private 的属性、方法。
- 子类可以拥有自己的属性和方法，即子类可以对父类进行扩展。
- 子类可以用自己的方式实现父类的方法。



### Java类为何只能单继承

产生了“菱形继承问题”。如果“爸爸”类和“妈妈”类中都有吃这个方法。然后“儿子”类继承了爸爸；类和妈妈类之后，如果要执行“吃”这个方法的时候，就不知道该执行爸爸的方法还是妈妈的方法。产生了“菱形继承问题”。



### 为何Java类继承(实现)多个接口没有问题呢？

1. Java接口是行为性的，接口只是定义某个行为的名称
2. 具体的实现动作都在实现类本身这里。

因此，即使实现的多个接口中出现了"同名的方法名"，实现类中也有且只会有一个实现。所以并**不会出现结构混乱的情况**。



### 子类如何访问父类的私有方法

当一个子类对象被创建的时候，首先会在内存中创建一个父类对象，然后在父类对象的外部放上子类独有的属性，这个两者结合起来形成了一个子类的对象。子类是拥有父类的私有属性和方法，但无法直接使用。

根据JAVA官方的定义： 
A subclass does not inherit the private members of its parent class. However, if the superclass has public or protected methods for accessing its private fields, these can also be used by the subclass. 
A nested class has access to all the private members of its enclosing class—both fields and methods. Therefore, a public or protected nested class inherited by a subclass has indirect access to all of the private members of the superclass. 

对于父类中的私有的属性，私有的方法或者私有的类，继承了它的子类是不能直接访问的。但是如果父类中有public的方法，例如setter或者getter，就能够通过这些方法来访问到私有的属性，方法和变量。或者如果父类中的构造函数修改了私有的属性，则子类可以通过构造函数来修改私有的属性。

```java
public class Person {
    private int age;
    public Person(){}
    public Person(int age){
        this.age=age;
        System.out.println("父类构造方法执行了,年龄为："+this.age);
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
}

public class Charactor extends Person {
    public Charactor(){}
    public Charactor(int age){
        super(age+25);
        this.setAge(age);
        System.out.println("子类构造方法执行了,年龄为："+this.getAge());
    }
    public void run(){
        System.out.println("子类对象开始奔跑！");
    }
    public static void main(String[] args) {
        Charactor cp=new Charactor(10);
        cp.run();
        System.out.println("子类实例对象的年龄："+cp.getAge());
        cp.setAge(18);
        System.out.println("子类实例对象的年龄："+cp.getAge());
    }
}
```





### 抽象类和接口的区别

相同点：

1. 抽象类和接口都不能直接实例化
2. 抽象类要被子类继承，接口要被类实现。

不同点：

1. 接口中的所有的方法都必须是抽象的，因此只能做方法申明。抽象类中可以有非抽象的方法，因此可以做方法申明，也可以做方法实现。
2. 接口里定义的变量只能是公共的静态的常量，抽象类中的变量是普通变量。
3. 只能单继承抽象类，但是可以实现多个接口。



## private

private作为一种权限修饰符，可以修饰类、属性和方法；用private修饰的类、属性、方法，只能自己使用，别的类是不能访问的，也就是说对于别的类来说是隐藏不可见的，private一般不修饰类，但是可以修饰内部类。

可以使用private实现封装：

1. 将属性和方法用private封装后表示，被封装的属性与方法只能在本类中使用，类外部不可见。
2. 此时要想访问被封装的属性，必须提供getter与setter方法
3. setter方法：主要进行属性内容的设置与修改
4. getter方法：主要进行属性内容的取得

类的设计原则：编写类的时候，没有额外说明，所有属性必须使用private封装（成员变量）

 private关键字

1. 修饰成员：可以修饰成员变量和成员方法
2. 特点：被private修饰的后的成员只能在本类中被访问
3. private的应用：定义类的时候，当把成员变量给private修饰时，需提供对应的getXxx()和setXxx()方法 ,这样提高了数据的安全性。

private修饰内部类

在例子中，我们在类Parcel2中声明了一个名称为PContents的内部类，并且该内部类用private关键词进行修饰。我们在类中声明了一个public的方法cont()，来帮助我们获取这个内部类。

```java
abstract class Contents{
	abstract public int value();
}
 
public class Parcel2 {
	private class PContents extends Contents{
		private int i = 11;
		public int value(){
			return i;
		}
	}
	
	public Contents cont(){
		return new PContents();
	}
}
```

```java
public class Test {
	public static void main(String[] args){
		Parcel2 p = new Parcel2();
		Contents c = p.cont();
		System.out.println(c.value());
	}
}
```



## this

this关键字指向的是当前对象的引用. 访问类中的成员变量，用来区分成员变量和局部变量（重名问题）



## protected

被 protected 修饰的成员对于本包和其子类可见. 

1. 基类的 protected 成员是包内可见的，并且对子类可见；
2. 若子类与基类不在同一包中，那么在子类中，子类实例可以访问其从基类继承而来的protected方法，而不能访问基类实例的protected方法。

**p1/Father1.java**

```java
package basic.testprotected.p1;
public class Father1 {
    protected void f() {}    // 父类Father1中的protected方法
}
```

**p1/Son1.java**

```java
package basic.testprotected.p1;
public class Son1 extends Father1{}
```

**p11/Son11.java**

```java
package basic.testprotected.p11;
import basic.testprotected.p1.Father1;
public class Son11 extends Father1{}
```

**p1/Test1.java** 

```java
package basic.testprotected.p1;
import basic.testprotected.p11.Son11;
public class Test1{
    public static void main(String[] args){
        Son1 son1 = new Son1();
        son1.f() // 编译成功 1
        son1.clone() // 编译错误 2
        
        Son11 son11 = new Son11();
        son1.f() // 编译成功 3
        son1.clone() // 编译错误 4
    }
}
```

我们先看1，3. 因为当前的包为package basic.testprotected.p1，pretected的方法f()也是在这个包下面被声明的，因此是可见的。所以可以编译成功。但是如果把包换成了其他的包 package basic.testprotected.p11， 则1，3都会出现编译错误，test不是Father1类的子类，而且也不在相同的包下，因此pretected方法对test1类来说是不可见的。



## default

**default介绍：接口内允许添加默认实现的方法**

Java 8 允许我们通过 default 关键字对接口中定义的抽象方法提供一个默认的实现，也就是虚拟扩展方法。是指在接口内部包含了一些默认的方法实现（也就是接口中可以包含方法体，这打破了Java之前版本对接口的语法限制），从而使得接口在进行扩展的时候，不会破坏与接口相关的实现类代码。

**default的出现：**

谈起之前的接口我们都知道，当需要修改接口时候，需要修改全部实现该接口的类。为了方便，因此引进了默认方法，他的目的是为了解决接口的修改与现有的实现不兼容的问题。

```java
public interface Formula {

    /**
     * 计算的方法
     * @param a
     * @return
     */
    double calculate(int a);

    /**
     * default，默认求平方根的方法
     * @param a
     * @return
     */
    default double sqrt(int a) {
        return Math.sqrt(a);
    }
}

```

在上面这个接口中，我们除了定义了一个抽象方法 calculate，还定义了一个带有默认实现的方法 sqrt。
我们在实现这个接口时，可以只需要实现 calculate 方法，默认方法 sqrt 可以直接调用即可，也就是说我们可以不必强制实现 sqrt 方法。

```java
package com.example.service.Impl;
import com.example.service.Formula;
import org.springframework.stereotype.Service;

/**
 * 定义接口的实现类
 *
 * @author lxp
 * @date 2019 -11-07 11:12:22
 */
@Service
public class FormulaImpl implements Formula {

    @Override
    public double calculate(int a) {

        //直接调用接口中default方法
        return sqrt(a * 100);
    }
}
```

通过 default 关键字这个新特性，可以非常方便地对之前的接口做拓展，而此接口的实现类不必做任何改动。

## super

由于子类不能继承父类的构造方法，因此，如果要调用父类的构造方法，可以使用 super 关键字。super 可以用来访问父类的构造方法、普通方法和属性。

super 关键字的功能：

- 在子类的构造方法中显式的调用父类构造方法
- 访问父类的成员方法和变量。

super调用父类构造方法

super 关键字可以在子类的构造方法中显式地调用父类的构造方法，基本格式如下：

```java
super(parameter-list);
```

其中，parameter-list 指定了父类构造方法中的所有参数。super( ) 必须是在子类构造方法的方法体的第一行。

```java
public class Person {
    public Person(String name, int age) {
    }
    public Person(String name, int age, String sex) {
    }
}
```

```java
public class Student extends Person {
    public Student(String name, int age, String birth) {
        super(name, age); // 调用父类中含有2个参数的构造方法
    }
    public Student(String name, int age, String sex, String birth) {
        super(name, age, sex); // 调用父类中含有3个参数的构造方法
    }
}
```

从上述 Student 类构造方法代码可以看出，super 可以用来直接调用父类中的构造方法，使编写代码也更加简洁方便。



**super访问父类成员**

当子类的成员变量或方法与父类同名时，可以使用 super 关键字来访问。如果子类重写了父类的某一个方法，即子类和父类有相同的方法定义，但是有不同的方法体，此时，我们可以通过 super 来调用父类里面的这个方法。

使用 super 访问父类中的成员与 this 关键字的使用相似，只不过它引用的是子类的父类，语法格式如下：

```
super.member
```

其中，member 是父类中的属性或方法。使用 super 访问父类的属性和方法时不用位于第一行。

**super调用成员属性**

```java
class Person {
    int age = 12;
}
class Student extends Person {
    int age = 18;
    void display() {
        System.out.println("学生年龄：" + super.age);
    }
}
class Test {
    public static void main(String[] args) {
        Student stu = new Student();
        stu.display();
    }
}
```

```
学生年龄：12
```

在上面的例子中，父类和子类都有一个成员变量 age。我们可以使用 super 关键字访问 Person 类中的 age 变量。

**super调用成员方法**

当父类和子类都具有相同的方法名时，可以使用 super 关键字访问父类的方法。具体如下代码所示。

```java
class Person {
    void message() {
        System.out.println("This is person class");
    }
}
class Student extends Person {
    void message() {
        System.out.println("This is student class");
    }
    void display() {
        message();
        super.message();
    }
}
class Test {
    public static void main(String args[]) {
        Student s = new Student();
        s.display();
    }
}
```

```
This is student class
This is person class
```



## final

当用final修饰一个类时，这个类不能被继承。也就是说，如果一个类你永远不能让他被继承，就可以使用final进行修饰。final类中的成员变量可以根据需要设置为final，但是要注意final类中的所有成员方法都会隐式的指定为final方法。

使用final方法的原因有两个。第一个原因是把方法锁定，以防任何继承类修改它的含义；

对于一个final变量，如果是基本数据类型的变量，那么数值一旦被初始化之后便不能被修改。如果是引用类型的变量，则在对其初始化之后便不能再让它指向另外一个对象。



## 字符串

### String，StringBuffer, StringBuilder继承结构：



### String，StringBuffer, StringBuilder区别：





## 线程同步

### 什么是线程安全

多个线程访问同一个对象时，如果不用考虑这些线程在运行时环境下的调度和交替执行，也不需要进行额外的同步，或者在调用方进行任何其他操作，调用这个对象的行为都可以获得正确的结果，那么这个对象就是线程安全的。

### 线程的安全程度

**一 不可变**

1.不可变的对象一定是线程安全的，无论是对象的方法实现还是调用者，都不需要再采取任何的线程安全保障措施。

2.不可变带来的安全性是最纯粹的最简单的。

3.final关键字就可以做到不可变。

**二 绝对的线程安全**

1. 不管运行时环境如何，调用者都不需要任何额外的同步措施。

2.通常代价是很大的，容易不切实际。

3.API中标注自己是线程安全的类，大多数都不是绝对的线程安全。比如vector

**三 相对的线程安全**

1.通常来说线程是安全的，但对于一些特定顺序的连续调用，就可能需要在调用端使用额外的同步手段来保证调用的正确性。

2.大部分线程都属于这种类型，如vector

**四 线程兼容**

本身不是线程安全的，但是可以通过调用端使用同步来保证安全性。

**五 线程对立**

无论是否采用同步措施，都无法在并发中使用。



### 线程池

在面型对象编程中，创建和销毁对象是很费时间和资源的事情。提高服务程序效率的一个手段就是尽可能减少创建和销毁对象的次数，特别是一些很消耗资源的对象。线程池是事先床架若干个线程放入线程池中，需要的时候从池中获取线程，而不用去创建线程，使用完毕之后，不需要将线程销毁，而是将线程重新放回到线程池中。



### 线程同步和线程调度的方法

wait():使线程处于等待（阻塞）状态。并且释放所持有的对象的锁

sleep():使一个正在运行的线程进入睡眠状态，是一个静态方法，调用这个方法不需要处理interruptdException

notify():唤醒一个处于等待状态的线程，当然在调用这个方法的时候，并不能确切的唤醒某一个等待的线程，而是有JVM决定唤醒哪一个线程，而且和线程的有限级别无关。

notifyAll():唤醒所有处于等待状态的线程，该方法不是将对象的所给所有线程，而是让他们竞争，只有获得锁的线程能够进入就绪状态。



### 当一个线程进入对象的synchronized方法A之后，其他的线程能够进入synchronized方法B么？

不能，其他的线程只能访问该对象的非同步方法，同步方法不能访问。



### 线程从创立到死亡的几种状态

1. 新建（new）

2. 可运行（runnable）：线程对象创建之后，其他线程（比如main线程）调用了该线程的start()方法，该状态的线程为于可运行的线程池中，等待被线程调度选中，获取CPU的使用权

3. 运行（running）：可运行状态（runnable）的线程获取了CPU时间片，执行程序代码
4. 阻塞（blocking）：阻塞状态是指线程因为某种原因放弃了CPU的使用权，也就是说让出了CPU时间片，暂时停止了运行。直到线程进入可运行状态（runnable），才有机会再次获得CPU时间片，而转到running状态。阻塞的情况分为三种：

（一）：等待阻塞：运行的线程在执行object.wait()方法，JVM会把线程转到等待队列中（waiting queue）

（二）：同步阻塞：运行状态的线程在获取对象的同步锁时，若该同步锁被别的线程占，则JVM会把该线程放入锁池中（lock pool）

（三）：其他阻塞：运行状态的线程执行Thread.sleep()或者t.join()方法，或者发出了I/O请求时，JVM会把该线程设置为阻塞状态。

5. 死亡（dead）：线程run(),main()方法执行结束，或者因异常退出了run()方法，则该线程的生命周期结束。死亡的线程不能再复生。



### 启动线程的方式

Runnable和Callable的区别是，
(1)Callable规定的方法是call(),Runnable规定的方法是run().
(2)Callable的任务执行后可返回值，而Runnable的任务是不能返回值得
(3)call方法可以抛出异常，run方法不可以
(4)运行Callable任务可以拿到一个Future对象，表示异步计算的结果。它提供了检查计算是否完成的方法，以等待计算的完成，并检索计算的结果。通过Future对象可以了解任务执行情况，可取消任务的执行，还可获取执行结果。



1. 继承Thread类，创建线程类

定义一个继承Thread类的子类：

```java
class SomeThead extends Thraad
{
    public void run()
    {
     //do something here
    }
}
```

构造子类的一个对象：

```java
SomeThread oneThread = new SomeThread();
```

步骤3：启动线程：

      oneThread.start();



2. 通过Runnable接口创建线程类

创建实现Runnable接口的类：

```java
class SomeRunnable implements Runnable
{
    public void run()
    {
      //do something here
    }
}
```

创建一个类对象

```java
Runnable oneRunnable = new SomeRunnable();
```

由Runnable创建一个Thread对象：

```java
Thread oneThread = new Thread(oneRunnable);
```

```java
oneThread.start();
```

至此，一个线程就创建完成了。

注释：线程的执行流程很简单，当执行代码oneThread.start();时，就会执行oneRunnable对象中的void run();方法，

该方法执行完成后，线程就消亡了。



3. 通过Callable和Future创建线程

Callable接口

```
public interface Callable<V>   
{   
    V call() throws Exception;   
} 
```

创建实现Callable接口的类SomeCallable<Integer>

创建一个类对象： Callable<Integer> oneCallable = new SomeCallable<Integer>();

由Callable<Integer>创建一个FutureTask<Integer>对象：

FutureTask<Integer> oneTask = new FutureTask<Integer>(oneCallable);

由FutureTask<Integer>创建一个Thread对象：

```java
Thread oneThread = new Thread(oneTask);
```

启动线程：

```java
oneThread.start();
```

### 公平锁和非公平锁

公平锁：当线程释放锁时，会在队列中查找，队列的头部的线程会得到锁。有新的线程请求锁时，将会排到队伍的末尾

非公平锁：当线程释放锁时，会先查找当前是否有线程在请求锁，如果有，则给该线程锁。如果没有，则给在队首等待的线程锁。



### synchronized和lock的区别：

| 类别     | synchronized                                                 | lock                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 存在层次 | java的关键字，在jvm层面上                                    | 是一个类                                                     |
| 锁的释放 | 1、以获取锁的线程执行完同步代码，释放锁       2、线程执行发生异常，jvm会让线程释放锁 | 在finally中必须释放锁，不然容易造成线程死锁                  |
| 锁的获取 | 假设A线程获得锁，B线程等待，如果A线程阻塞，B线程会一直等待   | 分情况而定，lock有多个锁获取的方法，可以尝试获得锁，线程可以不用功一直等待 |
| 锁状态   | 无法判断                                                     | 可以判断                                                     |
| 锁类型   | 可以重入，不可以中断，非公平                                 | 可重入 可以判断 可公平                                       |
| 性能     | 少量同步                                                     | 大量同步                                                     |





## 比较

### ”==“比较的是什么？

”==“对比两个对象基于内存引用，当两个对象的引用相同（指向同一个对象），返回True。如果两边都是基本类型，判断两边值是否相等。



### Object如果不重写hashcode()，hashcode()如何计算？

返回对象所在的内存地址。



### 为什么重写equals()还要重写hashcode()?

我们在业务系统中判断对象时有时候需要的不是一种严格意义上的相等，而是业务上的相等。在这种情况下，原声的equals()方法就不能满足我们的要求而需要进行修改。为什么还需要修改hashcode()？

我们看一下Object.hashcode的通用约定：《effective java》

1. 在一个应用的执行期间，如果一个对象的equals方法做比较时所用到的信息没有修改的话，那么，这个对象调用hashcode()方法多次，必须返回同一个整数。在同一个应用程序的多次调用中，可以返回不同的数。
2. 如果两个对象根据equals(Object)是相等的，那么调用这个两个对象的任意一个hashcode()必须返回相等的结果
3. 如果两个对象根据equals(Object)是不相等的，那么调用这个两个对象的任意一个hashcode()不要求必须返回不相等结果。但是返回不相等结果时候，有可能提升hashtable的性能

如果我们只重写了equals()，但是没有重写hashcode(),就会违反规定的第二条。

同时对于HashSet，HashMap这种基于基于hash实现的类。Hashmap的底层处理机制是以数组的方式保存放入数据的，其中的关键在于数组下标的处理。数组的下标是根据传入元素的hashcode方法的返回值再和特定的值异或得到的。如果在数组位置上已经有了放入的值，并且传入的对象相等，则不处理。如果对象不相等，则覆盖原有的值，如果在该位置上没有条目，则插入，并且加入到相应的链表中。检查键是否存在也是根绝hashcode决定的。如果不重写hashcode()，可能导致HashSet,HashMap不能正常运行。



### Comparable 和Comparator接口的区别？

Java中提供了一个只包含compareTo()方法的Comparable接口。这个方法可以给两个对象排序。具体来说，它返回负值，0，正值，来标明输入对象小于，等于或者大于已经存在的对象。

java中一共了包含compare()和equals()两个方法的Comparator接口。compare()方法用来给两个输入的参数排序，返回负值，0，正值来表明第一个参数是小于，等于或者大于第二个参数。equals()方法需要一个对象作为参数，用来判断输入参数是否和comparator相等。



## 面向对象

### 面向对象特征

面向对象的特征
主要有抽象、继承、封装和多态四个方面，下面是我们来详细分析它们的含义：

**抽象：**

抽象是将一类对象的共同特征总结出来构造类的过程，包括数据抽象和行为抽象两方面。抽象只关注对象有哪些属性和行为，并不关注这些行为的细节是什么。 

**继承：**

继承是从已有类得到继承信息创建新类的过程。提供继承信息的类被称为父类（超类、基类）；得到继承信息的类被称为子类（派生类）。继承让变化中的软件系统有了一定的延续性，同时继承也是封装程序中可变因素的重要手段。 

拓展：
    由于实际需要，某个类具有两个或两个以上的维度变化（例如我们去吃面：有拉面和板面两种选择，在这两中选择之上还有牛肉面和鸡蛋面两种选择，在这两层之上还有清淡、微辣、超辣等选择），如果仅仅使用继承实现这种需求，设计将会变得非常臃肿，这里我们可以引入桥接模式。桥接模式的做法就是把程序变化的部分抽象出来，让变化的部分与主类分离开来，从而将多个维度的变化彻底分离。最后提供一个管理类来组合不同维度上的变化，通过这个组合来满足业务需要。桥接模式在JavaEE应用中有非常广泛的应用。由于JavaEE应用需要实现跨数据库的功能，程序为了在不同的数据库之间迁移，系统需要在持久化技术这个维度上存在改变；另外，系统也需要在不同的业务逻辑之间迁移，因此也需要在业务逻辑这个维度迁移。因此，JavaEE应用都会推荐使用业务逻辑组件与DAO组件分离，让DAO组件负责持久化技术这个维度上的改变，让业务逻辑组件负责业务逻辑实现这个维度上的改变。JavaEE应用的DAO模式就是桥接模式的应用。从DAO组件的设计初衷来开，DAO组件是为了让应用在不同的持久化技术之间自由切换，也就是为了分离系统在持久化技术维度上的变化，从这个角度来看，JavaEE应用分离出DAO组件就是遵循桥接模式的。

**封装：**

通常认为封装是把数据和操作数据的方法绑定起来，对数据的访问只能通过已定义的接口。面向对象的本质就是将现实世界描绘成一系列完全自治、封闭的对象。我们在类中编写的方法就是对实现细节的一种封装；我们编写一个类就是对数据和数据操作的封装。可以说，封装就是隐藏一切可隐藏的东西，只向外界提供最简单的编程接口

**多态性：**

多态性是指允许不同子类型的对象对同一消息作出不同的响应。

多态性分为编译时的多态性和运行时的多态性。方法重载（overload）实现的是编译时多态性（也称为前绑定），而方法重写（override）实现的是运行时的多态性。（也称为后绑定）。Java 中使用多态特性的方法主要有：

1. 实现一个接口
2. 实现抽象类的一个方法
3. 覆盖父类的一个方法。

Java中多态的实现方式：接口实现，继承父类进行方法重写，同一个类中进行方法重载。

**方法的重载是不是多态？**

1. 这个问题分为两个方面，第一首先明确什么是多态？第二，重载是什么，是否满足了多态的要求？所谓多态就是父类的引用指向子类对象。当调用子父类同名参数时，执行的是子类重写的父类方法，就是虚拟方法调用。
2. 什么是虚拟方法调用？子类中定义了与父类同名同参数的方法，在多态的情况下，将此时父类的方法称为虚拟方法，父类根据赋予它的不同的子类，动态的调用该方法。这样的方法调用在编译期是无法确定的。
3. 重载是什么？重载是指允许多个同名但是参数不同的方法存在，编译期根据方法的参数表，对同名方法做修饰，对编译器而言，重载的方法，就是不同的方法，所以在编译期就已经确定调用地址了。所以，对于重载而言，在编译期就确定了的。而多态则是在调用时才确定，因此重载不是多态。



**静态绑定与动态绑定**

JVM 的方法调用指令有五个，分别是：

1. invokestatic：调用静态方法；
2. invokespecial：调用实例构造器<init>方法、私有方法和父类方法；
3. invokevirtual：调用虚方法；
4. invokeinterface：调用接口方法，运行时确定具体实现；
5. invokedynamic：运行时动态解析所引用的方法，然后再执行，用于支持动态类型语言。

其中，invokestatic 和 invokespecial 用于静态绑定，invokevirtual 和 invokeinterface 用于动态绑定。可以看出，动态绑定主要应用于虚方法和接口方法。

静态绑定在编译期就已经确定，这是因为静态方法、构造器方法、私有方法和父类方法可以唯一确定。这些方法的符号引用在类加载的解析阶段就会解析成直接引用。因此这些方法也被称为非虚方法，与之相对的便是虚方法。

虚方法的方法调用与方法实现的关联（也就是分派）有两种，一种是在编译期确定，被称为静态分派，比如方法的重载；一种是在运行时确定，被称为动态分派，比如方法的覆盖。对象方法基本上都是虚方法。

这里需要特别说明的是，final 方法由于不能被覆盖，可以唯一确定，因此 Java 语言规范规定 final 方法属于非虚方法，但仍然使用 invokevirtual 指令调用。静态绑定、动态绑定的概念和虚方法、非虚方法的概念是两个不同的概念。

**多态的实现** 

虚拟机栈中会存放当前方法调用的栈帧，在栈帧中，存储着局部变量表、操作栈、动态连接 、返回地址和其他附加信息。多态的实现过程，就是方法调用动态分配的过程，通过栈帧的信息去找到被调用方法的具体实现，然后使用这个具体实现的直接引用完成方法调用。

以 invokevirtual 指令为例，在执行时，大致可以分为以下几步：

1. 先从操作栈中找到对象的实际类型 class；
2. 找到 class 中与被调用方法签名相同的方法，如果有访问权限就返回这个方法的直接引用，如果没有访问权限就报错 java.lang.IllegalAccessError ；
3. 如果第 2 步找不到相符的方法，就去搜索 class 的父类，按照继承关系自下而上依次执行第 2 步的操作；
4. 如果第 3 步找不到相符的方法，就报错 java.lang.AbstractMethodError ；

可以看到，如果子类覆盖了父类的方法，则在多态调用中，动态绑定过程会首先确定实际类型是子类，从而先搜索到子类中的方法。这个过程便是方法覆盖的本质。

实际上，商用虚拟机为了保证性能，通常会使用虚方法表和接口方法表，而不是每次都执行一遍上面的步骤。以虚方法表为例，虚方法表在类加载的解析阶段填充完成，其中存储了所有方法的直接引用。也就是说，动态分派在填充虚方法表的时候就已经完成了。

在子类的虚方法表中，如果子类覆盖了父类的某个方法，则这个方法的直接引用指向子类的实现；而子类没有覆盖的那些方法，比如 Object 的方法，直接引用指向父类或 Object 的实现。



### 面向对象”六原则，一法则“

单一职责原则、开闭原则、依赖倒转原则、里氏替换原则、接口隔离原则、合成聚合复用原则和迪米特法则。

- 单一职责原则
一个类只做它该做的事情。

单一职责原则想表达的就是"高内聚"，写代码最终极的原则只有六个字"高内聚、低耦合"，就如同葵花宝典或辟邪剑谱的中心思想就八个字"欲练此功必先自宫"，所谓的高内聚就是一个代码模块只完成一项功能，在面向对象中，如果只让一个类完成它该做的事，而不涉及与它无关的领域就是践行了高内聚的原则，这个类就只有单一职责。我们都知道一句话叫"因为专注，所以专业"，一个对象如果承担太多的职责，那么注定它什么都做不好。这个世界上任何好的东西都有两个特征，一个是功能单一，好的相机绝对不是电视购物里面卖的那种一个机器有一百多种功能的，它基本上只能照相；另一个是模块化，好的自行车是组装车，从减震叉、刹车到变速器，所有的部件都是可以拆卸和重新组装的，好的乒乓球拍也不是成品拍，一定是底板和胶皮可以拆分和自行组装的，一个好的软件系统，它里面的每个功能模块也应该是可以轻易的拿到其他系统中使用的，这样才能实现软件复用的目标。

- 开闭原则
软件实体应当对扩展开放，对修改关闭。

在理想的状态下，当我们需要为一个软件系统增加新功能时，只需要从原来的系统派生出一些新类就可以，不需要修改原来的任何一行代码。

要做到开闭有两个要点：①抽象是关键，一个系统中如果没有抽象类或接口系统就没有扩展点；②封装可变性，将系统中的各种可变因素封装到一个继承结构中，如果多个可变因素混杂在一起，系统将变得复杂而换乱，如果不清楚如何封装可变性，可以参考《设计模式精解》一书中对桥梁模式的讲解的章节。



- 依赖倒转原则
面向接口编程。

该原则说得直白和具体一些就是声明方法的参数类型、方法的返回类型、变量的引用类型时，尽可能使用抽象类型而不用具体类型，因为抽象类型可以被它的任何一个子类型所替代，请参考下面的里氏替换原则。



-里氏替换原则
任何时候都可以用子类型替换掉父类型。

关于里氏替换原则的描述，Barbara Liskov女士的描述比这个要复杂得多，但简单的说就是能用父类型的地方就一定能使用子类型。里氏替换原则可以检查继承关系是否合理，如果一个继承关系违背了里氏替换原则，那么这个继承关系一定是错误的，需要对代码进行重构。例如让猫继承狗，或者狗继承猫，又或者让正方形继承长方形都是错误的继承关系，因为你很容易找到违反里氏替换原则的场景。需要注意的是：子类一定是增加父类的能力而不是减少父类的能力，因为子类比父类的能力更多，把能力多的对象当成能力少的对象来用当然没有任何问题。



- 接口隔离原则
接口要小而专，绝不能大而全。

臃肿的接口是对接口的污染，既然接口表示能力，那么一个接口只应该描述一种能力，接口也应该是高度内聚的。例如，琴棋书画就应该分别设计为四个接口，而不应设计成一个接口中的四个方法，因为如果设计成一个接口中的四个方法，那么这个接口很难用，毕竟琴棋书画四样都精通的人还是少数，而如果设计成四个接口，会几项就实现几个接口，这样的话每个接口被复用的可能性是很高的。Java中的接口代表能力、代表约定、代表角色，能否正确的使用接口一定是编程水平高低的重要标识。



- 合成聚合复用原则
优先使用聚合或合成关系复用代码。

通过继承来复用代码是面向对象程序设计中被滥用得最多的东西，因为所有的教科书都无一例外的对继承进行了鼓吹从而误导了初学者，类与类之间简单的说有三种关系，Is-A关系、Has-A关系、Use-A关系，分别代表继承、关联和依赖。其中，关联关系根据其关联的强度又可以进一步划分为关联、聚合和合成，但说白了都是Has-A关系，合成聚合复用原则想表达的是优先考虑Has-A关系而不是Is-A关系复用代码，原因嘛可以自己从百度上找到一万个理由，需要说明的是，即使在Java的API中也有不少滥用继承的例子，例如Properties类继承了Hashtable类，Stack类继承了Vector类，这些继承明显就是错误的，更好的做法是在Properties类中放置一个Hashtable类型的成员并且将其键和值都设置为字符串来存储数据，而Stack类的设计也应该是在Stack类中放一个Vector对象来存储数据。记住：任何时候都不要继承工具类，工具是可以拥有并可以使用的，而不是拿来继承的。



- 迪米特法则
迪米特法则又叫最少知识原则，一个对象应当对其他对象有尽可能少的了解。

迪米特法则简单的说就是如何做到"低耦合"，门面模式和调停者模式就是对迪米特法则的践行。

拓展：
对于门面模式可以举一个简单的例子，你去一家公司洽谈业务，你不需要了解这个公司内部是如何运作的，你甚至可以对这个公司一无所知，去的时候只需要找到公司入口处的前台美女，告诉她们你要做什么，她们会找到合适的人跟你接洽，前台的美女就是公司这个系统的门面。再复杂的系统都可以为用户提供一个简单的门面，Java Web开发中作为前端控制器的Servlet或Filter不就是一个门面吗，浏览器对服务器的运作方式一无所知，但是通过前端控制器就能够根据你的请求得到相应的服务。调停者模式也可以举一个简单的例子来说明，例如一台计算机，CPU、内存、硬盘、显卡、声卡各种设备需要相互配合才能很好的工作，但是如果这些东西都直接连接到一起，计算机的布线将异常复杂，在这种情况下，主板作为一个调停者的身份出现，它将各个设备连接在一起而不需要每个设备之间直接交换数据，这样就减小了系统的耦合度和复杂度。

如下图所示：

![img](https://img-blog.csdn.net/20150608234901153?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMjYzNDIwMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

使用门面模式后：

![img](https://img-blog.csdn.net/20150608234906098?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMjYzNDIwMDk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

迪米特法则用通俗的话来将就是不要和陌生人打交道，如果真的需要，找一个自己的朋友，让他替你和陌生人打交道。



### 内部类是否可以引用他包含类的成员，如果可以，有什么限制？

内部类对象可以访问创建它的外部类对象的内容，内部类如果不是static的，那么他可以访问创建它的外部类对象的所有属性。如果内部类是static的，那么即为nested class。那么它只可以访问创建它的外部类对象的所有static属性。一般普通类只有public或者package的访问修饰，而内部类可以实现static，protected，private的访问修饰。当从外部类继承的时候，内部类是不会被覆盖的，他们是完全独立的实体，每个都在自己的命名空间中。如果从内部类中明确的继承，就可以覆盖原来内部类的方法。



## 异常处理

### java中如何进行异常处理，关键字：throws，throw，try，catch，finally有什么含义？在try中能抛出异常么？

java通过面向对象的方法对异常进行处理，把各种不同的异常进行分类，并且提供了良好的接口。在java中，每个异常都是一个对象，他们是throwable类或者其他子类的实例。当一个方法出现异常后便抛出一个异常对象，这个对象中包含有异常信息，调用这个对象的方法可以捕获这个异常并且进行处理。java的异常处理是通过5个关键词实现的：try，catch，throw，throws，finally。一般情况下，使用try来执行一段程序，如果出现异常，系统会抛出(throws)一个异常对象，这个时候可以通过它的类型来捕捉它(catch)。或者最后(finally)由缺省处理器来处理。用try来指定一块预防所有异常的程序，紧跟在try后面，应该包含一个catch子句来指定要想捕获的异常的类型。throw语句来明确的抛出一个异常。throws来标明一个成员函数可能抛出的异常。finally为确保一段代码不论发生什么异常都会被执行的一段代码。可以在一个成员函数调用的外面写上try语句，在这个成员函数的内部写上另外一个try语句来保护其他的代码。每当遇到一个try语句的时候，”异常“的框架就会被放在堆栈上，直到所有的try语句都完成。如果下一级的try语句没有对某种”异常“进行处理，堆栈就会展开，直到遇到有处理这种异常的语句。



### final，finally和finallize的区别？

final用来声明属性，方法和类，分别表示属性不可变，方法不可变，类不可变

finally是异常处理语句结构的一部分，表示总是执行

finalize是object类的一个方法，在垃圾收集器执行的时候会调用被回收对象的此方法，可以覆盖此方法提供垃圾收集器的其他资源



## 反射

### 什么是反射

指程序可以访问、检测和修改它本身状态或行为的一种能力。

### Java的反射机制的主要的功能

1. 在运行时判断任意一个对象所属的类。

2. 在运行时构造任意一个类的对象。

3. 在运行时判断任意一个类所具有的成员变量和方法。

4. 在运行时调用任意一个对象的方法

### 如何用反射创建对象？

\- 方法1：通过类对象调用newInstance()方法，例如：String.class.newInstance()
\- 方法2：通过类对象的getConstructor()或getDeclaredConstructor()方法获得构造器（Constructor）对象并调用其newInstance()方法创建对象，例如：String.class.getConstructor(String.class).newInstance("Hello");

### 如何用反射来获取和设置对象私有字段的值？

通过对象的getDecleardField()方法获取字段（field）对象，然后再通过字段对象的setAccessible(True)将其设置为可以访问，接下来就是通过get/set方法来获取和设置字段。

 

## Static

static 详解

https://zhuanlan.zhihu.com/p/42961231

### JAVA中static的作用详解

static表示“全局”或者“静态”的意思，用来修饰成员变量和成员方法，也可以形成静态static代码块，但是Java语言中没有全局变量的概念。被static修饰的成员变量和成员方法独立于该类的任何对象。也就是说，它不依赖类特定的实例，被类的所有实例共享。

只要这个类被加载，Java虚拟机就能根据类名在运行时数据区的方法区内定找到他们。因此，static的内容可以在它的任何对象创建之前访问，无需引用任何对象。用public修饰的static成员变量和成员方法本质是全局变量和全局方法，当声明这个类的对象时，不生成static变量的副本，而是类的所有实例共享同一个static变量。

static变量前可以有private修饰，表示这个变量可以在类的静态代码块中，或者类的其他静态成员方法中使用（当然也可以在非静态成员方法中使用--废话），但是不能在其他类中通过类名来直接引用。实际上你需要搞明白，private是访问权限限定，static表示不要实例化就可以使用，这样就容易理解多了。static前面加上其它访问权限关键字的效果也以此类推。

static修饰的成员变量和成员方法习惯上称为静态变量和静态方法，可以直接通过类名来访问，访问语法为：

```
类名.静态方法名(参数列表...)
类名.静态变量名
```

用static修饰的代码块表示静态代码块，当Java虚拟机（JVM）加载类时，就会执行该代码块。



**static变量**

需要注意的是当一个内部类没有使用static修饰的时候，是不能直接使用内部类创建对象，须要先使用外部类对象点new内部类对象及(外部类对象.new 内部类（）

按照是否静态的对类成员变量进行分类可分两种：一种是被static修饰的变量，叫静态变量或类变量；另一种是没有被static修饰的变量，叫实例变量。

两者的区别是： 

- 对于静态变量在内存中只有一个拷贝（节省内存），JVM只为静态分配一次内存，在加载类的过程中完成静态变量的内存分配，可用类名直接访问（方便），当然也可以通过对象来访问（但是这是不推荐的）。
- 对于实例变量，每创建一个实例，就会为实例变量分配一次内存，实例变量可以在内存中有多个拷贝，互不影响（灵活）。

所以一般在需要实现以下两个功能时使用静态变量： - 在对象之间共享值时 - 方便访问变量时



**静态方法**

静态方法可以直接通过类名调用，任何的实例也都可以调用， **因此静态方法中不能用this和super关键字，不能直接访问所属类的实例变量和实例方法(就是不带static的成员变量和成员成员方法)，只能访问所属类的静态成员变量和成员方法。 因为实例成员与特定的对象关联！！**

因为static方法独立于任何实例，因此static方法必须被实现，而不能是抽象的abstract。

例如为了方便方法的调用，Java API中的Math类中所有的方法都是静态的，而一般类内部的static方法也是方便其它类对该方法的调用。

静态方法是类内部的一类特殊方法，只有在需要时才将对应的方法声明成静态的，一个类内部的方法一般都是非静态的。



**static代码块**

static代码块也叫静态代码块，是在类中独立于类成员的static语句块，可以有多个，位置可以随便放，它不在任何的方法体内，JVM加载类时会执行这些静态的代码块，如果static代码块有多个，JVM将按照它们在类中出现的先后顺序依次执行它们，每个代码块只会被执行一次。例如：

```java
public class test{
  
  private static int a;
  private int b;
  
  // 这是一个静态代码块
  static{
    // 修改静态变量
    test.a = 3;
    // 输出静态变量的值
    System.out.println(a);
    // 创建一个test类的对象
    Test5 t = new Test5();
    // 调用这个对象的成员方法
    t.f();
    // 修改这个对象的成员变量
    t.b = 1000;
    // 输出这个对象的成员变量的值
    System.out.println(t.b);
  }
  
  // 这是第二个静态代码块
  static{
    // 修改静态变量
    test.a = 4;
    // 输出静态变量的值
    System.out.println(a);
  }
  
  // 主函数
  public static void main(String[] args) {
  // TODO 自动生成方法存根
  }
  
  // 第三个静态代码块
  static{
    // 修改静态变量
    test.a = 3;
    // 输出静态变量的值
    System.out.println(a);
  }
  
  // 一个普通的类的成员方法
  public void f(){
    System.out.println("hhahhahah");
  }
}
```

运行结果：

```java
3
hhahhahah
1000
4
5
```

为什么会有这样的执行结果呢，我们要来分析一下。首先，我们会发现我们的main主函数中是没有内容的，因此不会执行任何的东西。但是为什么我们的结果中有输出东西呢？这是因为我们的静态代码块被执行了。但是静态代码块只会执行一次。我们在类中总共有三个静态的代码块，执行的顺序是从上到下执行。

利用静态代码块可以对一些static变量进行赋值，最后再看一眼这些例子，都一个static的main方法，这样JVM在运行main方法的时候可以直接调用而不用创建实例。



**static和final一块用表示什么**

static final用来修饰成员变量和成员方法，可简单理解为“全局常量”！

对于变量，表示一旦给值就不可修改，并且通过类名可以访问。对于方法，表示不可覆盖，并且可以通过类名直接访问。

有时你希望定义一个类成员，使它的使用完全独立于该类的任何对象。通常情况下，类成员必须通过它的类的对象访问，但是可以创建这样一个成员，它能够被它自己使用，而不必引用特定的实例。在成员的声明前面加上关键字static(静态的)就能创建这样的成员。如果一个成员被声明为static，它就能够在它的类的任何对象创建之前被访问，而不必引用任何对象。你可以将方法和变量都声明为static。static 成员的最常见的例子是main( ) 。因为在程序开始执行时必须调用main() ，所以它被声明为static。

声明为static的变量实质上就是全局变量。当声明一个对象时，并不产生static变量的拷贝，而是该类所有的实例变量共用同一个static变量。声明为static的方法有以下几条限制：

- 它们仅能调用其他的static 方法。
- 它们只能访问static数据。
- 它们不能以任何方式引用this 或super。

如果你需要通过计算来初始化你的static变量，你可以声明一个static块，Static 块仅在该类被加载时执行一次。下面的例子显示的类有一个static方法，一些static变量，以及一个static 初始化块：

```java
// Demonstrate static variables，methods，and blocks.
class UseStatic {
static int a = 3;
static int b;
static void meth(int x) {
	System.out.println("x = " + x);
	System.out.println("a = " + a);
	System.out.println("b = " + b);
}
static {
	System.out.println("Static block initialized.");
	b = a * 4;
}
public static void main(String args[]) {
	meth(42);
}
}
```

一旦UseStatic 类被装载，所有的static语句被运行。首先，a被设置为3，接着static 块执行(打印一条消息)，最后，b被初始化为a*4 或12。然后调用main()，main() 调用meth() ，把值42传递给x。3个println ( ) 语句引用两个static变量a和b，以及局部变量x 。

注意：在一个static 方法中引用任何实例变量都是非法的。下面是该程序的输出：

```java
Static block initialized.
x = 42
a = 3
b = 12
```

在定义它们的类的外面，static 方法和变量能独立于任何对象而被使用。这样，你只要在类的名字后面加点号运算符即可。例如，如果你希望从类外面调用一个static方法，你可以使用下面通用的格式：

```java
classname.method( )
```

这里，classname 是类的名字，在该类中定义static方法。可以看到，这种格式与通过对象引用变量调用非static方法的格式类似。一个static变量可以以同样的格式来访问——类名加点号运算符。这就是Java 如何实现全局功能和全局变量的一个控制版本。

下面是一个例子。在main() 中，static方法callme() 和static 变量b在它们的类之外被访问。

```java
class StaticDemo {
static int a = 42;
static int b = 99;
static void callme() {
System.out.println("a = " + a);
}
}
class StaticByName {
public static void main(String args[]) {
StaticDemo.callme();
System.out.println("b = " + StaticDemo.b);
}
}
```

下面是该程序的输出：

```java
a = 42
b = 99
```

static成员是不能被其所在class创建的实例访问的。

如果不加static修饰的成员是对象成员，也就是归每个对象所有的。

加static修饰的成员是类成员，就是可以由一个类直接调用，为所有对象共有的.



**与非静态代码区别**

静态代码块，在虚拟机加载类的时候就会加载执行，而且只执行一次；非静态代码块，在创建对象的时候（即new一个对象的时候）执行，每次创建对象都会执行一次。例如：

```java
public class Test3 {
    public Test3(){
        System.out.println("默认构造方法！-->");
    }

    //非静态代码块
    {
        System.out.println("非静态代码块！-->");
    }

    //静态代码块
    static{
        System.out.println("静态代码块！-->");
    }

    public static void test(){
        {
            System.out.println("普通方法中的代码块！");
        }
    }

    public static void main(String[] args) {
        Test3 test1 = new Test3();
        Test3.test();
        Test3 test2 = new Test3();
    }
}
```

输出结果

```java
静态代码块！-->
非静态代码块！-->
默认构造方法！-->
普通方法中的代码块！
非静态代码块！-->
默认构造方法！-->
```

先执行的是静态代码块

然后执行了主函数main，在主函数中我们先是创建了一个新对象。在创建对象的时候先是执行了普通代码块。然后执行了构造函数。创建完第一个对象之后，我们调用了静态方法。然后我们再创建了第二个对象。也是先执行了普通代码块



**static语句块详解**

static{}(即static块)，会在类被加载的时候执行且仅会被执行一次，一般用来初始化静态变量和调用静态方法。

````java
public class Test
{
    public static int X = 100;

    public final static int Y = 200;

    public Test()
    {
        System.out.println("Test构造函数执行");
    }
    static
    {
        System.out.println("static语句块执行");
    }

    public static void display()
    {
        System.out.println("静态方法被执行");
    }

    public void display_1()
    {
        System.out.println("实例方法被执行");
    }

}
public class StaticBlockTest
{
    public static void main(String args[])
    {
        try
        {
            Class.forName("Test");
            Class.forName("Test");
        }
        catch (ClassNotFoundException e)
        {
            e.printStackTrace();
        }
    }
}
````

结果:你会发现虽然执行了两条Class.forName("Test")语句，但是，只输出了一条"静态方法被执行"语句；其实第二条Class.forName()语句已经无效了，因为在虚拟机的生命周期中一个类只被加载一次；又因为static{}是伴随类加载执行的，所以，不管你new多少次对象实例，static{}都只执行一次。

**static{}语句块执行的时机**

static{}语句块执行的时机，即类被加载准确含义:

（1）用Class.forName()显示加载的时候;

（2）实例化一个类的时候，如将main()函数的内容改为:Test t=new Test();//这种形式其实和1相比，原理是相同的，都是显示的加载这个类，读者可以验证Test t=new Test();和Test t=(Test)Class.forName().newInstance();这两条语句效果相同。

（3）调用类的静态方法的时候，如将main()函数的内容改为:Test.display();

（4）调用类的静态变量的时候，如将main()函数的内容改为:System.out.println(Test.X);

总体来说就这四种情况，但是我们特别需要注意一下两点:

（1）调用类的静态常量的时候，是不会加载类的，即不会执行static{}语句块，读者可以自己验证一下(将main()函数的内容改为System.out.println(Test.Y);)，你会发现程序只输出了一个200；(这是java虚拟机的规定，当访问类的静态常量时，如果编译器可以计算出常量的值，则不会加载类，否则会加载类)

（2）用Class.forName()形式的时候，我们也可以自己设定要不要加载类，如

```java
将Class.forName("Test")
改为
Class.forName("Test",false,StaticBlockTest.class.getClassLoader())
```

你会发现程序什么都没有输出，即Test没有被加载，static{}没有被执行。



**static{}语句块的执行次序**

（1）当一个类中有多个static{}的时候，按照static{}的定义顺序，从前往后执行；

（2）先执行完static{}语句块的内容，才会执行调用语句；

```java
public class TestStatic
{
    static
    {
        System.out.println(1);
    }
    static
    {
        System.out.println(2);
    }
    static
    {
        System.out.println(3);
    }

    public static void main(String args[])
    {
        System.out.println(5);
    }

    static
    {
        System.out.println(4);
    }
}
```

运行结果：

```java
程序会输出1，2，3，4，5
```

（3）如果静态变量在定义的时候就赋给了初值(如 static int X=100)，那么赋值操作也是在类加载的时候完成的，并且当一个类中既有static{}又有static变量的时候，同样遵循“先定义先执行”的原则；

```java
class Test
{
    public static int X = 300;
    static
    {
        System.out.println(X);
        X = 200;
        System.out.println(X);
    }
}

public class StaticBlockTest
{
    public static void main(String args[])
    {
        System.out.println(Test.X);
    }
}
```

结果:程序会依次输出300，200，200，先执行完X=300，再执行static{}语句块。

（4）访问静态常量，如果编译器可以计算出常量的值，则不会加载类。如果a类的静态常量的值是通过B类的静态常量（static final）赋值得来的，则不加载类，否则就需要加载类A。

```java
public class TestA
{
    public static final int a = TestB.a;

    public static final int b = TestB.b;
　　 public static final int c = 90;
　　static
    {
        System.out.println("TestA static语句块执行");
    }
}

public class TestB
{
    public static int a = 90;

    public static final int b = 90;

    static
    {
        System.out.println("TestB static语句块执行");
    }
}

public class StaticTest
{
    public static void main(String args[])
    {
        System.out.println(TestA.a);
    }
}
```

System.out.println(TestA.a);的结果：

```java
TestB static语句块执行
TestA static语句块执行
90
```

System.out.println(TestA.b)和System.out.println(TestA.c)的结果：

```java
90
```



**类加载特性 :**

1）在虚拟机的生命周期中一个类只被加载一次。

2)  类加载的原则：延迟加载，能少加载就少加载，因为虚拟机的空间是有限的。

3)  类加载的时机： - 第一次创建对象要加载类. - 调用静态方法时要加载类,访问静态属性时会加载类。 - 加载子类时必定会先加载父类。 - 创建对象引用不加载类. - 子类调用父类的静态方法时

```java
(1)当子类没有覆盖父类的静态方法时，只加载父类，不加载子类
(2)当子类有覆盖父类的静态方法时，既加载父类，又加载子类
```

- 访问静态常量，如果编译器可以计算出常量的值，则不会加载类,例如:public static final int a =123;否则会加载类,例如:public static final int a = math.PI



### static关键字修饰类

java里面static一般用来修饰成员变量或函数。但有一种特殊用法是用static修饰内部类，普通类是不允许声明为静态的，只有内部类才可以。

被static修饰的内部类可以直接作为一个普通类来使用，而不需实例一个外部类（见如下代码）：

需要注意的是当一个内部类没有使用static修饰的时候，是不能直接使用内部类创建对象，须要先使用外部类对象点new内部类对象及(外部类对象.new 内部类（）)

```java
public class OuterClass {
      public static class InnerClass{
          InnerClass(){
              System.out.println("============= 我是一个内部类'InnerClass' =============");
          }
      }
  }
  
  
public class TestStaticClass {
     public static void main(String[] args) {
         // 不需要new一个InnerClass
         new OuterClass.InnerClass();
     }
 }
```

如果没有用static修饰InterClass，则只能按如下方式调用：需要先new 一个外部类实例

```java
package inner_class;
 
public class OuterClass {
    public class InnerClass{
        InnerClass(){
            System.out.println("============= 我是一个内部类'InnerClass' =============");
        }
    }
}

public class TestStaticClass {
    public static void main(String[] args) {
        // OutClass需要先生成一个实例，然后再new一个InnerClass();
        OuterClass oc = new OuterClass();
        oc.new InnerClass();
    }
}
```

没有使用static修饰的内部类不能直接创建对象

```java
public class SyncDubbo2 {

    static class Main {
        public int i = 10;
        public synchronized void operationSup(){
            try {
                i--;
                System.out.println("Main print i = " + i);
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    //没有使用static修饰的内部类
    class Sub extends Main {
        public synchronized void operationSub(){
            try {
                while(i > 0) {
                    i--;
                    System.out.println("Sub print i = " + i);
                    Thread.sleep(100);        
                    this.operationSup();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    
    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {  
                // 此处内部类没用static修饰会报错误The value of the local variable sub is not used
                Sub sub = new Sub(); 
                // 没有使用static修饰的内部类不能直接创建对象
						}}); 
      	t1.start();
    		} 
		}
```





### static是什么，java中是否可以override一个private或者static方法？

static关键字表明一个成员变量或者成员方法可以在所属的类没有实例化的情况下被访问。

java中的static方法不允许被覆盖，因为方法覆盖是基于运行时动态绑定的，而static方法是编译时静态绑定的。static和类的任何实例都不相关，所有概念上不适用。



### static nested class和inner class不同？

static nested class是被申明为static的内部类，它可以不依赖于外部类进行实例化。而通常的内部类需要在外部类实例化之后才能被实例化。static nested class的成员，既可以定义为静态(static)，也可以被定义为动态的(instance)。 Nested class的静态成员(method)，只能对外部类的静态成员(static memeber)进行操作，但是不能access外部类的动态成员。而Nested class的动态成员(instance member)可以访问外部类的所有成员。



### 是否可以在static环境中访问非static变量？

答案是不可以，因为static变量是属于类的，在类加载的时候就被初始化了，这时候非静态变量并没有加载，故非静态变量不能访问。



### 列举熟悉的Object类中的方法，并且简要说明

Object()默认构造方法

clone()创造并且返回一个对象的副本

equals()指示某个对象和当前对象是否相等

finallize()当垃圾处理器确定不存在对该对象的更多的引用时候，这个方法被调用

getClass()返回这个对象的运行时类

hashcode()返回对象的哈希值码

notify()唤醒在这个对象监视器等待的单个线程

notifyAll()唤醒在这个对象监视器等待的所有线程



## 垃圾回收

### GC中如何判断对象是否需要回收？

**GC主要做三个事情：**
1、什么对象可以回收
2、什么时候进行回收
3、如何回收
jvm里的垃圾就是对象，指无用的对象，在真正执行垃圾回收前，必须要判断对象是否是无用，是否可以回收，那么jvm是如何来判断一个对象能否回收呢？

**引用计数算法**

方式：给对象维护一个引用计数器，当有一个地方引用到它，则计数器加1，当有引用失效，则计数器减1，当为0时，说明没有地方引用到这个对象。
优点：实现简单、效率高
缺点：无法解决循环引用。

**可达性分析算法**

方式：从一系列被称为GC ROOT的对象开始，向下搜索，搜索走过的路径称为引用链，当一个对象到GC ROOT之间没有引用链，说明这个对象不可用。
可作为GC ROOT的对象：
（1）虚拟机栈中引用的对象；
（2）方法区内类的静态属性引用的对象；
（3）方法区常量引用的对象；
（4）本地方法栈中引用的对象。

**finalize**
当一个对象被判定为不可达对象后，也并不是非死不可。
在通过可达性分析算法判断没有引用链使之与GC ROOT相连，会判断该对象是否有必要执行finalize方法:
假如重写了finalize，并且未调用过，则说明有必要执行。
判断有必要执行finalize的对象，会被放入一个队列，有jvm建立的低优先级的Finalizer线程去执行。
当在finalize中自救成功的对象，就会在第二次标记时移除即将回收的集合。
自救失败的就会被回收，不会在执行finalize。
所谓自救就是把自己与引用链上的一个对象关联起来。



## JVM

### JVM分区

![img](https://img-blog.csdnimg.cn/20181226105629124.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNzU1NzU3,size_16,color_FFFFFF,t_70)

**1、程序计数器**
程序计数器是当前线程所执行的行号指示器。通过改变计数器的值来确定下一条指令，比如循环，分支，跳转，异常处理，线程恢复等都依赖计数器来完成。

由于在JVM中，多线程是通过线程轮流切换来获得CPU执行时间的，因此在任一时刻，一个CPU的内核只会执行一条线程中的指令，因此，为了能够使得每个线程都在线程切换后能够恢复在切换之前的程序执行位置，每个线程都需要有自己独立的程序计数器，并且不能互相被干扰，否则就会影响到程序的正常执行次序。因此每个计数器是每个线程私有的。

在JVM规范中规定，如果线程执行的是非native方法，则程序计数器中保存的是当前需要执行的指令的地址；如果线程执行的是native方法，则程序计数器中的值是undefind。

由于程序计数器中存储的数据所占空间的大小不会随程序的执行发生改变，因此，程序计数器是不会发生内存溢出（OutOfMemory）现象的。

**2、虚拟机栈**
虚拟机栈也就是我们所说的栈内存，是**java方法执行的内存模型**。每个方法在执行的时候都会创建一个栈帧，用于存储局部变量表、操作数栈、动态链接、和方法返回地址等信息。

局部变量表存储的是基本数据类型、returnAdress类型和对象引用。局部变量表的大小在编译期间完成分配，因此程序执行期间局部变量表的大小不会改变。

操作数栈主要用来存储运算结果及运算的操作数。在数据结构中，栈最典型的一个应用就是用来对表达式求值。程序中的所有计算过程都是借助操作数栈完成的。

每个栈帧都包含一个指向运行时常量池中该栈帧所属方法的引用，持有这个引用是为了支持方法调用中的动态链接就是将常量池中的符号引用在运行期间转化为直接引用。

**3、本地方法栈：**
本地方法栈和虚拟机栈类似，只不过本地方法栈为虚拟机使用本地方法（native）服务。



**所有线程共享的内存区域**

**4、堆**

java 堆是JVM内存区域中最大的一块，它被所有线程所公用。它随着JVM的启用而创建，**它主要是用来存放java程序中所产生的对象实例**。在java中我们不需要手动的去分配和释放内存。内存的分配是由程序完成的，我们通过关键字new 为每个对象申请内存空间 (基本类型除外)，所有的对象都在堆 (Heap)中分配空间。而释放内存是通过GC(垃圾收集器)管理释放的。堆还可以细分为**新生代和老年代**，**新生代再细致一点还可以分为Eden区、From Survivior区、To Survivor区。** 如果堆内存不足就可能导致堆内存溢出 java.lang.OutOfMemoryError

java堆是所有线程共享的一块内存，在虚拟机启动时创建，几乎所有的对象实例都在这里创建，因此该区域经常发生垃圾回收。从内存回收的角度看，由于现在收集器基本都是采用分代收集算法，所以java堆中还可以细分为：新生代和老年代；新生代又分为Eden空间、From Survivor空间、To Survivor空间三部分。

**5、方法区**

方法区**用于存储虚拟机加载的类信息、常量、静态变量（JDK7中被移到Java堆),即时编译期编译后的代码（类方法）等数据**等数据，虚拟机规范是把这块区域描述为堆的一个逻辑部分的，但实际它应该是要和堆区分开的。这里需要说一下**运行时常量池**，**它是方法区的一部分，用于存放编译期生成的各种字面量和符号引用（其实就是八大基本类型的包装类型和String类型数据（JDK7中被移到Java堆））**
jdk7已经把原本放在方法区的**字符串常量池**（注意名字是字符串常量池不是运行时常量池）移出。

方法区和java堆一样，是各个线程共享的内存区域，不需要连续的内存，并且可以动态扩展，动态扩展失败一样会抛出OutOfMemoryError异常。方法区用于存放已被虚拟机加载的类信息、常量、静态变量、即时编译器编译后的代码等数据。虽然Java虚拟机规范把方法区描述为堆的一个逻辑部分，但是为了与java堆区分开，方法区又叫非堆（Non-Heap）,很多人更愿意把方法区称为“永久代”。从jdk1.7已经开始准备“去永久代”的规划，jdk1.7的HotSpot中，已经把原来放在方法区中的静态变量，字符串常量池等移到堆内存中。在jdk1.8中，永久代已经不存在，存储的类信息、即时编译器编译后的代码等已经移动到元空间（MetaSpace）中，元空间并没有处于堆内存上，而是直接占用本地内存（NativeMemory）。

运行时常量池属于方法区的一部分，常量池中存放2类常量：字面量和符号引用。字面量比较接近java语言层面的常量概念，如文本字符串，被声明为final的常量值等。而符号引用则属于编译原理方面的概念，包括3类常量：类和接口的全限定名、字段的名称和描述符，方法的名称和描述符。

![这里写图片描述](https://img-blog.csdn.net/20180504164639666?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2h1YmluOTE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



### JVM回收算法

**1、引用算法（Reference Counting）**
 在对象头处维护一个counter，每增加一次对该对象的引用计数器自加，如果对该对象的引用失联，则计数器自减。当counter为0时，表明该对象已经被废弃，不处于存活状态。这种方式一方面无法区分软、虛、弱、强引用类别。另一方面，会造成死锁，假设两个对象相互引用始终无法释放counter，永远不能GC。此算法最致命的是无法处理循环引用的问题。

**2、复制算法（Copying）**
 将原有的内存空间分为两块，每次只使用其中的一块，在垃圾回收时候，将正在使用的内存中的存活对象复制到为未使用的内存中，清除正在使用的内存块中的所有对象，交换两个内存的角色，完成垃圾回收。此算法每次只处理正在使用中的对象，因此复制成本较小，同时复制过去以后还能进行相应的内存整理，不会出现 “ 碎片 ” 问题。当然，此算法的缺点也是很明显的，就是需要两倍内存空间。

**标记 - 清除 （Mark - Sweep）**
此算法执行分两阶段。第一阶段从引用根节点开始标记所有被引用的对象，第二阶段便利整个堆，把未标记的对象清除。此算法需要暂停整个应用，同时，会产生内存碎片。

**标记 - 整理（Mark - Compact）**
 此算法结合了 “标记 - 清除” 和 “复制” 两个算法的优点。也是分为两阶段，第一阶段从根节点开始标记所有被引用对象，第二阶段便利整个堆，把清除未标记对象并且把存活对象 “压缩” 到堆的其中一块，**按顺序排放**。此算法避免了 “标记 - 清除” 的碎片问题， 同时也避免了 “复制” 算法的空间问题。



