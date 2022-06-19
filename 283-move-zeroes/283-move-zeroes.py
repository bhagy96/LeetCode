class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
                
        L = len(nums)
        i=0
        c=0
        while (i+c)<L:
            if nums[i]==0:
                nums.pop(i)                
                c+=1
            else:
                i+=1
        nums += c*[0]
        return nums
    
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
    
        # c = nums.count(0)
        # c=0
        # for n in nums:
        #     if n==0:
        #         c+=1
        # # L = len(nums)
        # for _ in range(c):
        #     nums.remove(0)
        # nums += c*[0]
        # return nums
    
    
        # c = nums.count(0)
        # L = len(nums)
        # for _ in range(c):
        #     nums.remove(0)
        #     nums.insert(L-1,0)
        # return nums
        
        
    
        # L = len(nums)
        # for i in range(L):
        #     if nums[i]==0:
        #         nums.pop(i)
        #         nums.insert(L-1,0)
        # return nums
            
                