# Problem

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
#
#
# Example 1:
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#
# Note:
#
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        need_odd = []
        need_even = []
        for i in range(len(A)):
            if i % 2 and not A[i] % 2:
                if need_odd:
                    odd_index = need_odd.pop()
                    tmp = A[odd_index]
                    A[odd_index] = A[i]
                    A[i] = tmp
                else:
                    need_even.append(i)

            if not i % 2 and A[i] % 2:
                if need_even:
                    even_index = need_even.pop()
                    tmp = A[even_index]
                    A[even_index] = A[i]
                    A[i] = tmp
                else:
                    need_odd.append(i)
        return A


# Tests

cases = [{"input": [4, 2, 5, 7], "output": [4, 5, 2, 7]}]
Test(Solution().sortArrayByParityII, cases, True).test()
