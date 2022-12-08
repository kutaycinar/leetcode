from typing import List
import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t, b = l, r

                matrix[t][l+i], matrix[b-i][l] = matrix[b-i][l], matrix[t][l+i]
                matrix[b-i][l], matrix[b][r-i] = matrix[b][r-i], matrix[b-i][l]
                matrix[t+i][r], matrix[b][r-i] = matrix[b][r-i], matrix[t+i][r]

            l += 1
            r -= 1

# Time:  O(n*n)
# Space: O(1)
