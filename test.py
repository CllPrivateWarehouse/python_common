import logging.config
logger = logging.getLogger()
from queue import Queue
from functools import reduce
from collections import Iterable
import sys
import random



class Test:
    def __init__(self):
        self.test_queue = Queue()

    def PutQueue(self):
        data_dict = {}
        data_dict['name'] = "cll"
        data_dict['gender'] = "男"
        self.test_queue.put(data_dict)

    def GetQueue(self):
        while True:
            # 如果队列为空，则会一直阻塞 直到有数据
            task_dict = self.test_queue.get()
            # 进行任务
            self.test(task_dict)
            print("第三次判断队列是否为空队列", self.test_queue.empty())

    def test(self, param):

        for key, value in param.items():
            print("key,value", key, value)



"""
快速排序:
1、在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值;

2、数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边;

3、以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。
"""
# def quick_sort(alist, start, end):
#     """快速排序"""
#     if start >= end:  # 递归的退出条件
#         return
#     mid = alist[start]  # 设定起始的基准元素
#     low = start  # low为序列左边在开始位置的由左向右移动的游标
#     high = end  # high为序列右边末尾位置的由右向左移动的游标
#     while low < high:
#         # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
#         while low < high and alist[high] >= mid:
#             high -= 1
#         alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
#         # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
#         while low < high and alist[low] < mid:
#             low += 1
#         alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处
#
#     # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
#     alist[low] = mid  # 将基准元素放到该位置,
#     # 对基准元素左边的子序列进行快速排序
#     quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
#     # 对基准元素右边的子序列进行快速排序
#     quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后

def quick_sort(data):
    """quick_sort"""
    if len(data) >= 2:
        # 选取基准，随便选哪个都可以，这里选中间的作为基准，便于理解
        pivot = data[len(data)//2]
        # 定义基准值左右两个数列
        left, right = [], []
        # 从原始数组中移除基准值
        data.remove(pivot)
        for temp in data:
            if temp >= pivot:
                # 大于基准值放右边
                right.append(temp)
            else:
                # 小于基准值放左边
                left.append(temp)
        # 使用迭代进行比较
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return data

# # 快速排序简洁写法
# def quick_sort(data):
#     if len(data) < 2: return data
#     return quick_sort([lt for lt in data[1:] if lt <= data[0]]) + data[0:1] + quick_sort([rt for rt in data[1:] if rt > data[0]])

# 冒泡排序
# 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
# 如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
def BubbleSort(data):
    # 获取列表的长度
    n = len(data)
    # 遍历所有数组元素
    for i in range(n):  # 控制循环多少次
        # 相邻两个元素进行比较
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # 大数与小数互换

    return data

# 选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
def SelectionSort(data):
    # 以序号为依据
    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):  # 上一个值右边的数组
            if data[min] > data[j]:        # 使min为最小值，遇到比min小的值就赋值于min
                min = j

        data[i], data[min] = data[min], data[i]  # 交换最小值到左边

    return data







# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
# 特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
def recur_fibo(n):
    """递归函数输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))

# 列表翻转
def ReverseList(data_list):
    new_lst = data_list[::-1]
    return new_lst

# 字符串翻转
def ReverseStr(data_str):
    new_str = data_str[::-1]
    return new_str

# 质数判断(即素数判断)
# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等）
# 换句话说就是该数除了1和它本身以外不再有其他的因数。
def IsPrimeNumber():

    # 如果是指定输出范围内的素数 就加上下面三行代码，如果是判断固定数字是否为素数就把开始的3行去掉，并在函数赋予形参num即可
    lower = 10
    upper = 100
    for num in range(lower, upper + 1):

        if num > 1:
            # 循环判断能否整除，即余数是否为0，若为0，则不是素数。
            for i in range(2, num):
                if num % i == 0:
                    print("{}不是素数（质数）".format(num))
                    break
            # 这里的else和for是搭配的，当上述所有遍历结束后没有一次余数为0，就会到这里执行，并打印输出“该数是质数”
            else:
                print("{}是素数（质数）".format(num))

        else:
            print("{}不是素数（质数）".format(num))

# 计算 n 个自然数的立方和，即： (1)3 + (2)3 + (3)3 + (4)3 + …….+ (n)3
def CubeSum(n):
    cube_sum = 0
    for i in range(1, n + 1):
        cube_sum += i * i * i

    return cube_sum





if __name__ == '__main__':

    # t = Test()
    # print("第一次判断队列是否为空队列", t.test_queue.empty())
    # t.PutQueue()
    # print("第二次判断队列是否为空队列", t.test_queue.empty())
    # t.GetQueue()

    # a = [11, 99, 33, 69, 77, 88, 55, 12, 11, 33, 11, 11, 36, 39, 66, 44, 22, 98]
    # quick_sort(a)
    # quick_sort(a, 0, len(a) - 1)
    # print(a)
    # print(quick_sort(a))
    # param = [10, 11, 12, 13, 14, 15]
    # print(ReverseList(param))
    # param = 'hello world'
    # print(ReverseStr(param))

    # ret = BubbleSort(a)
    # print("冒泡排序后的数组：", ret)

    # ret = SelectionSort(a)
    # print("选择排序后的数组：", ret)

    # 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
    # 关于filter()方法, python3和python2有一点不同
    # Python2.x 中返回的是过滤后的列表, 而 Python3 中返回到是一个 filter 类。
    # Python 判断奇数偶数
    # 如果是偶数除以2,余数为 0
    # 如果余数为1, 则为奇数
    # new_list = filter(lambda x : x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print("过滤掉偶数后的新数组：", list(new_list))

    # 质数判断
    # IsPrimeNumber()

    # ret = CubeSum(8)
    # print("立方和为：", ret)

    # print("斐波那契数列:")
    # for i in range(20):
    #     print(recur_fibo(i))

    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    # b = [1, 4, 5, 7, 4, 7, 8]
    # c = [2, 3, 7, 9]
    # d = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    # # 求两个列表相同的元素
    # t1 = set(b)
    # t2 = set(c)
    # print(t1)
    # print(t2)
    # # 交集
    # print("交集的结果为:{}".format(t1 & t2))
    # # 并集
    # print("并集的结果为:{}".format(t1 | t2))
    # # 差集
    # print("差集的结果为:{}".format(t1 - t2))

    # s = set()
    # # 集合添加元素使用update比较好，参数可以是列表，元组，字典等,且参数可以传入多个
    # s.update(b, c, d)
    # print(s)
    # # set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
    # s.pop()
    # print(s)

    # # 列表解析（列表推导式）
    # arr = [2, 4, 8, 14, 25, 36, 47, 55, 68, 77]
    # ret = [i**2 for i in arr if i > 10 and i < 50]
    # print(ret)

    # map() 会根据提供的函数对指定序列做映射。注意：Python 2.x 返回列表,Python 3.x 返回迭代器。返回迭代器的好处就是节约内存
    # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    # # 使用 lambda 匿名函数
    # ret = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
    # # 由于返回的是迭代器 所有用list转换一下
    # print(list(ret))
    # # 提供了两个列表，对相同位置的列表数据进行相加
    # map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

    # # 使用 lambda 匿名函数计算列表元素之和
    # sum = reduce(lambda x, y: x + y, a)
    # print("a列表元素之和为：", sum)
    #
    # # # 使用 lambda 匿名函数计算列表元素乘积
    # product = reduce(lambda x, y: x * y, a)
    # # print("a列表元素之积为：", product)


    """
    sorted(iterable, key=None, reverse=False)  函数对所有可迭代的对象进行排序操作,并返回重新排序的列表。
    sort 与 sorted 区别：
        sort 是应用在 list 上的方法，而sorted 可以对所有可迭代的对象进行排序操作。
        list 的 sort 方法返回的是对已经存在的列表进行操作;
        而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    
    """
    # # 对列表采用sorted进行排序
    # example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    # result_list = sorted(example_list, key=lambda x: x*-1)
    # print("利用sorted函数key进行列表的倒序排序后为:{}".format(result_list))
    # result_list1 = sorted(example_list, reverse=True)
    # print("利用sorted函数reverse进行列表的倒序排序后为:{}".format(result_list1))

    # 通过key的值来进行数组/字典的排序
    # array = [{"age": 20, "name": "aaa"}, {"age": 25, "name": "bbb"}, {"age": 10, "name": "ccc"}, {"age": 10, "name": "abc"}]
    # result = sorted(array, key=lambda x: x['age'], reverse=False)
    # print("通过key的值来进行数组/字典的排序排序后为:{}".format(result))
    # # 先按照年龄降序排序，相同年龄的按照名字升序排序：
    # result1 = sorted(array, key=lambda x: (-x['age'], x['name']))
    # print("先按照年龄降序排序，相同年龄的按照名字升序排序：:{}".format(result1))

    # # 对字典进行排序
    # test_dict = {'ddd': 18, 'bbb': 15, 'eee': 12, 'ccc': 16, 'aaa': 22, 'fff': 17}
    # # 按key排序
    # ret_key = sorted(test_dict.items(), key=lambda x: x[0], reverse=False)
    # print(dict(ret_key))
    #
    # # 按value排序
    # ret_value = sorted(test_dict.items(), key=lambda x: x[1], reverse=False)
    # print(dict(ret_value))

    """
    isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
    如果要判断两个类型是否相同推荐使用 isinstance()。
    """
    # print(isinstance('abc', Iterable))  # str是否可迭代 其余类型判断同理

    # 迭代器与生成器
    """
    迭代（iteration）：
        1、迭代需要重复进行某一操作
        2、本次迭代的要依赖上一次的结果继续往下做，如果中途有任何停顿，都不能算是迭代
        即：重复+继续
    
    可迭代对象 （iterable）：
        通俗的说就是在每一种数据类型对象中，都会有一个__iter__()方法，正是因为这个方法，才使得这些基本数据类型变为可迭代
    
    迭代器（iterator）：
        通俗来讲任何具有__next__()方法的对象都是迭代器，对迭代器调用__next__()方法可以获取下一个值。
        迭代是Python最强大的功能之一，是访问集合元素的一种方式。
        迭代器是一个可以记住遍历的位置的对象。
        迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
        迭代器有两个基本的方法：iter() 和 next()。
        字符串，列表或元组对象都可用于创建迭代器。
    
    生成器（generator）：
        生成器是一个用简单的方式来完成迭代。简单来说，Python的生成器是一个返回可迭代对象的函数。
        在 Python 中，使用了 yield 的函数被称为生成器（generator）。
        跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
        在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
        调用一个生成器函数，返回的是一个迭代器对象。
    
    """
    # 列表创建迭代器
    # test_list = [1, 2, 3, 4, 5]
    # it = iter(test_list)      # 通过iter方法创建迭代器对象
    # print(next(it))           # 通过next方法输出迭代器的下一个元素
    # # for i in it:
    # #     print(i)
    # # 也可以通过next输出所有元素
    # for i in range(5):
    #     print(next(it))

    # # 字符串创建迭代器
    # test_str = {'1', '22', '3333'}
    # it_str = iter(test_str)
    # print(next(it_str))
    # for i in it_str:
    #     print(i)

#     # 使用 yield 生成器的方式实现斐波那契数列:
#     def fibonacci(n):  # 生成器函数 - 斐波那契
#         a, b, counter = 0, 1, 0
#         while True:
#             if counter > n:
#                 return
#             yield a
#             a, b = b, a + b
#             counter += 1
#
# # 调用一个生成器函数，返回的是一个迭代器对象。
# f = fibonacci(10)  # f 是一个迭代器，由生成器函数fibonacci()返回生成
#
# print(type(f))
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

###############################################################################
# Python 三目运算符、列表推导式(列表解析)、生成器推导式、字典推导式、集合推导式
###############################################################################

"""
三目运算符
语法格式：
    结果1 if 表达式 else 结果2
    若表达式值为真，则执行结果1，否则执行结果2
"""
# a = 10
# b = 6
# max = a if a >b else b
# print(max)

"""
列表推导式：把就列表按照表达式需要的形式推导成新的列表,返回的是新列表
语法格式：
    [表达式 for 变量 in 列表] 或者 [表达式 for 变量 in 列表 if 条件]
    或 [结果A if 条件 else 结果B for x in 列表]
优点：
    代码简洁、少量数据时效率更高       
