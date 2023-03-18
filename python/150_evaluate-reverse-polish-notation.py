from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t in operands:
                b, a = stack.pop(), stack.pop()
                match t:
                    case '+':
                        stack.append(a + b)
                    case '-':
                        stack.append(a - b)
                    case '*':
                        stack.append(a * b)
                    case '/':
                        stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack.pop()
    

Solution().evalRPN(tokens=["2", "1", "+", "3", "*"])
