class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
        # for i in range(len(nums)):
        #     try:
        #         j = nums.index(target-nums[i])
        #         flag = 0 if j==i else 1
        #     except:
        #         pass
        #     else:
        #         if flag: return [i,j]