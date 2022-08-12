class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n&(n-1)
            res += 1
        return res
    
    
        # # O(1)
        # res = 0
        # while n:
        #     res += n%2
        #     n = n >> 1 # right shift n by 1
        # return res
        
        # # naive O(1)
        # res = 0
        # s = format(n, 'b').zfill(32)
        # for c in s:
        #     if c=='1': res+=1
        # return res