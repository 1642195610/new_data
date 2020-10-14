# 删除链表重复值

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def delete_duplicated(self, nums):
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
        return slow + 1


if __name__ == '__main__':
    s = Solution()
    print([1, 1, 2, 2, 3, 4])
    result = s.delete_duplicated([1, 1, 2, 2, 3, 4])
    print(result)
    print()


# 移动零

class Solution:
    def move_duplicated(self, nums):
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums


if __name__ == '__main__':
    s = Solution()
    print([0, 1, 0, 3, 12])
    result = s.move_duplicated([0, 1, 0, 3, 12])
    print(result)
    print()


# 删除指定值
class Solution:
    def delete_duplicaticed_val(self, nums, val):
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = val
        return slow


if __name__ == '__main__':
    s = Solution()
    print("[3,2,2,3], 3")
    result = s.delete_duplicaticed_val([3, 2, 2, 3], 3)
    print(result)
    print()


# 栈-数组(列表)
class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.size = 0

    def __repr__(self):
        return f"{self.stack} "

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack is None:
            raise IndexError("栈为空")
        else:
            temp = self.stack.pop()
            self.size -= 1
            return temp


if __name__ == '__main__':
    s = Stack(4)
    for i in range(4):
        s.push(i)
    print(s)
    print("[", end="")
    for i in range(4):
        print(s.pop(), end=", ")
    print("]")
