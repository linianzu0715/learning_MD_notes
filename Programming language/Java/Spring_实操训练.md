### Spring 实操训练

#### LOC推导

##### 原来的方式

我们之前写业务需要的几个组件：

* UserDao 接口
* UserDaoImple 实现类
* UserService  接口

* UserServiceImple  实现类



###### 创建项目

![image-20200516180851726](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516180851726.png)



**maven是什么**

我先不说maven，也不说java开发，先说做菜，你可能像做个红烧小排(HongshaoxiaopaiApp)，你需要的材料是：

1. 小排(xiaopai.jar)，要小猪的（version=little pig）。
2. 酱油(jiangyou.jar)，要82年的酱油（version=1982）
3. 盐(yan.jar)
4. 糖(tang.jar)，糖要广东产的（version=guangdong）
5. 生姜(shengjiang.jar)
6. 茴香(huixiang.jar)

于是，你要去菜场买小排，去门口杂货店买酱油，买盐……可能你家门口的杂货店还没有1982年的酱油，你要去3公里外的农贸市场买……你买原材料的过程估计会很痛苦，可能买到的材料不是1982年的，会影响口感。

在你正式开始做小排前，你会为食材的事情，忙得半死。

现在有个超市出了个盒装版的半成品红烧小排，把生的小排，1982年的酱油，盐，广东产的糖等材料打包成一个盒子里，你回家只要按照说明，就能把红烧小排做出来，不用考虑材料的来源问题。

Maven就是那个超市，红烧小排就是你要开发的软件，酱油、盐什么的就是你开发软件要用到的jar包——我们知道，开发java系统，下载一堆jar包依赖是很正常的事情。有了maven，你不用去各个网站下载各种版本的jar包，也不用考虑这些jar包的依赖关系。Maven会给你搞定，就是超市的配菜师傅会帮你把红烧小排的配料配齐一样。

现在你应该明白Maven是做什么的了吧。

解释好了Maven是什么之后  我们还要看看project SDK是什么



**project SDK：**

软件开发套件



![image-20200516185035590](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516185035590.png)



![image-20200516185129018](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516185129018.png)



![image-20200516190116622](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516190116622.png)

![image-20200516190333022](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516190333022.png)

![image-20200516190424577](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516190424577.png)



###### 初始代码

然后就是创建我们的项目代码了 假设我们有一个Dao层的接口 定义一个```getUesr() ```方法 然后Dao层的实现类都要去实现这个方法  因此我们有```UserDaoImple()```要来实现这个方法  然后对于服务层 我们也有一个  ```getUesr() ```要去实现  基于```UserService```接口

总共的关系如图

![image-20200516214327773](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516214327773.png)

然后我们写一个测试程序来测试我们的代码

![image-20200516214427481](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516214427481.png)

能够成功输出

###### 在Dao层中有多个实现类

我们在Dao层中加入多个实现类

```java
package summer.nianzu.dao;

public class UserDaoImple implements UserDao{
    @Override
    public void getUser() {
        System.out.println("获取用户基本的数据");
    }
}
```

```java
package summer.nianzu.dao;

public class UserDaoSqlImpl implements UserDao{
    @Override
    public void getUser() {
        System.out.println("获取用户sql中的数据");
    }
}
```



现在我们有了两个实现类

但是如果我们想要使用新的实现类sql  我们需要在服务层也修改代码 如图

![image-20200516215415590](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516215415590.png)



这样才能得到正确的输出

![image-20200516215213405](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516215213405.png)



###### 问题

我们不希望当我们的用户的需求发生改变的时候  我们需要到服务层更改代码 



##### 解决问题

我们使用```set()```方法来解决在服务层需要修改代码的问题 我们不是在服务层写死这个实现类的类别  而是提供一个```set()```方法

![image-20200516220042711](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516220042711.png)

然后我们在用户使用的时候（也就是test时） 可以由用户决定使用哪个对象

![image-20200516220217090](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200516220217090.png)

这样我们就能在用户使用的时候再做决定  在原来的代码中 用户的需求可能影响我们的代码  因为我们需要根据用户的需求去修改源代码  如果我们项目的代码量十分大 那么我们修改一次程序的代价将会很高



#### Hello Spring

我们用spring来实现一个最简单的程序

spring xml 框架

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">


