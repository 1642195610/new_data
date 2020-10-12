"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# [3,9,20,null,null,15,7]


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        resualt = []
        if not root:
            return resualt
        queue = [root]
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            resualt.append(temp)
        return resualt


if __name__ == '__main__':
    t1 = TreeNode(3)
    t1.left = TreeNode(9)
    t1.right = TreeNode(20)
    t1.right.left = TreeNode(15)
    t1.right.right = TreeNode(7)
    t = Solution()
    print(t.levelOrder(t1))
