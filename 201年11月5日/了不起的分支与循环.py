score = int(input("请输入你的成绩："))
if 100.>= score >= 90:
	print("A")
elif 90 >= score >= 80:
	print("B")
elif 80 >= score >= 60:
	print("C")
elif 60 >= score >= 0:
	print("D")
else:
    print("输入错误")
########################################
#三元操作符
x,y = 4,5
if x < y:
        small = x
else:
        small = y
#可以改进为
small = x if x < y else y
