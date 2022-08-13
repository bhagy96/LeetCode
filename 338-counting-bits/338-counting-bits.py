class Solution:
    
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

    
    # dp method 
    
#     import math
 
#     def highestPowerof2(self,n):
#         return int(math.log(n, 2));
#     def countBits(self, n: int) -> List[int]:
#         if n==0: return [0]
#         start, end, e = 0,0,0
#         dp = [0]
#         power = self.highestPowerof2(n) + 1
#         for i in range(power):
#             for j in range(int(pow(2, i))):
#                 if len(dp)>n:
#                     return dp
#                 dp.append(dp[j]+1)
#         return dp
            
        
            
            
        