# Problem

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".
#
# Example 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

# Solution
from leetcode.test import Test


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# Tests

cases = [
    {"input": "1.1.1.1", "output": "1[.]1[.]1[.]1"},
    {"input": "255.100.50.0", "output": "255[.]100[.]50[.]0"},
]
Test(Solution().defangIPaddr, cases, True).test()
