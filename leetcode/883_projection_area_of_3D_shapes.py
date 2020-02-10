# Problem

# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
#
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
#
# Now we view the projection of these cubes onto the xy, yz, and zx planes.
#
# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
#
# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
#
# Return the total area of all three projections.
#
#
#
# Example 1:
#
# Input: [[2]]
# Output: 5
# Example 2:
#
# Input: [[1,2],[3,4]]
# Output: 17
# Explanation:
# Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
#
# Example 3:
#
# Input: [[1,0],[0,2]]
# Output: 8
# Example 4:
#
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 14
# Example 5:
#
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 21
#
#
# Note:
#
# 1 <= grid.length = grid[0].length <= 50
# 0 <= grid[i][j] <= 50

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ox_area = 0
        oz_area = 0
        oy_area = 0
        for i in range(len(grid)):
            max_x = 0
            max_y = 0
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    oz_area += 1
                    max_x = max(max_x, grid[i][j])
                    max_y = max(max_y, grid[j][i])
            ox_area += max_x
            oy_area += max_y
        return ox_area + oz_area + oy_area


# Tests

cases = [
    {"input": [[2]], "output": 5},
    {"input": [[1,2],[3,4]], "output": 17},
    {"input": [[1,0],[0,2]], "output": 8},
    {"input": [[1,1,1],[1,0,1],[1,1,1]], "output": 14},
    {"input": [[2,2,2],[2,1,2],[2,2,2]], "output": 21},
]
Test(Solution().projectionArea, cases, True).test()
