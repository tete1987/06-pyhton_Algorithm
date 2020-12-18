# pyhton_Algorithm
## 一、算法入门基础：
### （一）算法概念
1.概念：

算法（Algorithm）：一个计算过程，解决问题的方法。

Niklaus Wirth：“程序=数据结构+算法”

### （二）时间复杂度
示例1：
![时间复杂度1](https://github.com/tete1987/picture_resource/blob/master/py%E7%AE%97%E6%B3%95-%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E6%A6%82%E5%BF%B5.png)

问题：以上四组代码，哪一组运行时间最短？用什么方式来体现算法运行的快慢？

（n）为运行规模。

如果使用运行时间的快慢来衡量会出现两个问题：

- 运行的机器不同会导致效果不同。
- 如果是较为复杂的运算，执行一次好几个小时甚至几天，对于测试其时间来说耗费的过程时间较长，因此不适宜。

此处，需要引入“时间复杂度”的概念。
![时间复杂度2](https://github.com/tete1987/picture_resource/blob/master/py%E7%AE%97%E6%B3%95-%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E6%A6%82%E5%BF%B52.png)

解析：
- 如果将一个print 函数 的复杂度标记为 O(1)，那么一个for循环就相当于一个O(n)；
- 那么for循环中嵌套一个for循环，那么复杂度将升高为O(n²)，以此类推。

![时间复杂度3](https://github.com/tete1987/picture_resource/blob/master/py%E7%AE%97%E6%B3%95-%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E6%A6%82%E5%BF%B52.png)

注：此处标记的“1”为一个单位，并非一个数字，所以不论是print 三次还是十次，复杂度均不会上升，如下图：


示例2:

![时间复杂度4](https://github.com/tete1987/picture_resource/blob/master/py%E7%AE%97%E6%B3%95-%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E6%A6%82%E5%BF%B54.png)

如果循环当中出现折半的情况，则时间复杂度以对数形式展现。

3.时间复杂度-小结：

1）时间复杂度是用来估计算法运行时间的一个式子（单位）。

2）一般来说，时间复杂度高的算法比复杂度低的算法慢。

3）常见的时间复杂度（按效率排序）：

- O(1)<O(logn)<O(n)<O(nlogn)<O(n²)<O(n²logn)……

4）复杂问题的时间复杂度

- O(n!)<O(2²)<O(n^n)……


4.如何简单快速地判断算法复杂度

1）快速判断算法复杂度（适用于绝大多数简单情况）：
- 确定问题规模
- 循环减半过程-->logn
- k层关于n的循环 --> k^n
 
2）复杂情况：根据算法执行过程判断

### （三）空间复杂度
1.概念：空间复杂度用例评估算法内存占用大小的式子。

2.空间复杂度的表示方式与时间复杂度完全一样。
- 算法使用了几个变量：O(1)
- 算法使用了长度为n的一维列表：O(n)
- 算法使用了m行n列的二维列表：O(mn)

3.“空间换时间”

### （四）递归
1.递归的两个特点：

1）调用自身

2）结束条件
![递归](https://github.com/tete1987/picture_resource/blob/master/%E9%80%92%E5%BD%92.png)


上图中正确的递归函数为：func3 和 func4 。
- 当x=3时，
  - func3的输出结果为：3，2，1
  - func4 的输出结果为：1，2，3
  
![递归解析](https://github.com/tete1987/picture_resource/blob/master/%E9%80%92%E5%BD%92%E6%89%93%E5%8D%B0%E8%A7%A3%E6%9E%90.png)

2.递归实例：汉诺塔问题

![汉诺塔实例](https://github.com/tete1987/picture_resource/blob/master/%E6%B1%89%E8%AF%BA%E5%A1%94%E5%AE%9E%E4%BE%8B.png)

解析：

1）当 n=2时，

&ensp; ①把小圆盘从A移动到B

&ensp; ②把大圆盘从A移动到C

&ensp; ③把小圆盘从B移动到C

2）当n个盘子时：

&ensp; ①把 n-1 个小圆盘从A移动到B

&ensp; ②把第n个圆盘从A移动到C

&ensp; ③把 n-1 个小圆盘从B移动到C


实例：
```
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print(f"moving from %s to %s"%(a,c))
        hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')
```


3）递归实例：汉诺塔总结

&ensp; ①汉诺塔移动次数的递推式：h(x)=2h(x-1)+1

&ensp; ②h(64)=18446744073709551615

&ensp; ③假设婆罗门每秒钟搬一个盘子，则总共需要5800亿年！
