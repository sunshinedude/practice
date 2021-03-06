# Problem

# Given an array of integers arr, write a function that returns true if and only
# if the number of occurrences of each value in the array is unique.
#
#
#
# Example 1:
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
# No two values have the same number of occurrences.
# Example 2:
#
# Input: arr = [1,2]
# Output: false
# Example 3:
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for i in arr:
            if counter.get(i):
                counter[i] += 1
            else:
                counter[i] = 1
        quantity = list(counter.values())
        return len(quantity) == len(set(quantity))


cases = [
    {"input": [1, 2, 2, 1, 1, 3], "output": True},
    {"input": [1, 2], "output": False},
    {"input": [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], "output": True},
]
Test(Solution().uniqueOccurrences, cases, True).test()
