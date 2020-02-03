# Problem

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
#
#
#
# Example 1:
#
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#
#
# Constraints:
#
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.

# Solution
from collections import Counter
from typing import List

from leetcode.test import Test


class Solution:
    # Solution without collections
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        resp = []
        for i in arr2:
            while i in arr1:
                resp.append(i)
                arr1.remove(i)
        arr1.sort()
        return resp + arr1


class Solution_1:
    # Solution with Counter
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        resp = []
        c = Counter(arr1)
        for i in arr2:
            resp += [i] * c[i]
            c.pop(i)
        return resp + sorted(c.elements())


# Tests

cases = [
    {
        "input": [[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]],
        "output": [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]},
]
Test(Solution().relativeSortArray, cases, False).test()
Test(Solution_1().relativeSortArray, cases, False).test()