"""
# old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = [i**2 for i in old_list if i % 2 == 0]
# print(new_list)

# 偶数加3，奇数加1
# list1 = [x+3 if x % 2 == 0 else x+1 for x in [1, 2, 3, 4, 5, 6]]
# print(list1)
"""
生成器推导式：把列表推导式的[]换成()得到的就是生成器表达式，返回的是迭代器
语法格式：
    (表达式 for 变量 in 列表) 或者 (表达式 for 变量 in 列表 if 条件)
优点：
    节省大量内存，对大量数据的处理比较好    
"""
# # 生成器推导式
# gen = (i for i in range(10) if i % 2 == 0)
# print(type(gen))
# while True:
#     try:
#         print(next(gen), end=" ")
#     except StopIteration:
#         sys.exit()

"""
字典推导式：
语法格式：字典推导和列表推导的使用方法是类似的，只不中括号该改成大括号，返回新的字典
    {表达式 for 变量 in 字典} 或者 {表达式 for 变量 in 字典 if 条件}
"""
# 将字典键和值调换
# test_dict = {'name': 'aaa', 'age': 18}
# # ret = {v: k for k, v in test_dict.items()}
# ret = {test_dict[k]: k for k in test_dict.keys()}
# print(ret)

# # 将字典大小key合并
# test_dict = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# ret = {k.lower(): (test_dict.get(k.lower(), 0) + test_dict.get(k.upper(), 0)) for k in test_dict.keys()}
# print(ret)

"""
集合推导式：集合推导式和字典推导式的格式完全相同；(集合推导式自带去重功能)
            根据表达式进行判断，如果表达式以键值对（key：value）的形式，则证明此推导式是字典推导式；反之，则是集合推导式
            使用集合推导式可以借助列表、元组、字典、集合以及 range 区间，快速生成符合需求的集合。

语法格式：字典推导和列表推导的使用方法是类似的，只不中括号该改成大括号，返回新的字典
    {表达式 for 变量 in 可迭代对象} 或者 {表达式 for 变量 in 可迭代对象 if 条件}
"""
# test_list = [0, 1, 3, 3, 6, 8, 8, 12, 17, 21]
# ret = {i for i in test_list if i != 0}
# print(ret)

# 产生随机数
# set1 = set()
# for i in range(10):
#     ret = random.randint(0, 100)
#     set1.add(ret)
# print(set1)

# 文件读写操作txt类型文件
# with open('test.txt', 'wt') as out_file:
#     out_file.write("测试写文件")

# with open('test.txt', 'rt') as in_file:
#     result = in_file.read()
#     print(result)


"""
函数参数类型：
    1、必需参数
    2、关键字参数
    3、默认参数
    4、不定长参数

不定长参数：
    1、加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
    2、加了两个星号 ** 的参数会以字典的形式导入。
    
不定长参数实例：
    1、 *args 和 **kwargs 主要用于函数定义。    
        你可以将不定数量的参数传递给一个函数。不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 
        所以在这个场景下使用这两个关键字。其实并不是必须写成 *args 和 **kwargs。  
        *(星号) 才是必须的. 你也可以写成 *ar  和 **k 。而写成 *args 和**kwargs 只是一个通俗的命名约定。
        
    2、*args 与 **kwargs 的区别，两者都是 python 中的可变参数：
        *args 表示任何多个无名参数，它本质是一个 tuple;
        **kwargs 表示关键字参数，它本质上是一个 dict; 
"""
# # 单独使用*args
# def fun(name, *args):
#     print("姓名为:{}".format(name))
#     print("其余参数类型为", type(args))
#     for i in args:
#         print("分别打印其余参数", i)
# fun(1, 2, "hello", [2])
# # 打印内容如下：
# # 姓名为:1
# # 其余参数为 <class 'tuple'>
# # 分别打印其余参数 2
# # 分别打印其余参数 hello
# # 分别打印其余参数 [2]

# # 单独使用**kwargs
# def fun(name, **kwargs):
#     print("姓名为:{}".format(name))
#     print("其余参数类型为", type(kwargs))
#     print(kwargs)
#     # for k,v in kwargs.items():
#     #     print()
# # 调用函数时需使用关键字参数传入
# fun(1, a = 2, b = 4, c = 'hello')
# # 打印内容如下：
# # 姓名为:1
# # 其余参数类型为 <class 'dict'>
# # {'a': 2, 'b': 4, 'c': 'hello'}

# # 同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前,否则会报语法错误
# def fun(*args, **kwargs):
#     print('args=', args)
#     print('kwargs=', kwargs)
# fun(1, 2, 3, 4, 5, 6, a='A', b='B', c='C')
# # 打印内容如下：
# # args= (1, 2, 3, 4, 5, 6)
# # kwargs= {'a': 'A', 'b': 'B', 'c': 'C'}

##############
# 装饰器与闭包
##############
"""
装饰器: 
    1、装饰器本质上是一个 Python 函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，
       装饰器的返回值也是一个函数/类对象。
    2、   




闭包：
    1、
    2、



"""



# # 使用enumerate()函数遍历出列表的索引及对应的值
# data = [2, 4, 6]
# for i, v in enumerate(data):
#     data[i] = data[i] + 100
#     print("索引:{} 对应值:{}".format(i, v))
# print("计算后的列表为:{}".format(data))
#
# # 索引:0 对应值:2
# # 索引:1 对应值:4
# # 索引:2 对应值:6
# # 计算后的列表为:[102, 104, 106]

# # staticmethod 返回函数的静态方法
# class fun(object):
#
#     @staticmethod
#     def test():
#         print("test")
#
# # 静态方法无需实例化
# fun.test()
#
# # 也可以实例化后调用
# f = fun()
# f.test()

# # 字节转换为字符串（bytes to str）
# test = b'hello world'
# print(type(test))
# ret = test.decode()
# print(type(ret))
#
# # 字符串转换为字节（str to bytes）
# test = 'hello world'
# print(type(test))
# ret = test.encode()
# print(type(ret))

# list1 = ['Google', 'Runoob', 'Taobao', 'baidu', 'Taobao']
# list1.append('11111111')
# list1.append('22222222222')
# print("插入新元素到指定位置：", list1)
#
# list1.pop(1)
# print(list1)

# list1.reverse()
# print(f'翻转后的列表为:{list1}')

# ret = list1[::-1]
# print(ret)
# print(list1)

# for i in reversed(list1):
#     print(i)


# ret = reversed(list1)
# print(type(ret))


# tuple1 = (50, 60, 'c', 23, '67')
# print(type(tuple1))
#
# # tuple2 = print(tuple1*3)
# #
# print(tuple1[::-1])

# data_dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First', 'cll': 111}
# print(len(data_dict))
# print(str(data_dict))
#
# test = data_dict.copy()
# print(id(data_dict))
# print(id(test))
# print(test)



# test = set()
#
# test.update([6,2,8,4,12,1,3])
#
#
# print(test)
#
#
# test.pop()
# test.pop()
# test.pop()
# print(test)


# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
#
# z = x.union(y)
#
# print(z)


# def change(a):
#     print(f'传入参数后（形参）内存地址为:{id(a)}')  # 指向的是同一个对象
#     a = 10
#     print(f'在函数内修改形参后内存地址为:{id(a)}')  # 一个新对象
#
# a = 1
# print(f'传入参数前（实参）内存地址为:{id(a)}')
# change(a)
#
# # 传入参数前（实参）内存地址为:1723035104
# # 传入参数后（形参）内存地址为:1723035104
# # 在函数内修改形参后内存地址为:1723035392


#
# def changeme(mylist):
#     # 修改传入的列表
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist, id(mylist))
#     return
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist, id(mylist))
#
# # 函数内取值:  [10, 20, 30, [1, 2, 3, 4]] 2364532183816
# # 函数外取值:  [10, 20, 30, [1, 2, 3, 4]] 2364532183816

# sum = lambda x, y: x + y
# print(sum(3, 4))


# from collections import deque
#
# queue = deque(['c', 'a', '1', 'f'])
#
# queue.append('cll')
#
# print(queue)
#
# queue.popleft()
#
# print(queue)
# print(list(queue))

# 捕获异常
# def divide(x, y):
#     try:
#         result = x / y
#     except Exception:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
#
# divide(2, 0)


# class MyClass:
#     i = 123
#     # 构造方法(初始化)，类实例化时自动调用
#     def __init__(self):
#         self.name = 'cll'
#
#     def f(self):
#         return 'hello world'
#
# """
# 类的实例化包括以下4个步骤：
# 1、找有没有空间是MyClass内存地址
# 2、利用MyClass类，向内存申请一块和MyClass一样的空间
# 3、去MyClass类中寻找有没有__init__的魔法方法，若没有，则执行将开辟内存给对象名：m
# 4、若有__init__的魔法方法，则会进入该方法并执行该方法的动作，之后将内存地址赋值给对象：m
# """
# m = MyClass()
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", m.i)
# print("MyClass 类的方法 f 输出为：", m.f())
# print(m.name)



"""
面向对象：相对于面向过程而言，面向过程时需要关注实现的步骤，
而面向对象时重点关注对象，非过程，把具有相同属性和方法的事物进行抽象封装成类。

python一切皆对象，主要就是面向对象编程，即对其代码进行封装，使其具有更强的灵活性和扩展性。

面向对象技术：
类
对象
属性
方法


"""





# 类定义
# class People:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))

# 单继承
"""
1、若类中不定义__init__,则会调用父类super class的__init__;
2、若类继承父类时也需要定义自己的__init__，则在当前类的__init__中调用一下父类的__init__
3、调用父类三种方法：super().__init__(参数)、super(类名，对象).__init__(参数)
4、若父类有speak()方法，子类也定义一个speak()方法，默认搜索的原则：先找当前子类，若没有再去找父类，即方法的重写（覆盖）
    即，父类提供的方法不能满足子类的需求时，则需要在子类中定义一个同名的方法。
5、子类的方法中也可以调用父类方法：
    super().方法名()
6、父类中私有属性不会被继承    
"""
# class Student(People):
#     grade = ''
#     def __init__(self, n, a, w, g):
#         # 调用父类的构造方法,三种形式都可以
#         # People.__init__(self, n, a, w)  # 第一种写法
#         # super().__init__(n, a, w)   # super()表示父类对象  第二种写法
#         super(Student, self).__init__(n, a, w)  # 和第二种写法唯一区别是加了一个类型判断，判断self对象是不是Student类类型
#         self.grade = g
#
#     # 重写父类的方法
#     def speak(self):
#         print(f"{self.name} 说: 我 {self.age} 岁了，我在读 {self.grade} 年级")

# s = Student('test', 18, 20,5)
# s.speak()


# # 另一个类，多重继承之前的准备
# class Speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name, self.topic))
#
# # 多继承
# class Sample(Speaker, Student):
#     a = ''
#     def __init__(self, n ,a, w, g, t):
#         Student.__init__(self, n, a, w, g)
#         Speaker.__init__(self, n, t)
#
#     # def speak(self):
#     #     print("-----------多继承中的speak方法")
#
# s = Sample('Test', 25, 88, 4, "python")
# s.speak()


"""
多继承搜索顺序：
经典类搜索方式：按照从左至右，深度优先，即先查找自身是否有speak方法，没有则从左只有依次查找，直到找到结束。
新式类搜索方式：采用广度优先的方式查找属性和方法。

注：目前Python3中都是新式类搜索顺序，上述两者的搜索顺序对于Python2来说，或者对于Linux系统自带Python2来说。

方法名同，默认调用在括号中排在前面的父类的方法。
    即：当为class Sample(Speaker, Student)时，调用的是父类Speaker中的speak方法，
        运行返回的结果为：我叫 T，我是一个演说家，我演讲的主题是 python

        当为class Sample(Student, Speaker)时，调用的是父类Student中的speak方法，
        运行返回的结果为：T 说: 我 25 岁了，我在读 4 年级
"""


# # Python3中默认都是新式类，经典类(旧式类)被移除，不必显示的继承object
# # 经典类
# class Service1:
#     pass
#
# # 新式类
# class Service(object):
#     pass
#
# """
# 区别：
# 1、新式类都从object类继承，经典类不需要；
# 2、新式类的MRO(method resolution order 基类搜索顺序)算法采用C3算法广度优先搜索，而旧式类的MRO算法是采用深度优先搜索；
# 3、新式类相同父类只执行一次构造函数，经典类重复执行多次。
# """


