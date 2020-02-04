# Problem

# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.
#
#
#
# Example 1:
#
#
# Input: [1,1,1,1,1,null,1]
# Output: true
# Example 2:
#
#
# Input: [2,2,2,5,2]
# Output: false

# Solution

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Recursion method
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.value = root.val
        self.ans = True

        def is_equals(root):
            if not root:
                return
            if root.val != self.value:
                self.ans = False
            is_equals(root.left)
            is_equals(root.right)
        is_equals(root)
        return self.ans


class Solution_1:
    # Set recursion method
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = set()

        def add_val(root):
            if root:
                val.add(root.val)
                add_val(root.right)
                add_val(root.left)
        add_val(root)
        return len(val) <= 1
