# Problem

# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split
# it into S = A+B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string S, consider its primitive
# decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
#
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
#
#
#
# Example 1:
#
# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
#
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
#
# Input: "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
#
#
# Note:
#
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string

# Solution
from leetcode.test import Test


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        first_left_index = 0
        left_count = 0
        right_count = 0
        res = ""

        for i in range(len(S)):
            if S[i] == "(":
                if left_count == right_count:
                    first_left_index = i
                left_count += 1
            else:
                right_count += 1
                if right_count == left_count:
                    res += S[first_left_index + 1 : i]
                    left_count = 0
                    right_count = 0
        return res


# Tests

cases = [
    {"input": "(()())(())", "output": "()()()"},
    {"input": "(()())(())(()(()))", "output": "()()()()(())"},
    {"input": "()()", "output": ""},
]
Test(Solution().removeOuterParentheses, cases, True).test()
