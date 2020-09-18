a = [1,2,3]
def s(b):
    b[0] =[9]
    print("函数里面b:",b)
s(a)
print("函数外面a:",a)

a = [1,2,3]
def s(b):
    b = [9]
    print("函数里面b:",b)
s(a)
print("函数外面a:",a)

a = [1,2,3]
b = a.copy()
b = [9]
print("函数里面b:",b)
print("函数外面a:",a)