from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append((dist, x, y))

        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res

# Time:  O(n+k*log n)
# Space: O(n)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, [-(x*x + y*y), x, y])
            else:
                heapq.heappushpop(maxHeap, [-(x*x + y*y), x, y])

        return [[x, y] for _, x, y in maxHeap]

# Time:  O(n*log k)
# Space: O(k)
