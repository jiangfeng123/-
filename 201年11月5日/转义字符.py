#如何在句中输出单引号
print('Let\'s go!')
#如何在句末加上一个反斜杠呢
#直接添加会将反斜杠后面的引号转义，不取
#因此我们需要对转义进行反转义，然后删除最后一个反义字符。
str = r"C:\now\123\zhuishen\jiang\\"[2:5]
print(str)
#如何得到一个超多换行的字符串
str = """我爱你,
像风走了八万里,
不问归期,
12345678,
这个人在学习,
"""
print(str)
#注意标点符号！

