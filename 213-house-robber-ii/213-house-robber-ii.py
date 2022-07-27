class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def robf(nu):            
            rob1, rob2 = 0,0
            for n in nu:
                t = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = t
            return rob2
        return max(robf(nums[:-1]), robf(nums[1:]))