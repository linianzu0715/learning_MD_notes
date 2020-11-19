

### 目录

[TOC] 



## 三数之和：

### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那“两个”整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 循环数组的所有的位置
        for i in range(len(nums)):
            # 选取当前位置，得到目标的值
            target_now = target - nums[i]
            # 循环后面的位置
            for j in range(i+1,len(nums)):
                if nums[j] == target_now:
                    return [i,j]
```



### [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

```
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
```

```python
class Solution(object):
    def twoSum(self, numbers, target):
        # 一个指针在数组的左边
        left = 0
        # 一个指针的数组的右边
        right = len(numbers)-1
        # 当两个没有重合
        while left < right:
            if target - (numbers[left] + numbers[right]) == 0:
                return [left+1,right+1]
            elif target - (numbers[left] + numbers[right]) > 0:
                left = left + 1
            elif target - (numbers[left] + numbers[right]) < 0:
                right = right - 1
        return []
```



### [15. 三数之和](https://leetcode-cn.com/problems/3sum/)

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

```
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

Answer:

固定一个，移动两个

```python
#待重写
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 对数组进行排序
        nums.sort()
        # 声明结果集合
        result = []
        length = len(nums)
        if length < 3:
            return result
        
        for i in range(0,length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            pointer2 = i+1
            pointer3 = length-1
            while pointer2 < pointer3:
                if (nums[pointer2] + nums[pointer3]) == target:
                    result.append([nums[i], nums[pointer2], nums[pointer3]])
                    pointer3 = pointer3 -1
                    while pointer2 < pointer3 and nums[pointer3] == nums[pointer3+1]:
                        pointer3 = pointer3 -1
                    pointer2 = pointer2 +1
                    while pointer2 < pointer3 and nums[pointer2] == nums[pointer2-1]:
                        pointer2 = pointer2 +1
                elif (nums[pointer2] + nums[pointer3]) > target:
                    pointer3 = pointer3 -1
                    while pointer2 < pointer3 and nums[pointer3] == nums[pointer3+1]:
                        pointer3 = pointer3 -1
                else:
                    pointer2 = pointer2 +1
                    while pointer2 < pointer3 and nums[pointer2] == nums[pointer2-1]:
                        pointer2 = pointer2 +1
        return result
```



### [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = 0
        dis = 10000
        length = len(nums)
        for p1 in range(length):
            now = target - nums[p1]
            closest, dis= self.findOtherTwo(nums, target, length, closest, p1, now, dis)
        
        return closest
    
    def findOtherTwo(self, nums, target, length, closest, p1, now, dis):
        p2 = p1 +1
        p3 = length-1
        while p2 < p3:
            if (nums[p2] + nums[p3]) < now:
                dis_ = abs(now - nums[p2] - nums[p3])
                if dis_ < dis:
                    dis = dis_
                    closest = nums[p1] + nums[p2] + nums[p3]
                p2 += 1
                
            elif (nums[p2] + nums[p3]) > now:
                dis_ = abs(now - nums[p2] - nums[p3])
                if dis_ < dis:
                    dis = dis_
                    closest = nums[p1] + nums[p2] + nums[p3]
                p3 -= 1

            elif (nums[p2] + nums[p3]) == now:
                closest = target
                dis = 0
                break
            
        return closest, dis
```



### [18. 四数之和](https://leetcode-cn.com/problems/4sum/)

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        length = len(nums)
        result = []
        for p1 in range(length-3):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            for p2 in range(p1+1,length-2):
                if p2 > (p1+1) and nums[p2] == nums[p2-1]:
                    continue 
                result = self.searchForTwo(p1,p2,result,length,nums,target)
        return result
    
    def searchForTwo(self,p1,p2,result,length,nums,target):
        p3 = p2 + 1
        p4 = length - 1
        while p3 < p4:
            if (nums[p1] + nums[p2] + nums[p3] + nums[p4]) == target:
                result.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                p3 += 1
                while p3 < p4 and nums[p3] == nums[p3-1]:
                    p3 += 1
                p4 -= 1
                while p3 < p4 and nums[p4] == nums[p4+1]:
                    p4 -= 1
            elif (nums[p1] + nums[p2] + nums[p3] + nums[p4]) < target:
                p3 += 1
                while p3 < p4 and nums[p3] == nums[p3-1]:
                    p3 += 1
            else:
                p4 -= 1
                while p3 < p4 and nums[p4] == nums[p4+1]:
                    p4 -= 1
        return result
```



## 回文

### [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给定一个字符串 `s`，找到 `s` 中最长的回文子串。你可以假设 `s` 的最大长度为 1000。

**示例 1：**

```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```

**示例 2：**

```
输入: "cbbd"
输出: "bb"
```

