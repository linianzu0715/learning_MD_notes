### 什么是JsonPath？

JSONPath对于 JSON 来说相当于 XPATH 对于 XML。是一个简单的从JSON文档中抽取指定信息的工具，有一套自己的语法，类似于正则表达式，提供多种语言实现版本，包括：Javascript, Java, Python 和 PHP。



### JsonPath语法：

| JSONPath            | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| $                   | 根对象，例如$.name                                           |
| @                   | 当前对象，例如@.name                                         |
| .                   | 属性访问，例如$.name                                         |
| ..                  | 深度扫描属性访问，所有名字匹配的属性，例如$..name            |
| *                   | 对象的所有属性，例如$.leader.*                               |
| ['key']             | 属性访问。例如$['name']                                      |
| ['key0','key1']     | 多个属性访问。例如$['id','name']                             |
| [num]               | 数组访问，其中num是数字，可以是负数。例如$[0].leader.departments[-1].name |
| [num0,num1,num2...] | 数组多个元素访问，其中num是数字，可以是负数，返回数组中的多个元素。例如$[0,3,-2,5] |
| [start:end]         | 数组范围访问，其中start和end是开始小表和结束下标，可以是负数，返回数组中的多个元素。例如$[0:5] |
| [start:end :step]   | 数组范围访问，其中start和end是开始小表和结束下标，可以是负数；step是步长，返回数组中的多个元素。例如$[0:5:2] |
| [?(key)]            | 对象属性非空过滤，例如$.departs[?(name)]                     |





### JsonPath使用；

JsonPath.read( jsonstr, path );

入参：一个是json串 ，另一个是检索路径

返回值：通常read后的返回值可以自动转型到指定的类型。



### JsonPath使用举例：

#### **1、解析出cardExtension里面的内容，并以json类型格式返回**

path:$.data.cardExtension



#### **2、解析出cardExtension中offerAbstracts下moreTitle字段的值**

path:$.data.cardExtension.offerAbstracts.moreTitle



#### **3、解析出cardExtension中offerAbstracts下offerInfos下所有price的值**

path: $.data.cardExtension.offerAbstracts.offerInfos[*].price



#### 4、**解析出cardExtension中offerAbstracts下offerInfos下所有trace下keyword的值**

path: data.cardExtension.offerAbstracts.offerInfos[*].trace.keyword



#### 5、**解析出cardExtension中offerAbstracts下offerInfos下第一个trace下keyword的值**

path: data.cardExtension.offerAbstracts.offerInfos[0].trace.keyword