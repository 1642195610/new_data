import random


list = []
def randomlist(n):
    for i in range(n):
        a = random.randint(1,100)
        list.append(a)
    return list
