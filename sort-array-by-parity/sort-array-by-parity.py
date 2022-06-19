class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:    
        
        e,o=[],[]
        for n in nums:
            if n%2==0:
                e.append(n)
            else:
                o.append(n)                                    
        return e+o
    