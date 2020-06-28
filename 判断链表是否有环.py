class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def pan(data):
    curr = data
    prev = data
    while curr and curr.next is not None:
        prev = prev.next
        curr = curr.next.next
        if prev == curr:
            return True
    return  False


if __name__ == '__main__':
    j1 = Node(1)
    j2 = Node(2)
    j3 = Node(3)
    j1.next = j2
    j2.next = j3
    j3.next = j1
    print(pan(j1))
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.判断函数(pan()是和class同级别)