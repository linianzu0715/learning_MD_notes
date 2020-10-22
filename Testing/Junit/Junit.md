### Junit

#### 简介

```
JUnit 是一个 Java 编程语言的单元测试框架。JUnit 在测试驱动的开发方面有很重要的发展，是起源于 JUnit 的一个统称为 xUnit 的单元测试框架之一。
```

#### 好处

```
1. 可以书写一系列的测试方法，对项目所有的接口或者方法进行单元测试。
2. 启动后，自动化测试，并判断执行结果, 不需要人为的干预。
3. 只需要查看最后结果，就知道整个项目的方法接口是否通畅。
4. 每个单元测试用例相对独立，由Junit启动，自动调用。不需要添加额外的调用语句。
5. 添加，删除，屏蔽测试方法，不影响其他的测试方法。 开源框架都对JUnit有相应的支持。
```

#### 环境配置

```
从官网 http://www.junit.org 下载 JUnit 最新版本的压缩文件。
笔者使用Maven（Java包管理工具）导入所需要的jar包：
```

```xml
<!-- https://mvnrepository.com/artifact/junit/junit -->
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>
```

#### 基本用法

测试代码和生成代码分开放置，Maven默认目录正好符合这个要求。

被测试代码放在`main`下的`java`目录中，junit测试代码放在`test`下的`java`目录中，形成一一对应关系，测试代码使用`Test`开头命名。

##### Example:

被测试的代码：

```java
public class MessageDemo{
  private String message;
  public MessageDemo (String message){
    this.message = message;
  }
  public String printMessage(){
    System.out.println(this.message);
    return message
  }
}
```

测试代码TestMessageDemo:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestMessageDemo{
  private String message = "Hello World";
  private MessageDemo messageDemo = new MessageDemo(this.message);
  
  @Test
  public void testPrintMessage(){
    assertEquals(message, messageDemo.printMessage());
  }
}
```

基本的已经写好了，但是如何运行测试呢？
还需要建一个运行测试的文件：

```java
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class TestRunner{
  public static void main (String[] args){
    Result result = JUnitCore.runClasses(TestMessageDemo.class);
    for (Failure failure : result.getFailures()){
      System.out.println(failure.toString());
    }
    System.out.println("Test result: " + result.wasSuccessful());
  }
}

```

运行测试文件

```
Hello world
Test result: True
```

看到`true`表明测试成功，那么我们来尝试一下测试不成功是什么情况。

我们修改一下TestMessageDemo的代码

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestMessageDemo{
  private String message = "Hello World";
  private MessageDemo messageDemo = new MessageDemo(this.message);
  
  @Test
  public void testPrintMessage(){
    assertEquals("No", messageDemo.printMessage());
  }
}
```

再执行一遍

```
Hello world
testPrintMessage(TestMessageDemo):expected: <[No]> but was: <[Hello world]>
Test result: False
```

#### Junit断言

Junit所有的断言都包含在 Assert 类中。

这个类提供了很多有用的断言方法来编写测试用例。只有失败的断言才会被记录。Assert 类中的一些有用的方法列式如下：

```java
void assertEquals(boolean expected, boolean actual):检查两个变量或者等式是否平衡
void assertTrue(boolean expected, boolean actual):检查条件为真
void assertFalse(boolean condition):检查条件为假
void assertNotNull(Object object):检查对象不为空
void assertNull(Object object):检查对象为空
void assertSame(boolean condition):assertSame() 方法检查两个相关对象是否指向同一个对象
void assertNotSame(boolean condition):assertNotSame() 方法检查两个相关对象是否不指向同一个对象
void assertArrayEquals(expectedArray, resultArray):assertArrayEquals() 方法检查两个数组是否相等
```

#### JUnit 注解

```
@Test:这个注释说明依附在 JUnit 的 public void 方法可以作为一个测试案例。
@Before:有些测试在运行前需要创造几个相似的对象。在 public void 方法加该注释是因为该方法需要在 test 方法前运行。
@After:如果你将外部资源在 Before 方法中分配，那么你需要在测试运行后释放他们。在 public void 方法加该注释是因为该方法需要在 test 方法后运行。
@BeforeClass:在 public void 方法加该注释是因为该方法需要在类中所有方法前运行。
@AfterClass:它将会使方法在所有测试结束后执行。这个可以用来进行清理活动。
@Ignore:这个注释是用来忽略有关不需要执行的测试的。
```

#### JUnit 加注解执行过程

```
beforeClass(): 方法首先执行，并且只执行一次。
afterClass():方法最后执行，并且只执行一次。
before():方法针对每一个测试用例执行，但是是在执行测试用例之前。
after():方法针对每一个测试用例执行，但是是在执行测试用例之后。在 before() 方法和 after() 方法之间，执行每一个测试用例。
```

