class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum = nums[0]
        currentMax = nums[0]
        
        for i in range(1,len(nums)):
            
            currentMax = max(nums[i], currentMax + nums[i])
            maximum = max(currentMax, maximum)
            
        return maximum
    
    # below logic can be used in product too
#         curmax, curmin = 0,0
#         res = max(nums)
#         for n in nums:
#             t = n+curmax
#             curmax = max(n+curmax, n+curmin, n)
#             curmin = min(t, n+curmin, n)
#             res = max(res, curmax)
#             # print(n, t, curmax, curmin, res)
            
#         return res