# 元组 可以理解成一个稳固版的列表，因为元组是不可修改
letters=('a','b','c','d','e')
print(letters[4])

# 集合(Set)
# 每一个集合中的元素是无序的、不重复的任意对象，可以通过集合去判断数据的从属关系，
# 有时还可以通过集合把数据结构中重复的元素减掉
a_set = {2,3,4,5}
a_set.add(6)
print(a_set)
a_set.add(2)
print(a_set)

num_list = [5,3,2,6,7,1,4]
print(sorted(num_list,reverse=False))

# zip函数
num=[1,2,3,4,5]
str=['a','b','c','d','e']
for a,b in zip(num,str):
    print(b, 'is', a)

import time
a = []
t0 = time.clock()
for i in range(1,200000):
    a.append(i)
print(time.clock() - t0,'process time')

t0 = time.clock()
b = [i for i in range(1,200000)]
print(time.clock() - t0,'process time')

# list = [item for item in iterable]

print([i**2 for i in range(1,10)])
print([j+1 for j in range(1,10)])
print([letter.lower() for letter in 'ABCDEFGHIJK'])

print({i:j for i,j in zip(range(1,6),'abcdef')})

# 循环列表时获取元素的索引 使用python的 enumerate来进行

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
for num, letter in enumerate(letters):
    print(letter, 'is', num + 1)
