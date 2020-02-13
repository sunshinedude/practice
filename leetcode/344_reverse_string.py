# Problem

# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    # Cheat solution
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # Only for tests
        return s


class Solution_1:
    # Normal solution
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l // 2):
            s[i], s[l-i - 1] = s[l - i - 1], s[i]

        # Only for tests
        return s


# Tests

cases = [
    {"input": ["h", "e", "l", "l", "o"], "output": ["o", "l", "l", "e", "h"]},
    {"input": ["H", "a", "n", "n", "a", "h"], "output": ["h", "a", "n", "n", "a", "H"]},
]
Test(Solution().reverseString, cases, True).test()
cases = [
    {"input": ["h", "e", "l", "l", "o"], "output": ["o", "l", "l", "e", "h"]},
    {"input": ["H", "a", "n", "n", "a", "h"], "output": ["h", "a", "n", "n", "a", "H"]},
]
Test(Solution_1().reverseString, cases, True).test()
