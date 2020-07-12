# 有序数组去重


# # 第一种:
# from typing import List
#
#
# class Solution:
#     def removeDuplicated(self, nums: List[int]) -> int:
#         n = len(set(nums))
#         i = 0
#         while i < n - 1:
#             if nums[i] == nums[i + 1]:
#                 temp = nums[i + 1]
#                 nums[i + 1:len(nums) - 1] = nums[i + 2:]
#                 nums[-1] = temp
#                 continue
#             else:
#                 i += 1
#         return i + 1
#
#
# if __name__ == "__main__":
#     s = Solution()
#     print(s.removeDuplicated([1, 1, 2, 2, 3, 4]))


# 第一种(1):
# from typing import List
#
#
# class Solution:
#     def removeDuplicated(self, nums: List[int]) -> int:
#         n = len(set(nums))
#         i = 0
#         while i < n - 1:
#             if nums[i] == nums[i + 1]:
#                 temp = nums[i + 1]
#                 nums[i + 1:len(nums) - 1] = nums[i + 2:]
#                 nums[-1] = temp
#                 continue
#             else:
#                 i += 1
#         return nums
#
#
# if __name__ == "__main__":
#     s = Solution()
#     print(s.removeDuplicated([1, 1, 2, 2, 3, 4]))

# 第二种:
# from typing import List
#
#
# class Solution:
#     def removeDuplicated(self, nums: List[int]) -> int:
#         slow = 0
#         fast = 1
#         while fast < len(nums):
#             if nums[fast] == nums[slow]:
#                 fast += 1
#             else:
#                 slow +=1
#                 nums[slow] = nums[fast]
#                 fast += 1
#         return slow + 1


# from typing import List
#
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def get(self,index):
#         curr = self.head
#         for _ in range(index):
#             curr = curr.next
#         return curr
#
#     def insert(self,index,element):
#         new_node = Node(element)
#         if index < 0 or index > self.size:
#             raise Exception("索引越界")
#         elif self.size == 0:
#             self.head = new_node
#             self.tail = new_node
#         elif index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         elif index == self.size:
#             self.tail.next = new_node
#             self.tail = new_node
#         else:
#             prev = self.get(index-1)
#             new_node.next = prev.next
#             prev.next = new_node
#         self.size += 1
#
#     def __repr__(self):
#         curr = self.head
#         string = ""
#         while curr:
#             string += f"{curr} -->"
#             curr = curr.next
#         return string + "END"
#
#     def remove(self,index):
#         if index < 0 or index > self.size:
#             raise Exception("索引越界")
#         elif index == 0:
#             remove_node = self.head
#             self.head = self.head.next
#         elif index == self.size:
#             prev = self.get(index-1)
#             remove_node = prev.next
#             prev.next = None
#             self.tail = prev
#         else:
#             prev = self.get(index-1)
#             remove_node = prev.next
#             prev.next = prev.next.next
#         self.size -= 1
#
# if __name__ == '__main__':
#     j = LinkList()
#     j.insert(0,100)
#     j.insert(1,200)
#     j.insert(2,300)
#     print("链表为: %s"%(j))
#     print("get获取为: {}".format(j.get(1)))
#     j.remove(1)
#     print("删除元素后链表为: %s"%(j))


# 判断链表是否有环

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
