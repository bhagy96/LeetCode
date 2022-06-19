class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
        
        L = len(nums)
        i=0
        c=0
        # for i in range(len(nums)):
        while (i+c)<L:
            # print("i",i)
            if nums[i]==0:
                nums.pop(i)                
                c+=1
            else:
                i+=1
            # print(nums)
            # print("i+c",i+c,L)
        nums += c*[0]
        return nums
    
        # L = len(nums)
        # for i in range(L):
        #     if nums[i]==0:
        #         nums.pop(i)
        #         nums.insert(L-1,0)
        # return nums
            
                