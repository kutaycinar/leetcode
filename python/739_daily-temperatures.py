from typing import List


class Solution:
    # O(n^2)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, t1 in enumerate(temperatures):
            added = False
            for j, t2 in enumerate(temperatures[i:]):
                if(t1 < t2):
                    res.append(j)
                    added = True
                    break
            if not added:
                res.append(0)

        print(res)

Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
