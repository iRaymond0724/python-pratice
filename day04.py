# 從 07 的這邊開始

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a


# def main():
#     for val in fib(20):
#         print(val)


# if __name__ == '__main__':
#     main()

###################################################
"""

# yield 其中有一個地方就像return的效果，到那一行會先停住，
# 下一次使用next函數時，才會繼續走。而值會由上一次運算的結果繼續
# yield 會回傳一個生成器
def foo():
    print("starting...")
    while True:
        print("into while")
        res = yield 4
        print("res:", res)


g = foo()
print("finish new foo()")
print(next(g))
print("*"*20)
# g繼續跑，以send函數傳入的 7 作為上次運算的結果
print(g.send(7))

"""
###################################################
"""

# 元組和列表類似，不同點在於"元組的值不可修改"，列表的值可以
# 元組是 () ，列表是 []

# 定義元組
t = ('Raymond',"1","3")
print("t = {}".format(t))

# 獲取元組中的元素
print('t[0] = {}'.format(t[0]))

# 遍歷元組中的值
for _ in t:
    print(_)

# 把元組轉換成列表
person = list(t)
print("person = {}".format(person))

# 列表的值是可修改的
person[0] = "Ray"
print("person[0] = {}".format(person[0]))

# 把列表轉換成元組
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print("fruits_tuple = {}".format(fruits_tuple))

"""
###################################################

# 集合只用 {}

# 創建集合
set1 = {1, 2, 3, 4, 5, 6, 7}
print('set1 = {}'.format(set1))
print('set1 Length = ',len(set1))

# 創建集合的構造器語法
set2 = set(range(1,10))
set3 = set((1,2,3,4,5))
print("set2, set3 = ")
print(set2, set3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num_ for num_ in range(1,10) if num_ % 3 ==0 or num_ % 5 == 0}
print('set4 = {}'.format(set4)) # {9, 3, 5, 6}  為什麼9在第一個 ？

# 在集合中添加元素
set1.add(8)
print('add set1 = {}'.format(set1))

set1.update([11,12])
print('update set1 = {}'.format(set1))

# 在集合中刪除指定元素
set1.discard(5)
print('discard set1 = {}'.format(set1))

if 4 in set1:
    set1.remove(4)
    print('remove set1 = {}'.format(set1))

set5 = set(range(0,5))
set6 = set(range(1,5))

# 交集 
# print(set1.intersection(set2))
print('set5 & set6 = {}'.format(set5 & set6))

# 並集 
# print(set1.union(set2))
print('set5 | set6 = {}'.format(set5 | set6))

# 差集
# print(set1.difference(set2))
print('set5 - set6 = {}'.format(set5 - set6))

# 對稱差
# print(set1.symmetric_difference(set2))
print('set5 ^ set6 = {}'.format(set5 ^ set6))

# print(set2.issubset(set1))
print('set5 <= set6 --- {}'.format(set5 <= set6))

# print(set3.issubset(set1))
print('set5 <= set6 --- {}'.format(set5 <= set6))

# print(set1.issuperset(set6))
print('set5 >= set6 --- {}'.format(set5 >= set6))

# print(set5.issuperset(set6))
print('set5 >= set6 --- {}'.format(set5 >= set6))

###################################################