Answer:

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str 输入的字符串
        :rtype: str 返回的长度最长的回文
        """
        #初始化储存最长回文的变量
        max_list = ""
        #循环输入字符串中所有的位置
        for index in range(len(s)):
          	#从某个位置开始向左右两个方向推广会问串有两种情况
            #第一种情况是从一个字符展开
            temp = self.findPalindromic(s,index,index)
            if len(temp) > len(max_list):
                max_list = temp
            #第二种情况是这个和之后的两个字符相同，则再展开
            temp = self.findPalindromic(s,index,index+1)
            if len(temp) > len(max_list):
                max_list = temp
        return max_list
        
    def findPalindromic(self,s,left,right):
      	"""
        :type s: str 输入的字符串
        			left：开始点，左
        			right：开始点，右
        :rtype: str 返回的长度最长的回文
        """
        result = ""
        while(left >= 0 and right < len(s)):
            if s[left] == s[right]:
                if left == right:
                    result += s[left]
                else:
                    result = s[left] + result + s[right]
                left -= 1
                right += 1
            else:
                break
        return result
```



### [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # 将它先转化为字符串 然后再反转字符串 最后比较两个是否相等
        if x < 0:
            return False
        
        S = list(str(x))
        S.reverse()
        result = ""
        for item in S:
            result += item
        result = int(result)
        
        return result == x
```



### [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。**说明：**本题中，我们将空字符串定义为有效的回文串。

```python
class Solution(object):
    def isPalindrome(self, s):
        # 统一格式
        new_s = str(filter(str.isalnum, str(s)).lower())
        
        # 为空的特殊情况
        if len(new_s) == 0:
            return True
          
        # 从前往后和从后往前进行判断
        left = 0
        right = len(new_s)-1
        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
```



### [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/)

给定一个字符串 *s*，将 *s* 分割成一些子串，使每个子串都是回文串。返回 *s* 所有可能的分割方案。

```python
class Solution(object):
    def partition(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, stringlist, results):
        """
        :param s: 输入的字符串
        :param stringlist: 当前的字串的集合
        :param results: 结果集合
        """

        # 输入为空的特殊情况
        if len(s) == 0:
            results.append(list(stringlist))
            return

        # 找回文串
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            # 如果找到了一个，就将它加入到当前结果集合
            # 并且把余下的字符串作为输入，进入下一层递归
            if self.is_palindrome(prefix):
                stringlist.append(prefix)
                self.dfs(s[i:], stringlist, results)
                stringlist.pop()

    def is_palindrome(self, s):
        """
        用来判断输入的字符串是否是一个回文串
        :param s: 输入的字符串
        :return: 是否是回文串
        """
        return s == s[::-1]
```



## 数学

### [202. 快乐数](https://leetcode-cn.com/problems/happy-number/)

编写一个算法来判断一个数 n 是不是快乐数。「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

```python
class Solution(object):
    """
    创建set。每次的平方之后之后计算结果，如果出现了1则结束
    如果有重复则中断
    """
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Dict = set()
        while n != 1:
            Dict.add(n)
            Sum = sum([int(x) * int(x) for x in list(str(n))])
            if Sum == 1:
                return True
            elif Sum in Dict:
                return False
            else:
                n = Sum
        return True
```



### [204. 计数质数](https://leetcode-cn.com/problems/count-primes/)

统计所有小于非负整数 *n* 的质数的数量。

```python
class Solution(object):
    def countPrimes(self, n):
        """
        厄拉多塞筛法
        :param n:
        :return:
        """

        # 0，1，都不是质数
        if n < 3:
            return 0

        # 2是一个质数
        if n == 3:
            return 1

        res = 0

        # 构建布尔数组，记录这个位置上的数字是不是质数
        # 并且初始的时候设置所有的位置上都是True
        not_prime = [True] * n
        not_prime[0] = not_prime[1] = False
        not_prime[2] = True

        # 只用循环的到 n 开根号 + 1
        for i in range(2, int(n ** 0.5)+1):
            # 如果当前这个位置上的是质数
            if not_prime[i]:
                # 就把所有它的倍数设置为合数
                for j in range(i*i, n, i):
                    not_prime[j] = False
                    
        # 返回范围内所有的质数的数目
        return sum(not_prime)
```



### [263. 丑数](https://leetcode-cn.com/problems/ugly-number/)

编写一个程序判断给定的数是否为丑数。丑数就是只包含质因数 `2, 3, 5` 的**正整数**。

```python
"""
将输入的数字中所有的2，3，5的因数都除去，最后如果结果为1
则说明是丑数。如果结果不是1，则不是丑数。
"""

class Solution(object):
    def isUgly(self, num):
        if num <=0:
            return False
        while (num % 2) == 0:
            num = num/2
        while (num % 3) == 0:
            num = num/3
        while (num % 5) == 0:
            num = num/5
        return num == 1
```



### [264. 丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/)

编写一个程序，找出第 `n` 个丑数。丑数就是质因数只包含 `2, 3, 5` 的**正整数**。

```python
class Solution(object):
    def nthUglyNumber(self, n):
        # 创建一个队列
        # 但是过程中需要保证heap是排序好的
        heap = [1]
        # 创建一个记录访问过的数字的hashset
        visited = set([1])
        
        # 初始化当前的值为None
        val = None
        # 循环n次，找到第n个结果
        for i in range(n):
            # 从队列中获取第一个
            val = heapq.heappop(heap)
            # 相继乘上2，3，5的因数
            # 如果结果在visited中出现过，就跳过，
            # 如果没有出现过，则就加入到队列尾端，并且加入到visited集合中
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)
        return val
```



### [1201. 丑数 III](https://leetcode-cn.com/problems/ugly-number-iii/)

请你帮忙设计一个程序，用来找出第 `n` 个丑数。丑数是可以被 `a` **或** `b` **或** `c` 整除的 **正整数**。

```
让我们观察题目，可以看到，最终状态(即n)的范围非常大。试图自底向上递推或是按照通常的自顶向下回溯显然会超时(比如动态规划、DFS等方法)

面对这么大的状态空间，二分法的时间复杂度是logN,因此能够大大压缩需要遍历的状态数目

按照题意，所谓丑数是可以至少被a、b、c三者中的一者整除的，那么对于一个丑数X，我们能够确定它是第几个丑数吗？

--答案显然是可以的，我们只需要计算X中包含了多少个丑数因子即可。

即只需要知道在[0,X]范围内,还有多少个丑数即可，而这些丑数，无非就是一些能被a或者b或者c所整除的数。

那么显然，我们直接用X/a、X/b、X/c就能计算出[0,X]范围内有多少数能被a或者b或者c整除，然后把它们加起来就是答案！

但是仔细思考一下，我们是不是重复计算了些什么？如果一个数既能被a整除，又能被b整除，那么实际上该数在先前的计算中就被重复计算了一次(分别是在计算X/a和X/b时)。

--好吧，让我们思考所有可能的情况

1.该数只能被a整除 (该数一定是a 的整数倍)

2.该数只能被b整除 (该数一定是b 的整数倍)

3.该数只能被c整除 (该数一定是c 的整数倍)

4.该数只能被a和b同时整除 (该数一定是a、b最小公倍数的整数倍)

5.该数只能被a和c同时整除 (该数一定是a、c最小公倍数的整数倍)

6.该数只能被b和c同时整除 (该数一定是b、c最小公倍数的整数倍)

7.该数只能被a和b和c同时整除（该数一定是a、b、c的最小公倍数的整数倍）

所以，我们只需要分别计算以上七项就能得到结果了！让我们分别来看（用MCM+下标表示最小公倍数）:

情况1 = X/a - 情况4 - 情况5 - 情况7
情况2 = X/b - 情况4 - 情况6 - 情况7
情况3 = X/c - 情况5 - 情况6 - 情况7
情况4 = X/MCM_a_b - 情况7
情况5 = X/MCM_a_c - 情况7
情况6 = X/MCM_b_c - 情况7
情况7 = X/MCM_a_b_c

让我们整理上述方程后也就得到：

sum(情况) = X/a + X/b + X/c - X/MCM_a_b - X/MCM_a_c - X/MCM_b_c + X/MCM_a_b_c

好了，现在也就得到了计算X中包含多少个丑数因子的方法了！
```



```
输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
```



```python
class Solution(object):
    """
    找到两个数的最大公因数
    """
    def gcd(self, x, y): 
        while(y): 
            x, y = y, x % y
        return x 
  
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
        """
        三个整数的最小公倍数
        """
        def Lcm3(x,y,z):
            a = (x*y)//self.gcd(x,y)  
            return (a*z)//self.gcd(a,z)
        
        """ 计算到这个位置为止，前面有多少个丑数
        """
        def uglynum(x):
                return x//a+x//b+x//c-x//(a*b//self.gcd(a,b))-x//(a*c//self.gcd(a,c))-x//(b*c//self.gcd(b,c))+x//Lcm3(a,b,c)
            
        # 确定要进行二分查找的范围 右边界要保证至少有n个丑数在范围之内
        left=1
        right=n*min(a,b,c)
        
        # 二分查找
        while left<right:
            mid=(left+right)//2
            if uglynum(mid)<n:
                left=mid+1
            else:
                right=mid
        return left
```





### [274. H 指数](https://leetcode-cn.com/problems/h-index/)

给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数 不超过 h 次。）例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

```python
class Solution(object):
    # 输入的是一个数组citations
    def hIndex(self, citations):
        result = 0
        # 最终的结果最多就是n，n是citation的长度
        # 出现的场景是为数组中所有的数都是相等的
        for i in range(1,len(citations)+1):
            nums = 0
            # 循环citation中的所有的位置
            for j in range(len(citations)):
                # 如果当前位置的值大于i，计数器+1
                if citations[j] >= i:
                    nums += 1
            # 当循环完所有的位置之后，计数器的数字比i小，则返回上一个数字
            if nums < i:
                return i-1
            # 如果是最后一个数字，并且计数器的数字也更大，返回最后的数字
            if i == len(citations) and nums >= i:
                return i
        # 当第一都不满足的时候，返回0
        return result
```



### [279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/)

给定正整数 *n*，找到若干个完全平方数（比如 `1, 4, 9, 16, ...`）使得它们的和等于 *n*。你需要让组成和的完全平方数的个数最少。

```python
import math
class Solution(object):
    def numSquares(self, n):
        # 去除之中4的因数
        while (n % 4 == 0):
            n = n / 4
        # 如果除8余数为7，则可以用4个来组合成
        if (n % 8 == 7):
            return 4
        # 否则，就一定能用两个最多三个完全平方数来组成长这个数字
        a = 0
        # 找能否用两个数字来组成
        while (a**2 < n):
            b = int(math.sqrt(n - (a**2)))
            if (b**2 + a**2) == n:
                return int(a > 0) + int(b > 0)
            a = a+1
        # 否则一定能用三个来组成
        return 3
```



### [313. 超级丑数](https://leetcode-cn.com/problems/super-ugly-number/)

编写一段程序来查找第 `*n*` 个超级丑数。超级丑数是指其所有质因数都是长度为 `k` 的质数列表 `primes` 中的正整数。

```
输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
```



```python
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        # 用来存储当前的候选的superNum
        candidates = [1]*len(primes)
        # 用来存储这个位置上的candidates的数字上一个是从什么superNums得来的
        ids = [0]*len(primes)
        # 用来存储已经得到的超级丑数
        superNums = [1]
        nextMin = 1
        for count in range(1, n) :
            for i in range(len(primes)):
                # 找到了下一个进行相乘的数字
                if nextMin == candidates[i] :
                    candidates[i] = superNums[ids[i]]*primes[i]
                    ids[i] += 1
            # 找到最小值
            nextMin = min(candidates)
            # 得到这一轮的superNum
            superNums.append(nextMin)
        return superNums[-1]
```



### [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)

给定一个正整数 *n*，将其拆分为**至少**两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

```python
class Solution:
    # 拆出来的3的因数越多越好
    def integerBreak(self, n: int) -> int:
        # 当n为3，乘积最大为2
        # 当n为2，乘积最大为1
        if n <= 3: return n - 1
        # 找到这个数中最多有多少个3
        a, b = n // 3, n % 3
        # 如果余数为0，则就是所有的3相乘的结果
        if b == 0: return int(math.pow(3, a))
        # 如果余数是1
        if b == 1: return int(math.pow(3, a - 1) * 4)
        # 如果余数是2
        return int(math.pow(3, a) * 2)
```



### [367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)

给定一个正整数 *num*，编写一个函数，如果 *num* 是一个完全平方数，则返回 True，否则返回 False。

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0 
        right = num
        
        # 使用二分查找的方法，找到两个最靠近开方值的数字
        while left +1 < right:
            now = (left + right)/2
            if now**2 > num:
                right = now
            if now**2 < num:
                left = now
            if now**2 == num:
                return True
        # 找到之后进行检验
        if left**2 == num or right**2 == num:
            return True
        return False
```



### [372. 超级次方](https://leetcode-cn.com/problems/super-pow/)

你的任务是计算 *a**b* 对 1337 取模，*a* 是一个正整数，*b* 是一个非常大的正整数且会以数组形式给出。

```
输入: a = 2, b = [1,0]
输出: 1024
```

```
输入: a = 2, b = [3]
输出: 8
```

```python
class Solution(object):
    def superPow(self, a, b):
        # 特殊情况
        if a == 0:
            return 0
        # 存储结果的变量
        ans = 1
        # 对1337取模的方法
        def mod(x):
            return x % 1337
        # 每一位置，从后往前开始计算次方
        for num in b:
            ans = mod(mod(ans ** 10) * mod(a ** num))
        return ans
```




## 字符串

### [43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)

给定两个以字符串形式表示的非负整数 `num1` 和 `num2`，返回 `num1` 和 `num2` 的乘积，它们的乘积也表示为字符串形式。

```
输入: num1 = "2", num2 = "3"
输出: "6"
```

Answer:

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        res1 = res2 = 0
        for i in range(len1):
            res1 = res1*10 + ord(num1[i])-ord("0")
        for j in range(len2):
            res2 = res2*10 + ord(num2[j])-ord("0")
        return str(res1 * res2)
```



## 其他


### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。

**示例 1:**

```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

**Answer:**

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
          	#如果当前循环到的字符之前没有存在过
            if substring.find(ch) == -1:
              	#加入这个字符
                substring += ch
                #到目前为止，最长的长度为之前最长，和到新加入之后的总长最长相比
                max_len = max(max_len, len(substring))
            #如果当前循环到的字符之前出现过
            else:
								#则到目前为止没有重复的子字符串为
                #获取上一个重复的字符的位置往后的子字符串
                substring = substring[substring.find(ch)+1:] + ch
                #更新最大长度
                max_len = max(max_len, len(substring))
        return max_len
```



### [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。你可以假设 nums1 和 nums2 不会同时为空。

**示例 1:**

```
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
```

**示例 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
```

Answer:

非二分查找方法：将两个排序数组合并成一个数组，然后找到其中的中位数。但是这种方法的时间复杂度为O(m+n)。

要求的时间复杂度里面带有log，大概率使用二分查找的方法:

对于两个长度为m和n的数组，最后总长度为sum = m + n。则最后我们要找的中位数有两种情况。第一种情况就是当sum为奇数，则我们要找的中位数是第sum/2个数字。如果sum为偶数，则我们要找的中位数是偶数，则我们的中位数是第sum/2个数和第sum/2+1的数字的平均值。因此我们只需要找到这两个数字就行。

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
          	#初始化两个数组开始计算的位置
            index1, index2 = 0, 0
            while True:
                #当nums1中所有的数字都被排除完，则返回nums2中的数字
                if index1 == m:
                    return nums2[index2 + k - 1]
                #当nums2中的所有的数字被排除完，则返回nums1中的数字
                if index2 == n:
                    return nums1[index1 + k - 1]
                #如果只需要找一个数字，就从当前两个数组的队首找
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                #当前要比较的位置的索引
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                #当前要比较的数字值
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        #获取两个排序数组的长度
        m, n = len(nums1), len(nums2)
        #获取两个数组的总长度
        totalLength = m + n
        #如果总长度是奇数，就只用找到中间位置的数，返回
        #如果总长度是偶数，找到前后两个数，取平均值
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

```



### [6. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

```
L   C   I   R
E T O E S I I G
E   D   H   N
```

示例 2:

```
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
```

**answer**

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 如果每行就一个字母，则直接输出原字符串
        if numRows == 1:
            return s
        
        # 周期
        cycle = 2*numRows -2
        # 中间位置
        mid = numRows-1
        # 预先声明输出数组
        result = [""] * numRows
        #循环所有的行
        for lineN in range(numRows):
            # 如果是第一行
            if lineN == 0:
                index = 0
                while(index < len(s)):
                    result[lineN] += s[index]
                    index += cycle
            # 如果是最后一行
            if lineN == (numRows-1):
                index = mid
                while(index < len(s)):
                    print(index)
                    print(s[index])
                    result[lineN] += s[index]
                    index += cycle
            # 如果是中间的行
            if lineN > 0 and lineN < (numRows-1):
                indexA = lineN
                indexB = cycle-lineN
                while(indexA < len(s) or indexB < len(s)):
                    if indexA < len(s):
                        result[lineN] += s[indexA]
                        indexA += cycle
                    if indexB < len(s):
                        result[lineN] += s[indexB]
                        indexB += cycle
        # 将数组转化为字符串进行输出
        final = ""
        for string in result:
            final += string
        return final
```



### [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

```
输入: 123
输出: 321
```

Answer:

```python
"""
字符串方法
将数组先转化为字符串，然后字符串颠倒。最后字符串转为数字。
"""
import math
class Solution:
    def reverse(self, x: int) -> int:
        # 如果是负数
        if x < 0
            # 先转换为负数
            x = -x
            # 转为字符串
            str_x = str(x)
            str_x = str_x[::-1]
            # 保证在32位范围之内
            if -int(str_x) > (math.pow(2,31)-1) or -int(str_x) < -(math.pow(2,31)):
                return 0
            else:
                return -int(str_x)
        # 如果输入的是一个正数
        else:
            # 转为字符串
            str_x = str(x)
            str_x = str_x[::-1]
            # 保证在32位范围之内
            if int(str_x) > (math.pow(2,31)-1) or int(str_x) < -(math.pow(2,31)):
                return 0
            else:
                return int(str_x)
```



### [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

```python

class Solution(object):
    def myAtoi(self, Str):
        """
        :type str: str
        :rtype: int
        """
        # 方法用于截掉字符串左边的空格或指定字符。
        Str = Str.lstrip()
        # 如果截取之后为空，则返回0
        if len(Str) == 0:
            return 0
        # 判断正负性
        minus = False
        if Str[0] == "-":
            Str = Str[1:]
            minus = True
        elif Str[0] == "+":
            Str = Str[1:]
            minus = False   
        
        # 生成数字字符串
        result = ""
        i = 0
        while(i < len(Str) and ord(Str[i]) >= 48 and ord(Str[i]) <= 57):
            result = result + Str[i]
            i += 1
        
        if len(result) == 0:
            return 0
        
        # 在要求范围内输出
        num = int(result)
        if minus:
            num = -num
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647
        return num
```



### [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

**题目描述：**

给你一个字符串 `s` 和一个字符规律 `p`，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。

```
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
```

所谓匹配，是要涵盖 **整个** 字符串 `s`的，而不是部分字符串。

**正确解答：动态规划**

假设我们S字符串的开头到第$i$个字母,和P的从开头到第$j$个字母能否匹配的状态定义为$DP[i][j]$.假设我们已经有的$DP[i-1][j-1]$,$S[i]$,$P[j]$.我们要怎样得到$DP[i][j]$。我们可以分情况讨论：

1. 如果$S[i]$和$P[j]$相同，则表示当前字母可以匹配上：$dp[i][j] = dp[i-1][j-1]$

2. 如果$S[i]$和$P[j]$不相同，就需要进一步分情况讨论。

   2.1 如果当前$P[j]$是普通字符，则当前位置不能匹配，$dp[i][j] = False$ 

   2.2 如果当前$P[j]$是"."，则表示所有的字符都能匹配上，则$dp[i][j] = dp[i-1][j-1]$

   2.3 如果当前$P[j]$是"*"，则我们就需要看$P[j-1]$的情况。

   ​	2.3.1 如果$P[j-1] ！= S[i]$，这说明上一个字母不能匹配上，则我们只能想到让上一个字母出现0次来进行匹配。$dp[i][j] = dp[i][j-2]$

   ​	2.3.2 如果$P[j-1] == S[i]$或者$P[j-1] == "."$：

   ​		2.3.2.1 可能是最后一个数字出现了多次：例如S=####bccc P=###c*，则$dp[i][j] = dp[i-1][j]$

   ​		2.3.2.2 可能是最后一个数字没有出现过：例如S=####b P=###c*， 则$dp[i][j-2]$

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s and len(p) == 1: return False 

        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for r in range(nrow)]
        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c-1
            if p[j] == '*': dp[0][c] = dp[0][c-2]
        
        for r in range(1, nrow):
            i = r-1
            for c in range(1, ncol):
                j = c-1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r-1][c-1]
                elif p[j] == '*':
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[r][c] = dp[r-1][c] or dp[r][c-2]
                    else:
                        dp[r][c] = dp[r][c-2]
                else:
                    dp[r][c] = False

        return dp[nrow-1][ncol-1]
```



### [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

**示例：**

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49
```

Answer:

```python
"""
找出容量最大的桶
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 最先选择最左和最右的两个板子
        pointer1 = 0
        pointer2 = len(height)-1
        # 声明最大值变量
        maxs = 0
        # 声明当前值变量
        now = 0
        # 当两个指针没有重合的时候
        while pointer1 != pointer2:
            # 获取当前值
            now = min(height[pointer1],height[pointer2]) * (pointer2 - pointer1)
            # 如果有增大，则进行更新
            if now > maxs:
                maxs = now
            # 从较小的一边向中间移动
            if height[pointer1] <= height[pointer2]:
                pointer1 = pointer1 + 1
            else:
                pointer2 = pointer2 - 1
        return maxs
