class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        lastPosition = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            # print(i,nums[i])
            if (i + nums[i]) >= lastPosition:
                lastPosition = i
        return lastPosition==0
             
        
#         dp = [False]*len(nums)
#         dp[-1] = True
#         for i in range(len(dp)-2, -1, -1):
#             end = min(i+nums[i]+1, len(dp))
#             if any(dp[i:end]):
#                 dp[i] = True
#         return dp[0]
        
        
            
            
            