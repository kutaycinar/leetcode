class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0b0
        for _ in range(32):
            res = res << 1
            res += n & 1
            n = n >> 1
        return res

# Time:  O(1)
# Space: O(1)