```



### [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)

罗马数字包含以下七种字符： `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 用来记录第几位
        index = 0
        # 记录结果的变量
        s = ""
        
        # 从最低位开始，直到所有的位置上都转化完成
        while num != 0:
            # 得到当前的最后一位
            last_digit = num % 10
            # 如果这一位不是0，就进行解析
            if last_digit != 0:
                # 进入解析函数，传入当前位置和数字，加入在原有的左边
                s = self.parse(index, last_digit) +  s
            # 获得下一位置
            num = num / 10
            # index更新
            index += 1
        return  s   
        
        
    def parse(self, index, last_digit):
        NUM = {
            1 : "I",
            2 : "II",
            3 : "III",
            4 : "IV",
            5 : "V",
            6 : "VI",
            7 : "VII",
            8 : "VIII",
            9 : "IX"
        }
        
        R = {
            "I" : ["I", "X", "C", "M"],
            "V" : ["V", "L", "D", "?"],
            "X" : ["X", "C", "M", "?"]
        }
        
        s = NUM[last_digit]
        return s.replace("X", R["X"][index]).replace("V", R["V"][index]).replace("I", R["I"][index])
返回该题
```



### [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

example：

```
输入: "III"
输出: 3
```

```
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 先将每个字母和数字的对应表格列出来
        ROMAN = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        # 从倒数第二个位置上开始找起
        index = len(s) -2
        # 获取最后一个位置对应的数字
        Sum = ROMAN[s[-1]]
        # 从后往前循环所有的位置
        while index >= 0:
            # 如果当前位置上的数字比后面一个位置的数字要小
            if ROMAN[s[index]] < ROMAN[s[index+1]]:
                # 总和减去这个数字
                Sum -= ROMAN[s[index]]
            else:
                # 总和加上这个数字
                Sum += ROMAN[s[index]]
            index -= 1
        return Sum
```



### [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

```
输入: ["flower","flow","flight"]
输出: "fl"
```

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 特殊情况
        if len(strs) == 0:
            return ""
        
        # 找到数组中最短的字符串
        min_length = float('INF')
        for s in strs:
            min_length = min(min_length,len(s))
        
        # 声明结果变量
        con_string = ""
        # 从第一个字符开始查询，如果都能满足，则往后一位。直到把最短字符串的长度都找完
        for i in range(min_length):
            common = strs[0][i]
            for s in strs:
                if common != s[i]:
                    return strs[0][:i]
            
        return strs[0][:min_length]
```





### [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

```
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

Answer：

```python
#直接递归遍历
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 把每个按钮上面对应的字母列出到表格中
        Dict = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        # 特殊
        if len(digits) == 0:
            return []
        
        # 输入的数字的总长度
        length = len(digits)
        # 结果变量
        result = []
        # 位置变量
        index = 0
        nums = list(digits)
        now = ""
        result = self.dfs(result, nums, now, length, index, Dict)
        return result
    
    def dfs(self, result, nums, now, length, index, Dict):
        if len(now) == length:
            result.append(now)
            return result
            
        for n in list(Dict[int(nums[index])]):
            now = now + n
            result = self.dfs(result, nums, now, length, index+1, Dict)
            now = now[:-1]
        return result
```



### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 注意空字符串可被认为是有效字符串

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 预先声明一个堆栈容器
        stack = []
        # 循环字符串中的所有的括号
        for item in s:
            # 如果是前括号
            if item == "(" or item == "[" or item == "{":
                # 就在堆栈中加入这个 
                stack.append(item)
            # 如果是后括号
            else:
                # 如果当前的堆栈为空
                if not stack:
                    # 则结果肯定为错误
                    return False
                # 如果不能正确顺序匹配上，返回错误
                if (item == "]" and stack[-1] != "[") or (item == ")" and stack[-1] != "(") or (item == "}" and stack[-1] != "{"):
                    return False
                # 如果匹配上了，就把前括号删掉
                stack.pop()             
        return not stack
```



### [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

数字 *n* 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

```
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```

Answer:

有条件递归

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int 生成的括号的对数
        :rtype: List[str] 括号字符串的集合
        """
        
        # 初始化剩余可以使用的左括号和右括号的数目
        left = n
        right = n
        
        # 当前的括号字符串
        now = ""
        
        # 初始化结果集合
        result = []

        # 特殊情况
        if n == 0:
            return []
        # 进入递归方法
        result = self.generateHelper(left, right, now, n, result)
        return result

    def generateHelper(self, left, right, now, n, result):
        """
        :param left: int 可使用的左括号的数目
        :param right: int 可使用的右括号的数目
        :param now: str 当前的括号字符串
        :param n: 
        :param result: 结果集合
        :return: result
        """
        
        # 如果当前没有需要加入的括号，返回结果
        if left == 0 and right == 0:
            result.append(str(now))
            return result
        
        # 如果当前还有需要加入的左括号
        if left > 0:
            # 向字符串中加入一个左括号
            now += "("
            self.generateHelper(left - 1, right, now, n, result)
            now = now[:-1]
            
        # 计算出已经使用过的左括号和右括号的数目
        now_left = n - left
        now_right = n - right
        
        # 如果当前还有需要加入的右括号，并且当前的左括号的数目大于右括号数目
        if right > 0 and now_left > now_right:
            # 加入右括号，进入下一层
            now += ")"
            self.generateHelper(left, right - 1, now, n, result)
            now = now[:-1]
        return result
```



### [28. 找出 needle 字符串出现的第一个位置](https://leetcode-cn.com/problems/implement-strstr/)

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int needle 字符串出现的第一个位置
        """
        # 两个字符串的长度
        length_hay = len(haystack)
        length_nee = len(needle)

        # 特殊情况
        if length_nee == 0:
            return 0
        elif length_hay == 0:
            return -1
        # 从0号位置开始查找
        for i in range(length_hay - length_nee + 1):
            for j in range(length_nee):
                # 如果字符串匹配上，就返回正确位置
                if haystack[i + j] == needle[j]:
                    if j == (length_nee - 1):
                        return i
                    else:
                        continue
                else:
                    break
        return -1
```



### [29. 二进制两数相除](https://leetcode-cn.com/problems/divide-two-integers/)

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。返回被除数 dividend 除以除数 divisor 得到的商。整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

**示例 1:**

```
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
```

Answer:

```python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 最大的数字
        INT_MAX = 2147483647
        # 如果除数或者被除数两者之一为负数，则结果就是负数
        minus = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        # 将除数和被除数都转化为正数
        dividend = abs(dividend)
        divisor = abs(divisor)

        # 找到 dividend 中 最多有多少个 divisor
        # 先从 2^31 个开始 如果有 就先在 dividend 中先减去 然后找有没有 2^30
        # 直到最后找到 2^0 = 1 个 divisor
        ans = 0
        shift = 31
        while shift >= 0:
            if dividend >= (divisor << shift):
                dividend -= (divisor << shift)
                ans += (1 << shift)
            shift -= 1
            
        # 根据结果的正负性进行转化
        if minus:
            ans = -ans
            
        # 如果越界，返回最大值
        if ans > INT_MAX:
            return INT_MAX
        return ans
```





### [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

题目描述：

给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

Example：

```
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
```

```
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
```



正确解法：1

```python
from collections import Counter
"""
Counter的用法
b = Counter(a) #求a数组中每个数字出现了几次
print(b) 
output：Counter({2: 3, 4: 2, 3: 2, 1: 1})

print(b[2]) #计算数字2出现了几次 
output：3
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:return [] #常见输入错误报错
        
        one_word = len(words[0]) #获取词库中每个词的标准长度
        all_len = len(words) * one_word #目标子串的长度
        n = len(s) #输入字符串s的长度
        
        
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len] #获取当前子串
            c_tmp = [] #产生临时字符串数组
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word]) #将当前子串中的所有单词加入到数组中
            if Counter(c_tmp) == words: #如果和标准相同，正确
                res.append(i)
        return res
    
#时间复杂度 (n^2)
#这种方法虽然能成功AC 但是时间复杂度还算是比较久
```



### [31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/)

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。必须原地修改，只允许使用额外常数空间。以下是一些例子，输入位于左侧列，其相应输出位于右侧列。

```
1,2,3` → `1,3,2`
`3,2,1` → `1,2,3`
`1,1,5` → `1,5,1
```

Answer:

```python
#1 从后往前数，找到第一个下降的数字，例如1 2 3 5 4中第一个下降的数字是3，记为tar1
#2 前后调换tar1后面数字的顺序
#3 找到调换之后的数字，从前往后数，第一个比tar1大的数字tar2
#4 调换tar1和tar2

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer = len(nums) -2
        while pointer >= 0 and  nums[pointer] >= nums[pointer+1]:
            pointer = pointer -1
        
        print(pointer)
            
        p1 = pointer+1
        p2 = len(nums)-1
        while p1 < p2:
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1 += 1
            p2 -= 1
        
        for i in range(pointer+1,len(nums)):
            if nums[i] > nums[pointer]:
                temp = nums[pointer]
                nums[pointer] = nums[i]
                nums[i] = temp
                break
```



### [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

题目解释：

给定一个只包含 `'('` 和 `')'` 的字符串，找出最长的包含有效括号的子串的长度。

**示例**

```
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
```

```
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
```



正确解答：动态规划

```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 获取字符串的长度
        length = len(s)
        if length == 0 or length == 1:
            return 0
        # DP容器，长度为length
        DP = [ 0 for i in range(length)]
        # 从前往后找
        for i in range(1,length):
            # 如果当前为后括号
            if s[i] == ")":
                # 并且上一个是前括号，则连续两个为()
                if s[i-1] == "(":
                    if i >= 2:
                        DP[i] = DP[i - 2] + 2
                    else:
                        DP[i] = 2
                # 如果前一个不是前括号，但是中间是完整的括号，例如(())
                elif i - DP[i - 1] > 0 and s[i - DP[i - 1] - 1] == "(":
                    if (i - DP[i - 1]) >= 2:
                        DP[i] = DP[i-1] + DP[i - DP[i-1] -2] + 2
                    else:
                        DP[i] = DP[i-1] + 2
        return max(DP)
```



### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 你的算法时间复杂度必须是 O(log n) 级别。 如果数组中不存在目标值，返回 [-1, -1]。

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
```

Answer:

```python
#使用两次二分查找
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 两次二分查找使用一个函数来表示 改造
        
        #用两次二分查找
        
        length = len(nums)
        if length == 0:
            return [-1,-1]
        
        first_pos = 0
        second_pos = 0
        
        left = 0
        right = len(nums)-1
        #find first position
        while left < right-1:
            mid = (left + right)/2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            first_pos = left
        if nums[left] != target and nums[right] == target:
            first_pos = right
        if nums[left] != target and nums[right] != target:
            first_pos = -1
            
        left = 0
        right = len(nums)-1
        #find first position
        while left < right-1:
            mid = (left + right)/2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            second_pos = right
        if nums[right] != target and nums[left] == target:
            second_pos = left
        if nums[right] != target and nums[left] != target:
            second_pos = -1
        return [first_pos,second_pos]
```



### [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        # 如果比第一个小，或者比最后一个大，就返回错误
        if target < nums[0]:
            return 0
        if target > nums[length-1]:
            return length
        # 从头到尾查找
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            if nums[i] == target:
                return i
```



### [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

```
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
```

Answer

```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 对于横竖和小区域，都设置一个数组来记录
        row = [set() for i in range(9)]
        column = [set() for i in range(9)]
        grid = [set() for i in range(9)]
        
        # 如果横竖和小区域的数组中没有重复，就可以，否则返回错误
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in column[c]:
                    return False
                g = r / 3 * 3 + c / 3
                if board[r][c] in grid[g]:
                    return False
                row[r].add(board[r][c])
                column[c].add(board[r][c])
                grid[g].add(board[r][c])
        return True
```



### [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/)

编写一个程序，通过已填充的空格来解决数独问题。

```python
from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet    
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()
```



### [38. 外观数列](https://leetcode-cn.com/problems/count-and-say/)

```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 先把前几种特殊的情况列出来
        if n == 0:
            return "1"
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
        if n == 4:
            return "1211"
        if n == 5:
            return "111221"
        # 当前是n为5的时候的情况
        temp = [1,1,1,2,2,1]
        # 从5往后考虑
        for loop in range(5,n):
            length = len(temp)
            temp.append(0)
            i = 0
            temp2 = []
            for j in range(1,length+1):
                if temp[j] != temp[i]:
                    temp2.append(j-i)
                    temp2.append(temp[i])
                    i = j
            temp = temp2
        # 将结果转换为字符串
        out = "".join(str(i) for i in temp)
        return out
```



### [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

**说明：**

- 所有数字（包括 `target`）都是正整数。
- 解集不能包含重复的组合。 

**示例 1：**

```
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
```

**示例 2：**

```
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

Answer:

```python
#递归
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 寻常递归，没有特别之处
        result = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                result.append([candidates[i]])
            tar = target - candidates[i]
            now = [candidates[i]]
            result = self.find(candidates, tar, result, now)
        
        return result
        
        
    def find(self, candidates, tar, result, now):
        for i in range(len(candidates)):
            if candidates[i] > tar:
                continue
            elif candidates[i] == tar:
                now.append(candidates[i])
                if sorted(now) not in result:
                    result.append(list(sorted(now)))
                del now[-1]
            else:
                temp = tar
                tar = tar - candidates[i]
                now.append(candidates[i])
                result = self.find(candidates, tar, result, now)
                del now[-1]
                tar = temp
        return result
```



### [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。candidates 中的每个数字在每个组合中只能使用一次。

**说明：**

- 所有数字（包括目标数）都是正整数。
- 解集不能包含重复的组合。

**示例 1:**

```
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

Answer:

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 寻常递归
        
        result = []
        now = []
        index = 0
        for i in range(len(candidates)):
            if candidates[i] == target:
                result.append([candidates[i]])
            elif candidates[i] > target:
                continue
            else:
                temp = target
                target = target - candidates[i]
                now.append(candidates[i])
                result = self.dfs(candidates,target,i+1,now,result)
                now.pop()
                target = temp
        
        new = []
        for item in result:
            item.sort()
            if item not in new:
                new.append(item)
        return new
    
    def dfs(self,candidates,target,index,now,result):
        if index > len(candidates)-1:
            return result
        
        for i in range(index,len(candidates)):
            print(candidates[i])
            print(target)
            if candidates[i] == target:
                now.append(candidates[i])
                result.append(list(now))
                now.pop()
            elif candidates[i] > target:
                continue
            else:
                temp = target
                target = target - candidates[i]
                now.append(candidates[i])
                
                result = self.dfs(candidates,target,i+1,now,result)
                
                now.pop()
                target = temp
        return result
```



### [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 得到数组的长度
        n = len(nums)
        # 循环数组中的所有的数字
        for i in range(n):
            # 如果数字在长度范围之内，并且当前数字的应该在的位置上面的数字和当前数字不同
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交换
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # 对于交换完成之后的数组
        # 所有的数字都在它应该在的位置上面
        # 只要从前往后找，找到的一个数字和位置不匹配的就是结果
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```



### [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

给定 *n* 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

**示例:**

```
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
```

Answer:

```python
"""
暴力方法：
时间复杂度：O(n*2)
空间复杂度：O(1)

