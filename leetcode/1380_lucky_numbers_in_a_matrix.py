# Problem

# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#
#
#
# Example 1:
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:
#
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
#
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 10^5.
# All elements in the matrix are distinct.

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        resp = []
        for i in range(len(matrix)):
            min_index, min_value = min(enumerate(matrix[i]), key=lambda x: x[1])
            max_in_column = True
            for j in range(len(matrix)):
                if matrix[j][min_index] > min_value:
                    max_in_column = False
                    break
            if max_in_column:
                resp.append(min_value)
        return resp


# Tests


cases = [
    {"input": [[3, 7, 8], [9, 11, 13], [15, 16, 17]], "output": [15]},
    {"input": [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], "output": [12]},
    {"input": [[7, 8], [1, 2]], "output": [7]},
]
Test(Solution().luckyNumbers, cases, True).test()
