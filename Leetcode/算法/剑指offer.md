[toc]





##### [面试题03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

```python
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        check = [None] * length

        for item in nums:
            if check[item] == None:
                check[item] = item
            else:
                return item
        return 0
```

这样就不需要每次都在新的集合中搜索 而是直接通过索引  



##### [面试题04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

**减而治之**

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])
        if cols == 0:
            return False

        # 从右上角开始查找
        x = 0
        y = cols - 1
        while x < rows and y >= 0:
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                y -= 1
            else:
                x += 1
        return False
```



##### [面试题05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        length = len(s)
        str_temp=''
        for i in range(length):
            if s[i]==' ':
                str_temp = str_temp + '%20'
            else:
                str_temp = str_temp + s[i]
        return str_temp
```



##### [面试题06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

**示例 1：**

```
输入：head = [1,3,2]
输出：[2,3,1]
```

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        temp=[]
        while head:
            temp.append(head.val)
            head=head.next
        return temp[::-1]
```





##### [面试题07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

   3

   / \
  9  20
    /  \
   15   7



```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])
        return root

```

同 算法 105



##### [面试题09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )



维护两个栈，第一个栈存储元素，第二个栈用于辅助操作。

根据栈的特性，第一个栈的底部元素是最后插入的元素，第一个栈的顶部元素是下一个被删除的元素。为了维护队列的特性，每次插入的元素应该在第一个栈的底部。因此每次插入元素时，若第一个栈内已经有元素，应将已有的全部元素依次弹出并压入第二个栈，然后将新元素压入第一个栈，最后将第二个栈内的全部元素依次弹出并压入第一个栈。经过上述操作，新插入的元素在第一个栈的底部，第一个栈内的其余元素的顺序和插入元素之前保持一致。

删除元素时，若第一个栈非空，则直接从第一个栈内弹出一个元素并返回，若第一个栈为空，则返回 -1。

另外维护队列的元素个数，用于判断队列是否为空。初始元素个数为 0。每次插入元素，元素个数加 1。每次删除元素，元素个数减 1。

```python
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # 1 -> 2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # add value
        self.stack1.append(value)
        # 1 <- 2
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

    def deleteHead(self) -> int:
        if not self.stack1: return -1
        return self.stack1.pop()

```



##### [面试题10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**

```
输入：n = 2
输出：1
```

**示例 2：**

```
输入：n = 5
输出：5
```



```python
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
```



##### [面试题10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21

```python
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]%1000000007
```

同 算法 70



##### [面试题11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

```python
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]
```

要注意的是  数组中是否允许有重复数字 有和没有重复数字是两道不同的题目

类似于算法 153 154



##### [面试题12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        if row == 0:
            return False
        column = len(board[0])
        if column == 0:
            return False
        visited = [[False for i in range(column)] for j in range(row)]
        for i in range(row):
            for j in range(column):
                if self.dfs(word,board,i,j,row,column,visited):
                    return True
        
        return False
    
    def dfs(self, word, board, i, j, row, column, visited):
        if word == "":
            return True
        
        if i < 0 or i >= row or j < 0 or j >= column:
            return False
        
        if board[i][j] == word[0] and not visited[i][j]:
            visited[i][j] = True
            if self.dfs(word[1:],board,i-1,j,row,column,visited) or self.dfs(word[1:],board,i+1,j,row,column,visited) or self.dfs(word[1:],board,i,j-1,row,column,visited) or self.dfs(word[1:],board,i,j+1,row,column,visited):
                return True
            visited[i][j] = False
        return False
```

同 算法79



##### [面试题13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

我们将行坐标和列坐标数位之和大于 k 的格子看作障碍物，那么这道题就是一道很传统的搜索题目，我们可以使用广度优先搜索或者深度优先搜索来解决它，本文选择使用广度优先搜索的方法来讲解。

那么如何计算一个数的数位之和呢？我们只需要对数 x 每次对 10 取余，就能知道数 x 的个位数是多少，然后再将 x 除 10，这个操作等价于将 x 的十进制数向右移一位，删除个位数（类似于二进制中的 >> 右移运算符），不断重复直到 x 为 0 时结束。

同时这道题还有一个隐藏的优化：我们在搜索的过程中搜索方向可以缩减为向右和向下，而不必再向上和向左进行搜索。如下图，我们展示了 16 * 16 的地图随着限制条件 k 的放大，可行方格的变化趋势，每个格子里的值为行坐标和列坐标的数位之和，蓝色方格代表非障碍方格，即其值小于等于当前的限制条件 k。我们可以发现随着限制条件 k 的增大，(0, 0) 所在的蓝色方格区域内新加入的非障碍方格都可以由上方或左方的格子移动一步得到。而其他不连通的蓝色方格区域会随着 k 的增大而连通，且连通的时候也是由上方或左方的格子移动一步得到，因此我们可以将我们的搜索方向缩减为向右或向下。

DFS：

```python
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)
```



##### [面试题14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

**推论一：** 将绳子 **以相等的长度等分为多段** ，得到的乘积最大。

**推论二：** 尽可能将绳子以长度 33 等分为多段时，乘积最大。

最优： 3 。把绳子尽可能切为多个长度为 3 的片段，留下的最后一段绳子的长度可能为 0,1,2 三种情况。
次优： 2 。若最后一段绳子长度为 2 ；则保留，不再拆为 1+1。
最差： 1 。若最后一段绳子长度为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为 2 * 2 >3 * 1。

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

