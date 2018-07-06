#自定义函数，注意缩进
def function_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) + '°F'

C2F = function_converter(35)
print(C2F)

def g2kg_converter(g):
    intg = g /1000
    return str(intg) + "kg"

print(g2kg_converter(2101))

import math
def triangle_calc(a,b):
    return math.sqrt(a*a + b*b)
print(triangle_calc(3,4))

####函数参数问题
#位置参数
def trapezoid_area(base_up,base_down,height=3):
    return (base_down + base_up)*height/2
print(trapezoid_area(1,2,6))

#关键词参数
print(trapezoid_area(base_up=1,base_down=2,height=3))
print(trapezoid_area(1,2,height=6))

base_up = 1
base_down = 2
height = 3
print(trapezoid_area(height, base_down, base_up))
print(trapezoid_area(1,2))

#######
file = open("F:/code/python/text.txt",'w')
file.write('Hello World')
file.close()

def text_create(name,msg):
    dst_path = 'F:/code/python/'
    full_path = dst_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close();
    print("Done")

text_create('hello','123456789');

def text_filter(word,cencored_word='lame',changed_word='Awesome'):
    return word.replace(cencored_word,changed_word)
print(text_filter("Python is lame"))

def text_censored_create(name,msg,cencored_word='liu',changed_word='***'):
    cleanMsg = msg.replace(cencored_word,changed_word)
    text_create(name,cleanMsg)
text_censored_create('cencored_text','liuhui is ...')

#平方 = 幂
print(15**2)
#取整除 = 返回商的整数部分
print(9//2)
