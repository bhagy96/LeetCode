class Solution:
    def rob(self, nums: List[int]) -> int:
        
        p1, p2 = 0,0
        for n in nums:
            t = p1
            p1 = max(p2+n, p1)
            p2 = t
        return p1
    
        # memo = [0]*(len(nums)+1)
        # memo[1] = nums[0]
        # for i in range(1, len(nums)):
        #     memo[i+1] = max(memo[i], memo[i-1]+nums[i])
        # return memo[len(nums)]