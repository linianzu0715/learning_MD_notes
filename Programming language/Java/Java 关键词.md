## Java 关键词

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