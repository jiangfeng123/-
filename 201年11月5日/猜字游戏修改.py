#print("---------姜枫的猜字游戏------------")
#times = 3
#temp = input("不妨猜一下下心里想的是哪一个数字：")
#guess = int(temp)
#while (guess != 8) and (times > 0):
#    temp = input("对不起，猜错了请重新输入：")
#    guess = int(temp)
#    times = (times - 1)
#    if guess == 8:
 #       print("真聪明")
 #       print("哼，猜对了也没有奖励")
 #   else:
  #      if guess > 8:
   #         print("大了大了")
     #   else:
    #        print("小了小了")
        
import random
times = 5
secret = random.randint(1,10)
guess = 0
print("--------------坠神的猜字游戏开始了-------------")
temp = input("不妨猜一下心里想的那个数字：  ",end = "")
guess = int(temp)
while (guess != secret) and (times > 0 ):
    temp = input("错了，请重新输入一次吧：")
    guess = int(temp)
    times = times -1
    if guess == secret:
        print("真聪明")
        print("猜对了也没有奖励")
    else:
        if guess > secret:
            print("哥，大了大了")
        else:
            print("小了小了")
        if times > 0:
            print("再试一次吧")
        else:
            print("没机会了！")
    
        
