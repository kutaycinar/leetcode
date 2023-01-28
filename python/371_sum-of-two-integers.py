class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a & mask if b > 0 else a

# Time:  O(1)
# Space: O(1)
