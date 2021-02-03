### @Resource，@Autowired和@Service解析

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