```



##### [面试题14- II. 剪绳子 II](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/)

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



此题与 面试题14- I. 剪绳子主体等价，唯一不同在于本题目涉及 **“大数越界情况下的求余问题”** 。

快速幂求余：

根据求余运算性质可推出：

![image-20200525204841931](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200525204841931.png)

当 a*a* 为奇数时 a/2*a*/2 不是整数，因此分为以下两种情况（ ''////'' 代表向下取整的除法）：

![image-20200525204902554](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200525204902554.png)

解析： 利用以上公式，可通过循环操作每次把指数 a 问题降低至指数 a//2 问题，只需循环 log_2(N) 次，因此可将复杂度降低至对数级别。封装方法代码如下所示。

```python
# 求 (x^a) % p —— 快速幂求余
def remainder(x, a, p):
    rem = 1
    while a > 0:
        if a % 2: rem = (rem * x) % p
        x = x ** 2 % p
        a //= 2
    return rem

```



```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0: return (rem * 3) % p # = 3^(a+1) % p
        if b == 1: return (rem * 4) % p # = 3^a * 4 % p
        return (rem * 6) % p # = 3^(a+1) * 2  % p

```



##### [面试题15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
```





##### [面试题16. 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1
        temp = x
        while n != 0:
            if n % 2 == 1:
                ans = ans * temp
            temp = temp * temp
            n = n // 2
        return ans
```



##### [面试题17. 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

这道题目看似很简单 只要依次递增然后输出就行  但是要考虑大数问题 就是数字的范围可能超过long（java）的范围 因此我们要考虑怎样解决大数计算

* 由于存在大数问题，结果不能放入int数组中，故这里采用剑指offer原题的直接打印输出的模式。
* increment函数，若发生进位则一直进行for循环，直到不产生进位则break。如果i为0（即到了最高位）还发生了进位，则设置isOverflow为true，并返回至主函数的while判断。

因此我们不使用数字类型进行计算 而使用无限长度的字符串

这个是处理思想的代码  但是不适用于本题解答

```java
public class solution {
    public void printNumbers(int n) {
        StringBuilder str = new StringBuilder();
        // 将str初始化为n个'0'字符组成的字符串
        for (int i = 0; i < n; i++) {
            str.append('0');
        }
        while(!increment(str)){
            // 去掉左侧的0
            int index = 0;
            while (index < str.length() && str.charAt(index) == '0'){
                index++;
            }
            System.out.println(str.toString().substring(index));
        }
    }

    public boolean increment(StringBuilder str) {
        boolean isOverflow = false;
        for (int i = str.length() - 1; i >= 0; i--) {
            char s = (char)(str.charAt(i) + 1);
            // 如果s大于'9'则发生进位
            if (s > '9') {
                str.replace(i, i + 1, "0");
                if (i == 0) {
                    isOverflow = true;
                }
            }
            // 没发生进位则跳出for循环
            else {
                str.replace(i, i + 1, String.valueOf(s));
                break;
            }
        }
        return isOverflow;
    }
}

```



##### [面试题18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.



双指针

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head
```

##### [面试题19. 正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。



状态
很容易想到，dp[i][j] 表示的状态是 s 的前 i 项和 p 的前 j 项是否匹配。

转移方程
现在如果已知了 dp[i-1][j-1] 的状态，我们该如何确定 dp[i][j] 的状态呢？我们可以分三种情况讨论，其中，前两种情况考虑了所有能匹配的情况，剩下的就是不能匹配的情况了：

s[i] == p[j] or p[j] == '.'：比如 abb 和 abb，或者 abb 和 ab. ，很容易得到 dp[i][j] = dp[i-1][j-1] = True。因为 ab 和 ab 是匹配的，如果后面分别加一个 b，或者 s 加一个 b 而 p 加一个 . ，仍然是匹配的。

p[j] == '*'：当 p[j] 为星号时，由于星号与前面的字符相关，因此我们比较星号前面的字符 p[j-1] 和 s[i] 的关系。根据星号前面的字符与 s[i] 是否相等，又可分为以下两种情况：

p[j-1] != s[i]：如果星号前一个字符匹配不上，星号匹配了 0 次，应忽略这两个字符，看 p[j-2] 和 s[i] 是否匹配。 这时 dp[i][j] = dp[i][j-2]。

p[j-1] == s[i] or p[j-1] == '.':星号前面的字符可以与 s[i] 匹配，这种情况下，星号可能匹配了前面的字符的 0 个，也可能匹配了前面字符的多个，当匹配 0 个时，如 ab 和 abb*，或者 ab 和 ab.* ，这时我们需要去掉 p 中的 b* 或 .* 后进行比较，即 dp[i][j] = dp[i][j-2]；当匹配多个时，如 abbb 和 ab*，或者 abbb 和 a.*，我们需要将 s[i] 前面的与 p 重新比较，即 dp[i][j] = dp[i-1][j]

其他情况：以上两种情况把能匹配的都考虑全面了，所以其他情况为不匹配，即 dp[i][j] = False

![image-20200526112241227](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200526112241227.png)



```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1,m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':       # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:                       # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2] 
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]

```