</beans>
```





首先我们创建一个新的项目，并且在项目的src目录之下创建一个新类demo， demo中声明一个字符串name，并且为这个变量设置setter和getter方法。

![image-20200518193033566](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518193033566.png)

然后我们在resouces资源目录之下新建一个xml配置文件，在xml文件中加入spring的配置信息，并且将类demo也加入到spring中

![image-20200518193212921](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518193212921.png)

然后我们新建一个测试类，并且尝试从spring中取出我们的类，在这个过程中，我们没有使用new来创建类。类中的值已经在xml文件中声明好了

![image-20200518193334628](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518193334628.png)

这样我们就使用最简单的方式，从spring中取出了我们想要的对象

##### 参数是通过setter方法输出

当我们尝试在demo类中删除setter方法时，会发生什么？

![image-20200518194936700](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518194936700.png)

这个时候就会报错  提示我们在注入参数的时候发生了错误  说明在sprin中给参数注入具体的数值是通过setter方法实现的

### spring的构造方式：

#### 使用无参构造

我们在类中声明一下无参数构造方法，并且进行测试

![image-20200518203402012](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518203402012.png)

![image-20200518203416211](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518203416211.png)

发现spring默认是调用了类的无参数构造方法来构造了一个实例，并且使用setter方法给参数赋值



#### 使用有参数构造器

假设我们要覆盖类中的无参数构造器 就是要重新写一个有参数构造器

![image-20200518203709446](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518203709446.png)

这个时候就会发现我们初始化报错了

![image-20200518203751223](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518203751223.png)

因此我们原来那种方法是默认使用无参数构造器进行实例化的  当无参数构造器被覆盖之后 就无法正常进行实例化

##### 使用构造器参数索引

```xm
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg index="0" value="7500000"/>
    <constructor-arg index="1" value="42"/>
</bean>
```

因此我们要使用index，就需要在xml文件中进行相应的修改

![image-20200518204518459](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518204518459.png)

![image-20200518204538308](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518204538308.png)

然后我们这里就显示使用有参数构造成功

##### 使用构造器参数名称

```xm
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg name="years" value="7500000"/>
    <constructor-arg name="ultimateAnswer" value="42"/>
</bean>
```

我们同时也可以使用参数的名称在构造器中构造

![image-20200518204736437](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518204736437.png)

![image-20200518204758836](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518204758836.png)

也能构造成功

##### 使用构造器参数类别

```xm
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg type="int" value="7500000"/>
    <constructor-arg type="java.lang.String" value="42"/>
</bean>
```

![image-20200518205025654](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518205025654.png)

![image-20200518205043910](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200518205043910.png)



当我们有多个类在xml文件中被配置时，当spring的上下文对象被实例化时，所有xml配置的类都会被实例化，等待我们去调取

### Spring配置

#### 别名alias

我们可以给bean设置别名  这样我们就也能通过别名来取出我么的bean对象

![image-20200519115450015](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519115450015.png)

![image-20200519115543732](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519115543732.png)

#### bean对象

我们用bean在spring中配置我们的类

![image-20200519120731509](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519120731509.png)



#### import

导入其他的配置文件 用于团队协作

![image-20200519120715222](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519120715222.png)

### DI 依赖注入

依赖：bean对象的创建依赖于容器 

注入：bean对象中的所有属性，由容器注入

#### 构造器注入

前面说过了

#### setter方法注入

student类：

```java
package com.example.demo;

import java.util.*;

public class student {
    private address ads;
    private String name;
    private String[] books;
    private List<String> hobbies;
    private Map<String, String> cards;
    private Set<String> games;
    private Properties info;

    public address getAds() {
        return ads;
    }

    public void setAds(address ads) {
        this.ads = ads;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String[] getBooks() {
        return books;
    }

    public void setBooks(String[] books) {
        this.books = books;
    }

    public List<String> getHobbies() {
        return hobbies;
    }

    public void setHobbies(List<String> hobbies) {
        this.hobbies = hobbies;
    }

    public Map<String, String> getCards() {
        return cards;
    }

    public void setCards(Map<String, String> cards) {
        this.cards = cards;
    }

    public Set<String> getGames() {
        return games;
    }

    public void setGames(Set<String> games) {
        this.games = games;
    }

    public Properties getInfo() {
        return info;
    }

    public void setInfo(Properties info) {
        this.info = info;
    }

    @Override
    public String toString() {
        return "student{" +
                "ads=" + ads +
                ", name='" + name + '\'' +
                ", books=" + Arrays.toString(books) +
                ", hobbies=" + hobbies +
                ", cards=" + cards +
                ", games=" + games +
                ", info=" + info +
                '}';
    }
}

```

address类：

```java
package com.example.demo;

public class address {
    private String address;


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "address{" +
                "address='" + address + '\'' +
                '}';
    }
}

