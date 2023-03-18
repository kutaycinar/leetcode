from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        stack = []
        for t in tokens:
            if t in operands:
                b, a = stack.pop(), stack.pop()
                res = operands[t](a, b)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack.pop()

# Time:  O(n)
# Space: O(n)
