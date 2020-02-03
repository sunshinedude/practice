# Problem

# Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
# return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.
#
# A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
# or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
# that is, always ones may appear first and then zeros.
#
#
#
# Example 1:
#
# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]
# Explanation:
# The number of soldiers for each row is:
# row 0 -> 2
# row 1 -> 4
# row 2 -> 1
# row 3 -> 2
# row 4 -> 5
# Rows ordered from the weakest to the strongest are [2,0,3,1,4]
# Example 2:
#
# Input: mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# Output: [0,2]
# Explanation:
# The number of soldiers for each row is:
# row 0 -> 1
# row 1 -> 4
# row 2 -> 1
# row 3 -> 1
# Rows ordered from the weakest to the strongest are [0,2,3,1]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 2 <= n, m <= 100
# 1 <= k <= m
# matrix[i][j] is either 0 or 1.

# Solution
from typing import List

from leetcode.test import Test


class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

		counted_matrix = {}
		for i in range(len(mat)):
			counted_matrix[i] = mat[i].count(0)
		res = []
		while k:
			min_pair = list(counted_matrix.items())[0]
			for key, value in counted_matrix.items():
				if value > min_pair[1] or (value == min_pair[1] and key < min_pair[0]):
					min_pair = (key, value)
			res.append(min_pair[0])
			counted_matrix.pop(min_pair[0])
			k -= 1
		return res


# Tests

cases = [
	{
		"input": [
			[
				[1, 1, 0, 0, 0],
				[1, 1, 1, 1, 0],
				[1, 0, 0, 0, 0],
				[1, 1, 0, 0, 0],
				[1, 1, 1, 1, 1]],
			3],
		"output": [2, 0, 3]},
	{"input": [
		[
			[1, 0, 0, 0],
			[1, 1, 1, 1],
			[1, 0, 0, 0],
			[1, 0, 0, 0]],
		2],
		"output": [0, 2]},

]
Test(Solution().kWeakestRows, cases, False).test()
