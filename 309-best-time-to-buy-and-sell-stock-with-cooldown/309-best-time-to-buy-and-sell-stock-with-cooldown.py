class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # statemachine
        # see diagram here 
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
        #     or watch youtube video
        
        # O(n) and O(n)
#         l = len(prices)
#         if l==1: return 0
#         nostock, inhand, sold = [0]*l, [0]*l, [0]*l
#         nostock[0] = 0
#         inhand[0] = -prices[0]
#         sold[0] = 0
#         for i in range(1,l):
#             nostock[i] = max(nostock[i-1], sold[i-1])
#             inhand[i] = max(inhand[i-1], nostock[i-1] - prices[i])
#             sold[i] = inhand[i-1] + prices[i]
#         return max(nostock[-1], sold[-1])
    
        # O(n) O(1)
        nostock, inhand, sold = 0, -prices[0], 0
        for p in prices:
            prevsold = sold
            sold = inhand + p
            inhand = max(inhand, nostock-p)
            nostock = max(nostock, prevsold)
        return max(sold, nostock)
            
    #     int sold = 0, hold = INT_MIN, rest = 0;
    # for (int i=0; i<prices.size(); ++i)
    # {
    #     int prvSold = sold;
    #     sold = hold + prices[i];
    #     hold = max(hold, rest-prices[i]);
    #     rest = max(rest, prvSold);
    # }
    # return max(sold, rest);
    
    # dp recurssion
    
#         dic = {}
        
#         def dfs(i, buying):
#             if i>=len(prices):
#                 return 0
#             if (i,buying) in dic:
#                 return dic[(i,buying)]
#             if buying:
#                 buy = dfs(i+1, not buying) - prices[i]
#                 cooldown = dfs(i+1, buying)
#                 dic[(i,buying)] = max(buy, cooldown)
#             else:
#                 sell = dfs(i+2, not buying) +prices[i]
#                 cooldown = dfs(i+1, buying)
#                 dic[(i,buying)] = max(sell, cooldown)
#             return dic[(i, buying)]
#         r = dfs(0,True)
#         print(dic)
        return r
        