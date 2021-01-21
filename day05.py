# 從 day07 字典開始
# 创建字典的字面量语法
scores = {'Raymond':100,'Wlan':20}
print('scores = {}'.format(scores))

# 使用字典的構造器語法
item1 = dict(one=1, two=2, three=3, four=4)
print('item1 = {}'.format(item1))

# 通過zip函數將兩個序列壓成字典
item2 = dict(zip(['a','b','c'],'123'))
print('item2 = {}'.format(item2))

# 創建字典的推導式語法
item3 = {num: num ** 2 for num in range(1,10)}
print('item3 = {}'.format(item3))

'''
# 通過鍵可以獲取字典中對應的值
print('Raymond in scores value = {}'.format(scores['Raymond']))

# 對字典中所有鍵值進行遍歷
for key in scores:
    print(f'{key}:{scores[key]}')

# 更新字典中的元素
scores['Raymond'] = 90
scores.update(冷麵=65, 雷蒙=80)
print('after update scores = {}'.format(scores))

if 'Raymond' in scores:
    print(scores['Raymond'])
# get方法也可以通過key取值，還能設定默認值
print(scores.get('Raymond1',70))

# 刪除字典中的元素
print('start dict = {}'.format(scores))
# popitem() 默認先刪除最後面的那一個元素
print('scores.popitem = {}'.format(scores.popitem()))
# pop() 用key刪除指定元素
print(scores.pop('Wlan'))

# 清空字典
scores.clear()
print(scores)

'''
###################################################
###################################################
###################################################