##### [面试题20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。



```python
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:return False

        transTable = [
            [1,2,7,-1,-1,0],
            [-1,2,7,-1,-1,-1],
            [-1,2,3,4,-1,9],
            [-1,3,-1,4,-1,9],
            [6,5,-1,-1,-1,-1],
            [-1,5,-1,-1,-1,9],
            [-1,5,-1,-1,-1,-1],
            [-1,8,-1,-1,-1,-1],
            [-1,8,-1,4,-1,9],
            [-1,-1,-1,-1,-1,9]
        ]

        cols = {
            "sign":0,
            "number":1,
            ".":2,
            "exp":3,
            "other":4,
            "blank":5  
        }

        def get_col(c):
            if c.isdigit():return 'number'
            elif c in {'+','-'}:return 'sign'
            elif c == '.':return '.'
            elif c in {'E','e'}:return 'exp'
            elif c == ' ':return 'blank'
            else:return 'other'

        legal_state = {2,3,5,8,9}
        state = 0
        for c in s:
            state = transTable[state][cols[get_col(c)]]
            if state == -1:return False
        return True if state in legal_state else False

```



分清楚几个判断条件:

* 空格只能出现在首尾，出现在中间一定是非法的
* 正负号只能出现在两个地方，第一个地方是整数的最前面，表示符号。第二个位置是 e 后面，表示指数的正负。如果出现在其它位置也一定是非法的
* 数字，数字没有进行特别的判断，题目没有前导0的问题
* e 只能出现一次，并且 e 之后一定要有数字才是合法的， 12e 这种也是非法的
* 小数点，由于 e 之后的指数一定是整数，所以小数点最多只能出现一次，并且一定要在 e 之前。所以如果之前出现过小数点或者是 e,再次出现小数点就是非法的

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)
        # 用四个标记记录 e 和小数点以及数字和 e 之后的数字有没有出现过
        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False

        for i in range(n):
            c = s[i]
            # 如果是数字，则将数字和 e 后出现的数字都标记为 true
            # 没有 e 的浮点数也认为 e 之后出现过数字
            if c in numbers:
                num_show_up = True
                num_after_e = True
            # 如果是正负号， 只有出现在首位或是 e 后面才合法
            elif c in ('+', '-'):
                if i > 0 and s[i-1] != 'e':
                    return False
            # 如果是小数点，那么必须保证 e 和小数点都没有出现过
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            # 如果是 e, 要保证已经有数字出现，并且 e 没有出现过
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            # 其他情况都为非法
            else:
                return False
        return num_show_up and num_after_e
```





##### [面试题21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。



考虑定义双指针 ii , jj 分列数组左右两端，循环执行：

指针 i 从左向右寻找偶数；
指针 j 从右向左寻找奇数；
将 偶数 nums[i]和 奇数 nums[j]交换。
可始终保证： 指针 i 左边都是奇数，指针 j 右边都是偶数 。

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

```



##### [面试题22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

```



##### [面试题24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL



```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curt = None
        while head != None:
            #temp记录下一个节点，head是当前节点
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt
```



##### [面试题25. 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4



```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
```



##### [面试题26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

         3
        / \
      4   5
      / \
     1   2



给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true



```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

```



##### [面试题27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

         4
      /   \
      2     7
     / \   / \
    1   3 6   9

镜像输出：

         4
      /   \
      7     2
     / \   / \
    9   6 3   1

  ```python
class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        self.dfs(root)
        return root
        
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): self.dfs(left)
        if (right!=None): self.dfs(right)
  ```



##### [面试题28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
      2   2
     / \ / \
    3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

        1
       / \
      2   2
       \   \
       3    3

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.isSymmetric_helper(root, root)
    
    def isSymmetric_helper(self, l, r):
        if l == None and r == None:
            return True
        if l != None and r == None:
            return False
        if l == None and r != None:
            return False
        if l.val != r.val:
            return False
        
        return self.isSymmetric_helper(l.left, r.right) and self.isSymmetric_helper(l.right, r.left)
```



##### [面试题29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]



```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        up = 0
        left = 0
        right = len(matrix[0])-1
        down = len(matrix) -1
        
        result = []
        direct = 0 #0 向右  1 向下 2 向左  3 向上
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    result.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    result.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1,-1):
                    result.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    result.append(matrix[i][left])
                left += 1
            if left > right or down < up:
                return result
            direct = (direct+1) % 4
```



##### [面试题30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.



```python
class MinStack(object):


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []


    def push(self, number):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        else:
            self.minStack.append(min(number, self.minStack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        ret = self.stack[-1]
        del(self.stack[-1], self.minStack[-1])
        return ret

    def top(self):
        """
        :rtype: int
        """
        ret = self.stack[-1]
        return ret
        

    def min(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
```



##### [面试题31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

**示例 2：**

```
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```





考虑借用一个辅助栈 stack*s**t**a**c**k* ，**模拟** 压入 / 弹出操作的排列。根据是否模拟成功，即可得到结果。

入栈操作： 按照压栈序列的顺序执行。
出栈操作： 每次入栈后，循环判断 “栈顶元素 == 弹出序列的当前元素” 是否成立，将符合弹出序列顺序的栈顶元素全部弹出。

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

```



##### [面试题32 - I. 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

返回：

[3,9,20,15,7]



层次遍历

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res
```



