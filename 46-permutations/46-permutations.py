class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if len(nums)==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    
#     def permute(self, nums):
#         def backtrack(start, end):
#             if start == end:
#                 ans.append(nums[:])
#                 print(ans)
#             for i in range(start, end):
#                 print(nums[start],nums[i])
#                 nums[start], nums[i] = nums[i], nums[start]
#                 backtrack(start+1, end)
#                 print('af', nums[start],nums[i])
#                 nums[start], nums[i] = nums[i], nums[start]
                
#         ans = []
#         backtrack(0, len(nums))
#         return ans
        