# # 方法重写
# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

"""
类与类之间的关系：
1、has a:组合关系，关联关系的一种，即一个类中使用了另一个类的实例
2、is a:表示类之间的继承关系，即类的父子继承关系
"""
# # 实例1
# import random
# # 定义一个Road类
# class Road:
#     def __init__(self, name, len):
#         self.name = name
#         self.len = len
#
# # 定义一个Car类
# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#
#     def get_time(self, road):  # 此时road是Road类的一个对象 即road = r 两者指向同一内存空间地址
#         ran_time = random.randint(1, 10)
#         print(f'{self.brand}品牌的车在{road.name}上以{self.speed}速度行驶了{ran_time}小时')
#
#     def __str__(self):
#         return f'{self.brand}品牌的车，速度为{self.speed}'
#
#
# # 创建实例化对象
# r = Road('京藏高速', 20000)
#
# c = Car('马沙尔拉蒂', 160)
# # print(c)
# # 关联关系，把Road类的对象传入，组合类
# c.get_time(r)


"""
总结：
1、has a :一个类中使用了另外一种自定义的类型，即student使用了computer和book
2、类型：
    系统类型：str、int、float、list、dict、tuple、set
    自定义类型：自定义的类都可以当成一种类型
    s = Student() 说明s是Student类型的对象

"""
# # 实例2 创建了三个自定义类型：Computer类、Book类、Student类
# class Computer:
#     def __init__(self, brand, type, color):
#         self.brand = brand
#         self.type = type
#         self.color = color
#
#     def online(self):
#         print('正在使用电脑上网....')
#
#     def __str__(self):
#         return f'品牌：{self.brand}，型号：{self.type}，颜色：{self.color}'
#
#
# class Book:
#     def __init__(self, book_name, author, number):
#         self.book_name = book_name
#         self.author = author
#         self.number = number
#
#     def __str__(self):
#         return f'书名：{self.book_name}，作者：{self.author}，序号：{self.number}'
#
#
# class Student:  # has a 包含关系，谁里面有谁
#     def __init__(self, name, computer, book):
#         self.name = name
#         self.computer = computer
#         self.books = []
#         self.books.append(book)
#
#     def borrow_book(self, book):
#         for temp in self.books:
#             if temp.book_name == book.book_name:
#                 print('已经借过此书了！')
#                 break
#         else:
#             # 将参数book添加到books列表中
#             self.books.append(temp)
#             print('新书已添加成功！')
#
#     def show_book(self):
#         for temp in self.books:  # temp就是book的一个对象
#             print('目前已有的书', temp)
#
#     def __str__(self):
#         return f'学生姓名：{self.name}，电脑：{self.computer}，书籍：{self.books}'
#
#
# # 创建对象
# computer = Computer('mac', 'mac pro 2020', '银灰色')
#
# book = Book('盗墓笔记', '南派三叔', 16)
# # 对象student包含了computer对象和book对象
# student = Student('test', computer, book)
# print(student)
# # 查看借了哪些书
# student.show_book()
#
# book1 = Book('鬼吹灯', '天下霸唱', 10)
# student.borrow_book(book1)
# print('--------------------------------')
#
# # 再次查看借了哪些书
# student.show_book()


"""
类方法
特点:
1、定义时需要依赖装饰器@classmethod
2、类方法中参数不再是对象，而是类 print('类方法', cls)  # 打印结果为：类方法 <class '__main__.Test'>
3、类方法中只可以使用类的属性
4、类方法中不能调用普通方法
作用：
1、类方法不依赖与对象，可以独立于对象做一些事情
2、因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些功能。

静态方法
特点：
1、与类方法类似，需要装饰器@staticmethod
2、静态方法是无需传递参数的，即不依赖self和cls
3、也只能访问类的属性和方法，通过类名调用

静态方法与类方法的区别：
不同：
    1、装饰器不同
    2、类方法是有参数的，静态方法没有参数

相同：
    1、都只能访问类的属性和方法，对象的是无法访问的
    2、都可以通过类名调用访问
    3、都可以在创建对象之前使用，因为都不依赖于对象

普通方法与两者的区别：
1、没有装饰器
2、普通方法永远是要依赖类的对象，因为每个普通方法都有一个self,而self即为类的对象本身
3、只有创建了对象，即实例化一个类的对象，才可以调用普通方法，否则无法调用

"""

# class Test:
#     # 普通方法 依赖self，即类的对象本身
#     def fun1(self):
#         print('普通方法', self)  # 打印结果为：普通方法 <__main__.Test object at 0x00000266D4E95F98>
#
#     @staticmethod
#     def fun2():
#         print('静态方法')
#
#     @classmethod
#     def fun3(cls):    # cls参数 即class，此时传的是类
#         print('类方法', cls)  # 打印结果为：类方法 <class '__main__.Test'>
#
# # 实例化对象进行调用
# t = Test()
# t.fun1()
# t.fun2()
# t.fun3()
#
# # 静态方法和类方法，也可以无需实例化类对象，通过类名可以调用
# Test.fun2()
# Test.fun3()

"""
魔术方法：是指一个类或对象中的方法，和普通方法唯一的不同是，普通方法需要调用，而魔术方法是在特定时刻自动触发

常用的魔术方法：
1、__init__（重点）: 初始化魔术方法(不是实例化触发，但是和实例化在一个操作中)，至少有一个参数self用来接收对象，无返回值。
2、__new__: 实例化魔术方法，在实例化对象时触发，至少一个cls接收当前的类，必须返回一个对象的实例，
         注：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象，先触发__new__才会触发__init。
3、__del__: 析构魔术方法,当对象没有使用，即没有被任何变量引用时触发,至少有一个参数self用来接收对象，无返回值。
4、__call__:调用对象的魔术方法，将对象当作函数调用时触发，会默认调用__call__函数中的内容，至少有一个参数self用来接收对象，其余根据调用时参数决定。
5、__str__:（重点），打印对象名时，自动触发调用__str__里面的内容，注意需要使用return语句返回需要显示的内容,返回值必须是字符串类型。

"""
# import sys
# class Person:
#
#     # 初始化魔术方法,用来初始化对象成员
#     def __init__(self, name):
#         print(f'--init--获取的内存空间地址为：{self}')  # --init--获取的内存空间地址为：<__main__.Person object at 0x000001D35BCB5EB8>
#         self.name = name
#
#     # 实例化魔术方法,用来实例化对象，即开辟内存空间（地址），且必须返回一个对象的实例(即地址空间)
#     def __new__(cls, *args, **kwargs):
#         print('--new--')
#         result = super(Person, cls).__new__(cls)
#         print(f'--new--开辟的内存空间地址为：{result}')  # --new--开辟的内存空间地址为：<__main__.Person object at 0x000001D35BCB5EB8>
#         return result
#
#     # 调用对象的魔术方法，可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
#     def __call__(self, name):
#         print(f'--call--获得的参数名字为：{name}')
#
#     # 析构魔术方法
#     def __del__(self):
#         print(f'--------del---------')
#
# # 实例化调用时运行的顺序是，先执行__new__，申请开辟内存空间，然后把返回的对象实例(即__new__开辟的内存空间地址)传递
# # 给__init__中的self，执行完__init__之后,再赋值给p.
# p = Person('cll')
# print(f'最终实例化对象p的内存空间地址为：{p}')  # 最终实例化对象p的内存空间地址为：<__main__.Person object at 0x000001D35BCB5EB8>
#
# # 想把对象当作函数调用则重写__call__方法即可
# p('test')  # 此时默认调用__call__
#
# # 增加一个p对象的引用
# p1 = p  # 此时p1与p共同指向同一内存地址
# p1.name = 'cll'
# print(p.name)
#
# # 删除一个对象引用时会调用析构魔法方法
# del p1  # 删除p1对地址的引用
# # 查看p对象，即内存地址被引用的次数
# print('查看地址引用次数为：', sys.getrefcount(p)-1)
# # 当一块内存地址没有任何引用时，会默认执行__del__析构魔法方法
# del p


# class Person:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#
#      def __str__(self):
#          return f'姓名：{self.name},年龄：{self.age}'
#
#
# p = Person('test', 18)
# """
# 若没有__str__，单纯打印对象p，则显示的为内存地址<__main__.Person object at 0x00000262F60D5AC8>
# 若有__str__，则自动调用__str__魔法方法，打印里面的内容
# """
# print(p)



"""
私有化
封装两大特点：1、私有化属性 2、定义公有的set和get方法
优点：
1、隐藏属性不被外界随意修改，保证数据的安全性
2、可以通过自定义的set函数进行过滤，符合条件的参数进行修改
3、可以使用自定义的get函数获取具体的某个属性

"""
# class Student:
#
#      def __init__(self, name, age):
#          self.__name = name
#          self.__age = age
#          self.__score = 60
#
#      # 因为属性全部私有化了，外界无法调用和修改，因此提供公有的set和get方法,同时私有化属性之后还可以对外界的值进行限定
#      # 重新对私有化属性进行赋值
#      def set(self, name, age, score):
#          if len(name) > 0 and len(name) < 6:
#             self.__name = name
#          else:
#              print('姓名长度需在0-6位！')
#          if age > 0 and age < 120:
#             self.__age = age
#          else:
#             print('年龄不在指定的范围内！')
#          if score > 0 and score < 100:
#             self.__score = score
#          else:
#              print('分数不在指定的范围内！')
#
#      # 获取属性的值
#      def get(self):
#          return f'姓名：{self.__name}，年龄：{self.__age}，考试分数：{self.__score}'
#
#
#      def __str__(self):
#          return f'姓名：{self.__name}，年龄：{self.__age}，考试分数：{self.__score}'
#
#
# s = Student('test', 18)
# print(f'赋值前的打印结果：{s}')
#
# s.set('test', 20, 99)
# # print(f'赋值后的打印结果：{s}')
# # 或者采用get方法获取属性值
# result = s.get()
# print(print(f'赋值后的打印结果：{result}'))


"""
采用装饰器@property形式进行私有化属性
"""
# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     # 先有get的方法
#     @property
#     def age(self):
#         return self.__age
#
#     # 再有set的方法，因为set的方法装饰器依赖于get方法的装饰器，若两者顺序有误会报错，固定格式
#     @age.setter
#     def age(self, age):
#         if age > 0 and age < 120:
#             self.__age = age
#         else:
#             print('年龄不在指定的范围内！')
#
#
# # 没有私有化的name属性外界修改方式
# s = Student('test', 19)
# s.name = 'test1'
# print(s.name)
#
# # 为了能像name属性在外界修改方式一样的方便，采用@property装饰器的形式对私有化属性__age进行装饰
# s.age = 55   # 注意这里调用的age()方法在类中加了装饰器，因此外界调用时可以像name属性一样的调用，无需后面加()
# print(s.age)


# # 运算符重载
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     # 加运算符重载
#     def __add__(self, other):
#         if other.__class__ is Vector:
#             return Vector(self.a + other.a, self.b + other.b)
#         elif other.__class__ is int:
#             return Vector(self.a + other, self.b)
#
#     # 加运算运算符反向重载
#     def __radd__(self, other):
#         """反向算术运算符的重载
#         __add__运算符重载可以保证V+int的情况下不会报错，但是反过来int+V就会报错，通过反向运算符重载可以解决此问题
#         """
#         if other.__class__ is int or other.__class__ is float:
#             return Vector(self.a + other, self.b)
#         else:
#             raise ValueError("值错误")
#
#     #  减运算符重载
#     def __sub__(self, other):
#         if other.__class__ is Vector:
#             return Vector(self.a - other.a, self.b - other.b)
#         elif other.__class__ is int:
#             return Vector(self.a - other, self.b)
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)
# print(v1 + 5)
# print(6 + v2)
# print(2 + 3)
# print(3 - 2)
# print(v1 - v2)