```

配置文件：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="address" class="com.example.demo.address"></bean>

    <bean id="student" class="com.example.demo.student">
        <!-->普通值注入<!-->
        <property name="name" value="nianzu"></property>

        <!-->bean注入<!-->
        <property name="ads" ref="address"></property>

        <!-->数组注入<!-->
        <property name="books">
            <array>
                <value>红楼梦</value>
                <value>三国演义</value>
                <value>西游记</value>
                <value>水浒传</value>
            </array>
        </property>

        <!-->数组注入<!-->
        <property name="hobbies">
            <list>
                <value>打篮球</value>
                <value>踢足球</value>
                <value>唱歌</value>
            </list>
        </property>

        <!-->map注入<!-->
        <property name="cards">
            <map>
                <entry key="ID" value="1234567"></entry>
                <entry key="bank" value="7654321"></entry>
            </map>
        </property>

        <!-->set注入<!-->
        <property name="games">
            <set>
                <value>LOL</value>
                <value>popcart</value>
            </set>
        </property>

        <!-->property注入<!-->
        <property name="info">
            <props>
                <prop key="性别">男</prop>
                <prop key="年龄">23</prop>
            </props>
        </property>
    </bean>
</beans>
```

测试输出：

![image-20200519133046669](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519133046669.png)



#### 拓展方式注入

##### p命名空间注入

要使用p命名空间注入，我们需要在springxml配置框架中加入一行规定。

新的框架

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:p="http://www.springframework.org/schema/p" <!--> 这一行是新加入的 
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd">

    
</beans>
```

我们使用新的注入方式来注入我们的属性

![image-20200519151739011](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519151739011.png)

![image-20200519151807599](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519151807599.png)





##### c命名空间注入

c命名空间注入是通过向构造器中传入参数来构造的，需要在xml配置文件中接入新的一行



我们在使用时必须保证我们的类有有参数构造器

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:c="http://www.springframework.org/schema/c"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="beanTwo" class="x.y.ThingTwo"/>
    <bean id="beanThree" class="x.y.ThingThree"/>

    <!-- traditional declaration with optional argument names -->
    <bean id="beanOne" class="x.y.ThingOne">
        <constructor-arg name="thingTwo" ref="beanTwo"/>
        <constructor-arg name="thingThree" ref="beanThree"/>
        <constructor-arg name="email" value="something@somewhere.com"/>
    </bean>

    <!-- c-namespace declaration with argument names -->
    <bean id="beanOne" class="x.y.ThingOne" c:thingTwo-ref="beanTwo"
        c:thingThree-ref="beanThree" c:email="something@somewhere.com"/>

</beans>
```

![image-20200519153725206](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519153725206.png)

![image-20200519153741768](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519153741768.png)

### bean 作用域

![image-20200519165126310](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519165126310.png)

### bean的自动装配

spring会在上下文中自动寻找并且自动装配属性

在spring中有三种装配的方式：

1. 在xml中显示的装配属性
2. 在java中显示装配
3. 隐式装配



我们设置了三个类，people，dog，cat。 dog和cat都有shout()方法 

#### byName自动装配

我们在xml中设置自动装配

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="dog" class="com.example.demo.Dog"/>
    <bean id="cat" class="com.example.demo.Cat"/>
    <bean id="people" class="com.example.demo.People" autowire="byName"> <!-->在这里进行自动装配<!-->
        <property name="name" value="nianzu"></property>
    </bean>
</beans>
```

他要求我们声明的id名称需要和people类中声明的名称相同，如果我们更改声明名称 自动装配将会失败

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="dog" class="com.example.demo.Dog"/>
    <bean id="cat111" class="com.example.demo.Cat"/>
    <bean id="people" class="com.example.demo.People" autowire="byName"> <!-->在这里进行自动装配<!-->
        <property name="name" value="nianzu"></property>
    </bean>
</beans>
```

这样将会失败

#### byType自动装配

这种方法会在上下文中查询类型匹配的对象进行自动装配 这个时候就不需要名称相同

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="dog" class="com.example.demo.Dog"/>
    <bean id="cat222" class="com.example.demo.Cat"/>
    <bean id="people" class="com.example.demo.People" autowire="byType">
        <property name="name" value="nianzu"></property>
    </bean>
