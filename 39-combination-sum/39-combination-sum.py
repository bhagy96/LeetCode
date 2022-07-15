class Solution:
    def combinationSum(self, candidates, target):
        self.res = []
        def dfs(ind, curr_sol, target):  
            if target == 0:
                self.res.append(curr_sol)

            if target < 0 or ind >= len(candidates):
                return

            for i in range(ind, len(candidates)):
                dfs(i, curr_sol + [candidates[i]] , target - candidates[i])
        
        
        dfs(0, [], target)   
        return self.res
            
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         def dfs(i, cur_comb, total):
            
#             if total==target:
#                 res.append(cur_comb.copy())
#                 return
#             if total>target or i>=len(candidates):
#                 return
#             cur_comb.append(candidates[i])
#             dfs(i, cur_comb, total + candidates[i])
#             cur_comb.pop()
#             dfs(i+1, cur_comb, total)
#         dfs(0, [], 0)
#         return res

            