"""
面向对象的三大特点：封装、继承、多态

python中没有严格的多态

多态

"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def feed_pet(self, pet):  # pet即可以接收cat，也可以接收dog，或者其他类型
#         # isinstance(obj,类)  --->判断obj是不是类的对象或者是不是该类子类的对象
#         if isinstance(pet, Pet):  # Python通过isinstance实现多态的特点
#             print(f'{self.name}喜欢养宠物：{pet.role},昵称是：{pet.pet_name}')
#         else:
#             print('危险宠物！')
# class Pet:
#     role = 'Pet'
#     def __init__(self, pet_name, age):
#         self.pet_name = pet_name
#         self.age = age
#
#     def show(self):
#         print(f'宠物名字{self.pet_name}，年龄：{self.age}')
#
# class Cat(Pet):
#     role = 'cat'
#     def catch_mouse(self):
#         print('喜欢吃鱼')
#
# class Dog(Pet):
#     role = 'dog'
#     def watch_door(self):
#         print('喜欢吃骨头')
#
# # 创建对象
# cat = Cat('喵喵', 3)
#
# dog = Dog('金毛', 5)
#
# person = Person('小明')
# person.feed_pet(cat)
# person.feed_pet(dog)


"""
单例模式：即一个类有且仅有一个实例。
作用：
    单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例：如果实例不存在，
    会创建一个实例；如果已存在就会返回这个实例。

"""
# 单例模式实现方法有多种，这里采用常用的基于__new__方法实现，此外还可以通过类的装饰器等进行实现。
"""
实现原理：
1、一个类实例化过程(创建对象)，首先是先执行类的__new__方法，若没写该方法，则默认调用父类object的__new__方法，并返回
   一个类的实例化对象，之后再调用__init__方法对该对象进行初始化。
2、在一个类的__new__方法中先判断是不是存在实例化的对象，若存在，则直接返回该结果，若不存在，则新创建。
3、因此我们可以通过重写 __new__方法去实现类只创建一个实例，即实现单例模式。
"""
# class Singleton:
#     # 私有化属性，用于存放单例的地址，默认为空
#     __instance = None
#     # 重写__new__方法
#     def __new__(cls, *args, **kwargs):
#         print('------已进入重写方法__new__中-------')
#         # 判断实例化的对象是否存在，若为空，则新创建
#         if cls.__instance is None:
#             print('此时对象为空，表示第一次创建对象，准备新建')
#             # 通过父类object中的__new__方法创建对象
#             cls.__instance = object.__new__(cls)
#             print(f'新建对象的地址为：{cls.__instance }')
#             # 此时把创建好的对象传入给父类object中的__init进行初始化，初始化完毕之后，把结果赋值给s
#             return cls.__instance
#         # 若不为空，则直接返回上一次对象的引用
#         else:
#             print('对象已存在，直接返回')
#             # 此时把上一次已存在的对象传入给父类object中的__init进行初始化，初始化完毕之后，把结果赋值给s1
#             return cls.__instance
#
# # 第一次创建一个对象时，此时对象是为空的，准备新建
# s = Singleton()
# print(s)
#
# # 再次实例化一个对象时，对象已经存在了，直接返回上一次对象地址即可，因此确保了两次对象创建的地址是同一个
# s1 = Singleton()
# print(s1)

# 运行的结果为：
# ------已进入重写方法__new__中-------
# 此时对象为空，表示第一次创建对象，准备新建
# 新建对象的地址为：<__main__.Singleton object at 0x000002C396B15A90>
# <__main__.Singleton object at 0x000002C396B15A90>
# ------已进入重写方法__new__中-------
# 对象已存在，直接返回
# <__main__.Singleton object at 0x000002C396B15A90>


# total = 0  # 定义一个全局变量
#
# # 可写函数说明
# def sum(arg1, arg2):
#
#     global total         # 采用global关键字修改全局作用域
#     print("函数外是全局变量1 : ", total)
#     # 返回2个参数的和."
#     total = arg1 + arg2  # total在这里是局部变量.
#     print("函数内是局部变量 : ", total)
#     return total
#
# # 调用sum函数
# sum(10, 20)
# print("函数外是全局变量2 : ", total)
#
# # 运行结果：
# # 函数外是全局变量1 :  0
# # 函数内是局部变量 :  30
# # 函数外是全局变量2 :  30


# def outer():
#     total = 10   # outer函数局部变量
#     def inner():
#         nonlocal total   # 采用nonlocal关键字修改嵌套作用域中的局部变量total
#         total += 100
#         print('函数内是局部变量1:', total)
#
#     inner()  # 内部函数调用
#     print('函数内是局部变量2:', total)
#
#
# outer()
#
# # 运行结果：
# # 函数内是局部变量1: 110
# # 函数内是局部变量2: 110



# import glob
# r = glob.glob('*.py')
#
# print(r)


# 正则表达式
import re

# # match() 从字符串的起始位置（开头）匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# # 其中group() 用于返回被 RE 匹配的字符串
# str = 'www.baiadu.com'
# result = re.match('www', str)
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
#
# result1 = re.match('com', str)
# print(result1)
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 3)
# # 匹配成功获取的内容为：www
# # None


# # search() 扫描整个字符串并返回第一个成功的匹配，若匹配成功则返回一个匹配的对象，否则返回None
# str = 'www.baiadu.com www.qq.com'
# result = re.search('www', str)
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
# result1 = re.search('com', str)
# print(result1)
#
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 3)
# # 匹配成功获取的内容为：www
# # <_sre.SRE_Match object; span=(11, 14), match='com'>


# re.match 只匹配字符串的开始，如果字符串开始位置不符合正则表达式，则匹配失败，函数返回 None，
# 而 re.search 匹配整个字符串，直到找到一个匹配


# # findall() 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# # 注意： match 和 search 是匹配一次,而findall是匹配所有
# # c6d  f88f  j5f  d99a
# str = 'abc6dff88fdj5fd99aa7'
# result = re.findall('[a-z][0-9]+[a-z]', str)
# print(f'返回匹配成功的列表为：{result}')
#
# # 运行的结果为：
# # 返回匹配成功的列表为：['c6d', 'f88f', 'j5f', 'd99a']


# # finditer() 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# # c6d  f88f  j5f  d99a
# str = 'abc6dff88fdj5fd99aa7'
# result = re.finditer('[a-z][0-9]+[a-z]', str)
# print(f'返回匹配成功的列表为：{result}')
# # 对迭代器的进行遍历取值
# for temp in result:
#     print(temp.group())
#
# # 运行的结果为：
# # 返回匹配成功的列表为：<callable_iterator object at 0x000001A186E74C18>  # 返回的是一个迭代器
# # c6d
# # f88f
# # j5f
# # d99a


# # sub(正则表达式，'新内容'，string) 用于替换字符串中的匹配项，替换的新内容可以采用函数形式
#
# # 例1：移除非数字的内容
# phone = "186aA81B6c9b8%!8d88e#"
# result = re.sub(r'\D', "", phone)
# print(f"替换后的电话号码为:{result} ")
#
# # 运行的结果为：
# # 替换后的电话号码为:18681698888
#
# # 例2：替换新内容参数为函数的形式
# def func(param):
#     num = int(param.group())
#     num += 1
#     return str(num)
#
# msg = 'Java:95 Python:98 C:99'
# result = re.sub(r'\d+', func, msg)
# print(result)
#
# # 运行的结果为：
# # Java:96 Python:99 C:100


# # split():按照能够匹配的子串将字符串分割后返回列表
# msg = 'Java:95,Python:98,C:99'
# result = re.split(r'[,:]', msg)  # 在字符串中搜索，如果遇到:或者,就分割，并将分割后的内容以列表的形式返回
# print(result)
#
# # 运行的结果为：
# # ['Java', '95', 'Python', '98', 'C', '99']


# # # re.I使匹配对大小写不敏感
# res = re.findall(r"A", "abcAcgfAa", re.I)
# print(res)


# # qq号验证
# # 规则：5-12位且开头不能是0
# qq = '135467676511'
# result = re.match('^[1-9]\d{4,11}$', qq)  # ^和$表示从头到尾，把正则表达式当成一个整体进行匹配
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
#
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 12)
# # 匹配成功获取的内容为：135467676511

# # 用户名验证
# # 规则：用户名可以是数字、字母或下划线，开头不能是数字，用户名长度为6位以上15位以下
# username = 'admin_cll_888'
# result = re.search('^[a-zA-Z]\w{5,14}$', username)
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
#
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 13)
# # 匹配成功获取的内容为：admin_cll_888

# # 匹配0-100的整数
# num = '66'
# result = re.match(r'^[1-9]?\d?$|100$', num)
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
#
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 2)
# # 匹配成功获取的内容为：66

# # 邮箱验证是否为qq、163、126邮箱
# email = '504870987@qq.com'
# result = re.match(r'^\w{5,12}@(qq|163|126)\.(com|cn)$', email)
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
#
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 16)
# # 匹配成功获取的内容为：504870987@qq.com

# # 判断一个字符串是否为手机号(11位),且尾号不是4,7
# phone = '13686698888'
# result = re.match(r'^1[345789]\d{3,8}[0-35-689]$', phone)
# print('匹配成功返回的位置为：{}'.format(result.span()))   # 用于返回位置
# print(f'匹配成功获取的内容为：{result.group()}')          # 获取匹配的内容
#
# # 运行的结果为：
# # 匹配成功返回的位置为：(0, 11)
# # 匹配成功获取的内容为：13686698888

# # 匹配带区号（3位或4位区号）的座机号码
# # 采用()分组的形式进行匹配
# tel = '021-1234567'
# result = re.match(r'(\d{3}|\d{4})-(\d{7}$)', tel)
# print(result)
# print("获取分组1的内容：", result.group(1))  # 获取匹配成功后的第一个分组的内容
# print("获取分组2的内容：", result.group(2))  # 获取匹配成功后的第二个分组的内容
#
# # 运行的结果为：
# # <_sre.SRE_Match object; span=(0, 11), match='021-1234567'>
# # 获取分组1的内容： 021
# # 获取分组2的内容： 1234567

# 获取图片名称
# url = "http://172.16.230.87:20150/pics/ipcpic/32010400001320030078/2020081208/2fd50009-9c2b-4a90-ac77-581aa4c5cc86_82316542_203393.jpg"

# # 方法一：采用字符串内置函数rfind从右开始查找
# index = url.rfind('/')
# result = url[index+1:]
# print(f'图片的名称为：{result}')

# # 方法二采用正则表达式（有问题待完善）
# result = re.findall(r'(/.+?\.jpg)', url)
# print(f'图片的名称为：{result}')


# # 标签内容匹配
# msg = '<html>hello cll@kedacom.com</html>'
# msg1 = '<div>hello cll@kedacom.com</html>'
# # 该种方法存在前后标签不同时也能匹配成功的问题 即msg1形式
# result = re.match(r'<\w+>(.+)</\w+>', msg1)
# print(result)
#
# # # 采用引用位置的形式使得匹配前后标签对应
# # result = re.match(r'<(\w+)>(.+)</\1>$', msg)
# # print(result)
# # print(result.group(1))
# # print(result.group(2))


# # 采用\1...\9数字的形式进行引用分组匹配  这里采用两个分组\1 \2
# msg2 = '<html><h1>hello cll@kedacom.com</h1></html>'
# result = re.match(r'<(\w+)><(\w+)>(.+)</\2></\1>$', msg2)
# print(result)
# print("获取分组1的内容：", result.group(1))
# print("获取分组2的内容：", result.group(2))
#
# # 运行的结果为：
# # <_sre.SRE_Match object; span=(0, 43), match='<html><h1>hello cll@kedacom.com</h1></html>'>
# # 获取分组1的内容： html
# # 获取分组2的内容： h1
#
# # 采用起名的方式进行引用分组匹配
# # 语法格式：(?P<名字>正则表达式)    (?P=名字)
# msg3 = '<html><h1>hello cll@kedacom.com</h1></html>'
# result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg3)
# print(result)
# print("获取分组1的内容：", result.group(1))
# print("获取分组2的内容：", result.group(2))
# print("获取分组3的内容：", result.group(3))
#
# # 运行的结果为：
# # <_sre.SRE_Match object; span=(0, 43), match='<html><h1>hello cll@kedacom.com</h1></html>'>
# # 获取分组1的内容： html
# # 获取分组2的内容： h1
# # 获取分组3的内容： hello cll@kedacom.com


# # 采用？将贪婪模式转换为非贪婪模式
# msg = 'cll168cll'
# result = re.match(r'cll(\d+?)', msg)
# print(result)


# # 通过正则表达式匹配图片路径并下载到本地实例
# import requests
#
# path = '<img class="content-picture" src="http://172.16.230.87:20150/pics/ipcpic/3201040000132' \
#        '0030078/2020081208/2fd50009-9c2b-4a90-ac77-581aa4c5cc86_82316542_203393.jpg">'
# result = re.match(r'<img class="content-picture" src="(.*?)"', path)
# # 通过正则匹配获取需要的图片路径
# image_path = result.group(1)
# # 获取图片内容
# ret = requests.get(image_path)
# # 将图片写入当前文件夹
# with open("test.jpg", "wb") as wstream:
#     wstream.write(ret.content)



# import calendar
#
# cal = calendar.month(2020, 8)
# print("以下输出2020年8月份的日历:")
# print(cal)


# import re
# s = '<div class="name">python</div>'
# result = re.search(r'<div class=(.*)>(.*?)</div>', s)
#
# print(result.group(1))
# print(result.group(2))


"""
GIL锁
Python在设计的时候，还没有多核处理器的概念。
因此，为了设计方便与线程安全，直接设计了一个锁。
这个锁要求，任何进程中，一次只能有一个线程在执行。
因此，并不能为多个线程分配多个CPU。所以Python中的线程只能实现并发，而不能实现真正的并行。

