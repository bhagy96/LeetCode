class Solution:
    def reverse(self, x: int) -> int:
        f = 0
        if x<0: 
            f = 1
            x *= -1
        re = int(format(int(str(x)[::-1]), 'b'), 2)
        if re>((2**31)-1): return 0
        if f:
            return re*-1
        return re
        
        
        