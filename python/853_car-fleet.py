from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()
        pairs.reverse()
        stack = []
        for p, s in pairs:
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Time:  O(n*log n)
# Space: O(n)
