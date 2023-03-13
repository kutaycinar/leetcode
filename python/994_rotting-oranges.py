import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)  # rows
        n = len(grid[0])  # cols

        fresh = 0
        rotten = []

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1:
                    fresh += 1
                if col == 2:
                    rotten.append([r, c])

        minutes = -1
        queue = collections.deque(rotten)

        while queue:

            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # add neighbours
                # left
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    queue.append([r, c-1])
                    grid[r][c-1] = 2
                    fresh -= 1

                # right
                if c + 1 < n and grid[r][c+1] == 1:
                    queue.append([r, c+1])
                    grid[r][c+1] = 2
                    fresh -= 1

                # down
                if r + 1 < m and grid[r+1][c] == 1:
                    queue.append([r+1, c])
                    grid[r+1][c] = 2
                    fresh -= 1

                # up
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    queue.append([r-1, c])
                    grid[r-1][c] = 2
                    fresh -= 1

        return max(0, minutes) if not fresh else -1