### JUnit 执行测试

```
测试用例是使用 JUnitCore 类来执行的。JUnitCore 是运行测试的外观类。要从命令行运行测试，可以运行java org.junit.runner.JUnitCore。对于只有一次的测试运行，可以使用静态方法 runClasses(Class[])。
```

#### JUnit 套件测试

测试套件意味着捆绑几个单元测试用例并且一起执行他们。

在 JUnit 中，`@RunWith`和`@Suite`注释用来运行套件测试。

 被测试的代码还是MessageDemo。 新建两个类，用来展示套件测试：

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestMessageDemo{
  private String message = "Hello World";
  private MessageDemo messageDemo = new MessageDemo(this.message);
  
  @Test
  public void testPrintMessage(){
    assertEquals("No", messageDemo.printMessage());
  }
}
```

TestMessageDemo2:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestMessageDemo2{
  private String message = "Robert";
  private MessageDemo messageDemo = new MessageDemo(this.message);
  
  @Test
  public void testPrintMessage(){
    assertEquals("Hi", messageDemo.printMessage());
  }
}
```

TestSuit代码：

```java
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
  TestMessageDemo.class;
  TestMessageDemo2.class;
})
public class TestSuit(){
  
}
```

TestRunner代码：

```java
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class TestRunner{
  public static void main(String[] args){
    Result result = JUnitCore.runClasses(TestSuite.class);
    for (Failure failure in result.getFailures()){
      System.out.println(failure.toString())
    }
    System.out.println("Test result: " + result.wasSuccessful())	
  }
}
```

通过这样的方式，我们就可以一次运行多个测试了

#### JUnit时间测试

如果一个测试用例比起指定的毫秒数花费了更多的时间，那么 Junit 将自动将它标记为失败。`timeout`参数和 `@Test` 注释一起使用。是不是很强大？

就像这样：

```java
@Test(timeout=1000)
```

时间单位是毫秒。

#### JUnit异常测试：

Junit 用代码处理提供了一个追踪异常的选项。你可以测试代码是否它抛出了想要得到的异常。`expected` 参数和 `@Test` 注释一起使用。

```java
@Test(expected = ArithmeticException.class)
```

#### JUnit 参数化测试

Junit 4 引入了一个新的功能参数化测试。参数化测试允许开发人员使用不同的值反复运行同一个测试。你将遵循 5 个步骤来创建参数化测试。

```
用 @RunWith(Parameterized.class) 来注释 test 类。
创建一个由 @Parameters注释的公共的静态方法，它返回一个对象的集合(数组)来作为测试数据集合。
创建一个公共的构造函数，它接受和一行测试数据相等同的东西。
为每一列测试数据创建一个实例变量。
用实例变量作为测试数据的来源来创建你的测试用例。
```

一旦每一行数据出现测试用例将被调用。

### 参数化测试例子

被测试代码`PrimeNumberChecker`:

```java
public class PrimeNumberChecker{
  public void validate(final int primeNumber){
    for (int i = 2; i < (primeNumber / 2); i++){
      if (primeNumber % i == 0){
        return false;
      }
    }
    return true;
  }
}
```

测试代码`TestPrimeNumberChecker`：

```java
import org.junit.Before;
import org.junit.Test;
import org.junit,runner.RunWith;
import org.junit,runners.Paratmeterized;
import java.util.Arrays;
import java.util.Collection;
import static org.junit.Assert.assertEquals;

@RunWith(Parameterized.class)
public class TestPrimeNumberChecker{
  private int inputNumber;
  private boolean expectedResult;
  private PrimeNumberChecker primeNumberChecker;
  
  @Before
  public void intialize(){
    primeNumberChecker = new PrimeNumberChecker();
  }
  
  public TestPrimeNumberChecker(int inputNumber, boolean expectedResult){
    this.inputNumber = inputNumber;
    this.expectedResult = expectedResult;
  }
  
  @Parameterized.Parameters
  public static Collection primeNumbers(){
    return Array.asList(new Object[][]{
      {2, true},
      {6, false},
      {19,true},
      {22, false}
    });
  }
  
  @Test
  public void testPrimeNumberCheck(){
    System.out.println("Parameterized number is: " + inputNumber);
    assertEquals(expectedResult, primeNumberChecker(inputNumber));
  }
  
}
```

测试运行代码：

TestRunner:

```java
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class TestRunner:{
  public static void main (String[] args){
    Result result = JUniteCore.runClasses(TestPrimeNumberChecker.class);
    for (Failure failure : result.getFailures()){
      System.out.println(failure.toString());
    }
    System.out.println("Test result: " + result.wasSuccessul());
  }
}
```

测试结果：

```
Parameterized number is: 2
Parameterized number is: 6
Parameterized number is: 12
Parameterized number is: 22
Test result: true
```





