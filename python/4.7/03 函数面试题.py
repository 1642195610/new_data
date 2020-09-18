def calc(a,b,c,d = 1,e = 2):
    return (a + b) * (c - d) + e
print(calc(1,2,3,4,5))
# print(calc(1,2))
print(calc(e = 4,c = 5,a = 2,b = 3))
print(calc(1,2,3))
print(calc(1,2,3,e = 4))
# print(calc(1,2,3,d = 5,4))