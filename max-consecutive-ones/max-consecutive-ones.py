class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c, cur_c = 0,0
        print(len(nums))
        for n in nums:
            if n==1:
                cur_c += 1
            if max_c < cur_c:
                max_c = cur_c                
            if n==0:
                cur_c = 0
        return max_c
            
                
                