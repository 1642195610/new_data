# 3. 有序数组的两数之和(自己设定和是多少并实现)

def s(list,v):
    l = list[0]
    r = len(list) - 1
    res = []
    while r < len(list):
        if l + list[r] == v:
            res.extend([len(list)-r,r])
    return res


