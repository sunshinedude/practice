# Problem

# Given the root node of a binary search tree,
# return the sum of values of all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
#
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#
#
# Note:
#
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.

# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Recursion solution
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def r(node):
            if node:
                if L <= node.val <= R:
                    self.res += node.val
                elif L < node.val:
                    r(node.left)
                elif node.val < R:
                    r(node.right)

        self.res = 0
        r(root)
        return self.res


class Solution_1(object):
    # Cycle solution
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        tmp_list = [root]
        while tmp_list:
            root = tmp_list.pop()
            if root:
                if L <= root.val <= R:
                    res += root.val
                if L < root.val:
                    tmp_list.append(root.left)
                if R > root.val:
                    tmp_list.append(root.right)
        return res
