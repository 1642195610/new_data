# 非递归
from platform import node
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        resualt = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                resualt.append(root.val)
                root = root.right
        return resualt


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.right = TreeNode(2)
    t1.right.left = TreeNode(3)
    t = Solution()
    print(t.preorderTraversal(t1))


# 递归


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        if root is None:
            return
        self.preorderTraversal(root.left)
        print("%s" % root.val, end=" ")
        self.preorderTraversal(root.right)
        return node


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.right = TreeNode(2)
    t1.right.left = TreeNode(3)
    t = Solution()
    t.preorderTraversal(t1)
