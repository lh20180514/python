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
account_login()
#条件控制 if elif else
password_list = ['*#*#','12345']
def account_login_test():
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
        print("wrong password or invalid input!")
        account_login_test()
account_login_test()

##############################################################
##############循环 Loop
##############################################################
