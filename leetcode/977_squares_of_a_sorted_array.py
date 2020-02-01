from typing import List

from leetcode.test import Test


class Solution:
    # Solution for one pass through the list
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        L = len(A)
        while i < L and A[i] < 0:
            i += 1
        j = i
        i -= 1
        res = []
        while i >= 0 and j < L:
            sqr_i = A[i] * A[i]
            sqr_j = A[j] * A[j]
            if sqr_i < sqr_j:
                res.append(sqr_i)
                i -= 1
            else:
                res.append(sqr_j)
                j += 1

        while L > i >= 0:
            res.append(A[i] * A[i])
            i -= 1
        while j < L:
            res.append(A[j] * A[j])
            j += 1
        return res


class Solution_1:
    # Solution with sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i * i for i in A)


# Tests

cases = [
    {"input": [-4, -1, 0, 3, 10], "output": [0, 1, 9, 16, 100]},
    {"input": [-2, 0], "output": [0, 4]},
    {"input": [-1], "output": [1]},
]
Test(Solution().sortedSquares, cases, True).test()
Test(Solution_1().sortedSquares, cases, True).test()
