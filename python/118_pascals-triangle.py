from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, len(rows[i-1])):
                row.append(rows[i-1][j] + rows[i-1][j-1])
            rows.append(row + [1])
        print(rows)


# Time:  O(1)
# Space: O(1)
