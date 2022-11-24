class Solution:
    # Recursive approach
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
    # Time:  O(2^n)
    # Space: O(n)

    # Iterative approach
    def fib_iterative(self, n: int) -> int:
        f0, f1 = 0, 1

        while n > 0:
            f1, f0 = f0 + f1, f1
            n -= 1

        return f0
    # Time:  O(n)
    # Space: O(1)