</beans>
```

#### 使用注解进行自动装配

##### @Autowired

要使用注解 需要加入一些支持  新的框架如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <context:annotation-config/>

</beans>
```

然后我们就能加上@autowire的注解

```java
public class People {
    private String name;
    @Autowired
    private Cat cat;
    @Autowired
    private Dog dog;
```



如果我们遇到这种情况  在xml中配置了两个猫，两个狗，并且他们的名字也不同

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <bean id="dog1" class="com.example.demo.Dog"/>
    <bean id="dog2" class="com.example.demo.Dog"/>
    <bean id="cat1" class="com.example.demo.Cat"/>
    <bean id="cat2" class="com.example.demo.Cat"/>
    <bean id="people" class="com.example.demo.People">
        <property name="name" value="nianzu"></property>
    </bean>

    <context:annotation-config/>

</beans>
```

这个时候系统就不能自动绑定 因为不论是根据名字还是根据类别  都不能自动找到所对应的bean

这个时候我们可以手动给它加上@qualifier

![image-20200519192319788](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519192319788.png)



##### @Resource

我们也可以使用java的自动绑定注释  它也要求绑定的bean中名字获得类型是对应的

```java
public class People {
    private String name;

    @Resource
    private Cat cat;
    @Resource
    private Dog dog;
```

```xml
 <bean id="dog" class="com.example.demo.Dog"/>
    <bean id="dog2" class="com.example.demo.Dog"/>
    <bean id="cat" class="com.example.demo.Cat"/>
    <bean id="cat2" class="com.example.demo.Cat"/>
    <bean id="people" class="com.example.demo.People">
        <property name="name" value="nianzu"></property>
    </bean>
```

同时@Resource也允许通过name来具体绑定某个bean

```java
public class People {
    private String name;

    @Resource(name = "cat2")
    private Cat cat;
    @Resource(name = "dog2")
    private Dog dog;

    public String getName() {
        return name;
    }
```

@Resource 和 @Autowired的区别：

* 都是用来自动装配的，都可以放在属性字段的上面
* @Autowired 通过byType的的方式实现  并且要求这个对象存在
* @Resource 默认通过byName的方式实现，如果找不到名字，则通过byType的方式实现。如果都找不到，就报错！
* 执行方式不同

### 使用注解开发

#### @component

在spring4之后，要使用注解开发，不许要保证aop包导入

同时也要导入自动装配的配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <!-->指定自动扫描的包，这个包之下的注解都会被扫描到<!-->
    <context:component-scan base-package="com.example.demo"/>
    <context:annotation-config/>

</beans>
```



载入了配置之后，我们只要在类之前加入@Component的注解 就相当于已经在xml文件中配置了这个类

```java
@Component
public class Cat {
    public void shout(){
        System.out.println("miao~");
    }
}
```

```java
@Component
public class Dog {
    public void shout(){
        System.out.println("wang~");
    }

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <bean id="people" class="com.example.demo.People">
        <property name="name" value="nianzu"></property>
    </bean>

    <!-->指定自动扫描的包，这个包之下的注解都会被扫描到<!-->
    <context:component-scan base-package="com.example.demo"/>
    <context:annotation-config/>

</beans>
```

我们能看到xml文件中已经没有了\<bean>dog标签,但是依旧能允许成功 说明我们的注解帮助我们配置了这个类



#### @value

加入属性值

```java
@Component
public class People {

    @Value("nianzu")
    private String name;

    @Resource
    private Cat cat;
    @Resource
    private Dog dog;
}
```

我们直接在People类中加入了name的值  有了@component和@value之后  我们的xml文件就大大简化了

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">


    <!-->指定自动扫描的包，这个包之下的注解都会被扫描到<!-->
    <context:component-scan base-package="com.example.demo"/>
    <context:annotation-config/>

</beans>
```

就只剩下了框架 其余的操作我们都通过注释完成了

当然 这是简单类型的注入  复杂类型的注入还是更加推荐使用xml  更清晰

#### 衍生的注解：

1. Dao层：@Repository
2. Service层：@Service
3. Controller层：@Controller

这四个注解的意思都是一样的 都是将某个类注册到spring中，装配bean





![image-20200519202742555](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200519202742555.png)

#### @scope

规定作用域

```java
@Component
@Scope("singleton")
public class People {

