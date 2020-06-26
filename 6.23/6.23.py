# 删除指定元素:
# from typing import List
#
#
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         s = 0
#         f = 0
#         while f < len(nums):
#             if nums[f] == val:
#                 f += 1
#             else:
#                 nums[s] = nums[f]
#                 f += 1
#                 s += 1
#         return s
#
#
# if __name__ == '__main__':
#     j = Solution()
#     print(j.removeElement([3, 2, 2, 3], 3))


# from typing import List
#
#
# class Solution:
#     def removeElement(self,nums: List[int], val: int) -> int:
#         s = 0
#         f = 0
#         while f < len(nums):
#             if nums[f] == val:
#                 f += 1
#             else:
#                 nums[s] = nums[f]
#                 f += 1
#                 s += 1
#         return s
#
#
# if __name__ == '__main__':
#     j = Solution()
#     z = j.removeElement([3,2,2,3],3)
#     print(z)


# 移动零
# from typing import List
#
#
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         s = 0
#         f = 0
#         while f < len(nums):
#             if nums[f] == 0:
#                 f += 1
#             else:
#                 nums[s] = nums[f]
#                 s += 1
#                 f += 1
#         for i in range(s,len(nums)):
#             nums[i] = 0
#         return nums
#
# if __name__ == '__main__':
#     j = Solution()
#     print(j.moveZeroes([0,1,0,3,12]))


#两数之和.1
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in nums[i + 1:]:
#                 if j + nums[i] == target:
#                     return [i, nums.index(j)]
#
#
# if __name__ == '__main__':
#     ff = Solution()
#     print(ff.twoSum([2, 7, 11, 15], 9))


#两数之和.2
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
#         for i in range(len(nums)):
#             t = target - nums[i]
#             if t in dict:
#                 return [dict[t],i]
#             else:
#                 dict[nums[i]] = i
#
# if __name__ == '__main__':
#     j = Solution()
#     print(j.twoSum([2, 7, 11, 15], 9))


# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dic = {}
#         for i in range(len(nums)):
#             t = target - nums[i]
#             if t in dic:
#                 return [dic[t],i]
#             else:
#                 dic[nums[i]] = i
#
#
# if __name__ == '__main__':
#     j = Solution()
#     print(j.twoSum([2, 7, 11, 15], 9))


#两数之和.3
#只适合有序
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         b = 0
#         e = len(nums) - 1
#         while b < e:
#             curr = nums[b] + nums[e]
#             if curr == target:
#                 return [b,e]
#                 b += 1
#                 e -= 1
#                 break
#             else:
#                 if curr < target:
#                     b += 1
#                 else:
#                     e -= 1
#
#
#
#
# if __name__ == '__main__':
#     j = Solution()
#     print(j.twoSum([2, 7, 11, 15], 9))


#栈---stack


# class Stack:
#     def __init__(self,limit = 10):
#         self.stack = []
#         self.size = 0
#
#     def __str__(self):
#         return str(self.stack)
#
#     def push(self,data):
#         self.stack.append(data)
#         self.size += 1
#
#     def pop(self):
#         if self.stack:
#             self.stack = self.stack.pop()
#             self.size -= 1
#
#     def peek(self):
#         if self.stack:
#             return self.stack[-1]
#
#     def is_empty(self):
#         return not bool(self.stack)
#
#     def size(self):
#         return self.size
#
# if __name__ == '__main__':
#     stack = Stack()
#     for i in range(10):
#         stack.push(i)
#     print(stack)


#链表实现栈
# from typing import Any, Optional, NoReturn
#
#
# class Node:
#     def __init__(self,data: Any, next: Optional = None):
#         self.data: Any = data
#         self.next: Optional[Node] = next
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class LinkStack:
#     def __init__(self) -> NoReturn:
#         self.top: Optional[Node] = None
#
#     def push(self,item: Any) -> None:
#         node: Node = Node(item)
#         if self.top is None:
#             self.top = node
#         else:
#             node.next = self.top
#             self.top = node
#
#     def pop(self) -> Any:
#         if self.top is None:
#             raise IndexError("栈为空")
#         else:
#             node: Node = self.top
#             self.top = node.next
#             return node.data
#
#     def is_empty(self) ->bool:
#         return self.top is None
#
#     def __repr__(self):
#         current = self.top
#         str = ""
#         while current:
#             str += f"{current} -- >"
#             current = current.next
#         return str + "END"
#
#
# if __name__ == '__main__':
#     s = LinkStack()
#     s.push(5)
#     s.push(9)
#     s.push("python")
#     print(s)
#     s.pop()
#     print(s)
#     print(s.is_empty())


# from typing import Any,Optional,NoReturn
#
#
# class Node:
#     def __init__(self,data:Any,next:Optional = None):
#         self.data: Any = data
#         self.next: Optional[Node] = next
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class LinkStack:
#     def __init__(self) -> NoReturn:
#         self.top:Optional[Node] = None
#
#     def __repr__(self):
#         current = self.top
#         res = ""
#         while current:
#             res += f"{current} --> "
#             current = current.next
#         return res + "END"
#
#     def push(self,item: Any) -> None:
#         node: Node = Node(item)
#         if self.top is None:
#             self.top = node
#         else:
#             node.next = self.top
#             self.top = node
#
#     def pop(self):
#         if self.top is None:
#             raise IndexError("栈为空")
#         else:
#             node = self.top
#             self.top = node.next
#         return node.data
#
#     def is_empty(self):
#         return self.top is None
#
# if __name__ == '__main__':
#     j = LinkStack()
#     j.push(3)
#     j.push(2)
#     j.push(1)
#     print("栈为: %s"%j)
#     j.pop()
#     print("弹栈为: %s"%j)
#     print(j.is_empty())


# from typing import Any,Optional,NoReturn
#
#
# class Node:
#     def __init__(self,data:Any,next: Optional = None):
#         self.data : Any = data
#         self.next : Optional[None] = next
#
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class LinkStack:
#     def __init__(self):
#         self.top = None
#
#     def __repr__(self):
#         current = self.top
#         res = ""
#         while current:
#             res += f"{current} --> "
#             current = current.next
#         return res + "END"
#
#     def push(self,item: Any):
#         node:Node = Node(item)
#         if self.top is None:
#             self.top = node
#         else:
#             node.next = self.top
#             self.top = node
#
#
# if __name__ == '__main__':
#     j = LinkStack()
#     j.push(3)
#     j.push(2)
#     j.push(1)
#     print("栈为: %s"%j)


#增加了栈的大小
from typing import Any,Optional,NoReturn


class Node:
    def __init__(self,data: Any,next: Optional = None):
        self.data : Any = data
        self.next : Optional[Node] = next

    def __repr__(self):
        return f"Node({self.data})"


class LinkStack:
    def __init__(self):
        self.top : Optional[Node] = None
        self.size = 0

    def __repr__(self):
        current = self.top
        res = ""
        while current:
            res += f"{current} --> "
            current = current.next
        return res + "END"

    def push(self,item: Any) -> None:
        node : Node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("栈为空")
        else:
            node = self.top
            self.top = node.next
        self.size -= 1
        return node.data

    def is_empty(self):
        return self.top is None


if __name__ == '__main__':
    j = LinkStack()
    j.push(3)
    j.push(2)
    j.push(1)
    print("压栈为: %s"%j)
    print(j.size)
    j.pop()
    print("弹栈为: %s"%j)
    print(j.size)
    print(j.is_empty())




