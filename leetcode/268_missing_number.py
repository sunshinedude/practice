# Problem

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?

# Solution
from typing import List

from leetcode.test import Test


class Solution:
	# Solution with used Gauss formula
	def missingNumber(self, nums: List[int]) -> int:
		return len(nums) * (len(nums) + 1) // 2 - sum(nums)


# Tests

cases = [
	{"input": [3, 0, 1], "output": 2},
	{"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "output": 8},
]
Test(Solution().missingNumber, cases, True).test()
