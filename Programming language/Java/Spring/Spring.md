## Spring

[toc]

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