class Solution:
    
    # All are O(N*2^N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        # Visualize it like a tree taking and not taking nus of i at each level
        
        res = []
        subset = []
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # not include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
    
    
            
            
        
        
        # my solution
        
        # comb = [[]]
        # for n in nums:            
        #     for i in range(len(comb)):
        #         comb.append(comb[i]+[n])
        # return comb
        
        
        
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = []
#         # 2**n is 1000 (8) to 10000 (16) then ignore the first bit for 000 to 111
#         for i in range(2**n, 2**(n + 1)):
#             # generate bitmask, from 0..00 to 1..11
#             bitmask = bin(i)[3:] # because it has 0b in first 2 and we ignore the 3d bit 
            
#             # append subset corresponding to that bitmask
#             output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
#         return output
        