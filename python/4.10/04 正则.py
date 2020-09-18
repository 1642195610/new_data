# import re
# a = "hello world"
# b = re.search("h",a)
# print(b)
# #re.I查找时不区分大小写
# b = re.search("W",a,re.I)
# print(b.span()[0])
# b = re.search("l",a)
# print(b.span())

#手机号--正则
"""
第一位     第二位     第三-第11位
  1      [345789]       \d{9}
"""
# s =input("s=")
# import re
# p = re.search(r"^1[345789]\d{9}$",s)
# if p == None:
#     print(0)
# else:
#     print(1)
#座机号-正则
"""
第一      第二三     七位
 0        [2,3]      \d{7}
"""
# import re
# s =input("s=")
# import re
# p = re.search(r"^(0\d{2,3}-)?\d{7}$",s)
# if p == None:
#     print(0)
# else:
#     print(1)


