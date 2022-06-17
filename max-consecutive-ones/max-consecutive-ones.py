class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c, cur_c = 0,0
        print(len(nums))
        for n in nums:
            if n==1:
                cur_c += 1                
            else:
                if max_c < cur_c:
                    max_c = cur_c
                cur_c = 0
                
        if max_c < cur_c:
            max_c = cur_c
        return max_c
            
                
                