但是Python3中的GIL锁有一个很棒的设计，在遇到阻塞（不是耗时）的时候，会自动切换线程。

"""


"""
并发与并行:
并发：当有多个线程在操作时，若系统只有一个CPU，则它根本不可能真正同时进行一个以上的线程，它只能把CPU
      运行时间划分成若干个时间段，再将时间段分配给各个线程执行，在一个时间段的线程代码运行时，其它线
      程处于挂起状态，这种方式称为并发（concurrent）。
 
      一个CPU的时候运行，轮询调度实现并发执行
      
并行：当系统有一个以上的CPU时，则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另
      一个线程，两个线程互相不抢占CPU资源，可以同时进行，这种方式称为并行（parallel）。

实现多任务的方式：
     多进程模式
     多线程模式
     协程

进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，
               是操作系统结构的基础。在当代面向线程设计的计算机结构中，进程是线程的容器。程序是指令、
                数据及其组织形式的描述，而进程是程序的实体。
                
                表示的一个正在执行的程序。每个进程都拥有自己的地址空间、内存、数据栈以及其他用于跟
                踪执行的辅助数据操作系统负责其上所有进程的执行，操作系统会为这些进程合理地分配执行时间。
                
进程举例： 对于操作系统来说，一个任务就是一个进程，比如打开浏览器就是启动一个浏览器进程，打开记事本就是启动一个记事本进程                
   
多进程调用是没有顺序的，取决于CPU的调度
   
进程优缺点：   
    优点：稳定性高，一个进程崩溃了，不会影响其他的进程
    缺点：创建进程开销巨大，且操作系统能同时运行进程数量有限
 
与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内。
 
进程创建：
process = Process(target=函数名, name=进程名字, args=(传递的参数)) 
process为进程对象
对象调用方法：
process.start()  # 启动进程并执行任务
process.run()    # 只是执行了任务但是没有启动进程
process.terminate() # 终止进程
             
"""
# import time
# import os
# from multiprocessing import Process
#
# # 多进程对于全局变量的访问，在每一个全局变量里面都放一个m变量，保证每个进程访问变量互不干扰,即进程间不共享全局变量，或者说共享全局变量时，各自有一份
# # 定义全局变量可变和不可变类型
# m = 1  # 不可变类型
# list1 = []  # 可变类型
#
# def task1(s, name):
#     global m
#     while True:
#         time.sleep(s)
#         m += 1
#         list1.append(str(m) + 'task1')
#         print(f'这是{name}------当前进程id为：{os.getpid()}-------父进程id为：{os.getppid()}, 不可变类型变量m的值为{m}, 可变类型list1的值为{list1}')
#
#
# def task2(s, name):
#     global m
#     while True:
#         time.sleep(s)
#         m += 1
#         list1.append(str(m) + 'task2')
#         print(f'这是{name}------当前进程id为：{os.getpid()}-------父进程id为：{os.getppid()}, 不可变类型变量m的值为{m}, 可变类型list1的值为{list1}')
#
#
# # 定义个全局变量 用来测试进程退出问题
# number = 0
#
# if __name__ == '__main__':
#     # main此时为主进程
#     print(os.getpid())
#     # 在main主进程下创建一个子进程
#     p1 = Process(target=task1, name='任务名称1', args=(1, '任务1'))
#     p1.start()
#     print(p1.name)
#     # 在main主进程下再创建一个子进程
#     p2 = Process(target=task2, name='任务名称2', args=(1, '任务2'))
#     p2.start()
#     print(p2.name)
#
#     while True:
#         number += 1
#         time.sleep(0.5)
#         m += 1
#         print(f'不可变类型变量m的值为{m}')
#         if number == 50:
#             p1.terminate()
#             p2.terminate()
#             break
#         else:
#             print(f'当前number为--->{number}')




# # 自定义进程
#
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     # 重写run方法
#     def run(self):
#         n = 1
#         while True:
#             print(f'{n}---------->自定义进程，n:{self.name}')
#             n += 1
#             time.sleep(1)
#
# if __name__ == '__main__':
#     p1 = MyProcess('路路1')
#     p1.start()   # 此处做了2步，1，开新的进程，2，调用run()方法
#
#     p2 = MyProcess('路路2')
#     p2.start()


"""
进程池 

Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，就重用进程池中的进程。

当需要创建的子进程数量不多时，可以直接利用Process动态生成多个进程即可，
但是如果需要创建成百上千个进程的话，手动创建工作量巨大，且消耗内存空间资源等巨大，
此时就需要使用Pool来创建进程池，以达到进程复用的效果，
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
则会创建一个新的进程用来执行该请求，如果池中的进程数已经达到指定时的最大值（即池已满），
则该请求会等待，直到池中有进程结束，才会创建新的进程来执行。

进程池模式：
非阻塞式：把全部东西添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务之后才调用。
          非阻塞式可以最大化的利用CPU，达到程序的高效使用。

阻塞式：

"""

# # 非阻塞式
#
# from multiprocessing import Pool
# import time
# from random import random
# import os
#
# def task(task_name):
#     print('启动任务', task_name)
#     start = time.time()
#     time.sleep(random() * 2)
#     end = time.time()
#     # print(f'完成任务：{task_name}，用时为：{end-start},进程id为：{os.getpid()}')
#     return f'完成任务：{task_name}，用时为：{end-start},进程id为：{os.getpid()}'
#
# receive_list = []
# # 回调函数
# def callback_func(param):
#     receive_list.append(param)
#
# if __name__ == '__main__':
#     # 创建进程池，最大进程数为5
#     pool = Pool(5)
#     task_lists = ['听音乐', '看电影', '追剧', '看书', '敲代码', '逛超市', '散步', '打麻将']
#     for temp in task_lists:
#         pool.apply_async(task, args=(temp,), callback=callback_func)
#
#     pool.close()  # 添加任务结束
#     pool.join()   # 堵住主进程，相当于插队，插在主进程的前面，子进程不结束，主进程就不会往下走 即使主进程让步
#
#     for i in receive_list:
#         print(f'回调函数接收的参数列表内容：{i}')
#
#     print('over!!!!!!!!!!!')



"""
阻塞式
apply阻塞式：每运行一下，添加一个任务执行一个任务，该任务不结束，下面的任务就不添加不进来，比如听音乐先进来，不结束的话，下一个看电影就添加不进来

阻塞式一个任务一个任务进来，进去一个创建一个新进程，结束之后再进来第二个任务，再创建一个新进程，刚才的第一个进程处于闲置状态，
直到5个任务依次进来，一共创建了5个进程之后，后续再有任务进来，则从第一个进程开始复用，以此类推。

"""

# from multiprocessing import Pool
# import time
# from random import random
# import os
#
# def task(task_name):
#     print('启动任务', task_name)
#     start = time.time()
#     time.sleep(random() * 2)
#     end = time.time()
#     print(f'完成任务：{task_name}，用时为：{end-start},进程id为：{os.getpid()}')
#
#
#
# if __name__ == '__main__':
#     # 创建进程池，最大进程数为5
#     pool = Pool(5)
#     task_lists = ['听音乐', '看电影', '追剧', '看书', '敲代码', '逛超市', '散步', '打麻将']
#     for temp in task_lists:
#         pool.apply(task, args=(temp,))
#
#     pool.close()  # 添加任务结束
#     pool.join()   # 堵住主进程，相当于插队，插在主进程的前面，子进程不结束，主进程就不会往下走 即使主进程让步
#
#     print('over!!!!!!!!!!!')


# 进程间通信
# 进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列(Queue)和管道(Pipe)
# Queue只是实现了进程间数据交互，并没实现数据共享，即没有实现一个进程去更改另一个进程的数据。
##########
# 队列方式
##########
# from multiprocessing import Queue   # 进程队列，注意线程有线程队列，处于不同模块中
# from multiprocessing import Process
# import time
# import os
#
# def task1(q):
#     task_lists = ['听音乐', '看电影', '追剧', '看书', '敲代码', '逛超市', '散步', '打麻将']
#     for temp in task_lists:
#         print(f'正在添加任务:{temp},进程id:{os.getpid()}')
#         q.put(temp)  # 向队列中添加任务，最多添加5个，若果队列添加满了，则等待队列中有任务被取出才会继续添加新任务
#         time.sleep(0.5)
#
# def task2(q):
#     while True:
#         try:
#             data = q.get(timeout=3)   # 如果队列为空，则会一直阻塞,直到有数据,若加了timeout则会报错异常，不会一直等待
#             print(f'{data}:任务执行成功！进程id:{os.getpid()}')
#         except Exception as e:
#             print(f'所有任务全部执行完毕！')
#             break
#
# if __name__ == '__main__':
#     q = Queue(5)  # 创建个长度为5的队列 用于两个进程之间的通信
#     print(f'主进程id:{os.getpid()}')
#     p1 = Process(target=task1, name='进程1', args=(q,))
#     p1.start()
#
#     p2 = Process(target=task2, name='进程2', args=(q,))
#     p2.start()
#
#     p1.join()
#     p2.join()


##########
# 管道方式
##########
# Pipe对象返回的元组分别代表管道的两端，管道默认是全双工，两端都支持send和recv方法，
# 两个进程分别操作管道两端时不会有冲突，两个进程对管道一端同时读写时可能会有冲突
# from multiprocessing import Process, Pipe
# import time
# import os
#
# def task1(conn):
#     task_lists = ['听音乐', '看电影', '追剧', '看书', '敲代码', '逛超市', '散步', '打麻将']
#     for temp in task_lists:
#         print(f'正在添加任务:{temp},进程id:{os.getpid()}')
#         conn.send(temp)
#         time.sleep(0.5)
#
# def task2(conn):
#     while True:
#         data = conn.recv()
#         print(f'{data}:任务执行成功！进程id:{os.getpid()}')
#
#
# if __name__ == '__main__':
#     # Pipe实例化返回一个元祖对象，分别给到进程1端口和进程2端口
#     # Pipe(duplex=True):在进程之间创建一条管道，并返回元组（task1_conn,task2_conn）,其中task1_conn，task2_conn表示管道两端的连接对象，
#     # 注：必须在产生Process对象之前产生管道
#     # dumplex:默认管道是全双工的(双向管道)，如果将duplex设置成False(单向管道)，task1_conn只能用于接收，task2_conn只能用于发送;
#     # (一个进程只负责写，一个进程只负责读，否则一个进程既有读又有写，可能出现堵塞)
#     task1_conn, task2_conn = Pipe(duplex=False)
#     print(f'主进程id:{os.getpid()}')
#     p1 = Process(target=task1, name='进程1', args=(task2_conn,))
#     p1.start()
#
#     p2 = Process(target=task2, name='进程2', args=(task1_conn,))
#     p2.start()
#
#     p1.join()
#     p2.join()





"""
线程(也称为轻量级进程)，它是程序执行流的最小单元。线程依赖于进程，它是进程中的一个实体，是被系统独立
调度和分派的基本单位，线程自己不拥有系统资源，但可以与同一个进程中的其他线程共享该进程所拥有的全部资源。
同一个进程中的多线程之间可以并发执行，线程也有就绪、阻塞和运行三种基本状态。
每一个程序，即每一个进程至少有一个线程。

与进程类似，不过它们是在同一个进程下执行的，并且它们会共享相同的上下文。
当其他线程运行时，它可以被抢占（中断）；
和临时挂起（也成为睡眠） — 让步；
线程的轮训调度机制类似于进程的轮询调度。
只不过这个调度不是由操作系统来负责，而是由Python解释器来负责。


