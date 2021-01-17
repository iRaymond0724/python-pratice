# 從 07 的 使用列表 開始

###################################################
"""

list1 = [1, 3, 5, 7, 100]
print(list1)  # [1, 3, 5, 7, 100]

list2 = ['hello'] * 3
print(list2)  # ['hello', 'hello', 'hello']

# 計算列表長度(元素個數)
print(len(list1))  # 5

# 下標(索引)運算
print(list1[0])  # 1
print(list1[4])  # 100

# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 100
print(list1[-3])  # 5

list1[2] = 300
print(list1)  # [1, 3, 300, 7, 100]

# for 通過 "下標" , 印出 list1 元素
for index in range(len(list1)):
    print('list1 , index_{} = {}'.format(index, list1[index]))

# 通過 for 循環遍歷列表元素，不使用 "下標"
for elem in list1:
    print('list1 , elem = {}'.format(elem))

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print('index = {} , elem = {}'.format(index, elem))

"""
###################################################
"""

list1 = [1, 3, 5, 7, 100]

# 添加元素
list1.append(200)  # append 接在 list1 後面
print(list1)  # [1, 3, 5, 7, 100, 200]

list1.insert(1, 400)  # insert 插在 list1 前面
print(list1)

# 合併兩個列表
list1.extend([1000, 2000])  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(list1)

list1 += [3000, 4000]
print(list1)

print(len(list1))  # 11

# 先通過成員運算，判斷元素是否在list1中，有則刪除該元素
if 3 in list1:
    list1.remove(3)
print(list1)

# 從指定位置刪除元素
list1.pop(0)
print(list1)  # [400, 5, 7, 100, 200, 1000, 2000, 3000, 4000]
list1.pop(len(list1) - 1)
print(list1)  # [400, 5, 7, 100, 200, 1000, 2000, 3000]

# 清空列表元素
list1.clear()
print(list1)  # []

"""
###################################################
"""

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print('fruits = {}'.format(fruits))

# 複製取出列表指定的部分
fruits2 = fruits[1:4]
print('fruits2 = {}'.format(fruits2))

# 觀察這個，fruits3 = fruits 不是複製一份到fruits3 ， 而是一個指標指向fruits3 和 fruits
# 操作 fruits3 也會影響到 fruits
fruits3 = fruits
fruits3.pop(0)
# ['apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
print('fruits = {}'.format(fruits))
# ['apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
print('fruits3 = {}'.format(fruits3))

fruits4 = fruits[-3:-1]
print(fruits4)  # ['pitaya', 'pear']

# 取得反轉後的list
fruits5 = fruits[::-1]
# ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple']
print(fruits5)

"""
###################################################
"""

# sorted 返回的 list2 ， 不會影響到傳入 list1 ，是複製一份sorted的結果，存入list2
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print('list2 = {}'.format(list2))

"""
###################################################
"""

list1 = ['0', '1', '2', '3', '4', '5']
list2 = sorted(list1, reverse=True)
print('list2 = {}'.format(list2))  # ['5', '4', '3', '2', '1', '0']

list3 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# 通過 key 關鍵字，指定元素字串長度進行排序，而非默認的字母順序
list4 = sorted(list3, key=len)
# ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
print('list4 = {}'.format(list4))


list5 = list1[:]
# 直接排序列表
list5.sort(reverse=True)
print('list5 = {}'.format(list5))

"""
###################################################
"""

# list 生成式
# 生成器 vs 生成式
# 用生成式 可占用較少記憶體，但運行速度較慢一些，生成器反之。
import sys
f = [x for x in range(1, 10)]
print('f = {}'.format(f))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

w = [x + y for x in 'ABCD' for y in '12']  # 生成器
print('w = {}'.format(w))  # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']


# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
# x 先由for迴圈產生出來，丟到前面的 x ， x再進行平方(** 2)，運算完，丟入list
q = [x ** 2 for x in range(1, 10)]
print('size of q = {}'.format(sys.getsizeof(q)))  # 查看对象占用内存的字节数 192
print('q = {}'.format(q))

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
e = (x ** 2 for x in range(1, 10))
print('size of e = {}'.format(sys.getsizeof(e)))  # 相比生成式生成器不占用存储数据的空间 88
print(e)
for val in e:
    print(val)

"""
###################################################
