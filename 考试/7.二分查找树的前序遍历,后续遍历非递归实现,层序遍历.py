# 7. 二分查找树的前序遍历,后续遍历非递归实现,层序遍历


# 前序遍历
def h(head):
    if head is None:
        raise Exception("空!!!")
    else:
        print(head)
        head = head.left
        head = head.right
    return head


# 后序遍历
def e(head):
    if head is None:
        raise Exception("空!!!")
    else:
        head = head.left
        head = head.right
        print(head)
    return head


