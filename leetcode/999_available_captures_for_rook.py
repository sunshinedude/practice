# Problem

# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops,
# and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively.
# Uppercase characters represent white pieces, and lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions
# (north, east, west, and south), then moves in that direction until it chooses to stop,
# reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.
# Also, rooks cannot move into the same square as other friendly bishops.
#
# Return the number of pawns the rook can capture in one move.
#
#
#
# Example 1:
#
#
#
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
# [".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
# [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# In this example the rook is able to capture all the pawns.
# Example 2:
#
#
#
# Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],
# [".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],
# [".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],
# [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation:
# Bishops are blocking the rook to capture any pawn.
# Example 3:
#
#
#
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
# [".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],
# [".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],
# [".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# The rook can capture the pawns at positions b5, d6 and f5.
#
#
# Note:
#
# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'

# Solution
from typing import List

from leetcode.test import Test


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        R = []
        finded_R = False
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    R = [i, j]
                    finded_R = True
                    break
            if finded_R:
                break

        ans = 0
        i = R[1] + 1
        while i < 8:
            if board[R[0]][i] in ('p', 'B'):
                if board[R[0]][i] == 'p':
                    ans += 1
                break
            i += 1

        i = R[1] - 1
        while i >= 0:
            if board[R[0]][i] in ('p', 'B'):
                if board[R[0]][i] == 'p':
                    ans += 1
                break
            i -= 1

        i = R[0] + 1
        while i < 8:
            if board[i][R[1]] in ('p', 'B'):
                if board[i][R[1]] == 'p':
                    ans += 1
                break
            i += 1

        i = R[0] - 1
        while i >= 0:
            if board[i][R[1]] in ('p', 'B'):
                if board[i][R[1]] == 'p':
                    ans += 1
                break
            i -= 1
        return ans


# Tests

cases = [
    {
        "input": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                  [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]],
        "output": 3},

    {
        "input": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                  [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                  [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]],
        "output": 3},

    {
        "input": [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                  [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                  [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]],
        "output": 0},
    {
        "input": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", "B", "B", "B", "B", "B", "."],
                  [".", "p", "B", "p", "p", "p", "B", "p"], [".", "p", "B", "p", "R", "p", "B", "p"],
                  [".", "p", "B", "p", "p", "p", "B", "p"], [".", ".", "B", "B", "B", "B", "B", "."],
                  [".", ".", ".", "p", "p", "p", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]],
        "output": 4},

]
Test(Solution().numRookCaptures, cases, True).test()