对于每个位置，向左查找到最高的点，记录为left_max。向右查找到最高的点，记录为right_max。然后获取left_max和right_max的最小值为now_height。用now_height和当前高度做差得倒now_depth。求和所有的now_depth得到result。
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        length = len(height)
        for index in range(length):
          	left_index = index-1
            right_index = index+1
            left_max = height[index]
            right_max = height[index]
            while left_index > -1:
              	left_max = max(left_max, height[left_index])
                left_index -= 1
            while right_index < length:
              	right_max = max(right_max, height[right_index])
                right_index += 1
            depth = min(left_max, right_max) - heigth[index]
            result += depth
        return result
            
#方法超时
```

```python
"""方法二
先获得每个位置上，往左和往右的最大值。
然后循环所有的位置，得到装水的量

空间复杂度O(n)
时间复杂度O(n)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 得到每个位置上面，往右走的最大的值
        def get_left_max(height, length):
            result = []
            now_max = 0
            for index in range(length):
                now_max = max(now_max, height[index])
                result.append(now_max)
            return result
        # 得到每个位置上面，往左走的最大的值
        def get_right_max(height, length):
            result = [0 for i in range(length)]
            now_max = 0
            for index in range(length-1,-1,-1):
                now_max = max(now_max, height[index])
                result[index] = now_max
            return result

        
        result = 0
        length = len(height)

        left_max_list = get_left_max(height, length)
        right_max_list = get_right_max(height, length)
        # 针对于每个位置，能够容纳的深度是往左和往右的较小值
        for i in range(length):
            now_left = left_max_list[i]
            now_right = right_max_list[i]
            now_depth = min(now_left, now_right)
            result += (now_depth - height[i])
        return result
```



### [44. 通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/)

给定一个字符串 (`s`) 和一个字符模式 (`p`) ，实现一个支持 `'?'` 和 `'*'` 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。

```
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
```

```
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```

```
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
```



Answer:

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 获得要匹配的字符和模式的长度
        m, n = len(s), len(p)
        
        # 构建DP二维数组，代表到输入字符串的第几位为止，和到模式字符串的第几位为止能否匹配上
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # 循环模式字符串中的字符，如果为*，说明到哪个可以匹配上
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前循环到的值为*
                if p[j - 1] == '*':
                    #*为空，或者*匹配上所有的都行
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                # 如果不是* 则需要当前为？或当前刚好匹配上
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]
```



### [45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)

给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

```
输入: [2,3,1,1,4]
输出: 2
```

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = 0
        maxPosition = 0
        steps = 0
        length = len(nums)
        
        for i in range(length-1):
            # 得到下一步能去到最远的地方
            maxPosition = max(maxPosition, nums[i]+i)
            # 如果当前一步走完
            if i == end:
                # 得到下一步的终点
                end = maxPosition
                # 走下一步
                steps += 1
        return steps
```



### [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)

给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。

**示例 1:**

```
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
```

**示例 2:**

```
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
```

**Answer:**

```python
#动态规划
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 得到数组的长度
        length = len(nums)
        # 如果就只有一个数字，就肯定可以到达
        if length == 1:
            return True
        # 声明最大的位置的变量
        max_pos = 0
        # 从前往后遍历位置
        for i in range(length-1):
            # 如果当前位置比最远到达的位置远
            if max_pos < i:
                break
            # 更新最远能到达的位置
            max_pos = max((i + nums[i]),max_pos)
            # 如果能到最后一位
            if max_pos >= (length-1):
                return True
        return False
```



### [46. 全排列](https://leetcode-cn.com/problems/permutations/)

给定一个 **没有重复** 数字的序列，返回其所有可能的全排列。

**示例:**

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

Answer:

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 特殊情况
        if nums == None:
            return []
        if nums == []:
            return [[]]
        # 输出的结果变量
        result = []
        # 当前集合
        now = []
        # 输入数组的总长度
        length = len(nums)
        # 递归函数
        result = self.dfs(nums,result,now,length)
        return result
    
    def dfs(self, nums, result, now, length):
        # 如果当前的长度就是总长度，说明都用上了
        if len(now) == length:
            # 在结果集合中加入
            result.append(list(now))
            # 返回当前
            return result
        for i in range(len(nums)):
            # 循环加入集合
            now.append(nums[i])
            # 将除去当前的集合传入下个递归周期
            result = self.dfs(nums[:i]+nums[i+1:], result, now, length)
            now.pop()
        return result
```



### [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

给定一个可包含重复数字的序列，返回所有不重复的全排列。

**示例:**

```
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

Answer:

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        now = []
        def findHelper(nums,now):
            if len(nums) == 0:
                result.append(list(now))
                return 
            used = []
            for i in range(len(nums)):
                # 当这个数字已经在这一轮被使用过了
                if nums[i] in used:
                    continue
                else:
                    # 当前数组加入这个数组
                    now.append(nums[i])
                    # 下一轮递归
                    findHelper(nums[:i]+nums[i+1:],now)
                    # 撤销加入
                    now.pop()
                    # 把使用过的这个数字加入到used数组中
                    used.append(nums[i])
        findHelper(nums,now)
        return result
```



### [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/)

给定一个 *n* × *n* 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

**说明：**

你必须在**[原地](https://baike.baidu.com/item/原地算法)**旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要**使用另一个矩阵来旋转图像。

**示例 1:**

```
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**示例 2:**

```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

**Answer:**

```python
#原地旋转
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #获取矩阵的长和宽
        length = len(matrix[0])
        #四个数字为一组，转一次
        for r in range((length+1) / 2):
            for c in range(length / 2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[length - c -1][r]
                matrix[length - c -1][r] = matrix[length - r -1][length - c -1] 
                matrix[length - r -1][length - c -1]  = matrix[c][length - r -1] 
                matrix[c][length - r -1] = temp
```



### [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

**示例:**

```
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**说明：**

- 所有输入均为小写字母。
- 不考虑答案输出的顺序。

**Answer:**

```python
#字典
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 等待输出的结果
        result = []
        # 字典
        check_dict = {}
        # 循环所有的元素
        for item in strs:
            sorted_list = sorted(item)
            # 转换成字符串
            sorted_str = "".join(sorted_list)
            if check_dict.get(sorted_str) == None:
                check_dict[sorted_str] = [item]
            else:
                check_dict[sorted_str].append(item)
        for value in check_dict.values():
            result.append(value)
        return result
```



### [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

```
示例 1:

输入: 2.00000, 10
输出: 1024.00000
```

```
示例 2:

输入: 2.10000, 3
输出: 9.26100
```

```
示例 3:

输入: 2.00000, -2
输出: 0.25000
```

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
        # 二分法，
        ans = 1
        temp = x
        while n != 0:
            # 如果除2之后为奇数，则还得乘上一个temp
            if n % 2 == 1:
                ans = ans * temp
            temp = temp * temp
            n = n // 2
        return ans
```



### [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先将最大值设置为第一个值
        maxs = nums[0]
        # 如果第一个值小于0，就把sum设置为0
        if nums[0] < 0:
            sums = 0
        # 否则sum为第一个值
        else:
            sums = nums[0]
        # 循环之后的位置
        for i in range(1,len(nums)):
            # 加上当前值
            sums = sums + nums[i]
            # 如果当前值比之前的最大值大
            if sums > maxs:
                maxs = sums
            # 当前和小于0
            if sums < 0:
                sums = 0 
        return maxs
```





### [54. 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

```
示例 1:
输入:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
输出: [1,2,3,6,9,8,7,4,5]
```

```
示例 2:

输入:
[[1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

```

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 特殊情况
        if len(matrix) == 0:
            return []
        # 上下左右的边界
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


### [59. 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii/)

给定一个正整数 *n*，生成一个包含 1 到 *n*2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

```python
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

```python
import numpy as np
class Solution(object):
    """
    在54. 螺旋矩阵的基础之上，由查找改成填写
    """
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n == 0:
            return []
        
        left = 0
        right = n-1
        top = 0 
        bottom = n-1
        
        pad = np.zeros((n,n),dtype = int)
        
        turn = 0
        now = 1
        while left <= right and top <= bottom:
            if (turn % 4) == 0:
                for i in range(left,right+1):
                    pad[top][i] = now
                    now += 1
                turn += 1
                top += 1
                continue
            if (turn % 4) == 1:
                for i in range(top,bottom+1):
                    pad[i][right] = now
                    now += 1
                turn += 1
                right -= 1
                continue
            if (turn % 4) == 2:
                for i in range(right,left-1,-1):
                    pad[bottom][i] = now
                    now += 1
                turn += 1
                bottom -= 1
                continue
            if (turn % 4) == 3:
                for i in range(bottom,top-1,-1):
                    pad[i][left] = now
                    now += 1
                turn += 1
                left += 1
                continue
        return pad.tolist()
```



### [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

给出一个区间的集合，请合并所有重叠的区间。

**示例 1:**

```
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

**示例 2:**

```
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

**Answer：**

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先将数组根据第一个数字进行排序
        intervals.sort()
        i = 1
        # 循环所有的位置
        while i < len(intervals):
            # 如果当前区间的开始值，比上一个区间的结束值还要小
            if intervals[i][0] <= intervals[i-1][1]:
                # 如果当前区间的结束值，比上一个区间的结束值大
                if intervals[i][1] > intervals[i-1][1]:
                    # 将上一个区间的结束值，更新为当前区间的结束值
                    intervals[i-1][1] = intervals[i][1]
                    # 随后删除当前区间
                    del intervals[i]
                # 如果当前区间的结束值，比上一个区间的结束值小或者相等
                else:
                    # 随后删除当前区间
                    del intervals[i]
            else:
                i += 1
        return intervals
```



### [57. 插入区间](https://leetcode-cn.com/problems/insert-interval/)

给出一个*无重叠的 ，*按照区间起始端点排序的区间列表。在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

```
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
```

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 初始状况判断
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        # 已经是起点有序的了
        # 找到要开始插入的位置
        i = 0
        intervalsLen = len(intervals)
        while i < intervalsLen and intervals[i][1] < newInterval[0]:
            i += 1
        # 保存删除之前的位置，最后在这个位置上插入
        tempI = i
        while i < intervalsLen and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        else:
            # 删除被代替的区间
            del intervals[tempI:i]
            # 在相应的位置上面插入新的区间
            intervals.insert(tempI, newInterval)
        return intervals

```



### [58. 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。如果不存在最后一个单词，请返回 0 。说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

```
输入: "Hello World"
输出: 5
```



```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        count = 0
        for ch in s:
            # 如果遇到了空格，重置计数器
            if ch == " ":
                count = 0
            # 否则，计数器加一
            else:
                count += 1
        return count
```



### [60. 第k个排列](https://leetcode-cn.com/problems/permutation-sequence/)

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123""132""213""231""312""321" 给定 n 和 k，返回第 k 个排列。

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 先创建出初始的数组
        List = [i for i in range(1,n+1)]
        
        # 阶乘，得到每一层是有多少个
        count_list = [1]
        count = 1
        for i in range(2,n):
            count *= i 
            count_list.append(count)
        
        # 要输出的变量
        result = ""
        
        # 根据要输出的是第几个结果K，来一步步找到要输出的数字
        while k != 0 or len(List) > 0:
            # 如果当前层结果为0，则说明从这一层开始都只要输出最后一个数字就行
            if k == 0:
                result += str(List[-1])
                del List[-1]
            # 如果当前层不是0，则要找到当前层应该输出的数字是什么
            else:
                # 计算出当前层要输出的数字的index和下一层的序号next_
                divider = count_list.pop()
                index = k / divider
                next_ = k % divider
                # 如果下一层的序号不是0
                if next_ > 0:
                    # 将当前层的结果直接输出
                    result += str(List[index])
                    del List[index]
                    k = next_
                # 如果下一层的序号是0，则当前层的输出应该往上移动一位
                else: 
                    result += str(List[index-1])
                    del List[index-1]
                    k = next_
        return result
```





### [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

**示例 1:**

```
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
```

**示例 2:**

```
输入: m = 7, n = 3
输出: 28
```

**Answer**

```python
import numpy as np
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 创建一个m行n列的二维数组，初始值都为0
        test = np.zeros((m, n), dtype=np.int)
        # 把第一行和第一列的值设置为1
        for i in range(n):
            test[0][i] = 1
        for j in range(m):
            test[j][0] = 1
        # 针对于其他的位置，是上面位置和左边位置的数字的和
        for k in range(1,m):
            for l in range(1,n):
                test[k][l] = test[k-1][l] + test[k][l-1]
        return test[m-1][n-1]
```



### [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

Answer:

```python
import numpy as np
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 获得棋盘的长和宽
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        
        # 产生棋盘
        way = np.zeros((r+1,c+1), dtype = int)
        # 如果刚开始的时候就被堵塞住了，就为0.如果没有被堵塞住，则起始位置为1.
        if obstacleGrid[0][0] == 0:
            way[1][1] = 1
        else:
            return 0
        # 查看所有的位置
        for i in range(1,r+1):
            for j in range(1,c+1):
                # 如果是起始位置，就跳过
                if i == 1 and j == 1:
                    continue
                # 如果当前位置被堵塞住了，则这个位置不可达到，为0
                if obstacleGrid[i-1][j-1] == 1:
                    way[i][j] = 0
                # 如果当前位置没有被堵塞住，则这个位置可以被达到
                else:
                    way[i][j] = way[i-1][j] + way[i][j-1]
        return way[r][c]
```



### [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

给定一个包含非负整数的 *m* x *n* 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：**每次只能向下或者向右移动一步。

**示例:**

```python
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
```

Answer:

```python
#待重写
import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        
        # 创建新的NP数组
        way = np.zeros((r,c))
        way[0][0] = grid[0][0]
        
        # 初始化第一列和第一行
        for i in range(1,r):
            way[i][0] = grid[i][0] + way[i-1][0]
        for i in range(1,c):
            way[0][i] = grid[0][i] + way[0][i-1]
        # 开始其他位置的计算
        for i in range(1,r):
            for j in range(1,c):
                way[i][j] =  min(way[i-1][j], way[i][j-1]) + grid[i][j]
        return int(way[r-1][c-1])
```



### [65. 有效数字](https://leetcode-cn.com/problems/valid-number/)

验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。
同剑指offer 20
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


### [66. 加一](https://leetcode-cn.com/problems/plus-one/)

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。你可以假设除了整数 0 之外，这个整数不会以零开头。

EX:

```
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
```



```python
class Solution(object):
    def plusOne(self, digits):
        # 得到反序索引数组 [-1,-2,-3,-4]
        index = range(-(len(digits)),0)
        index.reverse()
        # 得到反序索引数组，从后往前循环所有的位置
        for i in index:
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
                # 如果当前位置是数组的首位，则在前面加上一个1
                if i == index[-1]:
                    result = [1]
                    result.extend(digits)
                    return result   
        return digits
```



### [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)

给你两个二进制字符串，返回它们的和（用二进制表示）。输入为 **非空** 字符串且只包含数字 `1` 和 `0`。

```
输入: a = "11", b = "1"
输出: "100"
```

```python
class Solution(object):
    def addBinary(self, a, b):
        # 从后往前一步步走，注意进位
        IndexA = len(a)-1
        IndexB = len(b)-1
        carry = 0
        result = ""
        # 一位一位相加
        while IndexA >= 0 or IndexB >= 0:
            numA = int(a[IndexA])  if IndexA >= 0 else 0
            numB = int(b[IndexB])  if IndexB >= 0 else 0
            ans = numA + numB + carry
            if ans % 2 == 0:
                result = "0" + result
            if ans % 2 == 1:
                result = "1" + result
            carry = ans / 2
            IndexA -= 1
            IndexB -= 1
        if carry == 1:
            result = "1" + result
        return result
```



### [68. 文本左右对齐](https://leetcode-cn.com/problems/text-justification/)

给定一个单词数组和一个长度 *maxWidth*，重新排版单词，使其成为每行恰好有 *maxWidth* 个字符，且左右两端对齐的文本。

```
输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

```python
class Solution:
    def process(self, curLen, curWords, maxWidth):
        # 空格数量
        num_space = maxWidth - curLen
        # 如果只有一个单词就没必要考虑分配，直接填充空格即可
        if len(curWords) == 1:
            return curWords[0] + ' ' * (maxWidth - curLen)
        # 每个空隙分到的空格数量
        num_sep = num_space // (len(curWords) - 1)
        # 分到空格数量多一个的空隙
        head_sep = num_space % (len(curWords) - 1)
        cur = ''
        # 分配
        for i in range(len(curWords) - 1):
            cur = cur + curWords[i] + (' ' * (num_sep + 1) if i < head_sep else ' ' * num_sep)
        # 分配结束之后把最后一个单词连上
        cur = cur + curWords[-1]
        return cur
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        curLen, curWords = 0, []
        
        for w in words:
            # 切分判断的条件，单词长度加上基本的空格长度
            if curLen + len(w) + len(curWords) <= maxWidth:
                curLen += len(w)
                curWords.append(w)
            else:
                ret.append(self.process(curLen, curWords, maxWidth))
                curLen, curWords = len(w), [w]
                
        # 剩下没有安排的就是最后一行，按照最后一行靠左处理
        if len(curWords) > 0:
            cur = ''
            for i in range(len(curWords) - 1):
                cur = cur + curWords[i] + ' '
            cur = cur + curWords[-1]
            cur += ' ' * (maxWidth - len(cur))
            ret.append(cur)
        return ret
```



### [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

实现 int sqrt(int x) 函数。计算并返回 x 的平方根，其中 x 是非负整数。由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

```python
class Solution(object):
    def mySqrt(self, x):
        # 特殊情况
        if x == 0:
            return 0
        if x == 1:
            return 1
        # 初始化当前的范围
        left = 0
        right = x
        # 递归，二分查找
        result = self.find(x, left, right)
        return result
    
    # 递归，二分查找
    def find(self, x, left, right):
        if left == right -1 and left * left <= x and right * right > x:
            return left
        mid = (left + right) / 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid
            result = self.find(x, left, right)
        if mid * mid > x:
            right = mid
            result = self.find(x, left, right)
        return result
```





### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划最基本题目
        #特殊情况
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 动态规划
        step = [0] * n
        step[0] = 1
        step[1] = 2
        for i in range(2,n):
            step[i] = step[i-1] + step[i-2]
        return step[-1]
        
```

同 剑指offer-10



### [71. 简化文件路径](https://leetcode-cn.com/problems/simplify-path/)

以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

```
输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
```

```
输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
```

```
输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
```





Answer:

```python

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 根据/将输入的进行分割
        path_list = path.split('/')
        delete_num = 0
        result_list = []
        # 对分割之后的数组进行操作
        while len(path_list) > 0:
            # 如果数组的最后一个是“。。”，删掉
            if path_list[-1] == "..":
                delete_num += 1
                del path_list[-1]
                continue
            # 如果是“。”或者“”，删掉
            if path_list[-1] == "." or path_list[-1] == "" :
                del path_list[-1]
                continue
            
            else:
                # 如果当前要往前滚
                if delete_num > 0:
                    delete_num -= 1
                    del path_list[-1]
                # 否则就将结果加入到新数组
                else:
                    result_list.append(path_list[-1])
                    del path_list[-1]
        result = "/"
        # 如果新数组中没有
        if len(result_list) == 0:
            return result
        # 如果新数组中有东西，就一哥哥加入
        while len(result_list) > 0:
            result = result + result_list[-1] + "/"
            del result_list[-1]
        result = result.rstrip("/")
        return result
```





### [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

**示例 1：**

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

**Answer:**

```python
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        
        # 有一个字符串为空串
        if n * m == 0:
            return n + m
        
        # DP 数组
        D = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j
        
        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)
        
        return D[n][m]
```



### [73. 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes/)

给定一个 *m* x *n* 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用**[原地](http://baike.baidu.com/item/原地算法)**算法**。**

```
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

Answer:

```python
class Solution(object):
    def setZeroes(self, matrix):
        """ 将矩阵中存在 0 的那一行和那一列设置为 0
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # 获取矩阵的额行数和列数
        m = len(matrix)
        n = len(matrix[0])
        
        # 如果行数或者列数为0，直接返回原矩阵
        if m == 0:
            return matrix

        if n == 0:
            return matrix
        
        # 新建两个数组 m_list n_list，用来记录这一行或者这一列是否存在0
        m_list = [0] * m
        n_list = [0] * n
        
        # 循环矩阵的所有的位置，如果找到了 0，就将相应的数组的位置上记录为1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m_list[i] = 1
                    n_list[j] = 1

        # 循环数组的所有的位置，如果这个位置上为1，这一行或者一列全部设置为0
        for Mindex in range(m):
            if m_list[Mindex] == 1:
                for i in range(n):
                    matrix[Mindex][i] = 0
        for Nindex in range(n):
            if n_list[Nindex] == 1:
                for i in range(m):
                    matrix[i][Nindex] = 0
        
        return matrix
