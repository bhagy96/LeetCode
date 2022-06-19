class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        c=0
        for n in nums:
            if n==0:
                c+=1
        # L = len(nums)
        for _ in range(c):
            nums.remove(0)
        nums += c*[0]
        return nums
    
    
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
            
                