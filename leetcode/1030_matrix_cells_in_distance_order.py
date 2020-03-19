# Problem

# We are given a matrix with R rows and C columns has cells with
# integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
#
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
#
# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0)
# from smallest distance to largest distance.  Here, the distance between two cells (r1, c1)
# and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.
# (You may return the answer in any order that satisfies this condition.)
#
#
#
# Example 1:
#
# Input: R = 1, C = 2, r0 = 0, c0 = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1]
# Example 2:
#
# Input: R = 2, C = 2, r0 = 0, c0 = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# Example 3:
#
# Input: R = 2, C = 3, r0 = 1, c0 = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
#
#
# Note:
#
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C

# Solution
from typing import List

from leetcode.test import Test


class Solution:
	def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
		resp = [[r0, c0]]
		i = 1
		while True:
			tmp = []
			for j in range(i):
				if r0 + j < R and c0 + i - j < C:
					tmp.append([r0 + j, c0 + i - j])
				if r0 + i - j < R and c0 - j >= 0:
					tmp.append([r0 + i - j, c0 - j])
				if r0 - j >= 0 and c0 - i + j >= 0:
					tmp.append([r0 - j, c0 - i + j])
				if r0 - i + j >= 0 and c0 + j < C:
					tmp.append([r0 - i + j, c0 + j])
			if not tmp:
				return resp
			i += 1
			resp += tmp


# Tests

cases = [
	{"input": [1, 2, 0, 0], "output": [[0, 0], [0, 1]]},
	{"input": [2, 2, 0, 1], "output": [[0, 1], [0, 0], [1, 1], [1, 0]]},
	{"input": [2, 3, 1, 2], "output": [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]},
]
Test(Solution().allCellsDistOrder, cases, False).test()
