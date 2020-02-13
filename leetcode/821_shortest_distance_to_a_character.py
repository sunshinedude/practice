# Problem

# Given a string S and a character C, return an array of integers representing the shortest distance
# from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
#
# Note:
#
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index_c = []
        for i in range(len(S)):
            if C == S[i]:
                index_c.append(i)
        ans = []
        j = 0
        for i in range(len(S)):
            if len(index_c) > j + 1 and index_c[j + 1] - i < i - index_c[j]:
                    j += 1
            ans.append(abs(i - index_c[j]))
        return ans


# Tests

cases = [
    {"input": ["loveleetcode", "e"], "output": [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]},
]
Test(Solution().shortestToChar, cases, False).test()
