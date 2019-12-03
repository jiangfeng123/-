count = 3
password = 'mima'
while count:
    passwd = input("请输入您的密码：")
    if passwd == password:
        break
        print("输入正确，正在进入程序")
    elif '*' in passwd:
        print("密码中不包含'*'")
        count -= 1
        continue
        print("运行到这里")
    else:
        print("输入错误，请重新输入：")
    print("nynmber=%d" %(count))
    count -= 1
