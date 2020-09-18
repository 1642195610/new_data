#赋值就是简单的引用
a = [1,2,3]
b = a
b[0] = 9
print("a:",a)
print("b:",b)
print("----------------------分隔符-------------------------")
#浅拷贝
import copy
a = [1,2,3]
b= copy.copy(a)
b = a.copy()
b[0] = 9
print("a:",a)
print("b:",b)
print("----------------------分隔符-------------------------")
#深拷贝

import copy
a = [[1],2,3]
b = copy.deepcopy(a)
b[0][0] = 9
print("a:",a)
print("b:",b)
