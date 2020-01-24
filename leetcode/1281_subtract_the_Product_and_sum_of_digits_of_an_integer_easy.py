# Problem

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#
#
# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
# Example 2:
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21

# Solution
from leetcode.test import Test


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        while n > 0:
            item = n % 10
            sum += item
            prod *= item
            n = int(n / 10)
        return prod - sum


# Tests

cases = [
    {"input": 234, "output": 15},
    {"input": 4421, "output": 21},
]
Test(Solution().subtractProductAndSum, cases, True).test()
