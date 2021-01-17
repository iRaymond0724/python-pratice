# 從 06 開始
"""
def add(a=0, b=0, c=0):
    #三數相加
    print('a=%d' % a)
    print('b=%d' % b)
    print('c=%d' % c)
    return a+b+c


print(add())
print(add(1, 2, 3))
# 參數可以不照順序傳
print(add(b=1, c=5, a=7))
"""
###################################################
"""
# 在参数名前面的*表示args是一个可变参数

def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1, 2))
print(add(1, 2, 3))
print(add(3, 5))

"""

###################################################
"""
# python 模塊

import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

"""
###################################################
"""

from module1 import foo as m1foo
m1foo()

"""
###################################################
"""
# module 名 是 該 .py 的檔名


# import module3 as m3
# print("111")
"""
###################################################
"""

def foo():
    b = 'hello'

    # Python中，可以在函數內部再定義函數
    def bar():
        c = True
        print('a = ' + str(a))
        print('b = ' + str(b))
        print('c = ' + str(c))
    print("=== bar() ===")
    bar()
    print("=== bar() ===")

    # print(c) # NameError: name 'b' is not defined
if __name__ == '__main__':
    # a 是 全局變量
    a = 100
    # print(b) # NameError: name 'b' is not defined
    foo()

"""
###################################################
"""

# global 關鍵字，可以宣告全域變數


def foo():
    global a
    a = 200
    print('in foo() func , a = ' + str(a))


# 直接執行.py的檔案，在這 __name__ 就是 __main__
if __name__ == '__main__':
    # print(__name__)
    a = 100
    print('before foo() a = ' + str(a))
    foo()
    print('after foo() a = ' + str(a))

"""
###################################################
"""
# 字串 乘法 與 相加
s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world

print('ll' in s1)  # True
print('good' in s1)  # False

"""
###################################################
"""
# 字串切割
str2 = '十年生死兩茫茫，不思量，自難忘'
# 取出指定index的字
print(str2[2])  # 生
print(str2[2:5])  # 生死兩
print(str2[2:])  # 生死兩茫茫，不思量，自難忘
print(str2[2::2])  # 生兩茫不量自忘 # ::2 -> 從起始點開始，取起始點index + 2 的那個字
print(str2[::2])  # 十生兩茫不量自忘
print(str2[::-1])  # 忘難自，量思不，茫茫兩死生年十  #  從起始點 0 ，開始取 0-1 , 0-2 , 0-3 ....下去
print(str2[-3:-1])  # 自難  #  取 默認起始點( 0 ) -3 ，到 -1 的位置

"""
###################################################
"""

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

"""
###################################################