```



### [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：每行中的整数从左到右按升序排列。每行的第一个整数大于前一行的最后一个整数。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """ 查找矩阵中的目标数字的位置 使用两个二分查找
            分别查找目标数字的行和列
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 特殊情况，直接返回 false
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        # 得到数组的行数和列数
        row_num = len(matrix)
        column_num = len(matrix[0])

        # 寻找目标数字所在的行，使用二分查找的方法
        left = 0
        right = row_num - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                right = mid
            if target > matrix[mid][0]:
                left = mid

        if matrix[left][0] == target or matrix[right][0] == target:
            return True
        if matrix[left][0] < target < matrix[right][0]:
            row = left
        if matrix[right][0] < target:
            row = right

        # 寻找目标数字所在的列，使用二分查找的方法
        left = 0
        right = column_num - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                right = mid
            if target > matrix[row][mid]:
                left = mid

        # 如果最后找到了，就返回 true
        if matrix[row][left] == target or matrix[row][right] == target:
            return True
        else:
            return False
```







### [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/)

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，**原地**对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

```
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
```

进阶：

* 一个直观的解决方案是使用计数排序的两趟扫描算法。
  首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
* 你能想出一个仅使用常数空间的一趟扫描算法吗？

Answer:

```python
class Solution:
    def sortColors(self, nums) -> None:
        """
        使用两次遍历 一次遍历将数字0放在数组的头部 第二次遍历将数组1放在0的后面
        :param nums: 
        """
        # 获取数组的长度
        n = len(nums)
        # 指针
        ptr = 0
        # 一次遍历将数字0放在数组的头部
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        # 第二次遍历将数组1放在0的后面
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
```



### [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

**示例：**

```
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
```

**说明：**

- 如果 S 中不存这样的子串，则返回空字符串 `""`。
- 如果 S 中存在这样的子串，我们保证它是唯一的答案。

```
输入：
"a"
"aa"

预计输出：
""

说明，当target字符串中有重复的字符的时候，需要把重复的字符都出现在s的子串中
```



**Answer:**

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # 创建一个字典，用来存储 t 中出现过的字符
        # 字典的默认值为 1
        Dict = {}
        for i in range(len(t)):
            # 如果这个字符之前没有被记录在 dict 中
            if Dict.get(t[i]) is None:
                Dict[t[i]] = 1
            # 如果已经出现过了，就+1
            else:
                Dict[t[i]] += 1

        def check_dict():
            """
            检查字典中所有的值是否都为0
            用来判断是否t中的字符都出现过
            :return: result boolean
            """
            result = True
            for v in Dict.values():
                if v > 0:
                    result = False
                    break
            return result

        # 获取字符串s的长度
        lenS = len(s)

        # 创建两个指针用于滑动窗口
        left_index = 0
        right_index = 0

        # 当前的窗口内部的字符串
        window = ""

        # 记录符合条件的最小的字符串，及长度
        minStr = ""
        minLen = float('inf')

        # 使用滑动窗口进行查找
        while right_index < lenS:
            # 将 s[right_index] 加入到窗口
            window += s[right_index]

            # 并且修改字典中的值
            # 如果 s[right_index] 在字典中，就把相应的值-1
            if Dict.get(s[right_index]) is not None:
                Dict[s[right_index]] -= 1

                # 如果 t 中的所有的字符都出现在了当前window中
                while check_dict():
                    # 如果当前的 window 中的字符的数目小于之前最小的字符的数目
                    # 更新最短字符串和长度
                    if len(window) < minLen:
                        minLen = len(window)
                        minStr = window

                    # 窗口的左边界往右移动一位
                    left_index += 1
                    if Dict.get(window[0]) is not None:
                        Dict[window[0]] += 1
                    window = window[1:]

            # 如果 s[right_index] 不在字典中 就不管

            # 窗口的右边界向右移动一位
            right_index += 1
        return minStr
```



### [77. 1 ... *n* 中所有可能的 *k* 个数的组合](https://leetcode-cn.com/problems/combinations/)

给定两个整数 *n* 和 *k*，返回 1 ... *n* 中所有可能的 *k* 个数的组合。

```
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```



```python
class Solution:
    def combine(self, n: int, k: int):
        def backtrack(first=1, curr=[]):
            """
            递归函数
            :param first: 默认值为1
            :param curr: 默认值是一个空的数组
            """
            # 如果当前数组中已经有了 k 个数字
            # 向结果数组中添加当前值
            if len(curr) == k:
                output.append(curr[:])
            # 从当前值，循环到 n
            for i in range(first, n + 1):
                # 加入到当前数组中
                curr.append(i)
                # 进入下一轮递归
                backtrack(i + 1, curr)
                # 回退
                curr.pop()

        output = []
        backtrack()
        return output
```



### [78. 子集](https://leetcode-cn.com/problems/subsets/)

给定一组**不含重复元素**的整数数组 *nums*，返回该数组所有可能的子集（幂集）。

**说明：**解集不能包含重复的子集。

**示例:**

```
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

**Answer:**

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 结果变量
        result = []

        def dfs(lis=nums, curr=[]):
            """
            递归函数
            :param lis: 默认值为 nums， 备选数字的数组
            :param curr: 默认值为空数组， 当前存储的数字的数组
            :return: 
            """
            # 将当前数组加入到结果数组中
            result.append(curr[:])
            # 循环备选数组的索引
            for i in range(len(lis)):
                # 加入当前数组
                curr.append(lis[i])
                # 下一轮
                dfs(lis[i + 1:], curr)
                # 回退
                curr.pop()
            return

        dfs()
        return result
