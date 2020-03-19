# Problem

# Consider all the leaves of a binary tree.  From left to right order,
# the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
#
# Note:
#
# Both of the given trees will have between 1 and 100 nodes.

# Solution


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

		def take_leaf(r, t):
			if r.left:
				take_leaf(r.left, t)
			if r.right:
				take_leaf(r.right, t)

			if not r.left and not r.right:
				t.append(r.val)

		t_1 = []
		t_2 = []
		if not root1 or not root2:
			return False
		take_leaf(root1, t_1)
		take_leaf(root2, t_2)
		return t_1 == t_2