##### [面试题32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3

   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res

```



##### [面试题32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res

```



##### [面试题33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

         5
        / \
       2   6
      / \
     1   3

示例 1：

输入: [1,6,3,2,5]
输出: false



```
输入: [1,3,2,6,5]
输出: true
```

二叉树遍历结果的最后一个是根节点 第一个比根节点大的节点的左边为左枝 右边为右树枝 

使用递归的方法 一层一层查询

```python
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
```



##### [面试题34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

```



##### [面试题35. 复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

请实现 `copyRandomList` 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 `next` 指针指向下一个节点，还有一个 `random` 指针指向链表中的任意节点或者 `null`。

```python
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        Dict = {}
        newHead = Node(head.val)
        old = head
        new = newHead
        Dict[old] = new
        
        while old != None:
            new.random = old.random
            if old.next != None:
                new.next = Node(old.next.val)
                Dict[old.next] = new.next
            else:
                new.next = None
            old = old.next
            new = new.next
        
        RandomLoop = newHead
        while RandomLoop != None:
            if RandomLoop.random != None:
                RandomLoop.random = Dict[RandomLoop.random]
            RandomLoop = RandomLoop.next
        return newHead
```



##### [面试题36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：

![img](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

![img](/Users/linianzu/Documents/Learning/md/大数据开发/pic/bstdllreturndll.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
```



##### [面试题37. 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

请实现两个函数，分别用来序列化和反序列化二叉树。

你可以将以下二叉树：

        1
       / \
      2   3
         / \
        4   5

序列化为 "[1,2,3,null,null,4,5]"

```python
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
```



##### [面试题38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```



```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res
```



##### [面试题39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

```
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
```



```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

```



##### [面试题40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

输入整数数组 `arr` ，找出其中最小的 `k` 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

```



```python
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def get_num(s, bit, ind):
            """
            :param s -> str: s是当前生成的字符串
            :param bit -> int: bit是当前已经生成的位数
            :param ind -> int: ind是第一个非零位的下标
            """
            if bit == n:
                # 排除0
                if s[ind:] != '': 
                    res.append(int(s[ind:]))
                return 
            for i in range(10):
                if ind == bit and i != 0 or ind < bit:
                    get_num(s + str(i), bit + 1, ind)
                else:
                    get_num(s + str(i), bit + 1, ind + 1)
        get_num('', 0, 0)
        return res

    def printNumbers_2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i for i in range(1, 10 ** n)]

```



##### [面试题18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.



双指针

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head
```

##### [面试题19. 正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。



状态
很容易想到，dp[i][j] 表示的状态是 s 的前 i 项和 p 的前 j 项是否匹配。

转移方程
现在如果已知了 dp[i-1][j-1] 的状态，我们该如何确定 dp[i][j] 的状态呢？我们可以分三种情况讨论，其中，前两种情况考虑了所有能匹配的情况，剩下的就是不能匹配的情况了：

s[i] == p[j] or p[j] == '.'：比如 abb 和 abb，或者 abb 和 ab. ，很容易得到 dp[i][j] = dp[i-1][j-1] = True。因为 ab 和 ab 是匹配的，如果后面分别加一个 b，或者 s 加一个 b 而 p 加一个 . ，仍然是匹配的。

p[j] == '*'：当 p[j] 为星号时，由于星号与前面的字符相关，因此我们比较星号前面的字符 p[j-1] 和 s[i] 的关系。根据星号前面的字符与 s[i] 是否相等，又可分为以下两种情况：

p[j-1] != s[i]：如果星号前一个字符匹配不上，星号匹配了 0 次，应忽略这两个字符，看 p[j-2] 和 s[i] 是否匹配。 这时 dp[i][j] = dp[i][j-2]。

p[j-1] == s[i] or p[j-1] == '.':星号前面的字符可以与 s[i] 匹配，这种情况下，星号可能匹配了前面的字符的 0 个，也可能匹配了前面字符的多个，当匹配 0 个时，如 ab 和 abb*，或者 ab 和 ab.* ，这时我们需要去掉 p 中的 b* 或 .* 后进行比较，即 dp[i][j] = dp[i][j-2]；当匹配多个时，如 abbb 和 ab*，或者 abbb 和 a.*，我们需要将 s[i] 前面的与 p 重新比较，即 dp[i][j] = dp[i-1][j]

其他情况：以上两种情况把能匹配的都考虑全面了，所以其他情况为不匹配，即 dp[i][j] = False

![image-20200526112241227](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200526112241227.png)



```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1,m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':       # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:                       # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2] 
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]

```



##### [面试题20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。


```python
class Solution:
    def __init__(self):
        self.p = 0
    
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s == '': return False
        number = self.scanInterger(s)
        
        if self.p > len(s)-1:
            return number

        if self.p < len(s) and s[self.p] == '.':
            self.p += 1
            if self.p > len(s)-1:
                return number
            number = self.scanUnsignedInterger(s) or number

        if self.p < len(s) and s[self.p] in ['e','E']:
            self.p += 1
            if self.p > len(s)-1:
                return False
            number=  number and self.scanInterger(s)

        if self.p < len(s):
            return False

        return number

    def scanInterger(self,s):
        if s[self.p] in ['+','-']:
            self.p += 1
        return self.scanUnsignedInterger(s)

    def scanUnsignedInterger(self,s):
        pre = self.p
        while(self.p < len(s) and s[self.p]>='0' and s[self.p]<='9'):
            self.p += 1
        return self.p > pre

```



