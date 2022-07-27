class Solution:
    def rob(self, nums: List[int]) -> int:
        #[rob1,rob2,n,n+1...]
        rob1, rob2 = 0,0
        for n in nums:
            t = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = t
        return rob2
    
        # memo = [0]*(len(nums)+1)
        # memo[1] = nums[0]
        # for i in range(1, len(nums)):
        #     memo[i+1] = max(memo[i], memo[i-1]+nums[i])
        # return memo[len(nums)]