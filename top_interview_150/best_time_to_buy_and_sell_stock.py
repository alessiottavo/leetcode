from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #This is equal to find the maximum difference between two sequential elements of an array
        #Key to O(n) solution: for any given sell day p, the best buy day is whichever earlier day had the lowest price.
        
        p = 0
        m = prices[0]
        for g in range(1, len(prices)):
            m = min(m, prices[g])
            if prices[g] - m > p:
                p = prices[g] - m
        return p
