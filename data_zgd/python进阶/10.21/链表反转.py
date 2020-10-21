# 1.链表反转
from randomList import randomList


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class LinkList:
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            new_node = cur.next
            cur.next = pre
            pre = cur
            cur = new_node
        return pre

    def print_p(self, head):
        cur = head
        s = ""
        while cur:
            s += f"{cur} --> "
            cur = cur.next
        return s + "END"


if __name__ == '__main__':
    ll = LinkList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    res = ll.reverse(node1)
    result = ll.print_p(res)
    print(result)

# 2.数组反转


def reverse_list(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


if __name__ == '__main__':
    list = randomList.randomList(3)
    print(list)
    print(reverse_list(list))

# 3.两两交换链表的结点




# 4.三数之和
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result += [nums[i],nums[l],nums[r]]
                while l < r and \
                    nums[l] == nums[l + 1]:
                    l += 1
                while l < r and \
                    nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return result


if __name__ == '__main__':
    result = three_sum([1,2,3,-1,0])
    print(result)

