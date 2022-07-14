class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         
        comb = [[]]
        for n in nums:            
            for i in range(len(comb)):
                comb.append(comb[i]+[n])
        return comb
        