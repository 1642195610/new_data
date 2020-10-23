"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and \
            self.is_same_tree(p.right, q.right)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    s = Solution()
    p1 = TreeNode(a[0])
    p2 = TreeNode(a[1])
    p3 = TreeNode(a[2])
    q1 = TreeNode(b[0])
    q2 = TreeNode(b[1])
    q3 = TreeNode(b[2])
    p1.left = p2
    p1.right = p3

    q1.left = q2
    q1.right = q3
    res = s.is_same_tree(p1, q1)
    print(res)
