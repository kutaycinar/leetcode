from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        initial = image[sr][sc]

        if initial == color:
            return image

        def fill(r, c):
            if not 0 <= r < len(image) or not 0 <= c < len(image[0]) or image[r][c] != initial:
                return None

            image[r][c] = color

            fill(r, c+1)
            fill(r, c-1)
            fill(r+1, c)
            fill(r-1, c)

        fill(sr, sc)

        return image

# Time:  O(m*n)
# Space: O(m*n)
