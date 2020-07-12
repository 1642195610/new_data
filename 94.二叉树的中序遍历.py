"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


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
