class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        
        # O(nlogn)
        # if len(nums)==0: return 0
        # nums = sorted(nums)
        # res,cnt = 0,1
        # # print(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == 1+nums[i-1] :
        #         cnt += 1
        #     elif nums[i]!=nums[i-1]:
        #         res = max(res,cnt)
        #         cnt = 1
        # return max(res,cnt)