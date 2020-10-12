# 面试题 02.08. 环路检测
# 给定一个有环链表，实现一个算法返回环路的开头节点。
# 有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。
#
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。


# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         curr = head
#         prev = head
#         while curr and curr.next is not None:
#             prev = prev.next
#             curr = curr.next.next
#             if prev == curr:
#                 curr = head
#                 while curr != prev:
#                     curr = curr.next
#                     prev = prev.next
#                 return curr
#         return None
#
#
# if __name__ == '__main__':
#     s = Solution()
#     j1 = ListNode(1)
#     j2 = ListNode(2)
#     j3 = ListNode(3)
#     j1.next = j2
#     j2.next = j3
#     j3.next = j1
#     print(s.detectCycle(j1))


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# def pan(data):
#     curr = data
#     prev = data
#     while curr and curr.next is not None:
#         prev = prev.next
#         curr = curr.next.next
#         if prev == curr:
#             return True
#     return  False
#
#


# if __name__ == '__main__':
#     j1 = Node(1)
#     j2 = Node(2)
#     j3 = Node(3)
#     j1.next = j2
#     j2.next = j3
#     j3.next = j1
#     print(pan(j1))
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.判断函数(pan()是和class同级别)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkList: #第一种
#     def huan(self, head):
#         if head is None or head.next is None:
#             return False
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False

class LinkList:  # 第二种
    def huan(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1
ll = LinkList()
print(f"链表是否有环: {ll.huan(n1)}")
