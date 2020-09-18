# 切片练习:
# # 查找一个元素在列表里面的最后的位置
# a = ['weq','aaa','bbb','weqw',123,465,67,78,'reer','aaa','ccc','adasd','dsfgd','bbb',213,234,32,534,654]
# a = ["weq","aaa","bbb","weqw",123,456,67,78,"reer","aaa","ccc","adasd","dsfgd","bbb",213,234,32,534,654]
# b = "aaa"
# for i in range(-1,-len(a),-1):
#     if b in a[i:i - 1:-1]:
#         break
# print(len(a)+i)

# 请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
# a =list(range(1,101))
# b = []
# for i in range(0,len(a),3):
#     b.append(a[i:3 + i])
# print(b)


