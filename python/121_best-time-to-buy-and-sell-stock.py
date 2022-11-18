from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        max = 0

        for _ in range(len(prices)-1):
            profit = prices[sell] - prices[buy]

            if profit > max:
                max = profit

            if prices[sell] < prices[buy]:
                buy = sell

            sell += 1

        return max


# Time:  O(n)
# Space: O(1)