```



### [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)

给定一个可能包含重复元素的整数数组 ***nums***，返回该数组所有可能的子集（幂集）。**说明：**解集不能包含重复的子集。

```python
输入: [1,2,2]
输出:
[[2],[1],[1,2,2],[2,2],[1,2],[]]
```

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先对输入的数组进行排序 保证相同的数字会在一起
        nums.sort()

        result = []

        def dfs(lis, current):
            # 将当前数组加入到结果中
            result.append(current[:])

            # 声明一个数组来记录前一个数字
            before = None

            # 循环备选数组中的所有的位置
            for i in range(len(lis)):
                # 如果当前的数组和前一个数字相同
                # 跳过
                if before == lis[i]:
                    continue
                # 加入当前数组，下一轮递归和回退
                current.append(lis[i])
                dfs(lis[i+1:], current)
                current.pop()
                # 更显前一个数字
                before = lis[i]
            # 当循环完成，返回
            return
        dfs(nums, [])
        return result
```



### [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

```
示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
```



```python
class Solution(object):
    def exist(self, board, word):
        """ 判断单词是否在二维数组中存在
        :type board: List[List[str]] 二维数组一个
        :type word: str 要查找的单词
        :rtype: bool 返回的结果
        """
        # 获得矩阵的额列数和行数
        row = len(board)
        column = len(board[0])

        # 如果列数或者行数为0，返回 false
        if row == 0:
            return False
        if column == 0:
            return False

        # 根据矩阵的列数和行数创建一个新的布尔二维数组
        # 新的二维数组的列数和行数和原有的一样
        # 默认所有的值都是 false
        visited = [[False for i in range(column)] for j in range(row)]

        # 循环 broad 二维数组的所有的位置
        # 进行递归查找
        for i in range(row):
            for j in range(column):
                if self.dfs(word, board, i, j, row, column, visited):
                    return True

        return False

    def dfs(self, word, board, i, j, row, column, visited):
        # 如果所有的字母都找到了，true
        if word == "":
            return True
        # 如果越界
        if i < 0 or i >= row or j < 0 or j >= column:
            return False
        # 如果当前字母匹配上了
        if board[i][j] == word[0] and not visited[i][j]:
            # 先在相应的位置上标记为 true
            visited[i][j] = True
            # 递归下一轮，上下左右
            if self.dfs(word[1:], board, i - 1, j, row, column, visited) or self.dfs(word[1:], board, i + 1, j, row,
                                                                                     column, visited) or self.dfs(
                word[1:], board, i, j - 1, row, column, visited) or self.dfs(word[1:], board, i, j + 1, row, column,
                                                                             visited):
                return True
            # 回退 visited 数组
            visited[i][j] = False
        return False
```

同 剑指offer 12



### [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例：

```
输入: [2,1,5,6,2,3]
输出: 10
```

**Answer：**

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈
        # 里面记录的是单调递增的元素的索引
        stack = []

        # 用来记录最大的矩阵的面积
        square = 0

        # 往数组中最后添加上一个0，使得能够处理最后一个值
        heights = heights + [0]

        # 遍历所有的位置，包括值和索引
        for index, height in enumerate(heights):
            # 当单调栈中有值并且当前循环到的值比单调栈的最后一个值小
            # 这就意味着 如果要维持单调栈 就必须要进行出栈和入栈的操作
            while stack and heights[stack[-1]] > height:
                # 先从单调栈中推出一个顶层元素
                poped = stack.pop()
                # 推出了一个元素之后的单调栈的顶层 他的index就是当前区间的左边界
                left = stack[-1] if stack else -1
                # 得到区间的宽度
                width = index - left - 1
                # 区间的高度
                high = heights[poped]
                # 计算面积并且更新
                square = max(high * width, square)
            # 向但到站中加入到新的
            stack.append(index)
        return square
```



### [85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

**示例:**

```
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
```

Answer:

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # 特殊情况
        if len(matrix) == 0:
            return 0
        
        # 创建一个数组 记录到当前层数为止 累计的高度
        height = [0] * len(matrix[0])
        
        # 创建一个变量来存储最大的面积
        max_square = 0
        
        # 循环矩阵的每行
        for row in matrix:
            # 循环每列
            for i in range(len(row)):
                # 如果当前值为1 则在 height 数组中+1
                if row[i] == "1":
                    height[i] = height[i] + 1
                # 否则 设置这个位置为 0
                else:
                    height[i] = 0
            # 记录完这一层 调用 findMax
            max_square = self.findMax(max_square, height)
        
        # 返回最大值
        return max_square

    def findMax(self, max_square, height):
        """
        这个函数基本上等同于 84 计算矩阵中最大的矩形
        也是采用的 单调栈 的方法
        :param max_square:
        :param height:
        :return:
        """
        square = 0
        stack = []
        for index, h in enumerate(height + [-1]):
            while stack and h < height[stack[-1]]:
                poped = stack.pop()
                left = stack[-1] if stack else -1
                width = index - left - 1
                high = height[poped]
                square = max(square, width * high)
            stack.append(index)
        return max(max_square, square)
```



### [89. 格雷编码](https://leetcode-cn.com/problems/gray-code/)

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。格雷编码序列必须以 0 开头。

Example：

```
输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
```



Example 2:

```
输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。
```



```python
class Solution(object):    
    def grayCode(self, n):
        # 将数字和它向右移动一位的数字进行 or 运算 得到的结果就是 格雷码
        return [i ^ (i >> 1) for i in range(1 << n)]
```



### [91. 数字字符解码方法](https://leetcode-cn.com/problems/decode-ways/)

一条包含字母 `A-Z` 的消息通过以下方式进行了编码：

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

给定一个只包含数字的**非空**字符串，请计算解码方法的总数。

Example：

```
输入："12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
```

```
输入："226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
```

```
输入：s = "0"
输出：0
```

```python
class Solution(object):
    def numDecodings(self, s):
        # 如果输入的字符的长度为1
        if len(s) == 1:
            # 并且输入的为0 就无法编码为任何字符
            if int(s) == 0:
                return 0
            # 否则就只能编码为一个字符
            else:
                return 1
        # 如果第一个数字为0，则也不能编码为任何字符
        if s[0] == "0":
            return 0

        #
        dp = [1, 1]

        # 从第三个数字开始看
        for i in range(2, len(s) + 1):
            # 如果前两个数字大于10，并且又小于26，并且不是整十数
            # 则这两个数字能拆成两个进行编码
            # 例如 25 可以编码成 一个 25 或者 2， 5
            # 就是前两个数字时 和 前一个数字时候的两个情况之和
            if 10 < int(s[i - 2:i]) <= 26 and s[i - 1] != "0":
                dp.append(dp[i - 1] + dp[i - 2])
            # 如果前两位是 10 或者 20 则只能把这两个作为一个整体
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:
                dp.append(dp[i - 2])
            # 是个位数 就只能这个数字作为一个整体
            elif s[i - 1] != "0":
                dp.append(dp[i - 1])
            # 如果又是个位数 又是0
            else:
                return 0

        return dp[-1]
```



### [93. 复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/)



给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

```
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
```

```
输入：s = "0000"
输出：["0.0.0.0"]
```

```
输入：s = "1111"
输出：["1.1.1.1"]
```

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        # 存储结果的数组 数组中的是能够组成的 ip 地址对应的字符串
        result = []

        # 用于记录当前处于第几个 block 的变量
        # 一个 ip 地址有四个 block
        block = 0

        # 当前字符串
        now_str = ""

        def dfs(s, block, now_str):
            # 递归终止条件 如果当前为第四个 block
            if block == 4:
                # 并且没有需要填入的字符
                if len(s) == 0:
                    result.append(now_str[1:])
                return

            # 在当前 block ，取1，2，3个数字
            for i in range(1, 4):
                # 如果还有剩余的数字可以取
                if i <= len(s):
                    # 在1-255范围内都可以取 进入下一层递归
                    if int(s[:i]) <= 255:
                        dfs(s[i:], block + 1, now_str + "." + s[:i])
                    # 如果首位数字为0 则不能取
                    if s[0] == '0':
                        break
                else:
                    break
        # 调用递归函数
        dfs(s, block, now_str)
        return result
```



### [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)

给定一个字符串 **S** 和一个字符串 **T**，计算在 **S** 的子序列中 **T** 出现的个数。一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

```
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```

```
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```



```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # n1 为s字符串的长度
        # n2 为t字符串的长度
        n1 = len(s)
        n2 = len(t)
        # 声明DP数组，行列数目为 n1+1 和 n2+1 所有的位置上面的初始数字都是0
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]

        # 将第一行的都设置为1
        for j in range(n1 + 1):
            dp[0][j] = 1

        """
        介绍一个矩阵的每个位置上的含义
        dp[2,3] = 表示字符串S[0:3]的子串为t[0:2]有几种方式
        """
        # 从第二行开始
        for i in range(1, n2 + 1):
            # 从每一行的一号位置上开始
            for j in range(1, n1 + 1):
                # 判断递归函数
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]
```



### [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。

```
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```



```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 咱先把前几行生成了
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        if numRows == 3:
            return [[1],[1,1],[1,2,1]]
        
        # 前三行的状态
        now = [[1],[1,1],[1,2,1]]
        for i in range(3,numRows):
            # 左右两边的数字肯定是1
            # 然后计算出中间的数组
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(now[i-1][j-1]+now[i-1][j])
            now.append(temp)
        return now
```



### [119. 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/)

给定一个非负索引 *k*，其中 *k* ≤ 33，返回杨辉三角的第 *k* 行。

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        方式方法和115 是一样的 就是输出的内容不一样 115是把整个三角形都输出出来
        118 只输出目的的一行
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        now = [[1],[1,1],[1,2,1]]
        for i in range(3,rowIndex+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(now[i-1][j-1]+now[i-1][j])
            now.append(temp)
        return now[rowIndex]
```



### [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
```



```python
import numpy as np
class Solution(object):
    def minimumTotal(self, triangle):
        """
        主要的思路是，在三角形的每一行的每一个位置上
        计算出到这个位置为止，最短的路径需要走多少步
        最后得到最后一行的最小值
        :param triangle:
        :return:
        """
        length = len(triangle)
        temp = np.zeros((length,length),dtype = int)
        for i in range(length):
            for j in range(i+1):
                if i == 0 and j == 0:
                    temp[i][j] = triangle[0][0]
                elif j == 0:
                    temp[i][j] = temp[i-1][j] + triangle[i][j]
                elif j == i:
                    temp[i][j] = temp[i-1][j-1] + triangle[i][j]
                else:
                    temp[i][j] = min(temp[i-1][j-1], temp[i-1][j]) + triangle[i][j]
        return min(list(temp[length-1]))
```



### [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```



```python
class Solution(object):
    def maxProfit(self, prices):
        """
        主要的过程是从前往后遍历数组
        然后在遍历的过程中，用一个变量记录之前的最小的数字
        然后计算出到当前位置卖出能获得的利润
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



### [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

给定一个数组，它的第 *i* 个元素是一支给定股票第 *i* 天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

```
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

```

```
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```



```python
class Solution(object):
    def maxProfit(self, prices):
        """
        122 和 121 的区别在于 122 允许进行多次交易
        我们还是采取从前往后遍历数组的方式
        并且也是记录一个到目前为止最低价格
        当我们遇到价格下降的时候，就进行一次交易，并且把最低价格更新为当前价格
        如果刚开始一直在下降，就只用更新价格
        如果价格在上升，就往后走
        最后记录交易的总收入
        :type prices: List[int]
        :rtype: int
        """
        p1 = 0
        gain = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                gain += (prices[i-1] - prices[p1])
                p1 = i
            elif i == len(prices) -1:
                gain += (prices[i] - prices[p1])
        return gain
```



### [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

1. 每次转换只能改变一个字母。
2. 转换过程中的中间单词必须是字典中的单词。

```python
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set([])
        for word in wordList:  #将wordList中的word加入WordSet
            wordSet.add(word)  

        wordLen = len(beginWord)
        queue = collections.deque([(beginWord, 1)])  
        while queue:    						#bfs
            currWord, currLen = queue.popleft()
            if currWord == endWord:
                return currLen
            for i in xrange(wordLen):
                part1 = currWord[:i]    #取出当前单词左部分
                part2 = currWord[i+1:]  #取出当前单词右部分
                for j in 'abcdefghijklmnopqrstuvwxyz':   #枚举替换字母
                    if currWord[i] != j:
                        nextWord = part1 + j + part2     #构成新单词
                        if nextWord in wordSet:			#如果新单词在Set中
                            queue.append((nextWord, currLen + 1))	#加入队列，继续搜索
                            wordSet.remove(nextWord)
        return 0
```






### [128. 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)

给定一个未排序的整数数组，找出最长连续序列的长度。要求算法的时间复杂度为 *O(n)*。

**示例:**

```
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**Answer:**

```python
"""
第二种 哈希表
时间复杂度：O(n)
算法描述：
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_list_length = 0
        #数组去重
        deduplicated_set = set(nums)
        #循环所欲的数组中的数字
        for num in deduplicated_set:
            now_list_length = 0
            temp_num = num
            #如果之前的一个数字在hashset中，则跳过
            if num-1 in deduplicated_set:
                continue
            #如果之前的一个数字不在hashset中
            else:
              	#一直往后面找，直到最后。然后更新最长长度。
                while temp_num in deduplicated_set:
                    now_list_length += 1
                    temp_num += 1
                longest_list_length = max(longest_list_length, now_list_length)
        return longest_list_length

```