    @Value("nianzu")
    private String name;

    @Resource
    private Cat cat;
    @Resource
    private Dog dog;
}
```

默认为单例模式

### 使用java的方式配置spring

我们不使用xml的方式进行配置 而是全权用java

javaconfig是spring的一个子项目 在spring 4之后被推荐



我们还是先创立一个类 并且给它加上注解

```java
@Component
public class User {

    @Value("nianzu")
    private String name;
}
```

然后我们不使用xml进行配置 而是给他加入一个config类

```java
@Configuration
public class Javaconfig {

    @Bean
    public User getUser(){
        return new User();
    }

}
```

这个类就相当于我们之前的xml文件

然后我们就能时候之前相似（但是有区别）的方法从spring中取出我们的bean

```java
public class Mytest {

    @Test
    public void test(){
        ApplicationContext ctx = new AnnotationConfigApplicationContext(Javaconfig.class);
        User user = ctx.getBean("getUser", User.class);

        System.out.println(user);

    }
}
```



当我们有多个配置文件的时候  我们要怎样使得多个配置文件合并到一个类里面去？

使用@import注解

```java

@Configuration
@Import("xx.class")
public class Javaconfig {

    @Bean
    public User getUser(){
        return new User();
    }

}
```

### 代理模式

#### 静态代理

角色分析：

* 抽象角色：一般会使用接口或者抽象类来解决
* 真实角色：被代理的角色
* 代理角色：代理真实角色，代理了之后，我们会一般做一些附属的操作
* 客户：客户访问代理角色

中介 租户 房东 example

rent接口：

```java
package com.example.demo;

public interface Rent {

    public void rent();
}

```

Host类：

```java
public class Host implements Rent {

    @Override
    public void rent() {
        System.out.println("房东出租房屋");
    }
}
```

proxy类

```java
package com.example.demo;

public class Proxy implements Rent{

    private Host host;


    public Proxy(){

    }

    public Proxy(Host host){
        this.host = host;
    }


    public void seeHouse(){
        System.out.println("中介带顾客看房");
    }

    public void  contract(){
        System.out.println("房东和顾客签订合约");
    }

    @Override
    public void rent() {
        seeHouse();
        host.rent();
        contract();
    }
}
```

client

```java
public class Client {

    public static void main(String[] args) {
        Host no1 = new Host();
        Proxy proxy = new Proxy(no1);

        proxy.rent();
    }
}
```



代理模式的好处：

* 可以使得真实角色的操作更加纯粹 不用关心一些公共的业务
* 公共的业务交给代理角色 实现了业务的分工
* 公共的业务发生拓展的时候，方便进行集中的管理

缺点：

* 一个真实的角色就需要一个代理角色，代码量就会翻倍-开发效率会遍地



增强理解

假设我们有一个业务，我们给他设置了一个接口 接口中有两个方法add和delete  

```java
public interface UserService {
    public void add();
    public void delete();

}
```

然后我们使用实现类来实现这个接口

```java
public class UserServiceImple implements UserService{
    @Override
    public void add() {
        System.out.println("增加了");
    }

    @Override
    public void delete() {
        System.out.println("删除了");
    }
}
```

然后我们有一个用户 可以通过这个实现类来试用服务

```java
public class Client {
    public static void main(String[] args) {
        UserServiceImple userServiceImple = new UserServiceImple();
        userServiceImple.add();
    }

}
```

但是我们现在想修改一下我们的服务 希望在进行了服务之后  打印出日志 但是我们不希望修改原有的服务层的代码 这个时候我们使用一个代理类来实现面向切片的编程

我们在实现类的基础上  给出了一个新的代理类

```java
public class UserServiceProxy implements UserService{

    private UserServiceImple userServiceImple;

    public UserServiceProxy(UserServiceImple userServiceImple) {
        this.userServiceImple = userServiceImple;
    }

    @Override
    public void add() {
        this.userServiceImple.add();
        log("add");
    }

    @Override
    public void delete() {
        this.userServiceImple.delete();
        log("delete");
    }

