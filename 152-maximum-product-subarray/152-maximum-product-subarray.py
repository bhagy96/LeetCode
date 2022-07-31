class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax, curmin = 1,1
        res = max(nums)
        for n in nums:
            if n==0:
                curmax, curmin = 0,0
            t = n*curmax
            curmax = max(n*curmax, n*curmin, n)
            curmin = min(t, n*curmin, n)
            res = max(res, curmax)
            # print(n, t, curmax, curmin, res)
            
        return res
        
        
        