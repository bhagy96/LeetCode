class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:    
        
        e,o=[],[]
        for n in nums:
            if n%2==0:
                e.append(n)
            else:
                o.append(n)                                    
        return e+o
        
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j]%2 == 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        # return nums
    