多线程：指从软件或者硬件上实现多个线程并发执行的技术。

优点：
使用线程可以把占据长时间的程序中任务放到后台处理；
前端页面更加优美，可以弹出进度条来显示处理的进度；
程序运行的速度加快；
在一些等待的任务实现如用户输入、文件读写和网络收发数据等。线程比较常用，从而使得
释放资源等

创建一个进程，CPU给分配一块固定的内存空间，线程依赖于进程，即线程只能在这个进程的内存空间里活动，且该进程内的多个线程
共享这片内存空间资源。

多线程之间的调度也是没有顺序的，取决于CPU

为了设计方便与线程安全，直接设计了一个锁。
这个锁要求，任何进程中，一次只能有一个线程在执行。
因此，并不能为多个线程分配多个CPU。所以Python中的线程只能实现并发，而不能实现真正的并行。

但是Python3中的GIL锁有一个很棒的设计，在遇到阻塞（不是耗时）的时候，会自动切换线程。


线程的状态：
新建 就绪 运行 阻塞 结束


"""

# # 多线程实例
# import time
# import threading
#
# def task1(n):
#     task_lists = ['看电影', '追剧', '看书', '敲代码', '逛超市', '散步', '打麻将']
#     for temp in task_lists:
#         print(f'正在{temp}任务！')
#         time.sleep(n)
#
#
# def task2(n):
#     musics = ['后来', '晚安', '飞鸟与蝉', '生而平凡', '平凡之路']
#     for music in musics:
#         print(f'正在听{music}这首歌！')
#         time.sleep(n)
#
# if __name__ == '__main__':
#     n = 1
#     t = threading.Thread(target=task1, name='线程1', args=(n,))
#     t.start()
#
#     t = threading.Thread(target=task2, name='线程2', args=(n,))
#     t.start()


"""
线程池：本质还是基于多线程，只是对开启线程的数量进行了限制；
使用原因：
大量创建线程，会消耗过多的CPU，影响系统的稳定。


优点：
降低资源消耗；
提高响应速度；
提高线程的可管理性；

目前线程池与进程池的主流模块concurrent.futures：
    concurrent.futures 模块提供异步执行可调用对象高层接口;
    管理并发任务池，concurrent.futures模块提供了使用工作线程或进程池运行任务的接口；
    线程和进程池API都是一样，所以应用只做最小的修改就可以在线程和进程之间地切换；
    ThreadPoolExecutor：线程池，提供异步调用；
    ProcessPoolExecutor: 进程池，提供异步调用；

基本方法：
1、submit(self, fn, *args, **kwargs)----提交任务
2、map(func, *iterables, timeout=None, chunksize=1)----取代for循环submit的操作
3、shutdown(wait=True):
    相当于之前进程池Pool模块的pool.close()+pool.join()操作；
    wait=True，等待池内所有任务执行完毕且释放已分配的资源后才返回；
    wait=False，立即返回，并不会等待池内的任务执行完毕；
    但不管wait参数为何值，整个程序都会等到所有任务执行完毕才会退出；
    submit和map必须在shutdown之前；
4、result(timeout=None)----取得结果
5、add_done_callback(fn)---回调函数

回调函数：
    可以为进程池或线程池内得每个进程或线程绑定一个函数，该函数在进程或线程的任务执行完毕后自动触发，
    并接受任务的返回值当作参数，该函数成为回调函数。

submit提交任务的两种方法：
1、同步调用：提交完任务后，就在原地等待任务执行完毕，拿到结果，在执行下一行代码，导致程序是串行；
2、异步调用：提交完任务后，不用原地等待任务执行完毕；


"""
# # 线程池与进程池实例
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed  # 目前进程池和线程池主流模块
# import time
# from random import random
# import os
#
# def task(task_name):
#     # print(f'启动任务:{task_name}，进程id为：{os.getpid()}') # 测试进程池时打印id
#     print(f'启动任务:{task_name}')
#     start = time.time()
#     time.sleep(random() * 2)
#     end = time.time()
#     # print(f'完成任务：{task_name}，用时为：{end-start},进程id为：{os.getpid()}')  # 测试进程池时打印id
#     # print(f'完成任务：{task_name}，用时为：{end - start}')
#     return f'完成任务：{task_name}，用时为：{end - start}'
#
# # 回调函数(同步调用测试时使用)
# def call_back_1(param):
#     print(f'回调函数拿到的结果为：{param}')
#
# # 回调函数(异步调用测试时使用)
# def call_back_2(param):
#     ret = param.result()
#     print(f'回调函数拿到的结果为：{ret}')
#
#
# if __name__ == '__main__':
#     # 模拟任务列表
#     task_lists = ['听音乐', '看电影', '追剧', '看书', '敲代码', '逛超市', '散步', '打麻将']
#     # 创建线程池方法一：创建线程池，最大线程数为5，需配合shutdown(True)使用
#     thread_pool = ThreadPoolExecutor(max_workers=5)   # 此处把ThreadPoolExecutor换成ProcessPoolExecutor就是进程池，其余用法全部相同
#
#     # # 创建线程池方法二：采用with语句避免了显式调用shutdown(True)方法，但需注意需缩进代码块
#     # with ThreadPoolExecutor(max_workers=5) as thread_pool:
#
#     # # 同步调用测试代码部分，即提交完一个任务后，就在原地等待该任务执行完毕，拿到结果，在执行下一行代码，导致程序是串行；
#     # for temp in task_lists:
#     #     ret = thread_pool.submit(task, temp).result()
#     #     call_back_1(ret)
#
#     # # 异步调用测试代码部分，即提交完一个任务后，不用原地等待该任务执行完毕，继续执行下面的代码
#     # for temp in task_lists:
#     #     thread_pool.submit(task, temp).add_done_callback(call_back_2)
#
#     # # 采用map方法调用,这里的map方法与python高阶函数map的含义相同，都是将序列中的每个元素都执行同一个函数
#     # results = thread_pool.map(task, task_lists)  # 返回的类型是<class 'generator'> 生成器
#     # # 获取结果 ，map方法返回的结果是有序的
#     # for result in results:
#     #     print(result)
#
#     # # as_completed方法调用，当子线程中的任务执行完后，直接用result()获取返回结果
#     # obj_list = []
#     # for temp in task_lists:
#     #     ret = thread_pool.submit(task, temp)
#     #     obj_list.append(ret)
#     # # as_completed()方法是一个生成器，在没有任务完成的时候，会一直阻塞，除非设置了timeout,先完成(失败)的任务会先返回给主线程。
#     # for future in as_completed(obj_list):
#     #     result = future.result()
#     #     print(result)
#
#     thread_pool.shutdown(True)
#     print('over!!!!!!!!!!!')


"""
线程与进程不同，线程是可以共享全局变量的,但会出现共享数据不安全的问题，原因是由于计算量较大，GIL锁自动释
放（原本Python底层只要用线程默认加锁）；
共享数据：
若多个线程对某个数据进行修改，则可能出现不可预料的结果，为了保证数据的安全性，此时就需要对多个线程进行同步，
（即：一个一个的完成，一个线程做完，另一个线程才能进来）；

线程同步之后解决了数据安全问题，但是会导致速度慢，效率低，实现了并发执行，但没有实现真正的并行执行。

常见的线程同步方式：加锁，队列，管道；

线程使用的场景：耗时操作、爬虫，IO等
进程使用的场景：计算密集型
"""
# import threading
# import time
# tickets = 5000000
# # 获取锁对象
# lock = threading.Lock()
#
# def task1():
#     # 获取线程锁，如果已经上锁，则等待锁的释放
#     lock.acquire()  # 阻塞
#     global tickets
#     for i in range(1000000):
#         tickets -= 1
#         # time.sleep(0.5)
#     lock.release()
#
# def task2():
#     # 获取线程锁，如果已经上锁，则等待锁的释放,如果不释放其他线程都无法进入运行状态
#     lock.acquire()  # 阻塞
#     global tickets
#     for i in range(2000000):
#         tickets -= 1
#         # time.sleep(0.5)
#     lock.release()
#
#
# if __name__ == '__main__':
#
#     t1 = threading.Thread(target=task1, name='进程t1')
#     t1.start()
#
#     t2 = threading.Thread(target=task2, name='进程t2')
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(f'剩余票数:{tickets}')


"""
死锁产生原因：
开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分
资源并且同时等待对方释放资源的时候，就会产生死锁，或者说资源先后顺序使用不当；

虽然死锁很少发生，但是一旦发生就会造成应用程序的停止响应，程序不做任何事情。

解决死锁的方法：
1、代码逻辑重构
2、增加定时参数timeout
lock_A.acquire(timeout=3)
"""

# # 死锁实例(采用自定义线程举例)
# import threading
# import time
#
# lock_A = threading.Lock()
# lock_B = threading.Lock()
#
# """
# 自定义线程:
# 目的是使得自己编写的代码也能够进行多线程;
# 自定义线程不能指定target,因为，自定义线程里面的任务统一都在run方法里面;
# 启动线程统一调用start方法，不要直接调用run方法，因为这样不是使用子线程去执行任务;
# """
#
# class MyThread1(threading.Thread):
#
#     def __init__(self, name):
#         # 调用父类的构造方法
#         super(MyThread1, self).__init__()
#         self.name = name
#
#     # 重写run方法
#     def run(self):
#         if lock_A.acquire():                    # 如果可以获取到锁，则返回True
#             print(self.name + '获取了A锁')
#             time.sleep(0.1)
#             if lock_B.acquire(timeout=3):
#                 print(self.name + '又获取了B锁，原来还有A锁')
#                 lock_B.release()
#             lock_A.release()
#
#
# class MyThread2(threading.Thread):
#
#     def __init__(self, name):
#         # 调用父类的构造方法
#         super(MyThread2, self).__init__()
#         self.name = name
#
#     # 重写run方法
#     def run(self):
#         if lock_B.acquire():                    # 如果可以获取到锁，则返回True
#             print(self.name + '获取了B锁')
#             time.sleep(0.1)
#             if lock_A.acquire(timeout=3):
#                 print(self.name + '又获取了A锁，原来还有B锁')
#                 lock_A.release()
#             lock_B.release()
#
#
# if __name__ == '__main__':
#     t1 = MyThread1('自定义线程1')
#     t1.start()
#
#     t2 = MyThread2('自定义线程2')
#     t2.start()



"""
生产者与消费者
本质是：两个线程之间的通信；

定义：
    生产者与消费者模式是通过一个容器来解决生产者与消费者的强耦合问题（即两个模块依赖性比较强）；
    生产者与消费者之间不直接通信，而是通过阻塞队列进行通信；
    生产者生产完数据之后无需等待消费者处理，直接扔进阻塞队列即可，同样，
    消费者也无需找生产者拿数据，而是直接从阻塞队列中取即可；
    阻塞队列相当于一个缓冲区，平衡了生产者与消费者的处理能力；

为什么要使用生产者和消费者模式？
    在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。
    在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，
    那么生产者就必须等待消费者处理完，才能继续生产数据。
    同理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。
    为了解决这个问题于是引入了生产者和消费者模式。

该模式的优点：
    1、解耦合(即降低模块之间的依赖程度为最低，从而降低代码的复杂性，使得代码可以复用)
    2、实现并发

    在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题；
    该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

使用队列实现线程间的同步：
    python的queue模块中提供了同步的、线程安全的队列类：
        Queue(FIFO：先进先出)
        LifoQueue(LIFO:后进先出)
        PriorityQueue(优先级队列)
    这些队列都实现了锁的原理，可以在线程中直接使用；
"""

# import threading
# import queue
# import random
# import time
#
# def Producer(q):
#     i = 0
#     while i < 10:
#         data = random.randint(1, 100)
#         q.put(f'生产者生产的数据：{data}')
#         print(f'生产者生产的数据：{data}, 第{i}次生产')
#         time.sleep(0.1)
#         i += 1
#
# def Consumer(q):
#     while True:
#         if q.empty():
#             print(f'队列为空，数据已取完！')
#             break
#         data = q.get()
#         print(f'消费者取出的数据：{data}')
#         time.sleep(0.5)
#         # q.task_done() 用于消费者，每次get()以后，使用task_done() 是告诉队列正在处理的get任务完成
#
#
# if __name__ == '__main__':
#     q = queue.Queue(5)
#
#     # 创建生产者线程
#     t1 = threading.Thread(target=Producer, args=(q,))
#     t1.start()
#     # 创建消费者线程
#     t2 = threading.Thread(target=Consumer, args=(q,))
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     # 作用是在使用join()的时候，当queue中所有的项目都被取出，且每个项目取出后
#     # 都使用了task_done()，那么就可以释放join()阻塞
#     # 如果不需要join()的时候也可以不使用task_done()
#     # q.join()
#     print("over!!!!!!!!")




