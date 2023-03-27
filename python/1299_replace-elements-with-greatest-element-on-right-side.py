from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        arr = arr[1:] + [-1]
        for i in range(len(arr)-3, -1, -1):
            if arr[i] < greatest:
                arr[i] = greatest
            else:
                greatest = arr[i]
        return arr


Solution().replaceElements(arr=[1])
