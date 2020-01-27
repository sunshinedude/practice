# Problem

# Given n and m which are the dimensions of a matrix initialized by zeros and given
# an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells
# in row ri and column ci by 1.
#
# Return the number of cells with odd values in the matrix after applying the increment to all indices.
#
#
#
# Example 1:
#
#
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# Example 2:
#
#
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
#
#
# Constraints:
#
# 1 <= n <= 50
# 1 <= m <= 50
# 1 <= indices.length <= 100
# 0 <= indices[i][0] < n
# 0 <= indices[i][1] < m

# Solution
from typing import List

from leetcode.test import Test


class Solution:
	def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
		matrix = [[0 for _ in range(m)] for _ in range(n)]
		for index in indices:
			matrix[index[0]] = [i + 1 for i in matrix[index[0]]]
			for line in matrix:
				line[index[1]] += 1
		res = 0
		for line in matrix:
			for item in line:
				if item % 2 != 0:
					res += 1
		return res


# Tests

cases = [
	{"input": [2, 3, [[0, 1], [1, 1]]], "output": 6},
	{"input": [2, 2, [[1, 1], [0, 0]]], "output": 0},

]
Test(Solution().oddCells, cases, False).test()
