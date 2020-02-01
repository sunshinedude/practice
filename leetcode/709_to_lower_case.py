# Problem

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
#
#
# Example 1:
#
# Input: "Hello"
# Output: "hello"
# Example 2:
#
# Input: "here"
# Output: "here"
# Example 3:
#
# Input: "LOVELY"
# Output: "lovely"

# Solution
from leetcode.test import Test


class Solution:
    # Cheatable python solution
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class Solution_1:
    # Honest algorithmic solution
    def toLowerCase(self, str: str) -> str:
        new_str = ""
        for s in str:
            new_str += chr(ord(s) + 32) if 65 <= ord(s) <= 90 else s

        return new_str


# Tests

cases = [
    {"input": "Hello", "output": "hello"},
    {"input": "here", "output": "here"},
    {"input": "LOVELY", "output": "lovely"},
]
Test(Solution_1().toLowerCase, cases, True).test()
