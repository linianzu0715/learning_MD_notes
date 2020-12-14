[toc]





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



### Nonlocal关键词

nonlocal 关键字用于在嵌套函数内部使用变量，其中变量不应属于内部函数。请使用关键字 nonlocal 声明变量不是本地变量。

```python
def myfunc1():
  x = "Bill"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())
# hello
```



### Collections

#### deque

deque是双端队列（double-ended queue）的缩写，由于两端都能编辑，deque既可以用来实现栈（stack）也可以用来实现队列（queue）。

![img](https://upload-images.jianshu.io/upload_images/140304-df9c6c6b39685f19.png)

相比于list实现的队列，deque实现拥有更低的时间和空间复杂度。list实现在出队（pop）和插入（insert）时的空间复杂度大约为O(n)，deque在出队（pop）和入队（append）时的时间复杂度是O(1)。



### range和xrange的区别:

range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个序列。

 xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。

要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间。