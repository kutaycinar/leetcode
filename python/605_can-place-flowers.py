from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) < 2:
            if flowerbed[0] == 0:
                count += 1
            return n <= count
        if flowerbed[0] == 0 and flowerbed[1] != 1:
            flowerbed[0] = 1
            count += 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                count += 1
        if flowerbed[-1] == 0 and flowerbed[-2] != 1:
            flowerbed[-1] = 1
            count += 1
        return n <= count

# Time:  O(n)
# Space: O(1)
