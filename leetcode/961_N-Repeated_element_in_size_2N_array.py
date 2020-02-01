# Problem

# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.
#
#
#
# Example 1:
#
# Input: [1,2,3,3]
# Output: 3
# Example 2:
#
# Input: [2,1,2,5,3,2]
# Output: 2
# Example 3:
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5
#
#
# Note:
#
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        keep_value = {}
        for i in A:
            if keep_value.get(i):
                return i
            else:
                keep_value[i] = 1


# Tests

cases = [
    {"input": [1, 2, 3, 3], "output": 3},
    {"input": [2, 1, 2, 5, 3, 2], "output": 2},
    {"input": [5, 1, 5, 2, 5, 3, 5, 4], "output": 5},
]
Test(Solution().repeatedNTimes, cases, True).test()
