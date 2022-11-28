class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverse = []

    def push(self, x: int) -> None:
        while self.reverse:
            self.stack.append(self.reverse.pop())
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.reverse.append(self.stack.pop())
        return self.reverse.pop()

    def peek(self) -> int:
        return self.stack[0] if self.stack else self.reverse[-1]

    def empty(self) -> bool:
        return not self.stack and not self.reverse

# Time:  O(1) amortized
# Space: O(n)
