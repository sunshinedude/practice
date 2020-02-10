# Problem

# Given an array A of strings made only from lowercase letters,
# return a list of all characters that show up in all strings within the list (including duplicates).
# For example, if a character occurs 3 times in all strings but not 4 times,
# you need to include that character three times in the final answer.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Note:
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        c = {}
        for i in A[0]:
            if not c.get(i):
                c[i] = A[0].count(i)
                for j in A[1::]:
                    c[i] = min(c[i], j.count(i))
        res = []
        for k, v in c.items():
            res += [k] * v
        return res


# Tests

cases = [
    {
        "input": ["bella", "label", "roller"],
        "output": ["e", "l", "l"]},
    {
        "input": ["cool", "lock", "cook"],
        "output": ["c", "o"]},
]
Test(Solution().commonChars, cases, True).test()
