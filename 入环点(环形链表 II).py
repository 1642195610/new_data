# 142.环形链表 II
# 题目:给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回null。
#
# 为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始）。 如果pos是 - 1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。



# 示例1：
#
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例2：
#
# 输入：head = [1, 2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例3：
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"



class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


if __name__ == '__main__':
    s = Solution()
    j1 = ListNode(1)
    j2 = ListNode(2)
    j3 = ListNode(3)
    j1.next = j2
    j2.next = j3
    j3.next = j1
    print(s.detectCycle(j1))