有限向量机

确定有限自动机：根据每一位字符进行状态转移即可，方框表示合法的结束状态。图中未标出的状态9表示字符串末尾的空格。

![IMG_3732.jpg](/Users/linianzu/Documents/Learning/md/大数据开发/pic/21bb5c376b6f9d17f85a2cb5149cf663e15581a3cc4e7092d994bd8df5c0bd92-IMG_3732.jpg)

![IMG_3733.jpg](/Users/linianzu/Documents/Learning/md/大数据开发/pic/b2f30ff15f23955ba82c297a892eab2a4fa53ba2bb9760fca83bb8b85fd3d41b-IMG_3733.jpg)



```python
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:return False

        transTable = [
            [1,2,7,-1,-1,0],
            [-1,2,7,-1,-1,-1],
            [-1,2,3,4,-1,9],
            [-1,3,-1,4,-1,9],
            [6,5,-1,-1,-1,-1],
            [-1,5,-1,-1,-1,9],
            [-1,5,-1,-1,-1,-1],
            [-1,8,-1,-1,-1,-1],
            [-1,8,-1,4,-1,9],
            [-1,-1,-1,-1,-1,9]
        ]

        cols = {
            "sign":0,
            "number":1,
            ".":2,
            "exp":3,
            "other":4,
            "blank":5  
        }

        def get_col(c):
            if c.isdigit():return 'number'
            elif c in {'+','-'}:return 'sign'
            elif c == '.':return '.'
            elif c in {'E','e'}:return 'exp'
            elif c == ' ':return 'blank'
            else:return 'other'

        legal_state = {2,3,5,8,9}
        state = 0
        for c in s:
            state = transTable[state][cols[get_col(c)]]
            if state == -1:return False
        return True if state in legal_state else False

```



分清楚几个判断条件:

* 空格只能出现在首尾，出现在中间一定是非法的
* 正负号只能出现在两个地方，第一个地方是整数的最前面，表示符号。第二个位置是 e 后面，表示指数的正负。如果出现在其它位置也一定是非法的
* 数字，数字没有进行特别的判断，题目没有前导0的问题
* e 只能出现一次，并且 e 之后一定要有数字才是合法的， 12e 这种也是非法的
* 小数点，由于 e 之后的指数一定是整数，所以小数点最多只能出现一次，并且一定要在 e 之前。所以如果之前出现过小数点或者是 e,再次出现小数点就是非法的

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)
        # 用四个标记记录 e 和小数点以及数字和 e 之后的数字有没有出现过
        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False

        for i in range(n):
            c = s[i]
            # 如果是数字，则将数字和 e 后出现的数字都标记为 true
            # 没有 e 的浮点数也认为 e 之后出现过数字
            if c in numbers:
                num_show_up = True
                num_after_e = True
            # 如果是正负号， 只有出现在首位或是 e 后面才合法
            elif c in ('+', '-'):
                if i > 0 and s[i-1] != 'e':
                    return False
            # 如果是小数点，那么必须保证 e 和小数点都没有出现过
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            # 如果是 e, 要保证已经有数字出现，并且 e 没有出现过
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            # 其他情况都为非法
            else:
                return False
        return num_show_up and num_after_e
```





##### [面试题21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。



考虑定义双指针 ii , jj 分列数组左右两端，循环执行：

指针 i 从左向右寻找偶数；
指针 j 从右向左寻找奇数；
将 偶数 nums[i]和 奇数 nums[j]交换。
可始终保证： 指针 i 左边都是奇数，指针 j 右边都是偶数 。

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

```



##### [面试题22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

```



##### [面试题24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL



```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curt = None
        while head != None:
            #temp记录下一个节点，head是当前节点
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt
```



##### [面试题25. 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4



```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
```



##### [面试题26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

         3
        / \
      4   5
      / \
     1   2



给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true



```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

```



##### [面试题27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

         4
      /   \
      2     7
     / \   / \
    1   3 6   9

镜像输出：

         4
      /   \
      7     2
     / \   / \
    9   6 3   1

  ```python
class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        self.dfs(root)
        return root
        
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): self.dfs(left)
        if (right!=None): self.dfs(right)
  ```



##### [面试题28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
      2   2
     / \ / \
    3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

        1
       / \
      2   2
       \   \
       3    3

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.isSymmetric_helper(root, root)
    
    def isSymmetric_helper(self, l, r):
        if l == None and r == None:
            return True
        if l != None and r == None:
            return False
        if l == None and r != None:
            return False
        if l.val != r.val:
            return False
        
        return self.isSymmetric_helper(l.left, r.right) and self.isSymmetric_helper(l.right, r.left)
```



##### [面试题29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]



```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        up = 0
        left = 0
        right = len(matrix[0])-1
        down = len(matrix) -1
        
        result = []
        direct = 0 #0 向右  1 向下 2 向左  3 向上
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    result.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    result.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1,-1):
                    result.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    result.append(matrix[i][left])
                left += 1
            if left > right or down < up:
                return result
            direct = (direct+1) % 4
```



##### [面试题30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.



