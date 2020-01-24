# Problem

# Given an array nums of integers, return how many of them contain an even number of digits.
#
#
# Example 1:
#
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:
#
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.
#
#
# Constraints:
#
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            count = 1
            while num > 9:
                num = int(num / 10)
                count += 1
            if count % 2 == 0:
                res += 1
        return res


class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += len(str(num)) % 2 == 0
        return res


# Tests

cases = [
    {"input": [12, 345, 2, 6, 7896], "output": 2},
    {"input": [555, 901, 482, 1771], "output": 1},
]
Test(Solution().findNumbers, cases, True).test()
