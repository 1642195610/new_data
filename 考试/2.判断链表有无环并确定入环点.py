# 2. 判断链表有无环并确定入环点

def h(list):
    m = 0
    k = 0
    while k < len(list):
        if list[m] == list[k]:
            break
        else:
            m = m.next
            k = k.next.next
    return k

