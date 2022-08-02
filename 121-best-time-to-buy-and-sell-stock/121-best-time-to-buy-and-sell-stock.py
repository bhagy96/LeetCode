class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        prof, sell = 0, prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i]>sell:
                sell = prices[i]
            else:
                prof = max(prof, sell - prices[i])
        return prof
            