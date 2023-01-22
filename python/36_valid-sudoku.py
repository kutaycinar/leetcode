import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subbox = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if (num in rows[r]) or (num in cols[c]) or (num in subbox[(r//3, c//3)]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                subbox[(r//3, c//3)].add(num)

        return True

# Time:  O(9^2)
# Space: O(9^2 * 3)
