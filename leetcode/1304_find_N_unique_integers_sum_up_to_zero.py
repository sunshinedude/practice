# Problem

# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
#
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
#
# Input: n = 1
# Output: [0]
#
#
# Constraints:
#
# 1 <= n <= 1000

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, int(n / 2) + 1):
            res += [i, 0 - i]
        if n % 2:
            res.append(0)
        return res


# Tests

cases = [
    {"input": 5, "output": [1, -1, 2, -2, 0]},
    {"input": 3, "output": [1, -1, 0]},
    {"input": 1, "output": [0]},
]
Test(Solution().sumZero, cases, True).test()
