# 4. 有序数组去重

def L(list):
    m = 0
    k = len(list) - m
    while k <= len(list):
        if list[m] == list[k]:
            m += 1
            list[m] = list[k]
            k += 1
        else:
            k += 1
    return