```python
class MinStack(object):


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []


    def push(self, number):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        else:
            self.minStack.append(min(number, self.minStack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        ret = self.stack[-1]
        del(self.stack[-1], self.minStack[-1])
        return ret

    def top(self):
        """
        :rtype: int
        """
        ret = self.stack[-1]
        return ret
        

    def min(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
```



##### [面试题31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

**示例 2：**

```
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```





考虑借用一个辅助栈 stack*s**t**a**c**k* ，**模拟** 压入 / 弹出操作的排列。根据是否模拟成功，即可得到结果。

入栈操作： 按照压栈序列的顺序执行。
出栈操作： 每次入栈后，循环判断 “栈顶元素 == 弹出序列的当前元素” 是否成立，将符合弹出序列顺序的栈顶元素全部弹出。

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

```



##### [面试题32 - I. 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

返回：

[3,9,20,15,7]



层次遍历

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res
```



##### [面试题32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3

   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res

```



##### [面试题32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res

```



##### [面试题33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

         5
        / \
       2   6
      / \
     1   3

示例 1：

输入: [1,6,3,2,5]
输出: false



```
输入: [1,3,2,6,5]
输出: true
```

二叉树遍历结果的最后一个是根节点 第一个比根节点大的节点的左边为左枝 右边为右树枝 

使用递归的方法 一层一层查询

```python
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
```



##### [面试题34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

```



##### [面试题35. 复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

请实现 `copyRandomList` 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 `next` 指针指向下一个节点，还有一个 `random` 指针指向链表中的任意节点或者 `null`。

```python
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        Dict = {}
        newHead = Node(head.val)
        old = head
        new = newHead
        Dict[old] = new
        
        while old != None:
            new.random = old.random
            if old.next != None:
                new.next = Node(old.next.val)
                Dict[old.next] = new.next
            else:
                new.next = None
            old = old.next
            new = new.next
        
        RandomLoop = newHead
        while RandomLoop != None:
            if RandomLoop.random != None:
                RandomLoop.random = Dict[RandomLoop.random]
            RandomLoop = RandomLoop.next
        return newHead
```



##### [面试题36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：

![img](/Users/linianzu/Documents/Learning/md/大数据开发/pic/bstdlloriginalbst-20200728095357139.png)

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

![img](/Users/linianzu/Documents/Learning/md/大数据开发/pic/bstdllreturndll-20200728095358034.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
```



##### [面试题37. 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

请实现两个函数，分别用来序列化和反序列化二叉树。

你可以将以下二叉树：

        1
       / \
      2   3
         / \
        4   5

序列化为 "[1,2,3,null,null,4,5]"

```python
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
```



##### [面试题38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```



```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res
```



##### [面试题39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

```
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
```



```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

```



##### [面试题40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

输入整数数组 `arr` ，找出其中最小的 `k` 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

```



##### [面试题41. 数据流中的中位数](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/)

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]



Python 中 heapq 模块是小顶堆。实现 **大顶堆** 方法： 小顶堆的插入和弹出操作均将元素 **取反** 即可。

```python
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
```



##### [面试题42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



![Picture1.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/8fec91e89a69d8695be2974de14b74905fcd60393921492bbe0338b0a628fd9a-Picture1.png)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
```



##### [面试题43. 1～n整数中1出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。



将 11 ~ n 的个位、十位、百位、...的 1 出现次数相加，即为 1 出现的总次数

某位中 1 出现次数的计算方法：

根据当前位 curcur 值的不同，分为以下三种情况：

当 cur = 0时： 此位 1 的出现次数只由高位 high 决定，计算公式为：
![image-20200527113559521](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200527113559521.png)



![Picture1.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/78e60b6c2ada7434ba69643047758e113fa732815f7c53791271c5e0f123687c-Picture1.png)



当 **cur = 1 时：** 此位 11 的出现次数由高位 high和低位 low 决定，计算公式为：

![image-20200527113733753](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200527113733753.png)

![Picture2.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/58c7e6472155b49923b48daac10bd438b68e9504690cf45d5e739f3a8cb9cee1-Picture2.png)



当 **cur = 2,3,4,5,6... 时：** 此位 1的出现次数由高位 high 决定，计算公式为：

$(high + 1) * digit$

![Picture3.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/0e51d37b434ef0ad93882cdcb832f867e18b872833c0c360ad4580eb9ed4aeda-Picture3.png)



```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: 
                res += high * digit
            elif cur == 1: 
                res += high * digit + low + 1
            else: 
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res


```



##### [面试题44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。



![Picture1.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/2cd7d8a6a881b697a43f153d6c10e0e991817d78f92b9201b6ab71e44cb619de-Picture1.png)



```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.
```



##### [面试题45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

**示例 1:**

```
输入: [10,2]
输出: "102"
```

```python
from functools import cmp_to_key
class Solution:
    def minNumber(self, nums: List[int]) -> str:

        return ''.join(sorted(map(str, nums),key=cmp_to_key(lambda x, y: int(x+y)-int(y+x))))
```



##### [面试题46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

![image-20200527142957955](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200527142957955.png)

```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a
```



##### [面试题47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

```
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```



```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
```



