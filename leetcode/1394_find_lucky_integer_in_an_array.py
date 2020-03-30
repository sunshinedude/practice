# Problem

# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
#
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them.
# If there is no lucky integer return -1.
#
#
#
# Example 1:
#
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
#
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:
#
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
# Example 4:
#
# Input: arr = [5]
# Output: -1
# Example 5:
#
# Input: arr = [7,7,7,7,7,7,7]
# Output: 7
#
#
# Constraints:
#
# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        frequency_number = {}
        for i in arr:
            if frequency_number.get(i):
                frequency_number[i] += 1
            else:
                frequency_number[i] = 1
        for k, v in frequency_number.items():
            if k == v and k > res:
                res = k
        return res


# Tests

cases = [
    {"input": [2, 2, 3, 4], "output": 2},
    {"input": [1, 2, 2, 3, 3, 3], "output": 3},
    {"input": [2, 2, 2, 3, 3], "output": -1},
    {"input": [5], "output": -1},
    {"input": [7, 7, 7, 7, 7, 7, 7], "output": 7},
]
Test(Solution().findLucky, cases, True).test()