    public void log(String msg){
        System.out.println(msg + "method used");
    }
}
```

有了这个代理类 就能在不改变原有代码的情况下  增加新的功能

```java
public class Client {
    public static void main(String[] args) {
        UserServiceImple userServiceImple = new UserServiceImple();
        UserServiceProxy userServiceProxy = new UserServiceProxy(userServiceImple);

        userServiceProxy.add();

        userServiceProxy.delete();
    }

}
```



#### 动态代理

动态代理和静态代理 代理的角色是一样的

只是动态代理是自动生成的  不是我们手动创建的

动态代理有两大类：

* 基于接口的动态代理：JDK动态代理
* 基于类的动态代理：cglib
* java字节码实现动态代理 javasist



我们使用动态代理的方法 实现host和proxy的例子

创建一个Rent接口 并且Host实现这个接口

```java
public interface Rent {
    public void rent();
}
```

```java
public class Host implements Rent{
    @Override
    public void rent() {
        System.out.println("房东出租了房子");
    }
}
```

我们现在用jdk中的动态代理的方式来代理实现这个接口的类

```java
public class ProxyInvocationHandler implements InvocationHandler {


    private Rent rent;

    public void setRent(Rent rent) {
        this.rent = rent;
    }


    public Object getProxy(){
        return Proxy.newProxyInstance(this.getClass().getClassLoader(),rent.getClass().getInterfaces(), this);

    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("中介看房子");
        Object result = method.invoke(rent,args);
        return result;
    }
}
```

然后在用户使用时 得到代理对象  在代理对象中调用rent()方法

```java
public class Client {
    public static void main(String[] args) {
        Host host = new Host();

        ProxyInvocationHandler pih = new ProxyInvocationHandler();//得到动态代理handler

        pih.setRent(host);

        Rent proxy = (Rent)pih.getProxy();//得到代理对象
        proxy.rent(); //调用代理的方法
    }
}
```



在这个例子中 我们只是固定的代理了rent()方法  我们再使用动态代理的方式 代理之前的UserService的例子

接口和实现类

```java
public interface UserService {
    public void add();
    public void delete();

}
```

```java
public class UserServiceImple implements UserService {
    @Override
    public void add() {
        System.out.println("增加了");
    }

    @Override
    public void delete() {
        System.out.println("删除了");
    }
}
```



invocationHandler

```java
public class ProxyInvocationHandler implements InvocationHandler {


    private Object target;

    public void setTarget(Object target) {
        this.target = target;
    }


    public Object getProxy(){
        return Proxy.newProxyInstance(this.getClass().getClassLoader(),target.getClass().getInterfaces(), this);

    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        log(method.getName());
        Object result = method.invoke(target,args);
        return result;
    }

    public void log(String msg){
        System.out.println(msg + " method used");
    }
```



client

```java
public class Client {
    public static void main(String[] args) {
        UserServiceImple userServiceImple = new UserServiceImple();

        ProxyInvocationHandler pih = new ProxyInvocationHandler();
        pih.setTarget(userServiceImple);

        UserService userService = (UserService)pih.getProxy();
        userService.add();
    }

}
```

这样我们在用proxy中使用方法，就能打印出不同方法的名称



### AOP

AOP是：面向切面编程，通过预，编程方式和运行期间动态代理，实现程序功能的统一维护，的一种技术。



AOP在spring中的作用：

提供声明式事务；云栖用户自定义切面

* 横切关注点：跨越应用程序多个模块的方法或者功能。
* 切面：
* 通知：
* 目标：
* 代理：
* 切入点：
* 连接点：



#### spring api实现

使用spring实现AOP需要导入一个包：

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

导入了这个包之后 就能够使用aop相关的一些东西了



我们给出一个例子 使用spring进行aop操作

我们先设计一个借口 因为动态代理代理的是接口

```java
public interface UserService {
    public void add();
    public void delete();
}
```

然后实现这个接口

```java
public class UserServiceImple implements UserService{
    @Override
    public void add() {
        System.out.println("进行了添加");
    }

    @Override
    public void delete() {
        System.out.println("进行了删除");
    }
}
```

然后使用spring aop接管他们

我们实现一个在代理方法运行之前执行的方法

```java
public class log implements MethodBeforeAdvice {