##### [面试题48. 最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        max_len = 0
        for ch in s:
            if substring.find(ch) == -1:
                substring += ch
                max_len = max(max_len, len(substring))
            else:
                substring = substring[substring.find(ch)+1:] + ch
                max_len = max(max_len, len(substring))
        max_len = max(max_len, len(substring))
        return max_len
```



##### [面试题49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)

我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```

```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visited = set([1])
        
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)
            
        return val
```



##### [面试题50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

```
s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
```

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '
```



##### [面试题51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

```
输入: [7,5,6,4]
输出: 5
```

具体看leetcode视频解析

```python
class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)

```



##### [面试题52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

输入两个链表，找出它们的第一个公共节点。

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA = 0
        indexA = headA
        countB = 0
        indexB = headB
        while indexA != None:
            countA = countA + 1
            indexA = indexA.next
        while indexB != None:
            countB = countB + 1
            indexB = indexB.next
        print(countA)
        print(countB)
        
        indexA = headA
        indexB = headB
        while countA > countB:
            indexA = indexA.next
            countA -= 1
        while countB > countA:
            indexB = indexB.next 
            countB -= 1
        
        while indexA is not indexB:
            indexA = indexA.next
            indexB = indexB.next 
        return indexA
```



##### [面试题53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

统计一个数字在排序数组中出现的次数。

```python
class Solution:
    def search(self, nums: [int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1
```





##### [面试题53 - II. 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/)

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i
```





##### [面试题54. 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4



解题思路：
本文解法基于此性质：二叉搜索树的中序遍历为 递增序列 。

根据以上性质，易得二叉搜索树的 中序遍历倒序 为 递减序列 。
因此，求 “二叉搜索树第 kk 大的节点” 可转化为求 “此树的中序遍历倒序的第 kk 个节点”。

**中序遍历的倒序** 为 “右、根、左” 顺序，递归法代码如下：

```python
# 打印中序遍历倒序
def dfs(root):
    if not root: return
    dfs(root.right) # 右
    print(root.val) # 根
    dfs(root.left)  # 左

```



```python
class Solution(object):
    def kthLargest(self, root, k):
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res

```



##### [面试题55 - I. 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

       3
      / \
      9  20
        /  \
       15   7

返回它的最大深度 3 。

层次遍历 找最大深度

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res
```



##### [面试题55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

      3
     / \
      9  20
        /  \
       15   7

返回 true 。



```python
class Solution(object):
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced
        
    def validate(self, root):
        if root is None:
            return True, 0
            
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0
            
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
```

同算法 110



一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 



##### [面试题56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

难度中等146

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

算法
先对所有数字进行一次异或，得到两个出现一次的数字的异或值。

在异或结果中找到任意为 11 的位。

根据这一位对所有的数字进行分组。

在每个组内进行异或操作，得到两个数字。

```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
```



##### [面试题56 - II. 数组中数字出现的次数 II](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)

在一个数组 `nums` 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

有限状态自动机

各二进制位的 位运算规则相同 ，因此只需考虑一位即可。如下图所示，对于所有数字中的某二进制位 1 的个数，存在 3 种状态，即对 3 余数为 0, 1, 2。

若输入二进制位 1 ，则状态按照以下顺序转换；
若输入二进制位 0 ，则状态不变。

![Picture4.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/f75d89219ad93c69757b187c64784b4c7a57dce7911884fe82f14073d654d32f-Picture4.png)

![Picture5.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/6ba76dba1ac98ee2bb982e011fdffd1df9a6963f157b2780461dbce453f0ded3-Picture5.png)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
```



##### [面试题57. 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

```
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
```

双指针

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            return []
        low = 0
        high = len(nums)-1
        while low < high:
            sum_ = nums[low] + nums[high]
            if sum_ == target:
                return [nums[low], nums[high]]
            if sum_ > target:
                high -= 1
            else:
                low += 1
        return []
```



##### [面试题57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

```
输入：target = 9
输出：[[2,3,4],[4,5]]
```



滑动窗口

```python
def findContinuousSequence(self, target: int) -> List[List[int]]:
    i = 1 # 滑动窗口的左边界
    j = 1 # 滑动窗口的右边界
    sum = 0 # 滑动窗口中数字的和
    res = []

    while i <= target // 2:
        if sum < target:
            # 右边界向右移动
            sum += j
            j += 1
        elif sum > target:
            # 左边界向右移动
            sum -= i
            i += 1
        else:
            # 记录结果
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            sum -= i
            i += 1

    return res

```





##### [面试题58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split()))
```





##### [面试题58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

```



##### [面试题59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)

给定一个数组 `nums` 和滑动窗口的大小 `k`，请找出所有滑动窗口里的最大值。

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        ans = []
        if not nums:
            return ans
        for i in range(0,len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans
```



##### [面试题59 - II. 队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)

请定义一个队列并实现函数 `max_value` 得到队列里的最大值，要求函数`max_value`、`push_back` 和 `pop_front` 的**均摊**时间复杂度都是O(1)。

若队列为空，`pop_front` 和 `max_value` 需要返回 -1

维护一个单调的双端队列

```python
import queue
class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
```



##### [面试题60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

动态规划

下面思路可能更容易理解。
n个骰子，一共有6**n种情况
n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
可以看作是从前(n-1)个骰子投完之后的状态转移过来。
其中F（N,S）表示投第N个骰子时，点数和为S的次数



```python
class Solution:
    def twoSum(self, n: int) -> List[float]:

        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):
            res.append(dp[n][i]*1.0/6**n)
        return res
