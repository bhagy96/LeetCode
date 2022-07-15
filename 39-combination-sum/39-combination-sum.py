class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur_comb, total):
            
            if total==target:
                res.append(cur_comb.copy())
                return
            if total>target or i>=len(candidates):
                return
            cur_comb.append(candidates[i])
            dfs(i, cur_comb, total + candidates[i])
            cur_comb.pop()
            dfs(i+1, cur_comb, total)
        dfs(0, [], 0)
        return res

            