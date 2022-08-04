class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # # tle
        # n = len(nums)
        # ways = 0
        # for i in range(2**n, 2**(n + 1)):
        #     bitmask = bin(i)[3:]
        #     sum_ = 0
        #     for i in range(n):
        #         if bitmask[i]=='0':
        #             sum_ -= nums[i]
        #         else:
        #             sum_ += nums[i]
        #     if sum_==target:
        #         ways+=1
        # return ways
        
        dp = {}
        # total = 0
        def backtrack(i,total):
            if i>=len(nums):
                return 1 if total==target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return dp[(i,total)]
        return backtrack(0,0)
            