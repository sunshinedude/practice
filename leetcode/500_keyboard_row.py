# Problem

# Given a List of words, return the words that can be typed using letters of alphabet
# on only one row's of American keyboard like the image below.
#
#
#
#
#
#
# Example:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
# Note:
#
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letters = {
            "Q": 1, "W": 1, "E": 1, "R": 1, "T": 1,
            "Y": 1, "U": 1, "I": 1, "O": 1, "P": 1,
            "q": 1, "w": 1, "e": 1, "r": 1, "t": 1,
            "y": 1, "u": 1, "i": 1, "o": 1, "p": 1,
            "A": 2, "a": 2, "S": 2, "s": 2, "D": 2,
            "d": 2, "F": 2, "f": 2, "G": 2, "g": 2,
            "H": 2, "h": 2, "J": 2, "j": 2, "K": 2,
            "k": 2, "L": 2, "l": 2, "Z": 3, "z": 3,
            "X": 3, "x": 3, "C": 3, "c": 3, "V": 3,
            "v": 3, "B": 3, "b": 3, "N": 3, "n": 3,
            "M": 3, "m": 3
        }
        resp = []
        for word in words:
            correct_word = True
            identify = letters[word[0]]
            for c in word:
                if letters[c] != identify:
                    correct_word = False
                    break
            if correct_word:
                resp.append(word)
        return resp


# Tests

cases = [
    {"input": ["Hello", "Alaska", "Dad", "Peace"], "output": ["Alaska", "Dad"]},
]
Test(Solution().findWords, cases, True).test()
