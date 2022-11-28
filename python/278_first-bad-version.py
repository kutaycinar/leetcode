# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False if version < 1 else True


class Solution:
    # Recursive approach
    def firstBadVersion(self, n: int) -> int:
        def search(l, r):
            mid = (l + r) // 2
            if r - l < 1:
                return mid
            return search(0, mid) if isBadVersion(mid) else search(mid+1, r)
        return search(1, n)
    # Time:  O(log n)
    # Space: O(log n)

    # Iterative approach
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while r - l > 0:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
    # Time:  O(log n)
    # Space: O(1)
