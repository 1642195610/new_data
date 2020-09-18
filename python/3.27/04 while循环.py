# c=1
# while c <= 4:
#     print("你好吗?")
#     c += 1

import random
# 猜拳游戏执行3次
# count = 1
# while count <= 3 :
#     print("用户输入石头(0)   剪刀(1)   布(2)")
#     a = int(input("请输入用户的数:"))
#     b = random.randint(0, 2)
#     print("电脑出的数为:%d" % (b))
#     if a == b:
#         print("平局")
#     elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
#         print("用户胜,用户出的为%s,电脑出的为%s" % (a, b))
#     else:
#         print("电脑胜,电脑出的为%s,用户出的为%s" % (b, a))
#     print("您已玩游戏:%s"%(count))
#     count += 1
# 直到用户赢,游戏结束
count = 1
while count != 0 :
    print("用户输入石头(0)   剪刀(1)   布(2)")
    a = int(input("请输入用户的数:"))
    b = random.randint(0, 2)
    print("电脑出的数为:%d" % (b))
    if a == b:
        print("平局")
    elif a - b == -1 or a - b == 2:
    # elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        print("用户胜,用户出的为%s,电脑出的为%s" % (a, b))
        count=0
        print("用户胜利,游戏结束")
    else:
        print("电脑胜,电脑出的为%s,用户出的为%s" % (b, a))
    # print("您已玩游戏:%s"%(count))