#成员运算符in
album = ['black star','david bowie',25,True]
album.append('new song')
print(album)
print(album[-2])
print(album.__contains__(25))
print("new song" in album)

#身份运算符is
#满足身份(Identity)、类型(type)、值(Value) 表示相同
print(bool(0))
print(bool([]))
print(bool(None))
print(bool(False))

#条件控制if else
def account_login():
    password = input('Password')
    if password == '12345':
        print('login success!')
    else:
        print('wrong password or invalid input!s')
        account_login()
# account_login()
#条件控制 if elif else
password_list = ['*#*#','12345']
def account_login_test(tries=3):
    while tries > 0:
        password = input('Password---:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print("login success")
        elif password_reset:
            new_password = input("enter a new password:")
            password_list.append(new_password)
            print('your password has changed successfully!')
            account_login_test()
        else:
            print("wrong password or invalid input!----")
            tries = tries - 1
            print('tries is', tries)
            account_login_test(tries)
    else:
        print('your account is locked')
#account_login_test(3)

##############################################################
##############循环 Loop
##############################################################
for every_letter in 'Hello World':
    print(every_letter)

for num in range(1,11): #不包含11，因此实际范围是1-10
    print(str(num) + ' + 1 = ',num + 1)

songlist = ['Holy Diver','Thunderstruck','Rebel Rebel']
for song in songlist:
    if song == 'Holy Diver':
        print(song, 'is','Dio')
    elif song == "Thunderstruck":
        print(song,'is','AC/CD')
    elif song == 'Rebel Rebel':
        print(song,'is','David Bowie')
#嵌套循环
# for i in range(1,10):
#     for j in range(1,10):
#         print('{0} X {1} = {2}'.format(i,j,i*j))

#while循环
# i = 1
# while i < 3:
#     print ("i is ", i)
#     i = i + 1

###################练习1
def create_file():
    for name in range(1,11):
        file_path = str('F:/code/python/') + str(name) + '.txt';
        file = open(file_path,'w')
        file.close()
#create_file();

def invest(amount,rate,time):
    i = 1
    while i <= time:
        result = (1 + rate) ** i * amount
        print("year {}: ${}".format(i,result))
        i = i + 1
    print('done')
invest(100,0.05,8)

def print_even():
    for index in range(1,101):
        if( index % 2 == 0):
            print(index)
print_even()

import random
print( random.randrange(1,7));