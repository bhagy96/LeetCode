class Solution:
    def reverse(self, x: int) -> int:
        f = 0
        if x<0: 
            f = 1
            x *= -1
        s = format(int(str(x)[::-1]), 'b')
        # if len(s)>32: return 0
        re = int(s, 2)
        if re>((2**31)-1): return 0
        if f:
            return re*-1
        return re
        
        
        