# Problem

# Given an array of distinct integers arr,
# find all pairs of elements with the minimum absolute difference of any two elements.
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
#
#
# Example 1:
#
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:
#
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:
#
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
#
#
# Constraints:
#
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = [[arr[0], arr[1]]]
        min_diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] < min_diff:
                ans = [[arr[i], arr[i + 1]]]
                min_diff = arr[i + 1] - arr[i]
            elif arr[i + 1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans


# Tests

cases = [
    {"input": [4, 2, 1, 3], "output": [[1, 2], [2, 3], [3, 4]]},
    {"input": [1, 3, 6, 10, 15], "output": [[1, 3]]},
    {"input": [3, 8, -10, 23, 19, -4, -14, 27], "output": [[-14, -10], [19, 23], [23, 27]]},
    {"input": [40, 11, 26, 27, -20], "output": [[26, 27]]},
]
Test(Solution().minimumAbsDifference, cases, True).test()
