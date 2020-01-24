# Problem

# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
#
#
# Example 1:
#
# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:
#
# Input: "III"
# Output: [0,1,2,3]
# Example 3:
#
# Input: "DDI"
# Output: [3,2,0,1]
#
#
# Note:
#
# 1 <= S.length <= 10000
# S only contains characters "I" or "D".

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = 0
        h = len(S)
        res = []
        for i in S:
            if i == "I":
                res.append(l)
                l += 1
            else:
                res.append(h)
                h -= 1
        res.append(h)
        return res


# Tests

cases = [
    {"input": "IDID", "output": [0, 4, 1, 3, 2]},
    {"input": "III", "output": [0, 1, 2, 3]},
    {"input": "DDI", "output": [3, 2, 0, 1]},
]
Test(Solution().diStringMatch, cases, True).test()
