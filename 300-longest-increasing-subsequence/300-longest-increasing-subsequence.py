class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # O(n2)
        lis = [0]*len(nums)
        lis[-1] = 1
        for i in range(len(nums)-1,-1,-1):
            # print(nums[i])
            for j in range(i,len(lis)):
                # print('in',nums[i], nums[j], lis[i], lis[j] )
                if nums[i]<nums[j]: # and lis[i]<lis[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
                # print('lis', lis[i])
            if lis[i]==0:
                lis[i] = 1
        # print(lis)
        return max(lis)
                
                    
                    
                    
            
            