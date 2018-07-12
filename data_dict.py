# 键值对形式出现
# 键是不能重复的，而值是可以重复的
# 键key是不可变得，也就无法修改，而值是可以变可以修改的，可以是任何对象
NASDAQ_code = {
'BIDU':'Baidu',
'SINA':'Sina',
'YOKU':'Youku'
}
print(NASDAQ_code['SINA'])
# add
NASDAQ_code['TEST'] = 'test';
print(NASDAQ_code)
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tetla'})
print(NASDAQ_code)
del NASDAQ_code['FB']
print(NASDAQ_code)
