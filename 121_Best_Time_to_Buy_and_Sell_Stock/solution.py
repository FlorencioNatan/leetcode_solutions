from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_of_prices = len(prices)
        i = j = max_profit = 0
        while (j < num_of_prices):
            if (prices[j] - prices[i] > max_profit):
                max_profit = prices[j] - prices[i]
            elif (prices[j] - prices[i] < 0):
                i = j
            j += 1
        return max_profit

