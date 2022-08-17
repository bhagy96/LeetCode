class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        nums = sorted(nums)
        res,cnt = 0,1
        # print(nums)
        for i in range(1,len(nums)):
            if nums[i] == 1+nums[i-1] :
                cnt += 1
            elif nums[i]!=nums[i-1]:
                res = max(res,cnt)
                cnt = 1
        return max(res,cnt)