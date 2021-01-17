###################################################
'''
# 使用变量保存数据并进行加减乘除运算

a = 321
b = 123
print(a+b)
print(a-b)
print(a*b)
print(a/b)

'''
###################################################

###################################################
'''
# 使用type()检查变量的类型

a = 100
b= 12.345
c= 1+5j
d='helo world'
e=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''
###################################################

###################################################
'''
# 使用 input() 函數獲取鍵盤輸入(字符串)
# 使用 int() 函數將輸入的字符串轉換成整數
# 使用 print() 函數輸出帶佔位符的字串


a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a+b))
print('%d / %d = %f' % (a, b, a/b))

'''
###################################################
'''
# int()：将一个数值或字符串转换成整数，可以指定进制。
# float()：将一个字符串转换成浮点数。
# str()：将指定的对象转换成字符串形式，可以指定编码。
# chr()：将整数转换成该编码对应的字符串（一个字符）。
# ord()：将字符串（一个字符）转换成对应的编码（整数）。

print(type(str(1111)))
print(ord('a'))


'''
###################################################
'''
# 将华氏温度转换为摄氏温度

f = float(input('請輸入華氏溫度 : '))
result = (f - 32) / 1.8
print('%.1f華氏溫度 = %.1f攝氏溫度' % (f, result))

'''
###################################################
'''
# 输入半径计算圆的周长和面积

radius = float(input('請輸入圓半徑 : '))
print("圓周長 : %f , 圓面積 : %f" % (radius*2*3.14, radius*radius*3.14))

'''
###################################################
'''

# 輸入年份，判斷是否為閏年

input_year = int(input("請輸入年份 : "))
if input_year % 4 == 0 and input_year % 100 != 0 or input_year % 400 == 0:
    print("是閏年")
else:
    print("不是閏年")
'''
###################################################
'''
# 用户身份验证

msg = input('請輸入登入成功訊息 : ')
username = input('請輸入username : ')
password = input('請輸入password : ')

if(username == 'Raymond' and password == '111111'):
    print('登入成功')
    if(len(msg) > 0 and len(msg) < 5):
        print(msg)
    elif(len(msg) > 5):
        print('HIIIIIIIIIIIIIIIIIII')
    else:
        print('Hello ~')
else:
    print('登入失敗')
'''
###################################################
'''
# 用for加總1~10
# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

sum = 0
for i in range(11):  # range 代表 0 ~ 10
    sum += i
print('sum = %d ' % sum)

even_sum = 0
for i in range(0, 101, 2):
    print(i)
    even_sum += i
print('even_sum = %d' % even_sum)

'''
###################################################
'''

# while 循環

sum = 0
index_ = 0
while sum <= 10:
    sum += index_
    print(index_)
    index_ += 1
print('sum = %d' % sum)
print('finish ~ ~ ')

'''
###################################################
