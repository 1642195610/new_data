# import random
# # 产生 1-10 的随机数
# a=random.randint(1,10)

import random
print("用户输入石头(0)   剪刀(1)   布(2)")
a=int(input("请输入用户的数:"))
b=random.randint(0,2)
print("电脑出的数为:%d"%(b))
if a == b :
    print("平局")
elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0)  :
    print("用户胜,用户出的为%s,电脑出的为%s"%(a,b))
else:
    print("电脑胜,电脑出的为%s,用户出的为%s" % (b,a))

