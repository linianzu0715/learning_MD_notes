### Iterable 接口、迭代器 Iterator

所有的集合类（List，Set...）都实现自 Collection 接口，而 Collection 又是继承于 Iterable 接口，因此可以说所有的集合类（List，Set...）都实现了 Iterable 接口。

当某个类实现Iterable 接口的时候，我们就能称这个类是一个“可数”的类，也就是可以使用 `iterable()`方法来获取一个迭代器 Iterator，然后使用这个迭代器 Iterator 实例去遍历这个类，因此所有的 Collection 类都能够使用迭代器 Iterator来遍历。



Iterable 接口

```java
public interface Iterable<T> {
    //當某個類實現Iterable接口的話，就能獲取到迭代器iterator，然後就能使用這個iterator去遍歷此類
    //实现这个接口允许对象成为 "foreach" 语句的目标。
    Iterator<T> iterator(); // 返回一个在一组 T 类型的元素上进行迭代的迭代器。
}
```



Iterator 接口

如果某个类实现了 Iterator 接口，那么它也需要创建一个内部类去实现一个 Iterator 类，让调用 Iterator 接口中的 Iterator()时，能够获取一个 Iterator 实例。

```java
public interface Iterator<E> {
    //是否有下一個元素
    boolean hasNext();

    //取得下一個元素
    E next();

    //刪除最後一個獲取的元素，因此調用remove()前一定得先調用一次next()
    void remove();
}
```

至于Iterator 接口如何实现，就看各个集合实现如何去定义“下一个元素”，像是 Arraylist 的下一个元素就是 element[index+1]，而HashMap 的下一个元素则是 Hash table 数组中存储的下一个 entry。

另外可以想象 Iterator 像是一个游标一样，一开始停在最前面，然后不停的往后走（只能向后移动），且此游标每次都是停在元素和元素的中间，当调用 next 时，迭代器就越过下一个元素，并返回刚刚越过的那个元素的引用

![](https://kucw.github.io/images/blog/iterator_next.png)



使用迭代器 iterator 遍历 ArrayList

```java
public class Main {
    public static void main(String[] args) {
        //ArrayList實現了Collection接口，因此他也實現了Iterable接口，所以他可以使用iterator迭代器來遍歷
        List<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");

        //調用Iterable接口中的iterator()取得此ArrayList的迭代器實例
        Iterator<String> its = list.iterator();

        //使用Iterator接口的hasNext()、next()來遍歷此ArrayList集合實現類
        while (true) {
            if (its.hasNext()) {
                String s = its.next();
                System.out.println(s);
            } else {
                break;
            }
        }
    }
}
```

而再进一步说，当某个类能使用迭代器 Iterator 来遍历时，就能使用 java 提供的 foreach 愈发来遍历此类（foreach 语法实际上就是简化的 `Iterator()`)。

Foreach 实际上会被编译器编译成使用迭代器 `Iterator()`去遍历集合，因此能使用 foreach 的，都是得实现 Iterabel 接口的集合类 Collection，像是List，Set。

所以 Map 就沒有办法直接使用 foreach（因为 Map 沒有实现 Iterable 接口），只有他的 `map.entrySet()`、`map.keySet()`、`map.values()` 这种返回一个集合体的方法，才能使用 foreach。

```java
public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");

        //原代碼，使用語法糖的foreach
        for (String s : list) {
            System.out.println(s);
        }

        //實際上會被編譯成使用iterator去遍歷
        for (Iterator<String> its = list.iterator(); its.hasNext(); ) {
            String s = its.next();
            System.out.println(s);
        }
    }
}
```



为什么 Iterator 要额外使用内部类去实现，而不是 ArrayList 直接实现此接口 ?

如果看过 Collection 类的源码（以ArrayList为例），可以发现 ArrayList 并不是由 ArrayList 去实现 Iterator 接口，而是 ArrayList 有一个内部类 Itr，专门去实现 Iterator 接口，而 ArrayList 的 `iterator()` 方法，只是去创建一个内部类 ArrayList.Itr 的实例而已。

```java
//ArrayList不實現Iterator接口，反而是由他的內部類進行實現
public class ArrayList<E> extends AbstractList<E> {
    //調用list.iterator()可以取得此list的迭代器
    public Iterator<E> iterator() {
        return new Itr(); //實際上就是去創建一個內部類的實例
    }

    //ArrayList中的內部類Itr，專門實現Iterator接口
    private class Itr implements Iterator<E> {
        int cursor; //記錄當前迭代到哪裡

        public boolean hasNext() { ... }
        public E next() { ... }
        public void remove() { ... }
    }
}
```

要这样设计是因为一个集合类可能同时有多个迭代器去遍历他，而每个迭代器遍历到集合的哪里，是每个迭代器自己的事情，彼此不互相干涉，因此才需要額外使用一个内部类去实现迭代器的 Iterator 接口。

- 如此当需要用到 Iterator 來遍历集合时，只需要调用 `list.iterator()`，就能取得一个全新的、不受別人影响的迭代器供自己使用，而迭代器彼此之間也不会互相干涉。
- 至于為为什么要特別使用内部类來实现 Iterator 接口，而不是创建一个 Iterator 公共类來供所有集合一起使用，是因为迭代器需要知道集合的内部结构，他才能知道要怎么去实现 `hasNext()`、`next()`、`remove()` 方法，而使用内部类才能无条件的取用外部类的所有信息（包含 private 的变量和方法），因此才需要將 Iterator 提取成接口，让每个集合自己使用内部类去实现 Iterator 接口。

为什么 Iterator 接口，只有 `hasNext()`、`next()`、`remove()` 方法，而沒有 `add(E)` 方法 ?

逻辑上來說，迭代器是一个一个去遍历集合中的元素，而当前 iterator 停下的地方，就是迭代到一半的地方

- 如果当迭代到一半时调用 `iterator.add()` 方法，理论上來說，应是要在当前这个元素 E1 后面新增一個元素 E2，使得下次遍历此集合时，E2 一定会出现在 E1 後面，也就是 [….E1, E2, ….]
- 假设 `add()` 方法是以这个语意为前提的話，那么迭代器不提供此方法是很合理的，对于有序的集合（像是ArrayList）來說，在此元素后面新增一个元素是一个很简单的事情，但是对于无序的集合（像是HashSet）來说，不能保证新插入的插入元素 E2 一定會在 E1 後面（因为还得计算 HashCode），如此就违反了 `add()` 的语意了，这也就是为什么 Iterator 接口不提供 `add()` 方法。

- 另一个说法是，在使用迭代器時，通常就是 “遍历” 的场景，这种场景下很少会去使用 `add()` 方法，因此 Iterator 接口沒必要提供这个方法。



















