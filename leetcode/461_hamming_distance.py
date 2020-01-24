# Problem

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

# Solution
from leetcode.test import Test


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        x_bit = bin(x)[2::]
        y_bit = bin(y)[2::]
        l_x = len(x_bit)
        l_y = len(y_bit)
        if x < y:
            x_bit = "0" * (l_y - l_x) + x_bit
            l = l_y
        else:
            y_bit = "0" * (l_x - l_y) + y_bit
            l = l_x

        res = 0
        for i in range(l):
            if x_bit[i] != y_bit[i]:
                res += 1
        return res


# Tests

cases = [
    {"input": (1, 4), "output": 2},
    {"input": (4, 14), "output": 2},
]
Test(Solution().hammingDistance, cases).test()
