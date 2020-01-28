# Problem

# Given an array arr, replace every element in that array with the greatest element among the
# elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
#
#
# Example 1:
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
#
# Constraints:
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5

# Solution
from typing import List

from leetcode.test import Test


class Solution:
	def replaceElements(self, arr: List[int]) -> List[int]:
		res = []
		max_i = arr[-1]
		for i in range(len(arr) - 1, 0, -1):
			if arr[i] < max_i:
				res.append(max_i)
			else:
				res.append(arr[i])
				max_i = arr[i]
		res.reverse()
		res.append(-1)
		return res


# Tests

cases = [
	{"input": [17, 18, 5, 4, 6, 1], "output": [18, 6, 6, 6, 1, -1]},
]
Test(Solution().replaceElements, cases, True).test()
