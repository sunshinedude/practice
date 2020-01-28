# Problem

# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
#
#
#
# Follow up:
#
# Recursive solution is trivial, could you do it iteratively?
#
#
#
# Example 1:
#
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:
#
#
#
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
#
#
# Constraints:
#
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]

# Solution

# Definition for a Node.
from typing import List


class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children


class Solution:
	# solution with recursion
	def preorder(self, root: 'Node') -> List[int]:
		res = []

		def added_children(roots):
			if roots:
				for i in roots:
					res.append(i.val)
					added_children(i.children)
		added_children([root] if root else [])
		return res


class Solution_1:
	# solution with cycle
	def preorder(self, root: 'Node') -> List[int]:
		res = []
		childs = [root] if root else []

		while childs:
			res.append(root.val)
			if root.children:
				root.children.reverse()
				childs += root.children
			root = childs[-1]
			childs.pop()
		return res
