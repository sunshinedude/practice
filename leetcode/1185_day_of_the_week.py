# Problem

# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values
# {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
#
#
#
# Example 1:
#
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# Example 2:
#
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# Example 3:
#
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"

# Solution
from leetcode.test import Test


class Solution:
	# Algorithmic solution
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		if month < 3:
			year -= 1
			month += 10
		else:
			month -= 2
		num = (day + 31 * month // 12 + year + year // 4 - year // 100 + year // 400) % 7
		days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		return days[num]


class Solution_1:
	# Python cheat solution
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		import datetime
		return datetime.date(year, month, day).strftime('%A')

# Tests

cases = [
	{"input": [31, 8, 2019], "output": "Saturday"},
	{"input": [18, 7, 1999], "output": "Sunday"},
	{"input": [15, 8, 1993], "output": "Sunday"},
]
Test(Solution().dayOfTheWeek, cases, False).test()
Test(Solution_1().dayOfTheWeek, cases, False).test()
