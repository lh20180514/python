# 四种数据结构 列表、字典、元组、集合
# list = [a,b,c,d]
# dict = {a:b,c:d}
# tuple = (a,b,c,d)
# set = {a,b,c,d}
# 列表中的每个元素都是可变的
# 列表中的元素是有序的，也就是每个元素都有一个位置
# 列表可以容纳Python中的任何对象

weekDay = ['Monday','Tuesday','Wednesday','Tursday','Friday']
print(weekDay[2])
# 列表中可以装入Python中所有的对象
all_in_list = [
    1,               #整数
    1.0,             #浮点数
    'a word',        #字符串
    print(1),        #函数
    True,            #布尔值
    [1,2],           #列表中套列表
    (1,2),           #元组
    {'key':'value'}  #字典
]
print(all_in_list)

#列表的增删改查
fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)
#fruit.remove('grape')
#print(fruit)
del fruit[0:2]
print(fruit)