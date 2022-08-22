class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res + i - nums[i]
        return res
        
        # or use sum of elements upto n formula i.e n*n+1 / 2
        # and sustract every elemrnt from it
        