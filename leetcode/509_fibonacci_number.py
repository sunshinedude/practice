# Problem

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
#
#
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
# Note:
#
# 0 ≤ N ≤ 30.

# Solution
from leetcode.test import Test


class Solution:
    # Solution with cycle
    def fib(self, N: int) -> int:
        f_n_2 = 1
        f_n_1 = 0
        i = 2
        while i <= N:
            f_n_i = f_n_2 + f_n_1
            f_n_1 = f_n_2
            f_n_2 = f_n_i
            i += 1
        return f_n_2 if N else 0


class Solution_1:
    # Recursion solution
    def fib(self, N: int) -> int:
        if N > 1:
            return self.fib(N-1) + self.fib(N-2)
        elif N == 1:
            return 1
        else:
            return 0


# Tests

cases = [
    {"input": 2, "output": 1},
    {"input": 3, "output": 2},
    {"input": 4, "output": 3},
]
Test(Solution().fib, cases, True).test()
Test(Solution_1().fib, cases, True).test()
