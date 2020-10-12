# min = x if x < y else y
# NameError: name 'x' is not defined

# max = x > y ? x : y
# SyntaxError: invalid syntax

# if(x > y) print x
# SyntaxError: invalid syntax

# while True : pass
# 可以运行,但是它是个死循环

a = [x ** 2 for x in range(8) if not x % 2]
print(a)

list = []
list1 = []
for x in range(8):
    if not x % 2:
        list1.append(not x % 2)
        list.append(x ** 2)
print(list1)
print(list)
