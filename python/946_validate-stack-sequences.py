from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        s = 0
        for i in range(len(popped)):
            if not stack:
                stack.append(pushed[i])
                s += 1
            while stack[-1] != popped[i]:
                if s > len(pushed) - 1:
                    return False
                stack.append(pushed[s])
                s += 1
            stack.pop()
        return True

# Time:  O(n)
# Space: O(n)
