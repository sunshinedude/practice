# Problem

# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
#
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.
#
# Return True if and only if Alice wins the game, assuming both players play optimally.
#
#
#
# Example 1:
#
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:
#
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

# Solution
from leetcode.test import Test


class Solution:
    # If the number is even, Alice selects 1 and makes the number odd. After that,
    # whatever Bob chooses, Alice will always finish turn 1. The situation is symmetric with an odd number.

    # You can't divide an odd number by an even number.
    # When subtracting from an odd number - odd, we get an even number
    def divisorGame(self, N: int) -> bool:
        return not bool(N % 2)


# Tests

cases = [
    {"input": 2, "output": True},
    {"input": 3, "output": False},
]
Test(Solution().divisorGame, cases, True).test()
