# 非递归
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        resualt = []
        if root is None:
            return resualt
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            root = stack1.pop()
            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
            stack2.append(root)
        while stack2:
            resualt.append(stack2.pop().val)
        return resualt


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.right = TreeNode(2)
    t1.right.left = TreeNode(3)
    t = Solution()
    print(t.postorderTraversal(t1))


# 递归


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        if root is None:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print("%s" % root.val, end=" ")
        return root


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.right = TreeNode(2)
    t1.right.left = TreeNode(3)
    t = Solution()
    t.postorderTraversal(t1)
