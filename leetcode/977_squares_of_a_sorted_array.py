from typing import List

from leetcode.test import Test


class Solution:
    # Solution for one pass through the list
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        while i < len(A) and A[i] < 0:
            i += 1
        j = i
        i -= 1
        res = []
        while i >= 0 and j < len(A):
            if A[i] ** 2 < A[j] ** 2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1

        while len(A) > i >= 0:
            res.append(A[i] ** 2)
            i -= 1
        while j < len(A):
            res.append(A[j] ** 2)
            j += 1
        return res


class Solution_1:
    # Solution with sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i * i for i in A)


# Tests

cases = [
    {"input": [-4,-1,0,3,10], "output": [0,1,9,16,100]},
    {"input": [-2, 0], "output": [0, 4]},
    {"input": [-1], "output": [1]},
]
Test(Solution().sortedSquares, cases, True).test()
Test(Solution_1().sortedSquares, cases, True).test()