"""
协程：又称微线程，
    它是实现多任务的另一种方式，只不过是比线程更小的执行单元。
    因为它自带CPU的上下文，这样只要在合适的时机，我们可以把一个协程切换到另一个协程。

    在单线程上执行多个任务，用函数切换，开销极小（推荐使用genvent和猴子补丁monkey.patchall）。
      不通过操作系统调度，没有进程、线程的切换开销。

协程使用场景：
    耗时操作：网络请求，网络下载（爬虫）
    IO操作：文件读写，阻塞（time.sleep()）

协程实现的三种方式：
yield生成器实现、greenlet库实现协程、gevent库实现协程

协程优缺点：
优点：
    线程的切换非常耗性能，但协程的切换只是单纯地操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。
    协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级；
    单线程内就可以实现并发的效果，最大限度地利用cpu；

缺点：
    协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程；
    协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程；
"""

# # yield生成器实现
# import time
#
# def task1():
#     for i in range(3):
#         print(f'task1任务 + {i}')
#         yield
#         time.sleep(0.5)
#
# def task2():
#     for i in range(3):
#         print(f'task2任务 + {i}')
#         yield
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     # 创建生成器对象
#     g1 = task1()
#     g2 = task2()
#     while True:
#         try:
#             next(g1)  # 执行生成器next(g1)，唤醒生成器g1，执行到yield后，挂起任务，下次再次唤醒时，从yield继续往下执行
#             print(f'This is main thread!')  # 主程序继续往下执行
#             next(g2)  # 执行生成器next(g2)，唤醒生成器g2，执行到yield后，挂起任务，退出，此时while大循环一轮结束，开始新的一轮循环，以此类推直到程序结束
#         except:
#             break



# # greenlet库实现协程(人工切换)
# import time
# from greenlet import greenlet
#
# def task1():
#     for i in range(3):
#         print(f'task1任务 + {i}')
#         g2.switch()  # 切换到g2的任务2中运行
#         time.sleep(0.5)
#
# def task2():
#     for i in range(3):
#         print(f'task2任务 + {i}')
#         g1.switch()  # 切换到g1的任务1中运行
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     # 创建greenlet对象
#     g1 = greenlet(task1)
#     g2 = greenlet(task2)
#
#     g1.switch()  # 先切换到g1中运行


"""
由于greenlet实现方式需要人工切换，比较麻烦，gevent库是对其进行了封装，
原理是当底层greenlet遇到网络请求，文件IO读写及阻塞操作时，
就会自动切换到其他的greenlet，再适当的时候切换回来继续执行，使得CPU达到高效利用的效果。

由于网络请求，文件IO读写及阻塞操作非常耗时，使得程序经常处于等待状态，有了gevent自动切换协程，
就可以保证总有greenlet在运行，而不是等待。
"""

# # gevent库及猴子补丁monkey.patch_all()实现协程
# import gevent
# import time
# from gevent import monkey
#
# monkey.patch_all()  # 猴子补丁感知所有耗时的操作，即给所有耗时操作打上补丁(这里是time.sleep())并自动替换为自己的gevent.sleep()
#                       # 如果不加这句话需要人工把time.sleep()换成gevent.sleep()
# def task1(n):
#     for i in range(n):
#         print(f'task1任务 + {i}')
#         time.sleep(0.5)  # 协程遇到耗时操作后会自动切换到其他协程运行
#
# def task2(n):
#     for i in range(n):
#         print(f'task2任务 + {i}')
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     # 创建协程
#     g1 = gevent.spawn(task1, 3)
#     g2 = gevent.spawn(task2, 3)
#
#     # g1.join()
#     # g2.join()
#     gevent.joinall([g1, g2])  # 等价于g1.join()和g2.join()  即阻塞到协程运行完毕
#
#     end = time.time()
#     print(f'This is main thread! over!!!  用时：{end-start}')



"""
异步协程

相关概念：
    同步：是指完成事务的逻辑，先执行第一个事务，如果阻塞了，会一直等待，直到这个事务完成，再执行第二个事务，顺序执行；
    异步：是和同步相对的，异步是指在处理调用这个事务的之后，不会等待这个事务的处理结果，直接处理第二个事务去了，
    通过状态、通知、回调来通知调用者处理结果。

python中使用协程最常用的库就是asyncio：主要用来实现异步网络操作、高并发、协程等。

asyncio库中概念介绍：
    event_loop事件循环：相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足条件时，就会调用对应的处理方法。
    coroutine协程：协程对象，只一个使用async关键字定义的函数，他的调用不会立即执行函数，而是会返回一个协程对象，
                   协程对象需要注册到事件循环中，由事件循环调用。
    task任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程的进一步封装，其中包含任务的各种状态。
    future：代表将来执行或没有执行的任务结果。它与task没有本质的区别。
    async/await关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。

定义一个协程： 
    通过async关键字定义一个协程，协程是一个对象，不能直接运行，需要把协程加入到事件循环（loop）中，
    由loop在适当的时候调用协程，asyncio.get_event_loop()方法可以创建一个事件循环，
    然后由run_until_complete(协程对象)将协程注册到事件循环中，并启动事件循环。
    
注意：
python 3.7 以前的版本调用异步函数的步骤：
    1、调用asyncio.get_event_loop()函数获取事件循环loop对象；
    2、通过不同的策略调用loop.run_forever()方法或者loop.run_until_complete()方法执行异步函数；
python3.7 以后的版本使用asyncio.run即可：
    此函数总是会创建一个新的事件循环并在结束时关闭之；
    它应当被用作asyncio程序的主入口点，理想情况下应当只被调用一次；   
"""

# # 异步协程实现
# import asyncio
#
# async def task(x):    # 通过async关键字定义一个协程
#     for i in range(3):
#         print(f'任务{x}已启动...')
#         # 使用await可以正对耗时操作进行挂起，就像生成器里的yield一样，函数让出控制权,
#         # 协程遇到await，事件循环就会挂起这个协程，执行别协程，直到其他协程也挂起或执行完毕，在进行下一个协程的执行。
#         await asyncio.sleep(x)
#     return f'任务{x}已启动...'
#
# # 回调函数
# def call_back(future):
#     print(f'回调函数：{future.result()}')
#
# coroutine = task(2)  # 协程是一个对象，不能直接运行
#
# # Python3.6采用以下方式运行
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# # result = loop.run_until_complete(coroutine)  # 将协程对象加入到事件循环中，并执行
# # print(result)  # 协程对象没有返回结果，打印None
#
# # 创建一个task对象
# task1 = loop.create_task(coroutine)  # 创建一个task对象 或者采用asyncio.ensure_future(coroutine)创建一个task对象
# # print(task1)
#
# task1.add_done_callback(call_back)  # 绑定回调函数
# # 其实是run_until_complete方法将协程包装成为了一个任务（task）对象. task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果
# loop.run_until_complete(task1)  # 将一个协程对象或task对象加入事件循环中，并返回finished的返回结果（前提是他们得有return的结果，否则返回None）
# # print(task1)


# """
# 嵌套函数：
#
# """
# def func():
#
#     n = 100     # 声明不可变类型的局部变量
#     list1 = [11, 3, 16, 8, 15, 24]  # 声明可变类型的局部变量
#     # 声明内部函数
#     def inner_func():
#         nonlocal n
#         for index, i in enumerate(list1):
#             list1[index] = i + n
#         list1.sort()
#
#         # 修改不可变类型的局部变量
#         n = n + 1
#     # 调用一下内部函数
#     inner_func()
#
#     print(f'修改排序后的列表为：{list1}')
#     print(f'修改后的n值：{n}')
#
# # 调用func
# func()


"""
闭包：内部函数调用外部函数局部变量的行为

条件：
    1、在一个外部函数中定义了一个内部函数；
    2、外部函数是有返回值，且返回值是内部函数名；
    3、内部函数引用了外部函数的局部变量；

格式：
    def 外部函数名():
        ...
        def 内部函数名():
            ...
        return 内部函数名    

缺点：
    作用域不太直观；
    由于变量不会被垃圾回收，存在占用一定内存的问题；

作用：
    可以使用同级的作用域；
    读取其他元素的内部变量；
    延长作用域，即外部变量的生命周期被延长；

总结：
1、闭包似优化了变量，原本需要类对象完成的工作，闭包也可以实现，即闭包也是实现面向对象的方法之一；
2、由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，而是绑定给了内部函数，使得外部函数局部变量生命
   周期延长，从而消耗内存；
3、闭包的好处，使代码变得简洁，便于阅读代码；
4、闭包实现装饰器的基础

"""
# def outer_func(a, b):
#     c = 100  # 局部变量(不可变类型)
#
#     def inner_func1():
#         # 内部函数中用到了外部函数的临时局部变量
#         sum = a + b + c
#         print(f'相加之后的结果:{sum}')
#
#     def inner_func2():
#         inner_func1()  # 调用inner_func1
#         # 闭包中内部函数修改外部函数局部变量
#         nonlocal c
#         c += 66
#         return f'------------>inner_func2, c:{c}'
#     # 外部函数返回值为内部函数的引用(可以理解为内存地址)
#     return inner_func2
#
# # 调用外部函数
# f = outer_func(6, 8)  # 此时f和inner_func2是指向同一个函数的引用(内存地址)，即两者可以看成是同样东西，且闭包具有保存参数状态的功能
# print(f)
# # 调用返回出来的内部函数inner_func2
# ff = f()    # 等价于inner_func2()
# print(ff)


"""
装饰器：

特点：
    1、函数作为参数
    2、满足闭包的特点
    


"""

# def outer_func(n):
#     a = 100  # 局部变量(不可变类型)
#
#     def inner_func():
#         nonlocal a
#         nonlocal n
#         n += 1
#         for i in range(n):
#             a += 1
#
#         print(f'修改之后的结果:{a}')
#
#
#     return inner_func
#
#
# # 调用
# f = outer_func(5)
# f()


# 函数作为参赛


# # 地址引用
#
# a = 10  # 声明整型变量
# b = a
#
#
# def test():     # 声明函数
#     print(f'---------test---------')
#
#
# # t = test
# # 下面两种调用是一样的
# # test()
# # t()
#
# def func(f):      # 此时 f = test
#     print(f'传入的参数：{f}')     # 传入的参数：<function test at 0x00000212D56B89D8>
#     f()
#     print('--------func---------')
#
# # 调用
# func(test)


# # 定义一个装饰器
#
# def decorate(func):
#     a = 10
#     def wrapper():
#         func()
#         print('进行刷墙')
#         print('进行铺地板')
#         print('进行装门窗')
#         print('装家具')
#
#     return wrapper
#
#
# # 使用上面定义的装饰器
#
# """
# 加上@decorate ，则会自动做以下操作(即底层自动完成)：
# 1、将被装饰函数house作为参数传给装饰器decorate
# 2、执行装饰器decorate函数
# 3、将装饰器decorate函数中的返回值wrapper返回给被装饰函数house，此时house = wrapper,即调用house()相当于调用wrapper()
# """
#
# @decorate   # 不改变原来house函数名的情况下丰富其功能，因为该函数有可能被很多模块所调用，而其中某个模块需要加一些新功能，但又不能影响其他模块正常使用，则采用装饰器方式
# def house():
#     print('现在是毛坯房！')
#
# # 调用house函数
# house() 此时house = wrapper,即调用house()相当于调用wrapper()


