# Problem

# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#
# Return the number of negative numbers in grid.
#
#
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
#
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
#
# Input: grid = [[-1]]
# Output: 1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

# Solution
from typing import List

from leetcode.test import Test


class Solution:
	def countNegatives(self, grid: List[List[int]]) -> int:
		mid = len(grid[0]) // 2
		low = 0
		high = len(grid[0]) - 1
		res = 0
		for i in range(len(grid)):
			while (grid[i][mid] >= 0 or (grid[i][mid] < 0 and mid - 1 >= 0 and grid[i][mid - 1] < 0)) and low <= high:
				if grid[i][mid] >= 0:
					low = mid + 1
				else:
					high = mid - 1
				mid = (low + high) // 2
			if low > high:
				mid = len(grid[0]) // 2
				high = len(grid[0]) - 1
				low = 0
			else:
				res += len(grid[i]) - mid
				low = 0
				high = mid
				mid = (low + high) // 2

		return res


# Tests

cases = [
	{
		"input": [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
		"output": 8},
	{
		"input": [[3, 2], [1, 0]],
		"output": 0},
	{
		"input": [[1, -1], [-1, -1]],
		"output": 3},
	{
		"input": [[-1]],
		"output": 1},
	{
		"input": [[3, -1, -3, -3, -3], [2, -2, -3, -3, -3], [1, -2, -3, -3, -3], [0, -3, -3, -3, -3]],
		"output": 16},

]
Test(Solution().countNegatives, cases, True).test()