### [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

给定一个二维的矩阵，包含 `'X'` 和 `'O'`（**字母 O**）。找到所有被 `'X'` 围绕的区域，并将这些区域里所有的 `'O'` 用 `'X'` 填充。

```
X X X X
X O O X
X X O X
X O X X
-->
X X X X
X X X X
X X X X
X O X X
```



```python
class Solution(object):
  	def solve(self, board):
        """
        我们矩阵中有三种元素：X，被X包围的O，没有被X包围的O
        由于边界上的O不会被填充为X。因此，我们只需要将所有的边界
        上的O以及和边界上的O相邻的O都标记上，然后将其余的O都替换为X就可以
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return

        n, m = len(board), len(board[0])
        q = [ij for k in range(max(n,m)) for ij in ((0, k), (n-1, k), (k, 0), (k, m-1))]
        while q:
            i, j = q.pop()
            if 0 <= i < n and 0 <= j < m and board[i][j] == 'O':
                board[i][j] = 'W'
                q += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'W'] for c in row] for row in board]
```



### [133. 克隆图](https://leetcode-cn.com/problems/clone-graph/)

给你无向 **[连通](https://baike.baidu.com/item/连通图/6460995?fr=aladdin)** 图中一个节点的引用，请你返回该图的 [**深拷贝**](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)（克隆）。

```python
class Solution(object):
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node
            
        nodes = self.getNodes(node)
        
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        return mapping[root]
        
    def getNodes(self, node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result
```



### [134. 加油站](https://leetcode-cn.com/problems/gas-station/)

在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)  
        if length == 0:
            return -1
        
        diff = []
        for i in xrange(length): diff.append(gas[i]-cost[i])
        
        if sum(diff) < 0:
            return -1
        
        for index in range(length):
            result = True
            now = index
            total = 0
            while now < (index + length):
                i = now % length
                total += diff[i]
                if total < 0:
                    result = False
                    break
                else:
                    now += 1
            if result:
                return index
        
        return -1
```



### [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

**示例 1：**

```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```

**示例 2：**

```
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
```

**示例 3：**

```
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

**Answer:**

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return False
        
        pd = [ False for i in range(len(s) + 1)]
        pd[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if pd[j] and s[j:i] in wordDict:
                    pd[i] = True
                    break
        return pd[-1]
```



### [146. LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)



### [150. 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

根据[ 逆波兰表示法](https://baike.baidu.com/item/逆波兰式/128437)，求表达式的值。有效的运算符包括 `+`, `-`, `*`, `/` 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

```
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
```

```python
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+': stack.append(op1 + op2)
                elif i == '-': stack.append(op1 - op2)
                elif i == '*': stack.append(op1 * op2)
                else: stack.append(int(op1 * 1.0 / op2))
        return stack[0]
```



### [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

给定一个字符串，逐个翻转字符串中的每个单词。

```python
输入: "the sky is blue"
输出: "blue is sky the"
```

```python
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split()))
```



### [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

给你一个整数数组 `nums`，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

```python
class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return None
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            if num > 0:
                curt_max = max(num, prev_max * num)
                curt_min = min(num, prev_min * num)
            else:
                curt_max = max(num, prev_min * num)
                curt_min = min(num, prev_max * num)
            global_max = max(global_max, curt_max)
            prev_max, prev_min = curt_max, curt_min
        return global_max
```



### [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。你可以假设数组中不存在重复元素。

```python
class Solution(object):
    def findMin(self, nums):
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
                
        return min(nums[start], nums[end])
```





### [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

```python
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, number):
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        else:
            self.minStack.append(min(number, self.minStack[-1]))

    def pop(self):
        ret = self.stack[-1]
        del(self.stack[-1], self.minStack[-1])
        return ret

    def top(self):
        ret = self.stack[-1]
        return ret
        

    def getMin(self):
        return self.minStack[-1]
```



### [162. 寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)

峰值元素是指其值大于左右相邻值的元素。给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。你可以假设 nums[-1] = nums[n] = -∞。

```python

class Solution(object):
    def findPeakElement(self, A):
        start, end = 0, len(A) - 1
        while start + 1 <  end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] < A[end]:
            return end
        else:
            return start
```



### [165. 比较版本号](https://leetcode-cn.com/problems/compare-version-numbers/)

比较两个版本号 version1 和 version2。如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        for i in range(0, max(len(v1_list), len(v2_list))):
            v1 = int(v1_list[i]) if len(v1_list) > i else 0
            v2 = int(v2_list[i]) if len(v2_list) > i else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
```



### [166. 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。如果小数部分为循环小数，则将循环的部分括在括号内。

```python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        result = ""
        if numerator/denominator < 0:
            result += "-"
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        if numerator % denominator == 0:
            return result+str(numerator/denominator)
        else:
            result += str(numerator/denominator)
            result += "."
        
        numerator = numerator % denominator
        Dict = {}
        i = len(result)
        
        while(numerator != 0):
            if Dict.get(numerator) == None:
                Dict[numerator] = i
            else:
                i = Dict[numerator]
                return result[:i]+"("+result[i:]+")"
            numerator = 10*numerator
            result += str(numerator/denominator)
            numerator = numerator % denominator
            i = i + 1
        return result
```



### [168. Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title/)

给定一个正整数，返回它在 Excel 表中相对应的列名称。

```python
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```

```python
class Solution(object):
    def convertToTitle(self, n):
        # write your code here
        return "" if n == 0 else self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))
```



### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。你可以假设数组是非空的，并且给定的数组总是存在多数元素。

```python
class Solution(object):
    def majorityElement(self, nums):
        storedNumber = None 
        counter = 1
        for num in nums:
            if num == storedNumber:
                counter += 1 
            else:
                counter -= 1 
                if counter == 0:
                    storedNumber = num
                    counter = 1 
                    
        return storedNumber
```



### [171. Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number/)

给定一个Excel表格中的列名称，返回其相应的列序号。例如

```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```

```python
class Solution(object):
    def titleToNumber(self, s):
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum
```



### [172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)

给定一个整数 *n*，返回 *n*! 结果尾数中零的数量。

```
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
```

```python
class Solution(object):
    def trailingZeroes(self, n):
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
```



### [179. 最大数](https://leetcode-cn.com/problems/largest-number/)

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

```python
class Solution(object):
    def largestNumber(self, nums):
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x)+str(y) > str(y)+str(x) else -1),reverse=True)
        print(nums)
        if nums[0] == 0:
            return '0'
        return "".join([str(x) for x in nums]) 
```



### [187. 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences/)

所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

```python
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dic, Str = {}, "x" + s[:9]
        for i in range(9,len(s)):
            Str = Str[1:] + s[i]
            print(Str)
            if dic.get(Str) == None:
                dic[Str] = 1
            else:
                dic[Str] = dic[Str] +1
        return [k for k, v in dic.items() if v > 1]
```





### [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)

颠倒给定的 32 位无符号整数的二进制位。

```python
class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1
            res += n & 1
            n = n >> 1
        return res
```



### [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

```python
class Solution(object):
    def rob(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)
        f = [0] * len(A)
        f[0], f[1] = A[0], max(A[0], A[1])
        for i in range(2, len(A)):
            f[i] = max(f[i - 1], f[i - 2] + A[i])
            
        return f[len(A) - 1]
```





### [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。

**示例 1:**

```
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
```

**示例 2:**

```
输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
```

**Answer:**

```python
class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                 if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    islands += 1        
        return islands                    
    
    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y):
                    continue
                queue.append((next_x, next_y))
                grid[next_x][next_y] = '0'
                
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'
```



### [205. 同构字符串](https://leetcode-cn.com/problems/isomorphic-strings/)

给定两个字符串 s 和 t，判断它们是否是同构的。如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        DictA = {}
        DictB = {}
        for i in range(len(s)):
            if DictA.get(s[i]) == None and DictB.get(t[i]) == None:
                #说明这两个字母的映射和被映射的关系都没有被设置
                DictA[s[i]] = t[i]
                DictB[t[i]] = s[i]
            if DictA.get(s[i]) != None and DictB.get(t[i]) == None:
                if DictA[s[i]] == t[i]:
                    DictB[t[i]] = s[i]
                    continue
                else:
                    return False
            if DictA.get(s[i]) == None and DictB.get(t[i]) != None:
                if DictB[t[i]] == s[i]:
                    DictA[s[i]] = t[i]
                    continue
                else:
                    return False
            if DictA.get(s[i]) != None and DictB.get(t[i]) != None:
                if DictB[t[i]] == s[i] and DictA[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True
```



### [207. 课程表](https://leetcode-cn.com/problems/course-schedule/)

你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

```python
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)] 
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
            
        queue, count = deque([]), 0
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == numCourses
```

### [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

在未排序的数组中找到第 **k** 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        L = []
        for i in range(len(nums)):
            if len(L) < k:
                L.append(nums[i])
            else:
                Min = min(L)
                if nums[i] > Min:
                    del L[L.index(Min)]
                    L.append(nums[i])
        return min(L)
```

### [217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)

给定一个整数数组，判断是否存在重复元素。



### [219. 存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii/)

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        Dict = {}
        for i in range(len(nums)):
            if Dict.get(nums[i]) == None:Dict[nums[i]] = i
            else:#在字典中存在这个数
                if abs(Dict[nums[i]] - i) <= k:return True
                else:Dict[nums[i]] = i
        return False
```



### [221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/)

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

```python
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        # intialization
        f = [[0] * m for _ in range(n)]
        for i in range(m):
            f[0][i] = int(matrix[0][i])
           
        edge = 0
        for i in matrix[0]:
            edge = max(edge,int(i))
        
        for i in range(1, n):
            f[i][0] = int(matrix[i][0])
            for j in range(1, m):
                if int(matrix[i][j]) == 1:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i-1][j - 1]) + 1
                else:
                    f[i][j] = 0
            edge = max(edge, max(f[i]))

        return edge * edge
```



### [240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：每行的元素从左到右升序排列。每列的元素从上到下升序排列。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix[0] == []:
            return False
            
        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False
```



### [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)



### [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

**示例:**

```
输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

**Answer:**

```python
"""
分治方法，但是这种方法的时间复杂度很高。会超时。靠缓存机制勉强不超时。
不超时主要是因为缓存了函数的结果
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        #在 Python 的 3.2 版本中，引入了一个非常优雅的缓存机制，即 functool 模块中的 lru_cache 装饰器，可以直接将函数或类方法的结果缓存住，后续调用则直接返回缓存的结果。
        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best
        return solve(0, n + 1)
      
"""
动态规划。
时间复杂度依然是O(n^3)，但是相当于主动保存了我上一种方法的缓存值。
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        return rec[0][n + 1]
```



### [290. 单词规律](https://leetcode-cn.com/problems/word-pattern/)

给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        List = str.split()
        DictA = {}
        DictB = {}
        if len(pattern) != len(List):
            return False
        for i in range(len(pattern)):
            if DictA.get(pattern[i]) == None and DictB.get(List[i]) == None:
                DictA[pattern[i]] = List[i]
                DictB[List[i]] = pattern[i]
            if DictA.get(pattern[i]) == None and DictB.get(List[i]) != None:
                #说明pattern中的字母没有出现过 但是List中的单词已经被映射了
                return False
            if DictA.get(pattern[i]) != None and DictB.get(List[i]) == None:
                #说明pattern中的字母已经映射了单词 但是这个单词并没有被字母映射
                return False
            if DictA.get(pattern[i]) != None and DictB.get(List[i]) != None:
                if DictA[pattern[i]] == List[i] and DictB[List[i]] == pattern[i]:
                    #说明是和之前相同的映射
                    continue
                else:
                    return False
        return True
```



### [299. 猜数字游戏](https://leetcode-cn.com/problems/bulls-and-cows/)

你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

你写出一个秘密数字，并请朋友猜这个数字是多少。
朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
朋友根据提示继续猜，直到猜出秘密数字。
请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。

xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。
请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。

```python
class Solution(object):
    def getHint(self, secret, guess):
        exist = [0] * 10
        expected = [0] * 10
        
        bull = 0
        cows = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else: #相同位置的两个数不相等
                exist[int(secret[i])] += 1
                expected[int(guess[i])] += 1
        print(exist)
        print(expected)
        for i in range(10):
            if exist[i] != 0:
                cows += min(exist[i], expected[i])
        return str(bull)+"A"+str(cows)+"B"
```



### [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

```python
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0 
        buy, sell, cooldown = [0 for _ in range(len(prices))], [0 for _ in range(len(prices))], [0 for _ in range(len(prices))]
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            cooldown[i] = sell[i - 1]
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])
            
        return max(sell[-1], cooldown[-1])
```



### [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。求所能获得硬币的最大数量。

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        return rec[0][n + 1]
```



### [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

```python
class Solution(object):
    def coinChange(self, coins, amount):
        MAX = 100000000000000
        ans = [MAX for i in range(amount + 1)]
        ans[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                ans[i] = min(ans[i], ans[i - coin] + 1)
        if ans[amount] == MAX:
            return -1
        return ans[amount]
```



### [334. 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 

```python
class Solution(object):
    def increasingTriplet(self, nums):
        minima = float('inf')
        second_minima = float('inf')
        for num in nums:
            if num < minima:
                minima = num
            if minima < num and num < second_minima:
                second_minima = num
            if num > second_minima and minima != float('inf') and second_minima != float('inf'):
                return True
        return False
```



### [337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

```python
class Solution(object):
    def rob(self, root):
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)
        
    def visit(self, root):
        if root is None:
            return 0, 0
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob
```





### [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

说明: 你可以假设 n 不小于 2 且不大于 58。

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
```

同 剑指offer 14



