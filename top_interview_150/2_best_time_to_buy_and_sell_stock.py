""" You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve. """



from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for p in range(1, len(prices)):
            if prices[p] > prices[p - 1]:
                profit2 = prices[p] - prices[p - 1]
                profit += profit2
        # By taking only the positive consecutive differences, we skip the dips (effectively selling before a drop, rebuying after).
        # Because a multi-day gain is just the sum of its daily gains.
        return profit