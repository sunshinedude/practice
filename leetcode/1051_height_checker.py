# Problem

# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order for all students to be standing in
# non-decreasing order of height.
#
#
#
# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
#
#
# Constraints:
#
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                res += 1
        return res


# Tests

cases = [
    {"input": [1,1,4,2,1,3], "output": 3},
]
Test(Solution().heightChecker, cases, True).test()