### [355. 设计推特](https://leetcode-cn.com/problems/design-twitter/)

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

1. postTweet(userId, tweetId): 创建一条新的推文
2. getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
3. follow(followerId, followeeId): 关注一个用户
4. unfollow(followerId, followeeId): 取消关注一个用户

```python
class Twitter(object):

    def __init__(self):
        self.tweets = []
        self.users = {}

    def postTweet(self, userId, tweetId):
        self.tweets.append((userId, tweetId))
        if self.users.get(userId) == None:
            self.users[userId] = [userId]
        

    def getNewsFeed(self, userId):
        if self.users.get(userId) == None:
            return []
        length = len(self.tweets)
        wanted = self.users[userId]
        index = -1
        count = 0
        result = []
        while index >= -length:
            currentUserid = self.tweets[index][0]
            currentTweetId = self.tweets[index][1]
            if count >= 10:
                break
            if currentUserid not in wanted:
                index -= 1
                continue
            else:
                result.append(currentTweetId)
                count += 1
                index -= 1
        return result

    def follow(self, followerId, followeeId):
        if self.users.get(followerId) == None:
            self.users[followerId] = [followerId]
        self.users[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if self.users.get(followerId) == None:
            self.users[followerId] = [followerId]
        if followerId != followeeId and followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)
```



### [365. 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem/)

有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。你允许：

1. 装满任意一个水壶
2. 清空任意一个水壶
3. 从一个水壶向另外一个水壶倒水，直到装满或者倒空

```python
class Solution(object):
    def canMeasureWater(self, x, y, z):
        if z > (x + y):
            return False
        if z == 0:
            return True
        return (z % self.gcd(x,y)) == 0
        
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y,x%y)
```



### [380. 常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/)

设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

1. insert(val)：当元素 val 不存在时，向集合中插入该项。
2. remove(val)：元素 val 存在时，从集合中移除该项。
3. getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。



### [451. 根据字符出现频率排序](https://leetcode-cn.com/problems/sort-characters-by-frequency/)

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。



### [593. 有效的正方形](https://leetcode-cn.com/problems/valid-square/)

给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。

一个点的坐标（x，y）由一个有两个整数的整数数组表示。

```python
class Solution(object):
    import math
    def validSquare(self, p1, p2, p3, p4):
        arr = [p1, p2, p3, p4]
        arr.sort(key=lambda x: (x[0], x[1]))
        
        if 0 < self.length(arr[0], arr[1]) == self.length(arr[0], arr[2]) == self.length(arr[2], arr[3]) == self.length(arr[3], arr[1]):
            if 0 < self.length(arr[0], arr[3]) == self.length(arr[2], arr[1]):
                return True
                
        return False
    
    def length(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
```



### [611. 有效三角形的个数](https://leetcode-cn.com/problems/valid-triangle-number/)

给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

```python
import math
class Solution(object):
    def triangleNumber(self, nums):
        nums = sorted(nums)
        total = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            end = i + 2
            for j in range(i+1, len(nums)-1):
                while end < len(nums) and nums[end] < (nums[i] + nums[j]):
                    end += 1
                total += end - j - 1
        return total
```





### [650. 只有两个键的键盘](https://leetcode-cn.com/problems/2-keys-keyboard/)

最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：

Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
Paste (粘贴) : 你可以粘贴你上一次复制的字符。
给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。

```python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factors(n):
            i = 2
            while i * i <= n:
                while n % i == 0:
                    n /= i
                    yield i
                i += 1
            if n > 1:
                yield n
        result = sum(factors(n))
        return result
```



### [676. 实现一个魔法字典](https://leetcode-cn.com/problems/implement-magic-dictionary/)

实现一个带有buildDict, 以及 search方法的魔法字典。

对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。

对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

```python
class MagicDictionary(object):

    def __init__(self):
        self.D = {}

    def buildDict(self, Dict):
        for item in Dict:
            length = len(item)
            if self.D.get(length) == None:
                self.D[length] = [item]
            else:
                self.D[length].append(item)

    def search(self, word):
        len_now = len(word)
        
        if self.D.get(len_now) == None:
            return False
        else:
            list_now = self.D[len_now]
            for item in list_now:
                different_num = 0
                for i in range(len_now):
                    if item[i] != word[i]:
                        different_num += 1
                    if different_num > 1:
                        break
                if different_num == 1:
                    return True
            return False
```



### [791. 自定义字符串排序](https://leetcode-cn.com/problems/custom-sort-string/)

字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

```python
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        index = [0] * len(S)
        other = ""
        for character in T:
            if S.find(character) == -1:
                other += character
            else:
                index[S.find(character)] += 1
        sort = ""
        for i in range(len(S)):
            sort += index[i] * S[i]
        
        return sort + other
```



### [794. 有效的井字游戏](https://leetcode-cn.com/problems/valid-tic-tac-toe-state/)

```
示例 1:
输入: board = ["O  ", "   ", "   "]
输出: false
解释: 第一个玩家总是放置“X”。
```

```python
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        countO = 0
        countX = 0
        
        for row in range(3):
            for column in range(3):
                if board[row][column] == "O":
                    countO += 1
                if board[row][column] == "X":
                    countX += 1
        if countX != countO and countX != (countO + 1):
            return False
        
        countOline = 0
        countXline = 0
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == "O":
                    countOline += 1
                if board[row][0] == "X":
                    countXline += 1
        
        for column in range(3):
            if board[0][column] == board[1][column] and board[1][column] == board[2][column]:
                if board[0][column] == "O":
                    countOline += 1
                if board[0][column] == "X":
                    countXline += 1
        
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == "O":
                countOline += 1
            if board[0][0] == "X":
                countXline += 1
                
        if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            if board[2][0] == "O":
                countOline += 1
            if board[2][0] == "X":
                countXline += 1

        if countXline == 2:
            return True
        if countOline == countXline and countOline == 1:
            return False
        if countXline == 1 and countX == countO:
            return False
        if countOline == 1 and countX == (countO + 1):
            return False
        return True
```



### [868. 二进制间距](https://leetcode-cn.com/problems/binary-gap/)

给定一个正整数 `N`，找到并返回 `N` 的二进制表示中两个相邻 1 之间的最长距离。 如果没有两个相邻的 1，返回 `0` 。

```python
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        index = 0
        last = -1
        while N > 0:
            now = N & 1
            N = N >> 1
            print(now)
            if now == 1:
                if last == -1:
                    last = index
                else:
                    ans = max(ans, index - last)
                    last = index
            index += 1
        return ans
```

### [887. 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)

你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？。

```python
class Solution(object):
    def superEggDrop(self, K, N):
        dp = [[0 for col in range(K + 1)] for row in range(N + 1)];
        m = 0;
        while dp[m][K] < N:
            m = m + 1;
            for i in range(1,K + 1):
                dp[m][i] = dp[m - 1][i - 1] + dp[m - 1][i] + 1;
        return m;
```



### [892. 三维形体的表面积](https://leetcode-cn.com/problems/surface-area-of-3d-shapes/)

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。请你返回最终形体的表面积。

```python
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0;
        for i in range(0, len(grid)):
            s = 0;
            for j in range(0, len(grid[0])):
                ans = ans + abs(grid[i][j] - s);
                s = grid[i][j];
            ans = ans + s;
        for j in range(0, len(grid[0])):
            s = 0;
            for i in range(0, len(grid)):
                ans = ans + abs(grid[i][j] - s);
                s = grid[i][j];
            ans = ans + s;
        s = 0;
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if not grid[i][j] == 0:
                    s = s + 1;
        ans = ans + s * 2;
        return ans;
```



### [914. 卡牌分组](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/)

给定一副牌，每张牌上都写着一个整数。此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

```python
import math
from functools import reduce

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic = {}
        for item in deck:
            if dic.get(item) == None:
                dic[item] = 1
            else:
                dic[item] = dic[item] + 1
        
        count_list = []
        for value in dic.itervalues():
            count_list.append(value)
        
        result = self.gcd_me(count_list)
        if result == 1:
            return False
        else:
            return True

     # greatest common divisor
    def gcd_me(self,numbers):
        return reduce(self.gcd, numbers)
    
    def gcd(self,a,b):
        x = a % b
        while (x != 0):
            a = b
            b = x
            x = a % b
        return b
```



### [1035. 不相交的线](https://leetcode-cn.com/problems/uncrossed-lines/)

我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。以这种方法绘制线条，并返回我们可以绘制的最大连线数。

```python
import numpy as np
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lengthA = len(A)
        lengthB = len(B)
        
        DP = np.zeros((lengthA + 1,lengthB + 1),dtype = int)
        for i in range(1,lengthA + 1):
            for j in range(1,lengthB + 1):
                if A[i-1] == B[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j],DP[i][j-1])
        return DP[-1][-1]
```

### [1037. 有效的回旋镖](https://leetcode-cn.com/problems/valid-boomerang/)



### [1052. 爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner/)

今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

```python
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        if X >= len(customers):
            return sum(customers)
        
        
        new_customers = [0]*len(customers)
        fix = 0
        for i,gru in enumerate(grumpy):
            if gru == 0:
                fix += customers[i]
            else:
                new_customers[i] = customers[i]
        change = []
        for j in range(len(new_customers) - X +1):
            sum_x = 0
            for k in range(X):
                sum_x += new_customers[j+k]
            change.append(sum_x)
        return max(change) + fix
```

### [1184. 公交站间的距离](https://leetcode-cn.com/problems/distance-between-bus-stops/)

环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。环线上的公交车都可以按顺时针和逆时针的方向行驶。返回乘客从出发点 start 到目的地 destination 之间的最短距离。

```python
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start == destination:
            return 0
        
        pa = min(start,destination)
        pb = max(start,destination)
        lineA = []
        lineB = []
        for i in range(pa,pb):
            lineA.append(distance[i])
        
        sec_distance = distance + distance
        length = len(distance)
        for j in range(pb, length+pa):
            lineB.append(sec_distance[j])
        return min(sum(lineA),sum(lineB))
```



### [1209. 删除字符串中的所有相邻重复项 II](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

```python
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        
        new_s = "*" + s + "*"
        i = 1
        new_str = []
        countnow = 0
        countdel = 0
        for i in range(1,len(new_s)):
            if new_s[i] != new_s[i-1] and new_s[i-1] != "*": #当前值和上一个值不相同
                if countnow < k and countnow > 0:
                    new_str.append([new_s[i-1],countnow])
                    countnow = 1
                elif countnow == 0:
                    countnow = 1
                    continue
                else:
                    countdel += 1
                    countnow = 1
                    continue
            else: #当前值和上一个值相同
                countnow += 1
                if countnow == k:
                    countdel += 1
                    countnow = 0
        s_now = ""
        for item in new_str:
            s_now += item[0] * item[1]
            
        if countdel == 0:
            return s_now
        else:
            return self.removeDuplicates(s_now, k)
```



### [1253. 重构 2 行二进制矩阵](https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix/)

给你一个 2 行 n 列的二进制数组：矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。

1. 第 0 行的元素之和为 upper。
2. 第 1 行的元素之和为 lower。
3. 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。

```python
import numpy as np
class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        sumcheck1 = upper + lower
        sumcheck2 = sum(colsum)
        if sumcheck1 != sumcheck2:
            return []
        
        result = np.zeros((2,len(colsum)),dtype = int)
        
        num_of_two = 0
        for index in range(len(colsum)):
            if colsum[index] == 2:
                num_of_two += 1
                result[0][index] = 1
                result[1][index] = 1
                
        upper = upper - num_of_two
        lower = lower - num_of_two
        
        if upper < 0 or lower < 0:
            return []
        for index in range(len(colsum)):
            if colsum[index] == 1:
                if upper > 0:
                    result[0][index] = 1
                    upper -= 1
                elif lower > 0:
                    result[1][index] = 1
                    lower -= 1
        return result.tolist()
```



### [1309. 解码字母到整数映射](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)

给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

1. 字符（'a' - 'i'）分别用（'1' - '9'）表示。
2. 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 

```python
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {
            "1":"a",
            "2":"b",
            "3":"c",
            "4":"d",
            "5":"e",
            "6":"f",
            "7":"g",
            "8":"h",
            "9":"i",
            "10#":"j",
            "11#":"k",
            "12#":"l",
            "13#":"m",
            "14#":"n",
            "15#":"o",
            "16#":"p",
            "17#":"q",
            "18#":"r",
            "19#":"s",
            "20#":"t",
            "21#":"u",
            "22#":"v",
            "23#":"w",
            "24#":"x",
            "25#":"y",
            "26#":"z"
        }
        result = ""
        i = 0
        while i < len(s):
            if i < (len(s)-2):
                if s[i+2] == "#":
                    now = s[i:i+3]
                    ch = dic[now]
                    result = result + ch
                    i = i+3
                else:
                    now = s[i]
                    ch = dic[now]
                    result = result + ch
                    i = i+1
            else:
                now = s[i]
                ch = dic[now]
                result = result + ch
                i = i+1
        return result
```

### [1352. 最后 K 个数的乘积](https://leetcode-cn.com/problems/product-of-the-last-k-numbers/)

请你实现一个「数字乘积类」ProductOfNumbers，要求支持下述两种方法：

1. add(int num)

将数字 num 添加到当前数字列表的最后面。
2. getProduct(int k)

返回当前数字列表中，最后 k 个数字的乘积。
你可以假设当前列表中始终 至少 包含 k 个数字。

```python
class ProductOfNumbers(object):

    def __init__(self):
        self.current = [1] 

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.current = [1]
        else:
            self.current.append(num * self.current[-1])

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        print(len(self.current))
        print(k)
        if k >= len(self.current):
            return 0
        else:
            return self.current[-1] // self.current[-k-1]
```

















