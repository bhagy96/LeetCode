class Solution:
    import math
 
    def highestPowerof2(self,n):
        return int(math.log(n, 2));
    def countBits(self, n: int) -> List[int]:
        if n==0: return [0]
        start, end, e = 0,0,0
        dp = [0]
        power = self.highestPowerof2(n) + 1
        for i in range(power):
            for j in range(int(pow(2, i))):
                if len(dp)>n:
                    return dp
                dp.append(dp[j]+1)
        return dp
            
        
            
            
        