#####动态规划
```



##### [面试题61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

```
输入: [1,2,3,4,5]
输出: True
```

```
输入: [0,0,1,2,5]
输出: True
```

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        num=nums.count(0)
        nums.sort()
        temp=nums[num:]
        if num==0:  #将形成一个等差数列
            if nums[-1]-nums[0]==4 and sum(nums)==5*(nums[0]+nums[-1])/2:
                return True
            else:return False
        else:
            for i in range(1,len(temp)):
                if temp[i]==temp[i-1] or temp[-1]-temp[0]>4:
                    return False
            return True
```

判断有没有0 然后判断能不能补充空缺





##### [面试题62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

我们知道，从 f(n - m) 场景下删除的第一个数的序号是 (m - 1) % n，那么 f(n - 1, m) 场景将使用被删除数字的下一个数，即序号 m % n 作为它的 0 序号。

设 f(n - 1, m) 的结果为 x，x 是从 f(n, m) 场景下序号为 m % n 的数字出发所获得的结果，因此，我们可以得出：m % n + x 是该数字在 f (n, m) 场景下的结果序号。即：

f(n, m) = m % n + x
但由于 m % n + x 可能会超过 n 的范围，所以我们再取一次模：

f(n , m) = (m % n + x) % n = (m + x) % n
将 f(n - 1, m) 代回，得到递推公式：

f(n, m) = (m + f(n - 1, m)) % n
有了递推公式后，想递归就递归，想迭代就迭代咯~

```python
sys.setrecursionlimit(100000)

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return self.f(n, m)

    def f(self, n, m):
        if n == 0:
            return 0
        x = self.f(n - 1, m)
        return (m + x) % n
```







##### [面试题63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 ```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        if len(prices) == 0:
            return 0
        premin = prices[0]
        gain = 0
        
        for i in range(1,len(prices)):
            premin = min(premin, prices[i])
            gain = max(gain, prices[i] - premin)
        return gain
 ```



##### [面试题64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

求 `1+2+...+n` ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

```python
class Solution:
    def sumNums(self, n: int) -> int:
        return (n+n**2)>>1
```



##### [面试题65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。



**无进位和** 与 **异或运算** 规律相同，**进位** 和 **与运算** 规律相同（并需左移一位）。因此，无进位和 n*n* 与进位 c*c* 的计算公式如下；

![image-20200527213609360](C:\Users\59584\AppData\Roaming\Typora\typora-user-images\image-20200527213609360.png)



![Picture1.png](/Users/linianzu/Documents/Learning/md/大数据开发/pic/56d56524d8d2b1318f78e209fffe0e266f97631178f6bfd627db85fcd2503205-Picture1.png)

Q ： 若数字 aa 和 bb 中有负数，则变成了减法，如何处理？
A ： 在计算机系统中，数值一律用 补码 来表示和存储。补码的优势： 加法、减法可以统一处理（CPU只有加法器）。因此，以上方法 同时适用于正数和负数的加法 。

```python
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
```

Python 负数的存储：
Python / Java 中的数字都是以 补码 形式存储的。但 Python 没有 int , long 等不同长度变量，即没有变量位数的概念。

**获取负数的补码：** 需要将数字与十六进制数 `0xffffffff` 相与。可理解为舍去此数字 3232 位以上的数字，从无限长度变为一个 3232 位整数。

返回前数字还原： 若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。 a ^ x 运算将 11 至 3232 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 3232 位以上的位取反，即由 00 变为 11 ， 11 至 3232 位不变。



##### [面试题66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

```
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```



双指针

```python
class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        length = len(a)
        left,right = 1,1
        result = [1] * length
        for i in range(length):
            indexA = i
            indexB = length-1-i
            result[indexA] = result[indexA] * left
            result[indexB] = result[indexB] * right
            left = left * a[indexA]
            right = right * a[indexB]
        return result
```



##### [面试题67. 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)

写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

 

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。



```
输入: "42"
输出: 42
```



输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

```python
class Solution(object):
    def myAtoi(self, Str):
        """
        :type str: str
        :rtype: int
        """
        Str = Str.lstrip()
        
        if len(Str) == 0:
            return 0
        
        minus = False
        if Str[0] == "-":
            Str = Str[1:]
            minus = True
        elif Str[0] == "+":
            Str = Str[1:]
            minus = False
            
        
        result = ""
        i = 0
        while(i < len(Str) and ord(Str[i]) >= 48 and ord(Str[i]) <= 57):
            result = result + Str[i]
            i += 1
        
        if len(result) == 0:
            return 0
        
        num = int(result)
        print(minus)
        if minus:
            num = -num
        print(num)
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647
        return num
```



##### [面试题68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

![img](/Users/linianzu/Documents/Learning/md/大数据开发/pic/binarysearchtree_improved.png)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
```







##### [面试题68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

![img](/Users/linianzu/Documents/Learning/md/大数据开发/pic/binarytree.png)

```python
class Solution(object):
    def lowestCommonAncestor(self, root, A, B):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if root == A or root == B:
            return root
        
        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)
        
        # A 和 B 一边一个
        if left_result and right_result: 
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result
        
        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result
        
        # 左右子树啥都没有
        return None
```

