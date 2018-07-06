################################
#字符串从左的0开始，从右边的-1开始
################################
name = 'My name is Mike'
print(name[0])
print(name[-4])
print(name[11:14]) # from 11th to 14th, 14th one is excluded
print(name[11:15]) # from 11th to 15th, 15th one is excluded
print(name[5:])
print(name[:5]);

##################################
url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name)
###############################

#replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)

############################
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

###################################
#格式化字符串format()
print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url);