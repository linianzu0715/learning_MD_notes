## Spring

[toc]

### Spring注解@Resource，@Autowired和@Service解析

今天在查看代码的时候遇到了一些疑问：

在Money_Processor的CommonOrderMsgListener中，出现了以下的两个对象：

```
@Autowired
private List<PlatformOrderProcessorAdapter> commonOrderProcessor;

@Resource
private List<TspVpOrderProcessorAdapter> tspVpOrderProcessorList;
```

这两个对象是两个存储有特定processor的两个容器。

他们的使用的场景是这样的：

```
for (TspVpOrderProcessorAdapter processor : tspVpOrderProcessorList) {
   processor.process(commonOrderMessageDTO);
}

for (PlatformOrderProcessorAdapter processor : commonOrderProcessor) {
   processor.process(commonOrderMessageDTO, MiniMoneyTradeUtil.tradeToPlatformId.get(commonOrderMessageDTO.getVp_type()), commonOrderMessageDTO.getVp_type());
}
```

会循环这两个容器中的processor，然后使用这些processor的process方法来处理消息体对象commonOrderMessageDTO



因此我就产生了一个疑问，这两个容器中是装载了哪些processor对象呢？

这两个对象/容器（commonOrderProcessor，tspVpOrderProcessorList）配置上了两种不同的注解，一个是@Resource，一个是@Autowired。



但是当我们查看@Autowired注解的commonOrderProcessor对象的时候。没有在xml文件中找到相对应的bean。而且我们发现其容器内对象的实现类中，用@Service注解进行了标记。

因此，我们来探究一下@Resource，@Autowired和@Service这三个注解。



我们来关注一下@Resource和@Autowired这两个注解的相同点和不同点。

共同点：

1、两者都可以写在字段和setter方法上。两者如果都写在字段上，那么就不需要再写setter方法。

不同点：

1、@Autowired为Spring提供的注解，需要导入包 org.springframework.beans.factory.annotation.Autowired。只按照byType注入。然后它有两种添加注解的方式。一种是直接在属性上面添加，一种是在属性上面的方法添加。

```
public class TestServiceImpl {
    // 下面两种@Autowired只要使用一种即可
    @Autowired
    private UserDao userDao; // 用于字段上
    
    @Autowired
    public void setUserDao(UserDao userDao) { // 用于属性的方法上
        this.userDao = userDao;
    }
}
```

2、@Autowired注解是按照类型（byType）装配依赖对象，默认情况下它要求依赖对象必须存在，如果允许null值，可以设置它的required属性为false。如果我们想使用按照名称（byName）来装配，可以结合@Qualifier注解一起使用。(通过类型匹配找到多个candidate,在没有@Qualifier、@Primary注解的情况下，会使用对象名作为最后的fallback匹配)如下：

```
public class TestServiceImpl {
    @Autowired
    @Qualifier("userDao")
    private UserDao userDao; 
}
```



3、@Resource默认按照ByName自动注入，由J2EE提供，需要导入包javax.annotation.Resource。@Resource有两个重要的属性：name和type，而Spring将@Resource注解的name属性解析为bean的名字，而type属性则解析为bean的类型。所以，如果使用name属性，则使用byName的自动注入策略，而使用type属性时则使用byType自动注入策略。如果既不制定name也不制定type属性，这时将通过反射机制使用byName自动注入策略。



所以说@Resource和@Autowired都是帮助我们的属性进行自动配置的。而@Service注解的功能是将一个类声明为一个bean。使得这个bean能够被自动装配上。



### tspVpOrderProcessorList

我们先来看@Resource注解的tspVpOrderProcessorList。我们通过全局查找找到了xml文件中的以下内容。

```
<bean id="tspVpOrderProcessorList" class="java.util.ArrayList">
        <constructor-arg>
            <list>
                <ref bean="tspVpOrderProcessor"/>
                <ref bean="tspAgentSaleMemberProcessor"/>
                <ref bean="tspMTGroupBuyECProcessor"/>
                <ref bean="tspBrandSelfMemberProcessor"/>
                <ref bean="tspRiderMallProcessor"/>
            </list>
        </constructor-arg>
    </bean>
```

这个bean存储了在这个容器中有哪些processor。



### commonOrderProcessor

但是我们没有在有关的xml文件中找到关于commonOrderProcessor的配置bean。这个是和使用@Resource注解的tspVpOrderProcessorList不相同的地方。经过查找资料了解到，@Resource和@Autowired都是用来进行自动装配的注解。并且@Autowired注解是默认通过类型来进行自动装配的。因此，我们现在看看commonOrderProcessor装配的类型：PlatformOrderProcessorAdapter：

```
public abstract class PlatformOrderProcessorAdapter {
}
```

我们看到PlatformOrderProcessorAdapter是一个抽象类，这个抽象类中声明了几个方法。我们找到PlatformOrderProcessorAdapter的实现类：

```
PlatformPartRefundProcessor
PlatformPayFinishProcessor
PlatformPayProcessor
PlatformRefundProcessor
```

这几个实现类中都使用了@Service注解。到此，我们就知道了为什么我们在其他地方找不到配置的原因了。



是因为这个类的抽象类的实现类都有@service这个注解 因此这个commonOrderProcessor对象在自动装配的时候 会把所有实现了这个抽象类的实现类的bean都装配进这个List里面去。