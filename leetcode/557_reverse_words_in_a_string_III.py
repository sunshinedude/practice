# Problem

# Given a string, you need to reverse the order of characters in each word within
# a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# Solution
from leetcode.test import Test


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))


# Tests

cases = [
    {"input": "Let's take LeetCode contest", "output": "s'teL ekat edoCteeL tsetnoc"},
]
Test(Solution().reverseWords, cases, True).test()