# # 装饰器模拟登陆校验功能
#
# import time
#
# # 定义一个装饰器
# def decorate(func):
#     def wrapper(*args, **kwargs):  # 采用可变参数，使得装饰器变成万能装饰器
#         print('正在校验中......')
#         time.sleep(3)
#         print('校验完毕......')
#         # 调用原函数
#         func(*args, **kwargs)   # fun1 fun2 fun3
#     return wrapper
#
#
# # 原函数fun1
# @decorate
# def fun1(n):
#     print('------f1-------', n)
#
#
# # 原函数fun2
# @decorate
# def fun2(name, age):
#     print('------f2-------', name, age)
#
#
# # 原函数fun3
# def fun3(std_list, gre='2020'):
#     print(f'{gre}班级的学生如下：')
#     for temp in std_list:
#         print('学生姓名为', temp)
#
#
# # 调用fun1、fun2和fun3
# fun1(6)
#
# fun2('hello', 20)
#
# students = ['cll', 'tom', 'lucy']
# fun3(students, '2019')


# # 多层装饰器
#
# # 装饰器1
# def decorate1(func):
#     print('装饰器1----->start')
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('进行刷墙')
#         print('进行铺地板')
#
#     print('装饰器1----->end')
#     return wrapper
#
# # 装饰器2
# def decorate2(func):
#     print('装饰器2----->start')
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('进行装门窗')
#         print('装家具')
#
#     print('装饰器2----->end')
#     return wrapper
#
#
# # 原函数house
# @decorate1
# @decorate2     # 两层装饰器，先装距离函数近的第一层装饰器，装完之后再把结果送给第二层装饰器继续装
# def house():
#     print('现在是毛坯房！')
#
# # 调用
# house()


# # 带参数的装饰器
# # 装饰器带参数，是在原来的装饰器基础上又加了一层，即三层
# def outer(param):  # 第一层  负责接收装饰器的参数
#     def decorate(func):   # 第二层  负责接收函数
#         def wrapper(*args, **kwargs):   # 第三层  负责接收函数的参数
#             func(*args, **kwargs)
#             print(f'铺{param}块地板')
#
#         return wrapper  # 返回的是第三层
#     return decorate   # 返回的是第二层
#
# # 原函数
# @outer(6)
# def house(time):
#     print(f'{time}日期拿到的毛坯房')
#
# @outer(80)
# def street():
#     print(f'新修的街道')
#
# # 调用
# house('2020-10-8')
#
# street()


# # 装饰器应用 （登陆验证）
# import time
#
# is_login = False  # 默认没有登陆状态
#
# # 定义一个登陆函数
# def login():
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
#     if username == 'admin' and password == '123456':
#         return True
#     else:
#         return False
#
# # 定义一个装饰器，用于付款验证
# def login_required(func):
#
#     def wrapper(*args, **kwargs):
#         global is_login
#         print('--------------付款---------------')
#         # 验证用户是否登陆
#         if is_login:
#             func(*args, **kwargs)
#         else:
#             # 跳转到登陆页面
#             print('用户没有登陆，不能进行付款！')
#             is_login = login()
#             print(f'登陆的结果为：{is_login}')
#     return wrapper
#
# # 定义一个付款原函数
# @login_required
# def pay(money):
#     print(f'正在付款，付款的金额是：{money}元')
#     print('付款中.....')
#     time.sleep(5)
#     print('付款完成！')
#
#
# # 调用
# pay(10000)  # 第一次调用处于未登录状态，10000付款失败
# pay(8000)   # 第二次调用时已经处于登陆成功的状态了，因此8000付款成功
#
# # 运行的结果为：
# # --------------付款---------------
# # 用户没有登陆，不能进行付款！
# # 请输入用户名:admin
# # 请输入密码:123456
# # 登陆的结果为：True
# # --------------付款---------------
# # 正在付款，付款的金额是：8000元
# # 付款中.....
# # 付款完成！


# # 浅拷贝和深拷贝对一般的列表对象进行复制是相同的，但是如果列表中嵌套列表（即包含子对象）就会有区别
# # 对于复杂数据的简单部分，无论是浅拷贝还是深拷贝，Python都会开辟一块新的内存地址，然后将值复制到新的内存地址空间；
# # 但是对于复杂数据的嵌套部分（即子列表），深拷贝在内存中开辟了一个新空间，并将子列表对象复制进去，但是浅拷贝没有对子
# # 列表对象开辟新空间，而是和原来的列表对象指向同一个内存空间，即同一个对象的引用。
# import copy
# test_list = [1, 2, 3, [6, 8, 9]]
# print(f'原列表的id地址：{id(test_list)}')
# # 浅拷贝
# copy_list = copy.copy(test_list)
# print(f'浅拷贝的结果：{copy_list}，浅拷贝id地址：{id(copy_list)}')
# # 深拷贝
# deepcopy_list = copy.deepcopy(test_list)
# print(f'深拷贝的结果：{deepcopy_list}, 深拷贝id地址：{id(deepcopy_list)}')
#
# # 返回的结果为
# # 原来列表的id地址：2763477160840
# # 浅拷贝的结果：[1, 2, 3, [6, 8, 9]]，浅拷贝id地址：2763477162120
# # 深拷贝的结果：[1, 2, 3, [6, 8, 9]], 深拷贝id地址：2763477249416
#
# # 但是如果改变嵌套列表中值两者就有区别了
# copy_list[3][0] = 5
# print(f'修改值后的浅拷贝的结果：{copy_list}，id地址：{id(copy_list)}')
# print(f'原列表的结果：{test_list}')
# # 由于copy_list是浅拷贝，修改嵌套列表中的值时，原列表的内容也会跟着修改
# # 修改值后的浅拷贝的结果：[1, 2, 3, [5, 8, 9]]，id地址：2763477162120
# # 原列表的结果：[1, 2, 3, [5, 8, 9]]
#
# deepcopy_list[3][0] = 7
# print(f'修改值后的深拷贝的结果：{deepcopy_list}，id地址：{id(deepcopy_list)}')
# print(f'原列表的结果：{test_list}')
# # 深拷贝时，修改嵌套列表中的值，原列表的内容则不会跟着修改
# # 修改值后的深拷贝的结果：[1, 2, 3, [7, 8, 9]]，id地址：2763477249416
# # 原列表的结果：[1, 2, 3, [6, 8, 9]]


# a = (1,)
# b = (1)
# c = ("1")
# print(f'a的类型为：{type(a)}')
# print(f'b的类型为：{type(b)}')
# print(f'c的类型为：{type(c)}')


# # 一行代码使得列表[[1, 2], [3, 4], [5, 6]]，展开为[1, 2, 3, 4, 5, 6]新列表
# lst = [[1, 2], [3, 4], [5, 6]]
# new_list = [j for i in lst for j in i]
# print(new_list)


# """二叉树"""
# # 定义一个节点类
# class Node(object):
#
#     def __init__(self, elem=-1, left_child=None, right_child=None):
#         self.elem = elem  # 默认为-1
#         self.left_child = left_child
#         self.right_child = right_child
#
#
# # 定义一个树类
# class Tree(object):
#     def __init__(self):
#         self.root = Node()
#         self.my_queue = []
#     # 定义一个为树添加节点的函数
#     def add(self, elem):
#         node = Node(elem)
#         if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
#             self.root = node
#             return
#         else:
#             self.my_queue.append(self.root)
#             while self.my_queue:     # 对已有的节点进行层次遍历
#                 tree_node = self.my_queue.pop(0)
#                 if tree_node.left_child is None:
#                     tree_node.left_child = node
#                     return
#                 else:
#                     self.my_queue.append(tree_node.left_child)
#                 if tree_node.right_child is None:
#                     tree_node.right_child = node
#                     return
#                 else:
#                     self.my_queue.append(tree_node.right_child)
#
#     # 采用递归的方式实现前序遍历(根节点->左子树->右子树)
#     def pre_order_recursion(self, root):
#         if root is None:
#             return
#         print(root.elem)
#         self.pre_order_recursion(root.left_child)
#         self.pre_order_recursion(root.right_child)
#
#     # 采用递归的方式实现中序遍历(左子树->根节点->右子树)
#     def middle_order_recurdion(self, root):
#         if root is None:
#             return
#         self.middle_order_recurdion(root.left_child)
#         print(root.elem)
#         self.middle_order_recurdion(root.right_child)
#
#     # 采用递归的方式实现后序遍历(左子树->右子树->根节点)
#     def later_order_recursion(self, root):
#         if root is None:
#             return
#         self.later_order_recursion(root.left_child)
#         self.later_order_recursion(root.right_child)
#         print(root.elem)
#
#     # 采用队列的方式实现层次遍历
#     def level_traversal(self, root):
#         if root is None:
#             return
#         queue = []
#         queue.append(root)
#         while queue:
#             node = queue.pop(0)
#             print(node.elem)
#             if node.left_child:
#                 queue.append(node.left_child)
#             if node.right_child:
#                 queue.append(node.right_child)
#
# if __name__ == '__main__':
#
#     tree = Tree()  # 创建一个树对象
#     for temp in range(5):
#         tree.add(temp)     # 向树逐个添加节点
#     # tree.pre_order_recursion(tree.root)  # 前序遍历   01342
#     # tree.middle_order_recurdion(tree.root)  # 中序遍历  31402
#     # tree.later_order_recursion(tree.root)   # 后序遍历  34120
#     # tree.level_traversal(tree.root)   # 层次遍历 01234


# """sql注入
# 当以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行，
# 比如例子中的SQL注入会删除数据库demo
# """
# input_data = 'cll'
# sql = 'select * from T_DEMO where PERSONNAME = "%s"' %input_data
# print(f'正常的sql语句：{sql}')  # 正常的sql语句：select * from T_DEMO where PERSONNAME = "cll"
#
# input_data = 'cll;drop database demo'
# sql = 'select * from T_DEMO where PERSONNAME = "%s"' %input_data
# print(f'sql注入语句：{sql}')  # sql注入语句：select * from T_DEMO where PERSONNAME = "cll;drop database demo"
#
# # 通过传参数方式解决sql注入问题
# params = [input_data]
# ret = Session.execute('select * from T_DEMO where PERSONNAME = %s', params)
#
# data = input('请输入字符串：')
# print(data.count())
# # print(len((data.split())[-1]))

# print(bin(int(input())).count('1'))



# import time
# import threading
#
# data_list = []
# lock = threading.Lock()
#
# def task1():
#     lock.acquire()
#     data_list.append('A')
#     time.sleep(0.01)
#     lock.release()
#
# def task2():
#
#     lock.acquire()
#     data_list.append('B')
#     time.sleep(0.01)
#     lock.release()
#
# def task3():
#     lock.acquire()
#     data_list.append('C')
#     time.sleep(0.01)
#     lock.release()
#
# def task4():
#     lock.acquire()
#     data_list.append('D')
#     time.sleep(0.01)
#     lock.release()
#
#
# if __name__ == '__main__':
#     n = int(input())
#     i = 0
#     while i < n:
#         t1 = threading.Thread(target=task1, name='线程1')
#         t1.start()
#         t1.join()
#
#         t2 = threading.Thread(target=task2, name='线程2')
#         t2.start()
#         t2.join()
#
#         t3 = threading.Thread(target=task3, name='线程3')
#         t3.start()
#         t3.join()
#
#         t4 = threading.Thread(target=task4, name='线程4')
#         t4.start()
#         t4.join()
#
#         i += 1
#     print(''.join(data_list))




# while True:
#     try:
#         data = input()
#         result = {}
#         for i in data:
#             result[i] = data.count(i)
#         ret = sorted(result.items(), key=lambda x: x[1], reverse=True)
#         s = ''
#         for k in dict(ret).keys():
#             s += k
#         print(s)
#     except:
#         break
#
# from collections import Counter
# while True:
#     try:
#         data_dict = dict(Counter(input()))
#         result = dict(sorted(data_dict.items(), key=lambda x: x[1], reverse=True))
#         s = ''
#         for k in result.keys():
#             s += k
#         print(s)
#     except:
#         break






# while True:
#     n = int(input())
#     result = []
#     for i in range(n):
#         s_list = input().split(' ')
#
#         if s_list.count('absent') > 1:
#             result.append('false')
#             break
#         if s_list.count('absent') + s_list.count('late') + s_list.count('leaveearly') > 3:
#             result.append('false')
#             break
#         for i in s_list:
#             if (i == 'late' and i+1 == 'late') or (i == 'leaveearly' and i+1 == 'leaveearly'):
#                 result.append('false')
#                 break
#         result.append('true')
#     print(' '.join(result))
#     break

s = input()
s_list = s.split(' ')
result = 0
if s_list.count('3') == 2:
    result += 1
for i in s_list:
    if i == '6':
        result += 1
print(result)










