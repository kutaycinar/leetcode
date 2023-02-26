class Solution:
    # Decision Tree
    def climbStairs(self, n: int) -> int:

        def climb(x):
            if x == n:
                return 1
            if x > n:
                return 0

            return climb(x+1) + climb(x+2)

        return climb(0)

    # Time:  O(2^n)
    # Space: O(n)

    # notice
        # n=1 -> 1
        # n=2 -> 2
        # n=3 -> 3
        # n=4 -> 5
        # n=5 -> 8

    # Optimal
    def climbStairs(self, n: int) -> int:

        one, two = 1, 0

        for _ in range(n):
            one, two = one + two, one

        return one

    # Time:  O(n)
    # Space: O(1)
