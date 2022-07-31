class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # O(n2)
        lis = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(lis)):
                if nums[i]<nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)
                
                    
                    
                    
            
            