    @Override
    public void before(Method method, Object[] objects, Object o) throws Throwable {
        System.out.println(o.getClass().getName() + "method will be used");
    }
}
```

然后添加一个代理方法执行之后的方法

```java
public class AfterLog implements AfterReturningAdvice {
    @Override
    public void afterReturning(Object o, Method method, Object[] objects, Object o1) throws Throwable {
        System.out.println(method.getName() + " is used and return value is :" + o);
    }
}
```

然后在xml中进行配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/aop
       http://www.springframework.org/schema/aop/spring-aop.xsd">

    <bean id="service" class="com.example.demo.UserServiceImple"/>
    <bean id="log" class="com.example.demo.log"/>
    <bean id="afterlog" class="com.example.demo.AfterLog"/>

    <aop:config>
        <aop:pointcut id="pointcut1" expression="execution(* com.example.demo.UserServiceImple.*(..))" />
        <aop:advisor advice-ref="log" pointcut-ref="pointcut1"/>
        <aop:advisor advice-ref="afterlog" pointcut-ref="pointcut1"/>
    </aop:config>
</beans>
```

注意这个框架中新加入了aop的约束



然后测试我们的程序

```java
public class Mytest {
    @Test
    public void test(){
        ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");

        //这里要注意 动态代理代理的是接口 不是具体的类
        UserService userService = (UserService) context.getBean("service");
        userService.add();

        userService.delete();

    }
}
```

![image-20200522174434690](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200522174434690.png)



#### DIY类实现AOP：

还是上面的例子  只是我们不再是为每个方法前 方法后执行的都创建一个类 而是创建出一个独立的diy类

```java
package com.example.diy;

public class DiyLog {
    public void before(){
        System.out.println("before method");
    }

    public void after(){
        System.out.println("after method");
    }
}
```



然后在xml中配置切面

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/aop
       http://www.springframework.org/schema/aop/spring-aop.xsd">

    <bean id="service" class="com.example.demo.UserServiceImple"/>
    <bean id="log" class="com.example.demo.log"/>
    <bean id="afterlog" class="com.example.demo.AfterLog"/>

<!--    <aop:config>-->
<!--        <aop:pointcut id="pointcut1" expression="execution(* com.example.demo.UserServiceImple.*(..))" />-->
<!--        <aop:advisor advice-ref="log" pointcut-ref="pointcut1"/>-->
<!--        <aop:advisor advice-ref="afterlog" pointcut-ref="pointcut1"/>-->
<!--    </aop:config>-->

    <bean id="diy" class="com.example.diy.DiyLog"/>

    <aop:config>
        <aop:aspect ref="diy">
            <aop:pointcut id="pointcut" expression="execution(* com.example.demo.UserServiceImple.*(..))"/>
            <aop:before pointcut-ref="pointcut" method="before"/>
            <aop:after method="after" pointcut-ref="pointcut"/>

        </aop:aspect>
    </aop:config>
</beans>
```



之后的运行方式和之前相同

```java
public class Mytest {
    @Test
    public void test(){
        ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");

        //这里要注意 动态代理代理的是接口 不是具体的类
        UserService userService = (UserService) context.getBean("service");
        userService.add();

        userService.delete();

    }
}
```



#### 注解实现

我们新加入一个注解类

```java
@Aspect
public class annotation {

    @Before("execution(* com.example.demo.UserServiceImple.*(..))")
    public void before(){
        System.out.println("=======运行前=======");
    }

    @After("execution(* com.example.demo.UserServiceImple.*(..))")
    public void after(){
        System.out.println("=======运行后=======");
    }

    @Around("execution(* com.example.demo.UserServiceImple.*(..))")
    public void around(ProceedingJoinPoint jp) throws Throwable {
        System.out.println("=======环绕前=======");
        Object proceed = jp.proceed();
        Signature signature = jp.getSignature();
        System.out.println("Signature: " + signature);
        System.out.println("=======环绕后=======");
    }


}
```

然后将注解类加入到 xml中

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/aop
       http://www.springframework.org/schema/aop/spring-aop.xsd">

    <bean id="service" class="com.example.demo.UserServiceImple"/>
    <bean id="log" class="com.example.demo.log"/>
    <bean id="afterlog" class="com.example.demo.AfterLog"/>


    <bean id="annotation" class="com.example.annotation.annotation"/>
    <aop:aspectj-autoproxy/>
</beans>
```



### Mybatis-spring

将Mybatis导入到spring中 需要导入一些包

* junit
* mybatis
* mysql
* spring
* aop
* mybatis-spring

编写配置文件

测试



流程：

1. 编写实体类
2. 编写核心配置文件
3. 编写接口
4. 编写Mapper.xml
5. 测试







### 声明式事务

* 把一组业务当成一个业务来做，要么都成功，要么都失败
* 事务在项目开发中，十分的重要，涉及到数据的一致性问题，不能马虎
* 确保完整性和一致性



ACID原则：

* 原子性
* 一致性
* 隔离性
* 持久性



