### Python 中 Is None 和 == None 的区别

我们知道对象中有__eq__函数，用于判断两个对象的值是否相等；但是__eq__函数是可以被我们自己定义的。比如我们让__eq__函数用于返回Ture。

但是is判断的是两个对象的id是否相等，即判断a对象是否是b对象。

python中数值类型（int,float），str字符串，tuple都是不可变类型。

python中None是一个特殊的常量，“不同的”None的id是一样的。

```python
a = None
b = None
print(a is b)
>> True
```

所以当判断数据结构中的某一直是否为None时，is会更好一些。

（is函数比==要快一些，不用运行查找和比较函数）



### 声明一个特定长度的数组：

```python
DP = [ 0 for i in range(length)]
```



### 字符串使用+=操作：

```
test = "1"
test += "0"
print(test)
>>10
```

会加在后面

