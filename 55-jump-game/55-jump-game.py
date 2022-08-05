class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        for i in range(len(dp)-2, -1, -1):
            end = min(i+nums[i]+1, len(dp))
            if any(dp[i:end]):
                dp[i] = True
        return dp[0]
        
        
            
            
            