# Problem

# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation:
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

# Note:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            good_word = True
            for i in word:
                if chars.count(i) < word.count(i):
                    good_word = False
                    break
            if good_word:
                res += len(word)
        return res


# Tests

cases = [
    {"input": [["cat","bt","hat","tree"], "atach"], "output": 6},
    {"input": [["hello","world","leetcode"], "welldonehoneyr"], "output": 10},
]
Test(Solution().countCharacters, cases, False).test()
