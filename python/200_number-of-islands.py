from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] != "1":
                return 0

            grid[r][c] = None

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return 1

        m = len(grid)
        n = len(grid[0])

        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += dfs(r, c)

        return islands

# Time:  O(m*n)
# Space: O(1)
