class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # print(i)
            try:
                j = nums.index(target-nums[i])
                flag = 0 if j==i else 1
                # flag = 1
                # print(i,j)
                # return [i,j]
            except:
                # print("exc")
                pass
            else:
                # print("else")
                if flag: return [i,j]