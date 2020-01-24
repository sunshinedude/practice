# Problem

# Given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
#
#
#
# Example 1:
#
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:
#
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:
#
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
#
#
# Constraints:
#
# 1 <= num <= 10^4
# num's digits are 6 or 9.

# Solution
from leetcode.test import Test


class Solution:
    def maximum69Number(self, num: int) -> int:
        s_num = str(num)
        first_6 = s_num.find("6")
        if first_6 >= 0:
            s_num = s_num[:first_6] + "9" + s_num[first_6 + 1 :]
        return int(s_num)


# Tests

cases = [
    {"input": 9669, "output": 9969},
    {"input": 9996, "output": 9999},
    {"input": 9999, "output": 9999},
    {"input": 696, "output": 996},
]
Test(Solution().maximum69Number, cases, True).test()
