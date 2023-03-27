class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]

        return matrix[-1][-1]


# Time:  O(m*n)
# Space: O(m*n)
