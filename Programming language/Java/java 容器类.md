## java 容器类

[toc]

### 数组

#### 创建数组Array的三种方式

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
        // 第一种 先声明数组的容量 然后设置里面的内容
        int[] test1 = new int[5];
        for(int i = 0; i < 5; i++){
            test1[i] = i;
            System.out.println(test1[i]);
        }
    }

    private static void Test2(){
        // 第二种 直接根据
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



#### 数组Array的底层实现

数组对于每一门编程语言来说都是重要的数据结构之一。Java 语言中提供的数组是用来存储固定大小的同类型元素。带有一个属性length。



### Collection接口继承架构

Collection接口：

* List接口: Arraylist, LInkedList, Vector
* Set接口: HashSet, TreeSet, LinkedHashSet





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



### Map接口

#### HashMap

##### HashMap底层实现原理

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



##### Hashmap解决hash冲突的方法：

1. 开放定址法
2. 再哈希法
3. 链地址法
4. 建立公共溢出区



#### ConcurrentHashMap

ConcurrentHashMap包含两个静态内部类 HashEntry和Segment。HashEntry用来封装映射表的键值对，Segment用来充当锁的角色，每个segment对象守护整个haxi映射表的若干个桶。每个桶是有若干个HashEntry对象连接起来的链表。



#### HashMap和HashTable的区别

HashMap和HashTable都实现了Map接口。

HashMap允许键和值是null，HashTable不允许。

HashTable是同步的，HashMap不是。因此HashMap适合于单线程环境，HashTable适合于多线程环境。

HashMap提供了可应用迭代的键的集合，因此HashMap是快速失败的。



#### Map实现类

java为数据结构中的映射定义了一个接口java.util.Map。它有四个实现类,分别是HashMap、Hashtable、LinkedHashMap 和TreeMap。

Map接口：主要用于存储健值对，根据键得到值，因此不允许键重复(重复了覆盖了),但允许值重复。

HashMap ：它根据键的 HashCode 值存储数据，具有很快的访问速度，遍历时，取得数据的顺序是完全随机的。

Hashtable ：将HashMap内部方法大多使用synchronized的关键字修饰得到的，没有做并发相关的优化，目前主要使用concurrentHashMap替代。

LinkedHashMap 是 HashMap的一个子类，保存了记录的插入顺序，再使用Iterator遍历时，先得到的数据肯定是先插入的，也可以在构造时用带参数，按照应用次数排序。遍历时会比HashMap慢，但当HashMap容量很大，实际数据很少时，遍历起来可能会必LinkedHashMap慢，因为LinkedHashMap的遍历只和实际数据有关，和容量无关。

TreeMap 实现SortMap接口，能够把它保存的记录根据键排序，默认键值是升序排序的，也可以指定排序的比较器，当遍历时，得到的记录是排序的。



### Queue

#### PriorityQueue

PriorityQueue 一个基于优先级的无界优先级队列。优先级队列的元素按照其自然顺序进行排序，或者根据构造队列时提供的 Comparator 进行排序，具体取决于所使用的构造方法。该队列不允许使用 null 元素也不允许插入不可比较的对象(没有实现Comparable接口的对象)。PriorityQueue 队列的头指排序规则最小那个元素。如果多个元素都是最小值则随机选一个。PriorityQueue 是一个无界队列，但是初始的容量(实际是一个Object[])，随着不断向优先级队列添加元素，其容量会自动扩容，无需指定容量增加策略的细节。

```
继承结构：
							  -> Serializeble
							 |
PriorityQueue -										 -------> Queue --------
			         |									|												｜
			          -> AbstractQueue -                         -> Collection ->Iterable
			                            |												｜
			                             -> AbstractCollection -
```





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