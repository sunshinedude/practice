# Problem

# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain,
# return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
# Example 1:
#
# Input: [0,1,0]
# Output: 1
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1
# Note:
#
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    # Linear search
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        while A[i] < A[i + 1]:
            i += 1
        return i


class Solution_1:
    # Binary search
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, hi = 0, len(A) - 1
        while low < hi:
            mid = (low + hi) // 2
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                hi = mid
        return low


class Solution_2:
    # One string python solution
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))


# Tests

cases = [
    {"input": [0, 1, 0], "output": 1},
    {"input": [0, 2, 1, 0], "output": 1},
]
Test(Solution_1().peakIndexInMountainArray, cases, True).test()
Test(Solution_2().peakIndexInMountainArray, cases, True).test()
Test(Solution().peakIndexInMountainArray, cases, True).test()
